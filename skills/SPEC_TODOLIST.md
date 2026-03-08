# Skills 模块 — 详细规格与开发清单

> 模块: `skills`  
> 状态: Phase 1 内容完成；执行联调待完成  
> 优先级: Phase 1 (内置) + Phase 3 (进化与市场)

---

## 1. 模块目标

构建可复用、可共享、可进化的技能库，让常见 3D 操作无需 LLM 即可快速执行，并通过 undo 驱动的反馈机制持续优化。

### 1.1 复查结论（2026-03-05）

- 已完成：Phase 1 内置技能文件清单（24 个 YAML）与格式字段落地。
- 未完成：SkillExecutor 与 engine 参数契约联调，当前 Capsule 仍存在 DSL 到底层工具参数的映射缺口。
- 风险项 1：Skill 数据格式与执行器格式不一致（`tool/args` vs `tool_name/arguments`）。
- 风险项 2：占位符格式不一致（内置 YAML 为 `$var`，执行器当前替换逻辑为 `${var}`）。
- 风险项 3：`execute_skill` 仅在 Skill 数据层出现，尚未在 engine 工具定义中提供同名工具。
- 风险项 4：大量 `modify_object` / `manage_material(assign)` 参数键与 engine 要求不一致（`name` vs `object_name`，`object_names` vs `object_name`）。

---

## 2. 内置技能包 (`builtin/`) — Phase 1

### 2.1 家具类

- [x] `low_poly_table.yaml` — 低面桌子
- [x] `simple_chair.yaml` — 简单椅子
- [x] `bookshelf.yaml` — 书架
- [x] `desk_lamp.yaml` — 台灯
- [x] `sofa.yaml` — 沙发

### 2.2 建筑类

- [x] `basic_room.yaml` — 基础房间(地板+四面墙)
- [x] `window.yaml` — 窗户(Boolean切割)
- [x] `door.yaml` — 门
- [x] `staircase.yaml` — 楼梯
- [x] `simple_house.yaml` — 简单小屋(组合技能)

### 2.3 材质类

- [x] `metal_material.yaml` — 金属材质(Principled BSDF)
- [x] `wood_material.yaml` — 木纹材质
- [x] `glass_material.yaml` — 玻璃材质
- [x] `emission_material.yaml` — 发光材质
- [x] `pbr_material_template.yaml` — PBR材质模板

### 2.4 灯光与场景类

- [x] `three_point_lighting.yaml` — 三点布光
- [x] `hdri_setup.yaml` — HDRI环境光设置
- [x] `studio_lighting.yaml` — 摄影棚布光
- [x] `camera_orbit.yaml` — 相机环绕动画
- [x] `render_setup_eevee.yaml` — Eevee渲染设置

### 2.5 修改器类

- [x] `subdivision_smooth.yaml` — 细分+平滑
- [x] `bevel_edges.yaml` — 边缘倒角
- [x] `array_circular.yaml` — 环形阵列
- [x] `mirror_object.yaml` — 镜像

---

## 3. Skill Capsule 格式规格

### 3.1 metadata 字段

- [x] name — 技能名称(唯一标识)
- [x] tags — 标签列表(用于模糊匹配)
- [x] description — 自然语言描述
- [x] author — 作者
- [x] version — 版本号
- [x] success_rate — 成功率(0.0-1.0)
- [x] usage_count — 使用次数
- [x] undo_rate — 被撤销比例
- [x] partial_undo_stats — 分步撤销统计

### 3.2 gene 字段

- [x] strategy — 给LLM理解的策略描述(自然语言)
- [x] parameters — 可配置参数(default/range/type)
- [x] constraints — 约束条件

### 3.3 capsule 字段

- [x] steps — 工具调用序列
  - [x] tool — 工具名称
  - [x] args — 参数(支持$变量引用)
  - [x] undo_group — 撤销分组
  - [x] condition — 条件执行(可选)
- [ ] 支持嵌套子技能调用（`simple_house.yaml` 已有 DSL 草案，待 SkillExecutor 实装）

### 3.4 validation 字段

- [x] object_exists — 验证对象存在
- [x] object_count_gte — 验证对象数量
- [x] material_exists — 验证材质存在
- [x] property_check — 验证属性值
- [ ] custom_script — 自定义验证脚本

---

## 4. 社区技能包 (`community/`) — Phase 3

- [ ] 技能包打包格式(.skill.zip)
- [ ] 技能包元数据索引
- [ ] 下载/安装/卸载机制
- [ ] 版本兼容检查
- [ ] 评分与评论系统(可选，需服务端)

---

## 5. 进化机制规格

### 5.1 Undo驱动反馈

- [ ] 监听undo事件(通过UndoAwareTracker)
- [ ] 记录每个Skill的undo_rate
- [ ] 分步撤销统计(partial_undo_stats)
- [ ] 捕获用户undo后的手动修正操作

### 5.2 自动优化触发

- [ ] undo_rate超过阈值(如>0.2)时标记待优化
- [ ] 高undo_rate步骤自动发送给LLM重新优化
- [ ] A/B测试: 新旧版本并行运行对比
- [ ] 优化结果自动更新Skill文件

---

## 6. 测试清单

- [ ] YAML格式解析测试(所有内置技能)
- [ ] 参数替换测试($变量)
- [ ] 验证规则执行测试
- [ ] 技能匹配准确率测试
- [ ] 技能执行端到端测试(在Blender中)
- [ ] 撤销分组正确性测试
- [ ] 社区包打包/解包测试
- [ ] 与 engine 工具参数契约联调测试
