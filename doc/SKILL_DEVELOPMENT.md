# 技能开发指南

> 如何创建和分享 BlenderAgentBot 技能

## 什么是技能？

技能（Skill）是一个可复用的操作序列，封装了完成特定任务的步骤。技能使用 JSON 格式定义，包含：

- **元数据** - 名称、描述、分类、参数
- **执行步骤** - 工具调用序列
- **示例** - 使用示例

## 技能结构

### 完整示例

```json
{
  "metadata": {
    "name": "create_cube",
    "version": "1.0.0",
    "description": "创建一个立方体并设置其位置、旋转和缩放",
    "category": "modeling",
    "author": "BlenderAgentBot",
    "tags": ["primitive", "cube", "basic", "modeling"],
    "parameters": [
      {
        "name": "name",
        "type": "string",
        "description": "立方体的名称",
        "required": false,
        "default": "Cube"
      },
      {
        "name": "location",
        "type": "object",
        "description": "立方体的位置 (x, y, z)",
        "required": false,
        "default": {"x": 0, "y": 0, "z": 0}
      }
    ],
    "examples": [
      {
        "description": "创建一个默认立方体",
        "input": {},
        "expected_output": "成功创建立方体"
      }
    ],
    "dependencies": []
  },
  "steps": [
    {
      "tool_name": "create_primitive",
      "arguments": {
        "type": "CUBE",
        "name": "$name"
      },
      "description": "创建立方体"
    },
    {
      "tool_name": "set_object_location",
      "arguments": {
        "object": "$name",
        "location": "$location"
      },
      "description": "设置立方体位置"
    }
  ]
}
```

## 元数据字段

### 必需字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 技能唯一标识符（小写，下划线分隔） |
| `version` | string | 语义化版本号（如 "1.0.0"） |
| `description` | string | 简短描述（1-2 句话） |
| `category` | string | 分类（见下方分类列表） |

### 可选字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `author` | string | 作者名称 |
| `tags` | array | 标签列表，用于搜索 |
| `parameters` | array | 参数定义列表 |
| `examples` | array | 使用示例列表 |
| `dependencies` | array | 依赖的其他技能 |

### 技能分类

- `modeling` - 建模操作
- `materials` - 材质和着色
- `lighting` - 灯光设置
- `animation` - 动画相关
- `rendering` - 渲染设置
- `compositing` - 合成操作
- `scripting` - 脚本工具
- `workflow` - 工作流程
- `general` - 通用操作

## 参数定义

### 参数类型

- `string` - 字符串
- `number` - 数字
- `boolean` - 布尔值
- `object` - 对象（JSON）
- `array` - 数组

### 参数示例

```json
{
  "name": "color",
  "type": "object",
  "description": "RGB 颜色值 (0-1)",
  "required": false,
  "default": {"r": 0.8, "g": 0.8, "b": 0.8}
}
```

## 执行步骤

### 步骤结构

```json
{
  "tool_name": "工具名称",
  "arguments": {
    "参数名": "参数值"
  },
  "description": "步骤描述（可选）"
}
```

### 参数替换

使用 `$参数名` 引用技能参数：

```json
{
  "tool_name": "set_object_location",
  "arguments": {
    "object": "$object_name",
    "location": "$location"
  }
}
```

执行时，`$object_name` 和 `$location` 会被替换为实际参数值。

### 嵌套参数

```json
{
  "tool_name": "set_material_property",
  "arguments": {
    "material": "$material_name",
    "property": "base_color",
    "value": "$color"
  }
}
```

## 可用工具

### 建模工具

- `create_primitive` - 创建基础几何体
  - 参数: `type` (CUBE/SPHERE/PLANE/...), `name`
- `set_object_location` - 设置对象位置
  - 参数: `object`, `location` {x, y, z}
- `set_object_rotation` - 设置对象旋转
  - 参数: `object`, `rotation` {x, y, z}
