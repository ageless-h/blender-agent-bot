# Frontend Blender 模块 — 详细规格与开发清单

> 模块: `packages/frontend-blender`  
> 状态: 新建  
> 优先级: Phase 1 (核心前端)

---

## 1. 模块目标

在 Blender 侧边栏实现完整的 AI 聊天面板，让艺术家不离开 Blender 即可通过自然语言驱动 3D 操作。

---

## 2. UI 面板 (`panels/`)

### 2.1 聊天面板 (`chat_panel.py`)

- [ ] `BLENDERAGENT_PT_chat` — 主聊天面板(N面板/侧边栏)
- [ ] 消息列表展示(AI消息 + 用户消息)
- [ ] 文本输入框 + 发送按钮
- [ ] 消息气泡样式(区分AI/用户)
- [ ] 截图预览嵌入(缩略图)
- [ ] 每条AI消息旁的撤销按钮
- [ ] 加载中动画/状态指示
- [ ] 消息滚动与历史查看

### 2.2 设置面板 (`settings_panel.py`)

- [ ] `BLENDERAGENT_PT_settings` — 设置面板
- [ ] LLM模型选择下拉框(云端/本地)
- [ ] API Key输入(安全存储)
- [ ] 本地模型端点配置(Ollama/vLLM URL)
- [ ] 安全等级选择(保守/标准/高级)
- [ ] 角色模板选择(architect/character/game_assets/beginner)
- [ ] Agent Core连接状态显示

### 2.3 预览面板 (`preview_panel.py`)

- [ ] `BLENDERAGENT_PT_preview` — 操作预览面板
- [ ] 即将执行的操作列表展示
- [ ] 操作安全等级标记(颜色区分)
- [ ] 确认/拒绝/修改按钮
- [ ] 执行进度条

---

## 3. 操作符 (`operators/`)

### 3.1 聊天操作 (`chat_ops.py`)

- [ ] `BLENDERAGENT_OT_send_message` — 发送用户消息
- [ ] `BLENDERAGENT_OT_clear_history` — 清空聊天历史
- [ ] `BLENDERAGENT_OT_copy_message` — 复制消息内容
- [ ] `BLENDERAGENT_OT_retry_last` — 重试上一条指令
- [ ] `BLENDERAGENT_OT_stop_generation` — 停止AI生成

### 3.2 撤销操作 (`undo_ops.py`)

- [ ] `BLENDERAGENT_OT_undo_action` — 撤销特定AI操作
- [ ] `BLENDERAGENT_OT_undo_all` — 撤销所有AI操作(回到初始状态)
- [ ] 撤销栈管理(消息ID <-> 撤销步骤映射)

### 3.3 确认操作 (`confirm_ops.py`)

- [ ] `BLENDERAGENT_OT_confirm_action` — 确认执行预览中的操作
- [ ] `BLENDERAGENT_OT_reject_action` — 拒绝预览中的操作
- [ ] `BLENDERAGENT_OT_modify_action` — 修改操作参数后执行

---

## 4. Agent Core 通信桥 (`bridge/`)

### 4.1 子进程管理 (`subprocess_bridge.py`)

- [ ] Agent Core子进程启动(随Addon启用自动启动)
- [ ] 子进程健康检查与自动重启
- [ ] 优雅关闭(随Addon禁用自动停止)
- [ ] 子进程日志转发
- [ ] 环境变量传递(API Key等)

### 4.2 消息处理 (`message_handler.py`)

- [ ] Stdin/Stdout消息编码/解码(JSON)
- [ ] 流式响应处理(逐token显示)
- [ ] 消息队列(防止并发冲突)
- [ ] 超时处理
- [ ] 错误消息解析与用户友好展示

---

## 5. Addon 注册 (`__init__.py`)

- [ ] `bl_info` 元数据定义
- [ ] `register()` — 注册所有面板/操作符/属性
- [ ] `unregister()` — 注销所有面板/操作符/属性
- [ ] Addon首选项面板(API Key/默认模型等)
- [ ] 版本兼容检查(Blender 4.2+)
- [ ] Agent Core子进程生命周期管理

---

## 6. 场景感知

- [ ] 自动检测当前选中物体(发送给Agent作为上下文)
- [ ] 自动检测当前活动编辑器类型
- [ ] 支持"让它变大" = 对当前选中物体操作

---

## 7. 多模态输入

- [ ] 支持拖入参考图(发送给视觉模型)
- [ ] 支持粘贴截图
- [ ] 参考图预览显示

---

## 8. 测试清单

- [ ] 面板注册/注销测试
- [ ] 操作符执行测试
- [ ] 子进程启动/停止测试
- [ ] 消息编解码测试
- [ ] 流式响应显示测试
- [ ] 撤销功能测试
- [ ] 多版本Blender UI兼容测试
