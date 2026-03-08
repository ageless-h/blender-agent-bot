# Skills — 技能库

> 可复用、可共享、可进化的 Skill Capsule 集合。

## 概述

技能库存储所有 Skill Capsule（YAML 格式），分为内置技能包和社区技能包。技能系统借鉴 EvoMap GEP 协议，将 AI 解决问题的经验封装为可复用的工具调用序列。

## 架构

```
skills/
├── builtin/               # 内置技能包 (24)
│   ├── 家具类 (5)
│   ├── 建筑类 (5)
│   ├── 材质类 (5)
│   ├── 灯光与场景类 (5)
│   └── 修改器类 (4)
├── community/             # 社区下载的技能包
│   ├── README.md
│   └── .gitkeep
├── README.md
└── SPEC_TODOLIST.md
```

## 内置技能包清单

### 家具类

- `low_poly_table.yaml`
- `simple_chair.yaml`
- `bookshelf.yaml`
- `desk_lamp.yaml`
- `sofa.yaml`

### 建筑类

- `basic_room.yaml`
- `window.yaml`
- `door.yaml`
- `staircase.yaml`
- `simple_house.yaml`

### 材质类

- `metal_material.yaml`
- `wood_material.yaml`
- `glass_material.yaml`
- `emission_material.yaml`
- `pbr_material_template.yaml`

### 灯光与场景类

- `three_point_lighting.yaml`
- `hdri_setup.yaml`
- `studio_lighting.yaml`
- `camera_orbit.yaml`
- `render_setup_eevee.yaml`

### 修改器类

- `subdivision_smooth.yaml`
- `bevel_edges.yaml`
- `array_circular.yaml`
- `mirror_object.yaml`

## 执行兼容性说明（复查）

- 内置 24 个 Skill Capsule 文件已齐备，覆盖 Phase 1 清单。
- 当前 Capsule 使用的是高层 DSL（如 `duplicate_to`、`object_names`、`execute_skill`），需要 SkillExecutor 做参数映射后执行。
- `agent-core` 当前执行器契约使用 `tool_name/arguments` 与 `${var}` 占位符，而内置 YAML 使用 `tool/args` 与 `$var`，两者尚未对齐。
- 与 engine 工具契约仍有缺口：例如 `simple_house.yaml` 使用的 `execute_skill` 不在 engine 工具定义中；大量 `modify_object` 步骤使用 `name` 而 engine 侧要求 `object_name`。
- 因此当前状态应视为“内容层完成、执行联调待完成”，而非端到端可直接运行完成。

## Skill Capsule 格式

```yaml
metadata:
  name: "low_poly_table"
  tags: ["furniture", "low-poly"]
  success_rate: 0.94
  usage_count: 1283
  undo_rate: 0.12

gene:
  strategy: |
    1. 创建扁平立方体作为桌面
    2. 在四角创建桌腿
    3. 添加统一材质
  parameters:
    table_width: { default: 1.5, range: [0.5, 3.0] }

capsule:
  steps:
    - tool: create_object
      args: { name: "TableTop", object_type: "MESH", primitive: "cube" }
    - tool: modify_object
      args: { object_name: "TableTop", scale: ["$table_width", 1.0, 0.05] }

validation:
  - object_exists: ["TableTop", "Leg_FL", "Leg_FR", "Leg_BL", "Leg_BR"]
  - object_count_gte: 5
```

## 进化机制

- **Undo 驱动**: 用户 Ctrl+Z 撤销 = 隐式负反馈
- **成功率追踪**: 每次执行后更新 success_rate
- **分步统计**: 哪一步最常被撤销 -> 精准优化