- `set_object_scale` - 设置对象缩放
  - 参数: `object`, `scale` {x, y, z}
- `delete_object` - 删除对象
  - 参数: `object`

### 材质工具

- `create_material` - 创建材质
  - 参数: `name`
- `assign_material` - 分配材质
  - 参数: `object`, `material`
- `set_material_property` - 设置材质属性
  - 参数: `material`, `property`, `value`

### 灯光工具

- `create_light` - 创建灯光
  - 参数: `type` (POINT/SUN/SPOT/AREA), `name`
- `set_light_energy` - 设置灯光强度
  - 参数: `light`, `energy`
- `set_light_color` - 设置灯光颜色
  - 参数: `light`, `color` {r, g, b}

### 相机工具

- `create_camera` - 创建相机
  - 参数: `name`
- `set_camera_location` - 设置相机位置
  - 参数: `camera`, `distance`, `angle`
- `point_camera_at` - 相机对准目标
  - 参数: `camera`, `target`
- `set_active_camera` - 设为活动相机
  - 参数: `camera`

### 场景工具

- `select_all_objects` - 选择所有对象
- `delete_selected` - 删除选中对象
- `get_scene_info` - 获取场景信息

## 开发流程

### 1. 规划技能

确定：
- 技能要完成什么任务？
- 需要哪些参数？
- 分解为哪些步骤？

### 2. 创建 JSON 文件

```bash
# 在 skills/builtin/ 或 skills/custom/ 创建文件
touch skills/custom/my_skill.json
```

### 3. 编写技能定义

参考现有技能，填写元数据和步骤。

### 4. 测试技能

```python
from pathlib import Path
from blender_agent_core.skills import SkillStore, SkillExecutor

# 加载技能
store = SkillStore(skills_dir=Path("skills/custom"))
skill = store.load_skill(Path("skills/custom/my_skill.json"))

# 测试执行
executor = SkillExecutor(tool_executor=your_tool_executor)
result = await executor.execute_skill(
    skill,
    parameters={"param1": "value1"}
)

print(result)
```

### 5. 验证和优化

- 测试不同参数组合
- 检查错误处理
- 优化步骤顺序
- 添加更多示例

## 最佳实践

### 1. 命名规范

- 技能名称：小写，下划线分隔（如 `create_simple_room`）
- 参数名称：小写，下划线分隔（如 `object_name`）
- 描述：简洁明了，动词开头

### 2. 参数设计

- 提供合理的默认值
- 使用清晰的参数名
- 添加详细的描述
- 标记必需参数

### 3. 步骤组织

- 逻辑顺序排列
- 每步一个明确目标
- 添加步骤描述
- 避免冗余操作

### 4. 文档完善

- 提供多个示例
- 说明预期结果
- 列出依赖关系
- 添加使用场景

### 5. 错误处理

虽然技能本身不包含错误处理逻辑，但应：
- 使用安全的默认值
- 验证参数类型
- 考虑边界情况

## 高级技巧

### 1. 组合技能

```json
{
  "metadata": {
    "name": "setup_studio_scene",
    "dependencies": ["setup_three_point_lighting", "setup_camera_view"]
  },
  "steps": [
    {
      "tool_name": "execute_skill",
      "arguments": {
        "skill": "setup_three_point_lighting"
      }
    },
    {
      "tool_name": "execute_skill",
      "arguments": {
        "skill": "setup_camera_view"
      }
    }
  ]
}
```

### 2. 条件参数

使用参数控制执行路径：

```json
{
  "parameters": [
    {
      "name": "with_material",
      "type": "boolean",
      "default": true
    }
  ],
  "steps": [
    {
      "tool_name": "create_primitive",
      "arguments": {"type": "CUBE"}
    },
    {
      "tool_name": "apply_material",
      "arguments": {"object": "Cube"},
      "condition": "$with_material"
    }
  ]
}
```

### 3. 循环操作

