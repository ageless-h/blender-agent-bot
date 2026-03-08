import { useCallback, useEffect, useState } from "react";

import { ActionPreview } from "./components/ActionPreview";
import { ChatPanel } from "./components/ChatPanel";
import { FileExport } from "./components/FileExport";
import { SettingsModal } from "./components/SettingsModal";
import { ShareLink } from "./components/ShareLink";
import { ToolBar } from "./components/ToolBar";
import { ViewportPreview } from "./components/ViewportPreview";
import { useAuth } from "./hooks/useAuth";
import { useChat } from "./hooks/useChat";
import { useViewport } from "./hooks/useViewport";
import { useWebRTC } from "./hooks/useWebRTC";
import { buildApiUrl, mergeHeaders } from "./network";

export default function App() {
  const auth = useAuth();
  const chat = useChat({ token: auth.apiToken || null });
  const viewport = useViewport({ token: auth.apiToken || null });
  const webrtc = useWebRTC({ token: auth.apiToken || null });

  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [isExportOpen, setIsExportOpen] = useState(false);
  const [isShareOpen, setIsShareOpen] = useState(false);

  const sendMessage = useCallback(
    async (message: string) => {
      await chat.sendMessage("web-user", message);
    },
    [chat]
  );

  const undo = useCallback(async () => {
    await fetch(buildApiUrl("/api/undo"), {
      method: "POST",
      headers: mergeHeaders(auth.apiToken || null)
    });
  }, [auth.apiToken]);

  useEffect(() => {
    document.body.dataset.theme = auth.theme;
  }, [auth.theme]);

  return (
    <main className="app-shell">
      <header className="topbar">
        <h1>Blender Frontend Web</h1>
        <div className="topbar-actions">
          <span className="status-tag">主题：{auth.theme}</span>
          <span className="status-tag">认证：{auth.isAuthenticated ? "Token 模式" : "匿名"}</span>
        </div>
      </header>

      <section className="grid-layout">
        <ViewportPreview
          snapshot={viewport.snapshot}
          loading={viewport.loading}
          wsState={viewport.wsState}
          transportMode={webrtc.transportMode}
          recommendedMode={webrtc.recommendedMode}
          onTransportModeChange={webrtc.setTransportMode}
          remoteStream={webrtc.remoteStream}
          localStream={webrtc.localStream}
          webrtcConnected={webrtc.connected}
          peers={webrtc.peers}
          onStartPublishing={webrtc.publishLocalCamera}
        />

        <ToolBar
          onUndo={undo}
          onOpenExport={() => setIsExportOpen(true)}
          onOpenSettings={() => setIsSettingsOpen(true)}
          onOpenShare={() => setIsShareOpen(true)}
        />

        <ActionPreview actions={chat.pendingActions} onConfirm={chat.confirmAction} />

        <ChatPanel
          messages={chat.messages}
          streamingText={chat.streamingText}
          isSending={chat.isSending}
          connectionText={chat.connectionText}
          onSend={sendMessage}
        />
      </section>

      <SettingsModal
        open={isSettingsOpen}
        initialApiToken={auth.apiToken}
        theme={auth.theme}
        onClose={() => setIsSettingsOpen(false)}
        onSave={(settings) => {
          auth.setApiToken(settings.apiToken);
          auth.setTheme(settings.theme);
        }}
      />

      <FileExport open={isExportOpen} token={auth.apiToken || null} onClose={() => setIsExportOpen(false)} />
      <ShareLink open={isShareOpen} token={auth.apiToken || null} onClose={() => setIsShareOpen(false)} />
    </main>
  );
}
