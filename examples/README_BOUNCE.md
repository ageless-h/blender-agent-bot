# 弹跳立方体动画示例

## 使用方法

### 方法 1：在 Blender 脚本编辑器中运行

1. 打开 Blender
2. 切换到 Scripting 工作区
3. 点击 "打开" 按钮，选择 `bounce_cube_animation.py`
4. 点击 "运行脚本" 按钮（或按 Alt+P）
5. 按空格键播放动画

### 方法 2：命令行运行

```bash
blender --python examples/bounce_cube_animation.py
```

### 方法 3：在已打开的 Blender 中执行

```bash
blender --background --python examples/bounce_cube_animation.py
```

## 动画效果

- 立方体从高处落下，弹跳 3 次
- 每次弹跳高度递减（模拟能量损失）
- 包含挤压和拉伸效果（增强卡通感）
- 总时长：5 秒（120 帧 @ 24fps）

## 自定义参数

编辑脚本中的以下变量：

```python
bounce_height = 5.0      # 最大弹跳高度
ground_level = 1.0       # 地面高度
num_bounces = 3          # 弹跳次数
scene.frame_end = 120    # 动画总帧数
```

## 技术细节

- 使用贝塞尔曲线插值实现平滑运动
- 自动调整曲线手柄模拟重力加速度
- Z 轴位置动画 + XY 轴缩放动画组合
