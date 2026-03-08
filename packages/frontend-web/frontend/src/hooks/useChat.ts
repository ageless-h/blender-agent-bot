import { useCallback, useEffect, useMemo, useState } from "react";

import { buildApiUrl, mergeHeaders } from "../network";
import type { ChatEntry, ChatResponse, PendingAction } from "../types";
import { useWebSocket } from "./useWebSocket";

interface UseChatOptions {
  token: string | null;
}

function nowIso() {
  return new Date().toISOString();
}

export function useChat(options: UseChatOptions) {
  const { token } = options;
  const [messages, setMessages] = useState<ChatEntry[]>([]);
  const [pendingActions, setPendingActions] = useState<PendingAction[]>([]);
  const [isSending, setIsSending] = useState(false);
  const [streamingText, setStreamingText] = useState("");

  const ws = useWebSocket("/ws/chat", { token });

  const fetchHistory = useCallback(async () => {
    const response = await fetch(buildApiUrl("/api/history?limit=200"), {
      headers: mergeHeaders(token)
    });
    if (!response.ok) {
      return;
    }
    const payload = (await response.json()) as { items: ChatEntry[] };
    setMessages(payload.items);
  }, [token]);

  const fetchPendingActions = useCallback(async () => {
    const response = await fetch(buildApiUrl("/api/pending"), {
      headers: mergeHeaders(token)
    });
    if (!response.ok) {
      return;
    }
    const payload = (await response.json()) as { items: PendingAction[] };
    setPendingActions(payload.items);
  }, [token]);

  useEffect(() => {
    void fetchHistory();
    void fetchPendingActions();
  }, [fetchHistory, fetchPendingActions]);

  useEffect(() => {
    if (!ws.lastMessage || typeof ws.lastMessage !== "object") {
      return;
    }
    const event = ws.lastMessage as Record<string, unknown>;
    const type = String(event.type ?? "");

    if (type === "chat_message") {
      const data = event.data as ChatEntry;
      setMessages((previous) => {
        if (previous.some((item) => item.id === data.id)) {
          return previous;
        }
        return [...previous, data];
      });
    }

    if (type === "token") {
      setStreamingText((current) => current + String(event.value ?? ""));
    }

    if (type === "done") {
      setStreamingText("");
      void fetchHistory();
      void fetchPendingActions();
    }
  }, [fetchHistory, fetchPendingActions, ws.lastMessage]);

  const sendMessage = useCallback(
    async (user: string, message: string) => {
      const trimmed = message.trim();
      if (!trimmed) {
        return;
      }

      setIsSending(true);
      setMessages((previous) => [
        ...previous,
        {
          id: crypto.randomUUID(),
          role: "user",
          user,
          message: trimmed,
          created_at: nowIso()
        }
      ]);

      const wsSent = ws.sendJson({ type: "message", user, message: trimmed });

      if (!wsSent) {
        const response = await fetch(buildApiUrl("/api/chat"), {
          method: "POST",
          headers: mergeHeaders(token),
          body: JSON.stringify({ user, message: trimmed })
        });
        if (response.ok) {
          const payload = (await response.json()) as ChatResponse;
          setMessages((previous) => [
            ...previous,
            {
              id: crypto.randomUUID(),
              role: "assistant",
              user: "assistant",
              message: payload.reply,
              created_at: nowIso()
            }
          ]);
        }
      }

      setIsSending(false);
      void fetchPendingActions();
    },
    [fetchPendingActions, token, ws]
  );

  const confirmAction = useCallback(
    async (actionId: string) => {
      const response = await fetch(buildApiUrl("/api/confirm"), {
        method: "POST",
        headers: mergeHeaders(token),
        body: JSON.stringify({ action_id: actionId })
      });
      if (response.ok) {
        await fetchHistory();
        await fetchPendingActions();
      }
    },
    [fetchHistory, fetchPendingActions, token]
  );

  const connectionText = useMemo(() => {
    if (ws.state === "open") {
      return "已连接";
    }
    if (ws.state === "connecting") {
      return "连接中";
    }
    return "已断开";
  }, [ws.state]);

  return {
    messages,
    pendingActions,
    isSending,
    sendMessage,
    confirmAction,
    streamingText,
    connectionText
  };
}
