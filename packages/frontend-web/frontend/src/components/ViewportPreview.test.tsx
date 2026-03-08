import { render, screen } from "@testing-library/react";

import { ViewportPreview } from "./ViewportPreview";

describe("ViewportPreview", () => {
  test("截图模式展示图片和刷新时间", () => {
    render(
      <ViewportPreview
        snapshot={{
          mime_type: "image/png",
          image_base64: "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO3b6x0AAAAASUVORK5CYII=",
          generated_at: new Date().toISOString(),
        }}
        loading={false}
        wsState="open"
        transportMode="snapshot"
        recommendedMode="snapshot"
        onTransportModeChange={() => {}}
        remoteStream={null}
        localStream={null}
        webrtcConnected={false}
        peers={[]}
        onStartPublishing={async () => {}}
      />
    );

    expect(screen.getByRole("img", { name: "Viewport Snapshot" })).toBeInTheDocument();
    expect(screen.getByText(/最近刷新/)).toBeInTheDocument();
  });

  test("WebRTC 模式展示连接状态和发布按钮", () => {
    render(
      <ViewportPreview
        snapshot={null}
        loading={false}
        wsState="open"
        transportMode="webrtc"
        recommendedMode="webrtc"
        onTransportModeChange={() => {}}
        remoteStream={null}
        localStream={null}
        webrtcConnected={false}
        peers={["peer-a", "peer-b"]}
        onStartPublishing={async () => {}}
      />
    );

    expect(screen.getByText(/连接状态/)).toBeInTheDocument();
    expect(screen.getByText(/房间在线：2 人/)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /发布视频流/ })).toBeInTheDocument();
  });
});
