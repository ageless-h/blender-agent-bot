## Builtin Skill Capsules

该目录提供 BlenderAgentBot 的内置 Skill Capsule，优先覆盖高频建模、材质、灯光与修改器场景。

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

### 约定

- 每个技能必须包含 `metadata`、`gene`、`capsule`、`validation` 四段。
- 参数占位符统一使用 `$parameter_name`。
- `undo_group` 用于撤销统计分组（结构、细节、材质、灯光等）。
