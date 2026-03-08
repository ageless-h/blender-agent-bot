"""
通过 blender-mcp socket 创建弹跳动画
"""

import socket
import json
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def send_request(sock, method, params):
    """发送 JSON-RPC 请求"""
    request = {"jsonrpc": "2.0", "id": int(time.time() * 1000), "method": method, "params": params}

    message = json.dumps(request) + "\n"
    sock.sendall(message.encode("utf-8"))

    response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk
        if b"\n" in response:
            break

    return json.loads(response.decode("utf-8"))


def create_bounce_animation():
    """创建弹跳立方体动画"""

    HOST = "127.0.0.1"
    PORT = 9876

    print(f"连接到 Blender (localhost:{PORT})...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print("✅ 已连接")

        # 1. 获取场景信息
        print("\n1. 获取场景信息...")
        response = send_request(sock, "tools/call", {"name": "blender_get_scene", "arguments": {}})
        print(f"   场景: {response.get('result', {}).get('content', [{}])[0].get('text', 'N/A')[:100]}...")

        # 2. 确保有立方体
        print("\n2. 检查立方体...")
        response = send_request(
            sock, "tools/call", {"name": "blender_get_objects", "arguments": {"name_filter": "Cube"}}
        )

        objects = json.loads(response.get("result", {}).get("content", [{}])[0].get("text", "{}"))
        if not objects.get("objects"):
            print("   创建新立方体...")
            send_request(
                sock,
                "tools/call",
                {
                    "name": "blender_create_object",
                    "arguments": {
                        "name": "Cube",
                        "object_type": "MESH",
                        "primitive": "cube",
                        "size": 2.0,
                        "location": [0, 0, 1],
                    },
                },
            )
        else:
            print(f"   找到立方体: {objects['objects'][0]['name']}")

        # 3. 设置场景参数
        print("\n3. 设置场景参数...")
        send_request(
            sock,
            "tools/call",
            {
                "name": "blender_setup_scene",
                "arguments": {"timeline": {"frame_start": 1, "frame_end": 120, "frame_current": 1, "fps": 24}},
            },
        )

        # 4. 清除现有动画
        print("\n4. 清除现有动画...")
        send_request(
            sock,
            "tools/call",
            {
                "name": "blender_execute_script",
                "arguments": {
                    "code": """
import bpy
cube = bpy.data.objects.get('Cube')
if cube and cube.animation_data:
    cube.animation_data_clear()
"""
                },
            },
        )

        # 5. 创建弹跳关键帧
        print("\n5. 创建弹跳动画关键帧...")

        bounce_height = 5.0
        ground_level = 1.0
        num_bounces = 3
        frames_per_bounce = 120 // num_bounces

        keyframes = []

        for i in range(num_bounces + 1):
            frame = 1 + i * frames_per_bounce
            height_multiplier = 1.0 - (i / (num_bounces + 1))
            current_height = ground_level + bounce_height * height_multiplier

            keyframes.append({"frame": frame, "data_path": "location", "index": 2, "value": ground_level})

            if i < num_bounces:
                mid_frame = frame + frames_per_bounce // 2
                keyframes.append({"frame": mid_frame, "data_path": "location", "index": 2, "value": current_height})

        send_request(
            sock,
            "tools/call",
            {"name": "blender_edit_animation", "arguments": {"object_name": "Cube", "keyframes": keyframes}},
        )

        # 6. 设置插值和手柄
        print("\n6. 设置动画曲线插值...")
        send_request(
            sock,
            "tools/call",
            {
                "name": "blender_execute_script",
                "arguments": {
                    "code": """
import bpy
cube = bpy.data.objects.get('Cube')
if cube and cube.animation_data and cube.animation_data.action:
    for fcurve in cube.animation_data.action.fcurves:
        if fcurve.data_path == 'location' and fcurve.array_index == 2:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'BEZIER'
                keyframe.handle_left_type = 'AUTO_CLAMPED'
                keyframe.handle_right_type = 'AUTO_CLAMPED'
"""
                },
            },
        )

        # 7. 添加挤压拉伸效果
        print("\n7. 添加挤压拉伸效果...")

        scale_keyframes = []
        for i in range(num_bounces + 1):
            frame = 1 + i * frames_per_bounce

            scale_keyframes.extend(
                [
                    {"frame": frame, "data_path": "scale", "index": 0, "value": 1.15},
                    {"frame": frame, "data_path": "scale", "index": 1, "value": 1.15},
                    {"frame": frame, "data_path": "scale", "index": 2, "value": 0.7},
                ]
            )

            if i < num_bounces:
                mid_frame = frame + frames_per_bounce // 2
                scale_keyframes.extend(
                    [
                        {"frame": mid_frame, "data_path": "scale", "index": 0, "value": 0.9},
                        {"frame": mid_frame, "data_path": "scale", "index": 1, "value": 0.9},
                        {"frame": mid_frame, "data_path": "scale", "index": 2, "value": 1.2},
                    ]
                )

        send_request(
            sock,
            "tools/call",
            {"name": "blender_edit_animation", "arguments": {"object_name": "Cube", "keyframes": scale_keyframes}},
        )

        # 8. 设置缩放曲线插值
        print("\n8. 设置缩放曲线插值...")
        send_request(
            sock,
            "tools/call",
            {
                "name": "blender_execute_script",
                "arguments": {
                    "code": """
import bpy
cube = bpy.data.objects.get('Cube')
if cube and cube.animation_data and cube.animation_data.action:
    for fcurve in cube.animation_data.action.fcurves:
        if fcurve.data_path == 'scale':
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = 'BEZIER'
                keyframe.handle_left_type = 'AUTO_CLAMPED'
                keyframe.handle_right_type = 'AUTO_CLAMPED'
"""
                },
            },
        )

        print("\n✅ 弹跳动画创建完成！")
        print("   - 对象: Cube")
        print("   - 帧范围: 1-120 (5秒 @ 24fps)")
        print("   - 弹跳次数: 3")
        print("   - 在 Blender 中按空格键播放动画")


if __name__ == "__main__":
    create_bounce_animation()
