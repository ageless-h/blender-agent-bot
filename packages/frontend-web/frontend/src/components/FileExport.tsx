import { FormEvent, useState } from "react";

import { buildApiUrl, mergeHeaders } from "../network";
import type { ExportResult } from "../types";

interface FileExportProps {
  open: boolean;
  token: string | null;
  onClose: () => void;
}

const formats = ["blend", "fbx", "glb", "obj", "stl"] as const;

export function FileExport(props: FileExportProps) {
  const { open, token, onClose } = props;
  const [format, setFormat] = useState<(typeof formats)[number]>("glb");
  const [filename, setFilename] = useState("");
  const [result, setResult] = useState<ExportResult | null>(null);
  const [loading, setLoading] = useState(false);

  if (!open) {
    return null;
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    const response = await fetch(buildApiUrl("/api/export"), {
      method: "POST",
      headers: mergeHeaders(token),
      body: JSON.stringify({ format, filename: filename.trim() || undefined })
    });
    if (response.ok) {
      const payload = (await response.json()) as ExportResult;
      setResult(payload);
    }
    setLoading(false);
  }

  return (
    <div className="modal-mask" role="dialog" aria-modal="true">
      <form className="modal-card" onSubmit={submit}>
        <h3>文件导出</h3>

        <label>
          格式
          <select value={format} onChange={(event) => setFormat(event.target.value as (typeof formats)[number])}>
            {formats.map((item) => (
              <option key={item} value={item}>
                .{item}
              </option>
            ))}
          </select>
        </label>

        <label>
          文件名（可选）
          <input value={filename} onChange={(event) => setFilename(event.target.value)} placeholder={`scene_export.${format}`} />
        </label>

        {result ? (
          <div className="result-box">
            <p>导出完成：{result.filename}</p>
            <a href={buildApiUrl(result.download_url)} target="_blank" rel="noreferrer">
              下载文件
            </a>
          </div>
        ) : null}

        <div className="modal-actions">
          <button type="button" onClick={onClose}>
            关闭
          </button>
          <button type="submit" disabled={loading}>
            {loading ? "导出中" : "开始导出"}
          </button>
        </div>
      </form>
    </div>
  );
}
