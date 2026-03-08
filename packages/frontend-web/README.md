# Frontend Web — Web 应用

> 远程/协作的入口 — 浏览器即可控制 Blender。

## 概述

Web 前端应用，通过浏览器远程控制 Blender，支持实时视口预览、多人协作和文件导出。后端基于 FastAPI + WebSocket，前端基于 React。

## 架构

```
frontend-web/
├── src/                   # Python 后端 (FastAPI)
│   ├── __init__.py
│   ├── app.py             # FastAPI 应用入口
│   └── api/
│       ├── __init__.py
│       ├── routes.py      # REST API 路由
│       ├── websocket.py   # WebSocket 实时通信
│       └── auth.py        # 认证(可选)
├── frontend/              # React 前端
│   ├── src/
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   ├── components/    # UI 组件
│   │   └── hooks/         # 自定义 Hooks
│   └── public/
├── pyproject.toml
└── SPEC_TODOLIST.md
```

## 核心特性

| 特性 | 说明 |
|:---|:---|
| 实时视口 | WebRTC 视频流或定时截图刷新 |
| 无需本地安装 | Blender + Agent 跑在服务器 |
| 分享链接 | 生成临时链接，他人可实时观看 |
| 文件导出 | 直接在 Web 端下载 .blend/.fbx/.glb |

## 技术栈

- **后端**: FastAPI + WebSocket + uvicorn
- **前端**: React + TypeScript + TailwindCSS
- **通信**: WebSocket (实时流) + REST (文件操作)

## 开发

```bash
# 后端
cd packages/frontend-web
pip install -e ".[dev]"
uvicorn src.app:app --reload

# 前端
cd frontend
npm install && npm run dev
```

## 已实现接口

- `POST /api/chat` 聊天消息（含高风险操作确认）
- `GET /api/history` 聊天历史
- `GET /api/scene` 场景概要
- `GET /api/viewport` 视口截图（SVG Base64）
- `POST /api/export` + `GET /api/download/{file_id}` 导出与下载
- `GET /api/status` 运行状态
- `POST /api/undo` 撤销最近用户消息
- `POST /api/confirm` 确认待执行操作
- `POST /api/auth/share-link` + `POST /api/auth/share-link/verify` 分享链接
- `GET /api/webrtc/config` WebRTC 信令配置

## WebSocket

- `/ws/chat` 实时聊天 + token 流式输出
- `/ws/viewport` 视口实时推送 + 心跳
- `/ws/webrtc/{room_id}` WebRTC SDP/ICE 信令中继

## 测试

```bash
# 后端
pytest -q

# 前端
cd frontend
npm run test
```
