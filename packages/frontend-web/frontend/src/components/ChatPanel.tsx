import { FormEvent, useState } from "react";

import type { ChatEntry } from "../types";

interface ChatPanelProps {
  messages: ChatEntry[];
  streamingText: string;
  isSending: boolean;
  connectionText: string;
  onSend: (message: string) => Promise<void>;
}

export function ChatPanel(props: ChatPanelProps) {
  const { messages, streamingText, isSending, connectionText, onSend } = props;
  const [input, setInput] = useState("");

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const value = input.trim();
    if (!value) {
      return;
    }
    setInput("");
    await onSend(value);
  }

  return (
    <section className="panel chat-panel">
      <header className="panel-header">
        <h2>聊天面板</h2>
        <span className="status-tag">{connectionText}</span>
      </header>

      <div className="chat-list">
        {messages.length === 0 ? <p className="muted">暂无消息，先发一条试试。</p> : null}
        {messages.map((message) => (
          <article key={message.id} className={`chat-item ${message.role}`}>
            <div className="chat-meta">
              <strong>{message.user}</strong>
              <time>{new Date(message.created_at).toLocaleTimeString()}</time>
            </div>
            <p>{message.message}</p>
          </article>
        ))}

        {streamingText ? (
          <article className="chat-item assistant streaming">
            <div className="chat-meta">
              <strong>assistant</strong>
              <time>streaming</time>
            </div>
            <p>{streamingText}</p>
          </article>
        ) : null}
      </div>

      <form className="chat-input" onSubmit={submit}>
        <input
          value={input}
          onChange={(event) => setInput(event.target.value)}
          placeholder="输入对 Blender 的指令..."
          disabled={isSending}
        />
        <button type="submit" disabled={isSending || input.trim().length === 0}>
          {isSending ? "发送中" : "发送"}
        </button>
      </form>
    </section>
  );
}
