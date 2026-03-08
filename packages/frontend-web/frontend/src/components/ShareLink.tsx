import { FormEvent, useState } from "react";

import { buildApiUrl, mergeHeaders } from "../network";
import type { ShareLinkResult, ShareMode } from "../types";

interface ShareLinkProps {
  open: boolean;
  token: string | null;
  onClose: () => void;
}

export function ShareLink(props: ShareLinkProps) {
  const { open, token, onClose } = props;
  const [ttlSeconds, setTtlSeconds] = useState(3600);
  const [mode, setMode] = useState<ShareMode>("readonly");
  const [result, setResult] = useState<ShareLinkResult | null>(null);
  const [loading, setLoading] = useState(false);

  if (!open) {
    return null;
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    const response = await fetch(buildApiUrl("/api/auth/share-link"), {
      method: "POST",
      headers: mergeHeaders(token),
      body: JSON.stringify({ ttl_seconds: ttlSeconds, mode })
    });
    if (response.ok) {
      const payload = (await response.json()) as ShareLinkResult;
      setResult(payload);
    }
    setLoading(false);
  }

  async function copyLink() {
    if (!result) {
      return;
    }
    const url = `${window.location.origin}${result.url_path}`;
    await navigator.clipboard.writeText(url);
  }

  return (
    <div className="modal-mask" role="dialog" aria-modal="true">
      <form className="modal-card" onSubmit={submit}>
        <h3>分享链接</h3>

        <label>
          模式
          <select value={mode} onChange={(event) => setMode(event.target.value as ShareMode)}>
            <option value="readonly">只读观看</option>
            <option value="interactive">可交互</option>
          </select>
        </label>

        <label>
          过期时间（秒）
          <input
            type="number"
            value={ttlSeconds}
            min={60}
            max={86400}
            onChange={(event) => setTtlSeconds(Number(event.target.value))}
          />
        </label>

        {result ? (
          <div className="result-box">
            <p>会话：{result.session_id}</p>
            <p>过期：{new Date(result.expires_at).toLocaleString()}</p>
            <a href={result.url_path} target="_blank" rel="noreferrer">
              打开分享链接
            </a>
            <button type="button" onClick={() => void copyLink()}>
              复制链接
            </button>
          </div>
        ) : null}

        <div className="modal-actions">
          <button type="button" onClick={onClose}>
            关闭
          </button>
          <button type="submit" disabled={loading}>
            {loading ? "生成中" : "生成链接"}
          </button>
        </div>
      </form>
    </div>
  );
}
