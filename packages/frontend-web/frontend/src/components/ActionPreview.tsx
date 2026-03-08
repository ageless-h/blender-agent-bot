import type { PendingAction } from "../types";

interface ActionPreviewProps {
  actions: PendingAction[];
  onConfirm: (actionId: string) => Promise<void>;
}

export function ActionPreview(props: ActionPreviewProps) {
  const { actions, onConfirm } = props;

  return (
    <section className="panel pending-panel">
      <header className="panel-header">
        <h2>待确认操作</h2>
      </header>

      {actions.length === 0 ? <p className="muted">暂无待确认操作。</p> : null}

      {actions.map((action) => (
        <article key={action.id} className="pending-item">
          <p>{action.message}</p>
          <div className="pending-meta">
            <span>{action.user}</span>
            <span>{new Date(action.created_at).toLocaleTimeString()}</span>
          </div>
          <button onClick={() => void onConfirm(action.id)}>确认执行</button>
        </article>
      ))}
    </section>
  );
}
