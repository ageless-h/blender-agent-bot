"""
弹跳立方体动画脚本
在 Blender 脚本编辑器中运行此脚本，或通过命令行：
blender --python bounce_cube_animation.py
"""

import bpy
import math


def create_bounce_animation():
    """为默认立方体创建弹跳动画"""

    # 获取或创建立方体
    if "Cube" in bpy.data.objects:
        cube = bpy.data.objects["Cube"]
    else:
        bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
        cube = bpy.context.active_object
        cube.name = "Cube"

    # 设置场景参数
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 120  # 5秒动画 (24fps)
    scene.render.fps = 24

    # 清除现有动画数据
    if cube.animation_data:
        cube.animation_data_clear()

    # 弹跳参数
    bounce_height = 5.0  # 最大弹跳高度
    ground_level = 1.0  # 地面高度（立方体中心）
    num_bounces = 3  # 弹跳次数

    # 计算每次弹跳的帧数
    frames_per_bounce = (scene.frame_end - scene.frame_start) // num_bounces

    # 创建弹跳关键帧
    for i in range(num_bounces + 1):
        frame = scene.frame_start + i * frames_per_bounce

        # 每次弹跳高度递减
        height_multiplier = 1.0 - (i / (num_bounces + 1))
        current_height = ground_level + bounce_height * height_multiplier

        # 在地面
        cube.location.z = ground_level
        cube.keyframe_insert(data_path="location", index=2, frame=frame)

        # 在空中（弹跳中点）
        if i < num_bounces:
            mid_frame = frame + frames_per_bounce // 2
            cube.location.z = current_height
            cube.keyframe_insert(data_path="location", index=2, frame=mid_frame)

    # 设置插值类型为贝塞尔曲线以获得平滑的弧线运动
    if cube.animation_data and cube.animation_data.action:
        for fcurve in cube.animation_data.action.fcurves:
            if fcurve.data_path == "location" and fcurve.array_index == 2:
                for keyframe in fcurve.keyframe_points:
                    keyframe.interpolation = "BEZIER"
                    # 调整手柄以模拟重力效果
                    keyframe.handle_left_type = "AUTO_CLAMPED"
                    keyframe.handle_right_type = "AUTO_CLAMPED"

    # 添加轻微的挤压和拉伸效果（可选）
    add_squash_stretch(cube, scene.frame_start, scene.frame_end, frames_per_bounce, num_bounces)

    # 设置视图
    bpy.context.scene.frame_set(scene.frame_start)

    print(f"✅ 弹跳动画创建完成！")
    print(f"   - 对象: {cube.name}")
    print(f"   - 帧范围: {scene.frame_start} - {scene.frame_end}")
    print(f"   - 弹跳次数: {num_bounces}")
    print(f"   - 按空格键播放动画")


def add_squash_stretch(obj, start_frame, end_frame, frames_per_bounce, num_bounces):
    """添加挤压和拉伸效果以增强弹跳感"""

    ground_level = 1.0

    for i in range(num_bounces + 1):
        frame = start_frame + i * frames_per_bounce

        # 在地面时挤压
        obj.scale.z = 0.7
        obj.scale.x = 1.15
        obj.scale.y = 1.15
        obj.keyframe_insert(data_path="scale", frame=frame)

        # 在空中时拉伸
        if i < num_bounces:
            mid_frame = frame + frames_per_bounce // 2
            obj.scale.z = 1.2
            obj.scale.x = 0.9
            obj.scale.y = 0.9
            obj.keyframe_insert(data_path="scale", frame=mid_frame)

    # 设置缩放动画的插值
    if obj.animation_data and obj.animation_data.action:
        for fcurve in obj.animation_data.action.fcurves:
            if fcurve.data_path == "scale":
                for keyframe in fcurve.keyframe_points:
                    keyframe.interpolation = "BEZIER"
                    keyframe.handle_left_type = "AUTO_CLAMPED"
                    keyframe.handle_right_type = "AUTO_CLAMPED"


# 执行动画创建
if __name__ == "__main__":
    create_bounce_animation()
