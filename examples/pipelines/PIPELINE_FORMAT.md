# Pipeline YAML 格式说明（`blender-agent run`）

本文档描述当前 CLI 执行器真实支持的 YAML 字段约定（基于 `run` 命令解析逻辑）。

## 1. 顶层结构

```yaml
name: pipeline_name
version: "1.0"
description: 文本说明
vars: {}
steps: []
```

说明：

- `vars` 与 `variables` 均可用，推荐统一使用 `vars`
- `steps` 必填且必须是数组

## 2. 变量与模板替换

- 普通变量：`{{ var_name }}`
- 对象字段：`{{ camera.location }}`
- 循环变量：`{{ item }}` 或自定义变量名（如 `{{ cam.name }}`）

推荐将路径、分辨率、采样等环境差异放入 `vars`，避免硬编码。

## 3. Step 字段

每个步骤对象支持常用字段：

- `name`: 步骤名称（可选，建议填写）
- `tool`: 要调用的工具名（必填）
- `args`: 工具参数对象（可选，默认 `{}`）
- `if`: 条件表达式（可选）
- `loop` 或 `for`: 循环配置（可选）
- `retry`: 重试次数（可选）
- `on_error`: `stop` / `continue` / `retry`
- `save_as`: 保存步骤结果到变量（可选）
- `set`: 设置变量映射（可选）

示例：

```yaml
- name: setup-render
  tool: blender_set_render_params
  args:
    engine: CYCLES
    samples: "{{ samples }}"
  on_error: stop
```

## 4. 循环与条件

### 4.1 循环

```yaml
- name: render-loop
  tool: blender_render_still
  args:
    output: "./out/{{ cam.name }}.png"
  loop:
    var: cam
    in: "{{ camera_positions }}"
```

### 4.2 条件

```yaml
- name: optional-report
  if: "{{ enable_report }} == true"
  tool: blender_get_scene
```

## 5. 错误处理

- `on_error: stop`：失败即终止
- `on_error: continue`：记录错误后继续
- `on_error: retry`：按 `retry` 次数重试

示例：

```yaml
- name: export-model
  tool: blender_export_model
  args:
    format: glb
    file: ./outputs/model.glb
  retry: 1
  on_error: retry
```

## 6. 最佳实践

- 单个脚本控制在 5~20 步，超长脚本拆分维护
- 统一使用语义化 `name`，便于日志定位
- 所有产物路径统一落在 `outputs/` 目录
- 提交前至少执行一次 `--dry-run` 验证结构合法性