创建多个对象：

```json
{
  "parameters": [
    {
      "name": "count",
      "type": "number",
      "default": 3
    }
  ],
  "steps": [
    {
      "tool_name": "create_array",
      "arguments": {
        "object_type": "CUBE",
        "count": "$count",
        "spacing": 2
      }
    }
  ]
}
```

## 示例技能

### 简单技能：创建彩色球体

```json
{
  "metadata": {
    "name": "create_colored_sphere",
    "version": "1.0.0",
    "description": "创建一个带颜色的球体",
    "category": "modeling",
    "parameters": [
      {
        "name": "color",
        "type": "object",
        "description": "球体颜色 RGB",
        "required": false,
        "default": {"r": 1.0, "g": 0.0, "b": 0.0}
      }
    ]
  },
  "steps": [
    {
      "tool_name": "create_primitive",
      "arguments": {"type": "SPHERE", "name": "ColoredSphere"}
    },
    {
      "tool_name": "create_material",
      "arguments": {"name": "SphereMaterial"}
    },
    {
      "tool_name": "set_material_property",
      "arguments": {
        "material": "SphereMaterial",
        "property": "base_color",
        "value": "$color"
      }
    },
    {
      "tool_name": "assign_material",
      "arguments": {
        "object": "ColoredSphere",
        "material": "SphereMaterial"
      }
    }
  ]
}
```

### 复杂技能：产品展示场景

```json
{
  "metadata": {
    "name": "setup_product_showcase",
    "version": "1.0.0",
    "description": "设置产品展示场景（背景、灯光、相机）",
    "category": "workflow",
    "parameters": [
      {
        "name": "product_object",
        "type": "string",
        "description": "产品对象名称",
        "required": true
      }
    ]
  },
  "steps": [
    {
      "tool_name": "create_primitive",
      "arguments": {"type": "PLANE", "name": "Background"},
      "description": "创建背景"
    },
    {
      "tool_name": "set_object_scale",
      "arguments": {
        "object": "Background",
        "scale": {"x": 10, "y": 10, "z": 1}
      }
    },
    {
      "tool_name": "execute_skill",
      "arguments": {"skill": "setup_three_point_lighting"}
    },
    {
      "tool_name": "execute_skill",
      "arguments": {
        "skill": "setup_camera_view",
        "parameters": {"target": "$product_object"}
      }
    }
  ]
}
```

## 分享技能

### 1. 提交到官方库

```bash
# Fork 项目
git clone https://github.com/your-username/BlenderAgentBot.git

# 添加技能
cp my_skill.json BlenderAgentBot/skills/community/

# 提交 PR
git add skills/community/my_skill.json
git commit -m "Add: my_skill - 技能描述"
git push origin main
```

### 2. 创建技能包

```bash
# 创建技能包目录
mkdir my-skill-pack
cd my-skill-pack

# 添加技能文件
cp skill1.json skill2.json .

# 创建 README
cat > README.md << EOF
# My Skill Pack
技能包描述
EOF

# 发布到 GitHub
git init
git add .
git commit -m "Initial commit"
git push
```

## 故障排除

### 技能无法加载

- 检查 JSON 格式是否正确
- 验证所有必需字段
- 确认文件编码为 UTF-8

### 参数替换失败

- 确认参数名拼写正确
- 检查参数类型匹配
- 验证默认值格式

### 工具调用失败

- 确认工具名称正确
- 检查参数格式
- 查看工具文档

## 资源

- 📖 [API 文档](API.md)
- 💡 [示例技能](../../skills/builtin/)
- 🔧 [工具参考](TOOLS.md)
- 💬 [社区讨论](https://github.com/your-org/BlenderAgentBot/discussions)

## 贡献

欢迎贡献新技能！请遵循：
1. 代码规范
2. 完整文档
3. 测试验证
4. PR 模板

---

**Happy Skill Building!** 🚀
