interface ToolBarProps {
  onUndo: () => Promise<void>;
  onOpenExport: () => void;
  onOpenSettings: () => void;
  onOpenShare: () => void;
}

export function ToolBar(props: ToolBarProps) {
  const { onUndo, onOpenExport, onOpenSettings, onOpenShare } = props;

  return (
    <section className="panel toolbar-panel">
      <header className="panel-header">
        <h2>工具栏</h2>
      </header>

      <div className="toolbar-actions">
        <button onClick={() => void onUndo()}>撤销</button>
        <button onClick={onOpenExport}>导出</button>
        <button onClick={onOpenShare}>分享</button>
        <button onClick={onOpenSettings}>设置</button>
      </div>
    </section>
  );
}
