# 10_procedural_materials — 程序化材质

## 目标

不依赖外部贴图，使用节点系统构建可调程序化材质。

## 前置条件

- 了解 Shader Editor 基础节点
- 场景中有至少一个可测试对象

## 操作步骤

1. 新建材质并使用 `Principled BSDF` 作为主节点。
2. 用 `Noise Texture + ColorRamp` 驱动 Base Color 变化。
3. 用 `Noise Texture`（不同缩放）驱动 Roughness 微差异。
4. 增加 `Bump` 或 `Normal` 输入模拟表面细节。
5. 暴露 3~4 个参数（色调、粗糙度、纹理尺度、凹凸强度）便于复用。

## 验收标准

- 材质在不同光照角度下有可见层次变化
- 参数可调且不会轻易失真
- 不依赖外部纹理文件

## 常见问题

- 材质“脏”：降低噪声对比，收敛 ColorRamp 区间
- 凹凸过强：减少 Bump Strength 避免塑料感

## 可复用 Prompt

> 帮我做一个可调的程序化木材/石材材质，并给出关键参数范围。
