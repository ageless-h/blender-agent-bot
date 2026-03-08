# Examples 模块 — 详细规格与开发清单

> 模块: `examples`  
> 状态: **已完成（内容交付）**  
> 优先级: Phase 3 (内容建设)

---

## 1. 模块目标

提供丰富的使用示例，降低用户上手门槛，展示 BlenderAgentBot 的全部能力。

---

## 2. System Prompt 模板 (`prompts/`)

### 2.1 内置角色模板

- [x] `architect.md` — 建筑可视化专家
  - [x] 擅长: 室内外建筑场景、空间布局、材质真实感
  - [x] 默认工具偏好: `setup_scene`, `manage_material`, `three_point_lighting`
- [x] `character.md` — 角色建模专家
  - [x] 擅长: 人物/角色建模、骨骼绑定、表情动画
  - [x] 默认工具偏好: `create_object`, `add_modifier(Mirror/Subdivision)`
- [x] `game_assets.md` — 游戏资产专家
  - [x] 擅长: 低面数建模、LOD管理、UV展开、PBR材质
  - [x] 默认工具偏好: `create_object`, `manage_material`, `import_export`
- [x] `beginner.md` — 教学助手
  - [x] 擅长: 解释每步操作、教学引导、概念说明
  - [x] 额外行为: 每步操作后附带解释说明

### 2.2 自定义模板

- [x] `custom_template.md` — 自定义角色模板说明文档
- [x] 模板变量说明（`{{model_name}}`, `{{blender_version}}` 等）
- [x] 模板继承机制（Base + Model + Persona 三层）

---

## 3. 实战食谱 (`recipes/`) — 20 Cookbook

### 3.1 入门系列

- [x] `01_first_cube.md` — 你的第一个立方体
- [x] `02_simple_house.md` — 建造一个简单小屋
- [x] `03_material_setup.md` — 材质与纹理基础
- [x] `04_lighting_scene.md` — 场景布光入门
- [x] `05_animation_basics.md` — 动画基础

### 3.2 进阶系列

- [x] `06_low_poly_landscape.md` — 低面风景场景
- [x] `07_interior_design.md` — 室内设计场景
- [x] `08_product_visualization.md` — 产品可视化
- [x] `09_character_base_mesh.md` — 角色基础网格
- [x] `10_procedural_materials.md` — 程序化材质

### 3.3 高级系列

- [x] `11_batch_asset_generation.md` — 批量资产生成
- [x] `12_scene_from_reference.md` — 参考图驱动建模
- [x] `13_animation_sequence.md` — 复杂动画序列
- [x] `14_render_pipeline.md` — 渲染流水线
- [x] `15_custom_skills.md` — 自定义技能包制作

### 3.4 集成系列

- [x] `16_cursor_workflow.md` — Cursor + Blender 工作流
- [x] `17_cli_batch_mode.md` — CLI 批处理实战
- [x] `18_web_collaboration.md` — Web 多人协作
- [x] `19_local_model_setup.md` — 本地模型配置（Ollama）
- [x] `20_pipeline_integration.md` — 生产 Pipeline 集成

---

## 4. 批处理 Pipeline (`pipelines/`)

### 4.1 示例 Pipeline

- [x] `batch_render.yaml` — 多角度批量渲染
  - [x] 相机位置列表
  - [x] 渲染参数配置
  - [x] 输出路径模板
- [x] `asset_generator.yaml` — 批量资产生成
  - [x] 参数化家具生成（尺寸/材质变体）
  - [x] 自动导出（`.glb`）
- [x] `scene_setup.yaml` — 标准场景初始化
  - [x] 灯光、相机、世界环境一键配置
  - [x] 适合作为项目模板

### 4.2 Pipeline YAML 格式文档

- [x] 完整语法说明（见 `pipelines/PIPELINE_FORMAT.md`）
- [x] 变量与参数替换
- [x] 条件分支与循环
- [x] 错误处理策略

---

## 5. 测试清单

- [x] Prompt 模板结构完整性检查（标题、角色、流程、约束）
- [x] Pipeline YAML 样例语法检查（字段结构与占位符一致性）
- [x] `blender-agent run --dry-run` 结构校验（3 个示例脚本通过）
- [ ] 食谱步骤可执行性实机验证（需 Blender 运行环境）
- [ ] Pipeline 端到端执行测试（需主程序执行器）

---

## 6. 本次交付摘要

- 新增 5 个 Prompt 模板文档
- 新增 20 个实战食谱文档
- 新增 3 个 Pipeline YAML + 1 个格式规范文档
- 更新模块 README，补全学习路径与维护约定
