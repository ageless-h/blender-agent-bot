import { useCallback, useEffect, useRef, useState } from "react";

import { buildWsUrl } from "../network";

export type ConnectionState = "connecting" | "open" | "closed";

interface WebSocketOptions {
  token?: string | null;
  autoReconnect?: boolean;
  reconnectDelayMs?: number;
}

export function useWebSocket(path: string, options: WebSocketOptions = {}) {
  const { token = null, autoReconnect = true, reconnectDelayMs = 1200 } = options;
  const socketRef = useRef<WebSocket | null>(null);
  const reconnectTimerRef = useRef<number | null>(null);
  const [state, setState] = useState<ConnectionState>("connecting");
  const [lastMessage, setLastMessage] = useState<unknown>(null);

  const cleanupTimer = useCallback(() => {
    if (reconnectTimerRef.current !== null) {
      window.clearTimeout(reconnectTimerRef.current);
      reconnectTimerRef.current = null;
    }
  }, []);

  const connect = useCallback(() => {
    cleanupTimer();
    setState("connecting");

    const url = new URL(buildWsUrl(path));
    if (token) {
      url.searchParams.set("token", token);
    }

    const socket = new WebSocket(url.toString());
    socketRef.current = socket;

    socket.onopen = () => {
      setState("open");
    };

    socket.onclose = () => {
      setState("closed");
      if (autoReconnect) {
        reconnectTimerRef.current = window.setTimeout(connect, reconnectDelayMs);
      }
    };

    socket.onerror = () => {
      setState("closed");
    };

    socket.onmessage = (event) => {
      try {
        setLastMessage(JSON.parse(event.data));
      } catch {
        setLastMessage(event.data);
      }
    };
  }, [autoReconnect, cleanupTimer, path, reconnectDelayMs, token]);

  useEffect(() => {
    connect();
    return () => {
      cleanupTimer();
      socketRef.current?.close();
      socketRef.current = null;
    };
  }, [cleanupTimer, connect]);

  const sendJson = useCallback((payload: unknown) => {
    if (socketRef.current?.readyState !== WebSocket.OPEN) {
      return false;
    }
    socketRef.current.send(JSON.stringify(payload));
    return true;
  }, []);

  return {
    state,
    lastMessage,
    sendJson
  };
}
