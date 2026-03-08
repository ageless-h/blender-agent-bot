import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import { buildApiUrl, buildWsUrl, mergeHeaders } from "../network";

type TransportMode = "snapshot" | "webrtc";

interface IceServerConfig {
  urls: string[];
}

interface WebRTCConfig {
  ice_servers: IceServerConfig[];
  signal_url_template?: string;
  heartbeat_seconds?: number;
}

interface UseWebRTCOptions {
  token: string | null;
  roomId?: string;
}

function inferNetworkMode(): TransportMode {
  const nav = navigator as Navigator & { connection?: { rtt?: number; downlink?: number } };
  const rtt = nav.connection?.rtt;
  const downlink = nav.connection?.downlink;
  if (typeof rtt === "number" && rtt > 250) {
    return "snapshot";
  }
  if (typeof downlink === "number" && downlink < 2) {
    return "snapshot";
  }
  return "webrtc";
}

function normalizeSignalPath(template: string | undefined, roomId: string): string {
  if (!template) {
    return `/ws/webrtc/${roomId}`;
  }
  if (template.includes("{room_id}")) {
    return template.replace("{room_id}", roomId);
  }
  return template;
}

export function useWebRTC(options: UseWebRTCOptions) {
  const { token, roomId = "default" } = options;
  const [remoteStream, setRemoteStream] = useState<MediaStream | null>(null);
  const [localStream, setLocalStream] = useState<MediaStream | null>(null);
  const [peerId, setPeerId] = useState<string>("");
  const [peers, setPeers] = useState<string[]>([]);
  const [connected, setConnected] = useState(false);
  const [transportMode, setTransportMode] = useState<TransportMode>(inferNetworkMode());
  const wsRef = useRef<WebSocket | null>(null);
  const pcsRef = useRef<Map<string, RTCPeerConnection>>(new Map());
  const selfPeerIdRef = useRef<string>("");
  const localStreamRef = useRef<MediaStream | null>(null);
  const configRef = useRef<WebRTCConfig>({ ice_servers: [{ urls: ["stun:stun.l.google.com:19302"] }] });

  const recomputeConnected = useCallback(() => {
    const anyConnected = [...pcsRef.current.values()].some((pc) => pc.connectionState === "connected");
    setConnected(anyConnected);
  }, []);

  const sendSignal = useCallback((payload: Record<string, unknown>) => {
    if (wsRef.current?.readyState !== WebSocket.OPEN) {
      return;
    }
    wsRef.current.send(JSON.stringify(payload));
  }, []);

  const removePeerConnection = useCallback(
    (remotePeerId: string) => {
      const pc = pcsRef.current.get(remotePeerId);
      if (!pc) {
        return;
      }
      pc.close();
      pcsRef.current.delete(remotePeerId);
      recomputeConnected();
    },
    [recomputeConnected]
  );

  const ensurePeerConnection = useCallback(
    (remotePeerId: string) => {
      const existing = pcsRef.current.get(remotePeerId);
      if (existing) {
        return existing;
      }

      const iceServers = configRef.current.ice_servers.map((item) => ({ urls: item.urls }));
      const pc = new RTCPeerConnection({ iceServers });

      if (localStreamRef.current) {
        for (const track of localStreamRef.current.getTracks()) {
          pc.addTrack(track, localStreamRef.current);
        }
      }

      pc.onicecandidate = (event) => {
        if (!event.candidate) {
          return;
        }
        sendSignal({ type: "candidate", target: remotePeerId, candidate: event.candidate.toJSON() });
      };
      pc.ontrack = (event) => {
        const [stream] = event.streams;
        if (stream) {
          setRemoteStream(stream);
        }
      };
      pc.onconnectionstatechange = () => {
        recomputeConnected();
      };

      pcsRef.current.set(remotePeerId, pc);
      return pc;
    },
    [recomputeConnected, sendSignal]
  );

  const createOffer = useCallback(
    async (remotePeerId: string) => {
      const pc = ensurePeerConnection(remotePeerId);
      const offer = await pc.createOffer();
      await pc.setLocalDescription(offer);
      sendSignal({ type: "offer", target: remotePeerId, sdp: offer.sdp, sdpType: offer.type });
    },
    [ensurePeerConnection, sendSignal]
  );

  const publishLocalCamera = useCallback(async () => {
    try {
      const media = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
      setLocalStream(media);
      localStreamRef.current = media;

      for (const remotePeerId of peers) {
        const pc = ensurePeerConnection(remotePeerId);
        for (const track of media.getTracks()) {
          pc.addTrack(track, media);
        }
        await createOffer(remotePeerId);
      }
    } catch {
      return;
    }
  }, [createOffer, ensurePeerConnection, peers]);

  useEffect(() => {
    const initialize = async () => {
      let signalPath = `/ws/webrtc/${roomId}`;
      const response = await fetch(buildApiUrl("/api/webrtc/config"), { headers: mergeHeaders(token) });
      if (response.ok) {
        const payload = (await response.json()) as WebRTCConfig;
        configRef.current = payload;
        signalPath = normalizeSignalPath(payload.signal_url_template, roomId);
      }

      const signalUrl = new URL(buildWsUrl(signalPath));
      signalUrl.searchParams.set("peer_id", crypto.randomUUID());
      if (token) {
        signalUrl.searchParams.set("token", token);
      }

      const socket = new WebSocket(signalUrl.toString());
      wsRef.current = socket;

      socket.onmessage = async (event) => {
        const message = JSON.parse(event.data) as Record<string, unknown>;

        if (message.type === "system") {
          const currentPeerId = String(message.peer_id ?? "");
          selfPeerIdRef.current = currentPeerId;
          setPeerId(currentPeerId);
          const incomingPeers = Array.isArray(message.peers)
            ? message.peers.map((item) => String(item)).filter((item) => item && item !== currentPeerId)
            : [];
          setPeers(incomingPeers);

          if (localStreamRef.current) {
            for (const remotePeerId of incomingPeers) {
              await createOffer(remotePeerId);
            }
          }
          return;
        }

        if (message.type !== "signal") {
          return;
        }

        const payload = (message.payload ?? {}) as Record<string, unknown>;
        const signalType = String(payload.type ?? payload.event ?? "");
        const fromPeerId = String(message.from ?? payload.peer_id ?? "");

        if (signalType === "peer_join") {
          const joinedPeerId = String(payload.peer_id ?? "");
          if (!joinedPeerId || joinedPeerId === selfPeerIdRef.current) {
            return;
          }
          setPeers((previous) => (previous.includes(joinedPeerId) ? previous : [...previous, joinedPeerId]));

          if (localStreamRef.current) {
            await createOffer(joinedPeerId);
          }
          return;
        }

        if (signalType === "peer_leave") {
          const leftPeerId = String(payload.peer_id ?? "");
          setPeers((previous) => previous.filter((item) => item !== leftPeerId));
          if (leftPeerId) {
            removePeerConnection(leftPeerId);
          }
          return;
        }

        if (!fromPeerId || fromPeerId === selfPeerIdRef.current) {
          return;
        }

        const pc = ensurePeerConnection(fromPeerId);

        if (signalType === "offer") {
          const sdp = String(payload.sdp ?? "");
          try {
            await pc.setRemoteDescription({ type: "offer", sdp });
            const answer = await pc.createAnswer();
            await pc.setLocalDescription(answer);
            sendSignal({ type: "answer", target: fromPeerId, sdp: answer.sdp, sdpType: answer.type });
          } catch {
            return;
          }
          return;
        }

        if (signalType === "answer") {
          const sdp = String(payload.sdp ?? "");
          try {
            await pc.setRemoteDescription({ type: "answer", sdp });
          } catch {
            return;
          }
          return;
        }

        if (signalType === "candidate") {
          const candidate = payload.candidate;
          if (candidate && typeof candidate === "object") {
            try {
              await pc.addIceCandidate(candidate as RTCIceCandidateInit);
            } catch {
              return;
            }
          }
        }
      };
    };

    void initialize();

    return () => {
      localStreamRef.current?.getTracks().forEach((track) => track.stop());
      localStreamRef.current = null;
      for (const pc of pcsRef.current.values()) {
        pc.close();
      }
      pcsRef.current.clear();
      wsRef.current?.close();
      wsRef.current = null;
      setConnected(false);
    };
  }, [createOffer, ensurePeerConnection, removePeerConnection, roomId, sendSignal, token]);

  const recommendedMode = useMemo(() => inferNetworkMode(), []);

  return {
    transportMode,
    setTransportMode,
    recommendedMode,
    remoteStream,
    localStream,
    publishLocalCamera,
    connected,
    peerId,
    peers,
  };
}
