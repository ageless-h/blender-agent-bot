const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "";
const WS_BASE_URL = import.meta.env.VITE_WS_BASE_URL ?? "";

export function buildApiUrl(path: string): string {
  if (/^https?:\/\//.test(path)) {
    return path;
  }
  if (!API_BASE_URL) {
    return path;
  }
  return `${API_BASE_URL.replace(/\/$/, "")}${path}`;
}

export function buildWsUrl(path: string): string {
  if (/^wss?:\/\//.test(path)) {
    return path;
  }
  if (WS_BASE_URL) {
    return `${WS_BASE_URL.replace(/\/$/, "")}${path}`;
  }
  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  return `${protocol}://${window.location.host}${path}`;
}

export function mergeHeaders(token: string | null): HeadersInit {
  if (!token) {
    return { "Content-Type": "application/json" };
  }
  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`
  };
}
