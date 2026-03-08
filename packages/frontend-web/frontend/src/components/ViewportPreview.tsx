import type { ViewportSnapshot } from "../types";

interface ViewportPreviewProps {
  snapshot: ViewportSnapshot | null;
  loading: boolean;
  wsState: string;
  transportMode: "snapshot" | "webrtc";
  recommendedMode: "snapshot" | "webrtc";
  onTransportModeChange: (mode: "snapshot" | "webrtc") => void;
  remoteStream: MediaStream | null;
  localStream: MediaStream | null;
  webrtcConnected: boolean;
  peers: string[];
  onStartPublishing: () => Promise<void>;
}

export function ViewportPreview(props: ViewportPreviewProps) {
  const {
    snapshot,
    loading,
    wsState,
    transportMode,
    recommendedMode,
    onTransportModeChange,
    remoteStream,
    localStream,
    webrtcConnected,
    peers,
    onStartPublishing,
  } = props;

  return (
    <section className="panel viewport-panel">
      <header className="panel-header">
        <h2>视口预览</h2>
        <span className="status-tag">WS: {wsState}</span>
      </header>

      <div className="toolbar-actions viewport-tools">
        <button
          className={transportMode === "snapshot" ? "active" : ""}
          onClick={() => onTransportModeChange("snapshot")}
          type="button"
        >
          截图模式
        </button>
        <button
          className={transportMode === "webrtc" ? "active" : ""}
          onClick={() => onTransportModeChange("webrtc")}
          type="button"
        >
          WebRTC 模式
        </button>
        <span className="muted">推荐：{recommendedMode === "webrtc" ? "WebRTC" : "截图"}</span>
      </div>

      <div className="viewport-stage">
        {transportMode === "webrtc" ? (
          <video
            className="viewport-image"
            autoPlay
            playsInline
            muted
            ref={(node) => {
              if (node && remoteStream && node.srcObject !== remoteStream) {
                node.srcObject = remoteStream;
              }
            }}
          />
        ) : null}

        {transportMode === "snapshot" && loading ? <p className="muted">正在加载视口帧...</p> : null}
        {transportMode === "snapshot" && !loading && snapshot ? (
          <img
            src={`data:${snapshot.mime_type};base64,${snapshot.image_base64}`}
            alt="Viewport Snapshot"
            className="viewport-image"
          />
        ) : null}
      </div>

      {transportMode === "webrtc" ? (
        <div className="webrtc-status">
          <p className="muted">连接状态：{webrtcConnected ? "已连接" : "等待信令"}</p>
          <p className="muted">房间在线：{peers.length} 人</p>
          <button onClick={() => void onStartPublishing()} type="button">
            发布视频流
          </button>
          {localStream ? <p className="muted">本地发布中</p> : null}
        </div>
      ) : null}

      {snapshot && transportMode === "snapshot" ? (
        <p className="muted">最近刷新：{new Date(snapshot.generated_at).toLocaleString()}</p>
      ) : null}
    </section>
  );
}
