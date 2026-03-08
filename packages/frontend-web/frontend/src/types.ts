export type ChatRole = "user" | "assistant" | "system";
export type ShareMode = "readonly" | "interactive";

export interface ChatEntry {
  id: string;
  role: ChatRole;
  user: string;
  message: string;
  created_at: string;
}

export interface ChatResponse {
  reply: string;
  requires_confirmation: boolean;
  pending_action_id: string | null;
}

export interface ViewportSnapshot {
  mime_type: string;
  image_base64: string;
  generated_at: string;
}

export interface PendingAction {
  id: string;
  user: string;
  message: string;
  created_at: string;
}

export interface ExportResult {
  file_id: string;
  filename: string;
  format: "blend" | "fbx" | "glb" | "obj" | "stl";
  download_url: string;
  expires_at: string;
}

export interface ShareLinkResult {
  session_id: string;
  token: string;
  url_path: string;
  expires_at: string;
  mode: ShareMode;
}
