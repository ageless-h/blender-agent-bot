# Frontend Web 模块 — 详细规格与开发清单

> 模块: `packages/frontend-web`  
> 状态: 新建  
> 优先级: Phase 2 (扩展前端)

---

## 1. 模块目标

通过浏览器远程控制 Blender，支持实时视口预览、聊天交互、多人协作和文件导出。

---

## 2. Python 后端 (`src/`)

### 2.1 FastAPI 应用 (`app.py`)

- [x] FastAPI 应用初始化与中间件配置
- [x] CORS 配置(跨域支持)
- [x] 静态文件服务(前端构建产物)
- [x] 启动时连接 Agent Core
- [x] 优雅关闭处理

### 2.2 REST API 路由 (`api/routes.py`)

- [x] `POST /api/chat` — 发送聊天消息(同步)
- [x] `GET /api/history` — 获取聊天历史
- [x] `GET /api/scene` — 获取当前场景信息
- [x] `GET /api/viewport` — 获取视口截图
- [x] `POST /api/export` — 导出文件(.blend/.fbx/.glb)
- [x] `GET /api/download/{file_id}` — 下载导出文件
- [x] `GET /api/status` — 连接状态与系统信息
- [x] `POST /api/undo` — 撤销操作
- [x] `POST /api/confirm` — 确认待执行操作

### 2.3 WebSocket (`api/websocket.py`)

- [x] `WS /ws/chat` — 实时聊天(流式响应)
- [x] `WS /ws/viewport` — 视口实时推送(定时截图/WebRTC)
- [x] 连接管理(多用户并发)
- [x] 心跳检测与自动重连
- [x] 消息序列化/反序列化

### 2.4 认证 (`api/auth.py`)

- [x] 简单Token认证(可选)
- [x] 临时分享链接生成
- [x] 会话管理

---

## 3. React 前端 (`frontend/`)

### 3.1 核心组件

- [x] `ChatPanel` — 聊天消息列表 + 输入框
- [x] `ViewportPreview` — 3D视口实时预览
- [x] `ToolBar` — 操作工具栏(撤销/导出/设置)
- [x] `SettingsModal` — 设置弹窗(模型选择/API Key)
- [x] `ActionPreview` — 操作预览确认面板
- [x] `FileExport` — 文件导出下载面板
- [x] `ShareLink` — 分享链接生成/管理

### 3.2 Hooks

- [x] `useWebSocket` — WebSocket连接管理
- [x] `useChat` — 聊天状态管理
- [x] `useViewport` — 视口预览状态
- [x] `useAuth` — 认证状态

### 3.3 UI/UX

- [x] 响应式布局(桌面/平板/手机)
- [x] 深色/浅色主题
- [x] 流式消息显示(逐token)
- [x] 截图预览嵌入
- [x] 加载状态指示

---

## 4. 实时视口方案

- [x] 方案A: WebRTC视频流(低延迟，高带宽)
- [x] 方案B: 定时截图刷新(简单，低带宽)
- [x] 自适应选择(根据网络条件)

---

## 5. 文件导出

- [x] 支持格式: .blend, .fbx, .glb, .obj, .stl
- [x] 服务端临时文件管理(自动清理)
- [x] 导出进度显示

---

## 6. 分享功能

- [x] 生成临时访问链接(TTL可配置)
- [x] 只读模式(观看AI建模过程)
- [x] 可交互模式(远程操控)

---

## 7. 测试清单

- [x] FastAPI路由单元测试
- [x] WebSocket连接/断线测试
- [x] React组件渲染测试
- [x] 流式消息端到端测试
- [x] 视口预览延迟测试
- [x] 多用户并发测试
- [x] 文件导出/下载测试
