import { FormEvent, useEffect, useState } from "react";

import type { ThemeMode } from "../hooks/useAuth";

interface SettingsModalProps {
  open: boolean;
  initialApiToken: string;
  theme: ThemeMode;
  onSave: (settings: { apiToken: string; theme: ThemeMode; model: string }) => void;
  onClose: () => void;
}

export function SettingsModal(props: SettingsModalProps) {
  const { open, initialApiToken, theme, onSave, onClose } = props;
  const [apiToken, setApiToken] = useState(initialApiToken);
  const [model, setModel] = useState("gpt-4.1-mini");
  const [currentTheme, setCurrentTheme] = useState<ThemeMode>(theme);

  useEffect(() => {
    setApiToken(initialApiToken);
  }, [initialApiToken, open]);

  useEffect(() => {
    setCurrentTheme(theme);
  }, [theme, open]);

  if (!open) {
    return null;
  }

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSave({ apiToken: apiToken.trim(), theme: currentTheme, model: model.trim() || "gpt-4.1-mini" });
    onClose();
  }

  return (
    <div className="modal-mask" role="dialog" aria-modal="true">
      <form className="modal-card" onSubmit={submit}>
        <h3>设置</h3>

        <label>
          模型
          <input value={model} onChange={(event) => setModel(event.target.value)} />
        </label>

        <label>
          API Token
          <input value={apiToken} onChange={(event) => setApiToken(event.target.value)} />
        </label>

        <label>
          主题
          <select value={currentTheme} onChange={(event) => setCurrentTheme(event.target.value as ThemeMode)}>
            <option value="dark">深色</option>
            <option value="light">浅色</option>
          </select>
        </label>

        <div className="modal-actions">
          <button type="button" onClick={onClose}>
            取消
          </button>
          <button type="submit">保存</button>
        </div>
      </form>
    </div>
  );
}
