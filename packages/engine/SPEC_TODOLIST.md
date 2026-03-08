# Engine 模块 — 详细规格与开发清单

> 模块: `packages/engine`  
> 状态: 从 blender-mcp 重构  
> 优先级: Phase 0 (基础重构)

---

## 1. 模块目标

将 blender-mcp 的核心引擎逻辑抽取为独立包 `blender-engine`，与 MCP 协议层完全解耦，使其可被 Agent Core、CLI、Web 等多个上层模块复用。

---

## 2. 工具层规格 (`tools/`)

### 2.1 感知层 (`tools/perception/`) — 11 个工具

- [x] `get_objects` — 获取场景中所有对象列表
- [x] `get_object_info` — 获取单个对象详细信息
- [x] `get_scene` — 获取场景全局信息
- [x] `get_node_tree` — 获取节点树结构
- [x] `get_modifiers` — 获取修改器列表
- [x] `get_constraints` — 获取约束列表
- [x] `get_materials` — 获取材质列表
- [x] `get_animation_data` — 获取动画数据
- [x] `get_render_settings` — 获取渲染设置
- [x] `get_world_settings` — 获取世界环境设置
- [x] `capture_viewport` — 截取视口截图(base64)

### 2.2 声明式写入层 (`tools/declarative/`) — 3 个工具

- [x] `edit_nodes` — 声明式节点编辑(JSON描述->节点图)
- [x] `edit_animation` — 声明式动画编辑(关键帧批量操作)
- [x] `edit_sequencer` — 声明式序列编辑器操作

### 2.3 命令式写入层 (`tools/imperative/`) — 9 个工具

- [x] `create_object` — 创建对象(支持所有基本体)
- [x] `modify_object` — 修改对象属性(位置/旋转/缩放等)
- [x] `delete_object` — 删除对象
- [x] `manage_material` — 创建/编辑/分配材质
- [x] `add_modifier` — 添加修改器
- [x] `add_constraint` — 添加约束
- [x] `set_parent` — 设置父子关系
- [x] `manage_collection` — 管理集合
- [x] `setup_scene` — 设置场景参数(渲染/世界/相机)

### 2.4 后备层 (`tools/fallback/`) — 3 个工具

- [x] `execute_script` — 执行任意Python脚本(最高权限)
- [x] `execute_operator` — 调用bpy.ops操作符
- [x] `import_export` — 导入/导出文件(.blend/.fbx/.glb/.obj)

---

## 3. 传输层规格 (`transport/`)

- [x] `SocketTransport` — TCP Socket通信(当前blender-mcp模式)
- [x] `StdioTransport` — Stdin/Stdout传输(子进程启动模式)
- [x] `TransportBase` — 抽象基类，定义统一接口
- [x] 支持多会话并发(Web多用户场景)
- [x] 连接健康检查与自动重连

---

## 4. Addon层规格 (`addon/`)

- [x] `__init__.py` — Addon注册/注销入口(bl_info)
- [x] `operators.py` — 自定义Operator(UNDO支持)
  - [x] `BLENDERAGENT_OT_execute` — AI操作执行器(bl_options={'REGISTER','UNDO'})
  - [x] 失败时返回CANCELLED不污染撤销栈
- [x] `panels.py` — 基础UI面板
- [x] `timers.py` — bpy.app.timers轮询(每0.1s)
  - [x] 非阻塞主线程轮询
  - [x] 命令队列消费

---

## 5. 执行器规格 (`executor/`)

- [x] `sandbox.py` — 沙箱执行环境
  - [x] AST静态分析黑名单(os.system, subprocess, 网络请求, 文件删除)
  - [x] 执行超时保护
- [x] `context_override.py` — 动态上下文捕获
  - [x] VIEW_3D区域/窗口/屏幕自动查找
  - [x] 4.5+ temp_override兼容
  - [x] 4.2 LTS旧版上下文覆盖兼容

---

## 6. 核心设计约束

- [x] 用名称(str)引用对象，不缓存bpy引用(undo后引用失效)
- [ ] 所有bpy操作仅在主线程通过timers执行
- [x] 不在exec内部调用bpy.ops.ed.undo()
- [ ] undo后立即清除所有缓存引用

---

## 7. 重构任务

- [x] 从blender-mcp抽取engine层为独立包
- [x] 定义统一的AgentRequest/AgentResponse消息协议
- [ ] 确保重构后MCP模式完全兼容
- [ ] 所有现有MCP测试通过
- [ ] `uvx ageless-blender-mcp`继续可用

---

## 8. 版本兼容矩阵

- [ ] Blender 4.2 LTS — 最低要求，兼容旧版上下文API
- [ ] Blender 4.5 LTS — 推荐版本，temp_override稳定
- [ ] Blender 5.0/5.1 — 完全支持
- [ ] Blender 5.2 — 预留接口

---

## 9. 测试清单

- [ ] 26个工具的单元测试
- [x] Socket/Stdio传输层集成测试
- [ ] Addon注册/注销测试
- [ ] 撤销/重做机制验证
- [ ] 多版本Blender兼容性测试
- [x] 沙箱安全性测试(恶意代码注入)
- [ ] 多会话并发测试
