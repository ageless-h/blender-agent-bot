import { useCallback, useEffect, useState } from "react";

import { buildApiUrl, mergeHeaders } from "../network";
import type { ViewportSnapshot } from "../types";
import { useWebSocket } from "./useWebSocket";

interface UseViewportOptions {
  token: string | null;
}

export function useViewport(options: UseViewportOptions) {
  const { token } = options;
  const [snapshot, setSnapshot] = useState<ViewportSnapshot | null>(null);
  const [loading, setLoading] = useState(true);
  const ws = useWebSocket("/ws/viewport", { token });

  const fetchSnapshot = useCallback(async () => {
    const response = await fetch(buildApiUrl("/api/viewport"), {
      headers: mergeHeaders(token)
    });
    if (!response.ok) {
      return;
    }
    const payload = (await response.json()) as ViewportSnapshot;
    setSnapshot(payload);
    setLoading(false);
  }, [token]);

  useEffect(() => {
    if (!ws.lastMessage || typeof ws.lastMessage !== "object") {
      return;
    }
    const event = ws.lastMessage as Record<string, unknown>;
    if (event.type !== "viewport") {
      return;
    }
    const data = event.data as ViewportSnapshot;
    setSnapshot(data);
    setLoading(false);
  }, [ws.lastMessage]);

  useEffect(() => {
    void fetchSnapshot();

    if (ws.state === "open") {
      return;
    }

    const timer = window.setInterval(() => {
      void fetchSnapshot();
    }, 2500);

    return () => {
      window.clearInterval(timer);
    };
  }, [fetchSnapshot, ws.state]);

  return {
    snapshot,
    loading,
    wsState: ws.state
  };
}
