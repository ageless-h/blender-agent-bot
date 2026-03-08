# Examples — 示例与模板

> 本模块包含可直接复用的角色 Prompt、20 个实战食谱和 3 个批处理 Pipeline 示例。

## 模块内容

- `prompts/`: System Prompt 模板（4 个内置角色 + 1 个自定义模板说明）
- `recipes/`: 从入门到集成的 20 个 Cookbook
- `pipelines/`: 批处理 YAML 示例与格式说明

## 目录结构

```text
examples/
├── prompts/
│   ├── architect.md
│   ├── character.md
│   ├── game_assets.md
│   ├── beginner.md
│   └── custom_template.md
├── recipes/
│   ├── 01_first_cube.md
│   ├── 02_simple_house.md
│   ├── 03_material_setup.md
│   ├── ...
│   └── 20_pipeline_integration.md
├── pipelines/
│   ├── batch_render.yaml
│   ├── asset_generator.yaml
│   ├── scene_setup.yaml
│   └── PIPELINE_FORMAT.md
├── README.md
└── SPEC_TODOLIST.md
```

## 快速使用

```bash
# 1) 以内置角色启动
blender-agent chat --persona architect

# 2) 参考食谱执行
# 打开 examples/recipes/xx_xxx.md，按步骤在对话中执行

# 3) 先做结构验证（推荐）
blender-agent run pipelines/batch_render.yaml --dry-run --output json

# 4) 再执行真实批处理（需可用 Blender 运行时）
blender-agent run pipelines/batch_render.yaml
```

## 推荐学习路径

1. 先完成 `01` 到 `05` 入门食谱
2. 选一个角色 Prompt（如 `game_assets.md`）进行专项任务
3. 用 `scene_setup.yaml` 统一项目初始场景
4. 最后尝试 `20_pipeline_integration.md` 的生产化整合

## 维护约定

- 所有新增食谱使用 `NN_topic_name.md` 命名
- Pipeline 示例优先保持可读和可改，而非追求复杂语法
- 若新增变量，占位符统一写成 `{{variable_name}}`
