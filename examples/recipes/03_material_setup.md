# 03_material_setup — 材质与纹理基础

## 目标

为场景中的房体与地面设置基础 PBR 材质。

## 前置条件

- 已完成 `02_simple_house`
- 已切换到 `Material Preview` 视图

## 操作步骤

1. 为 `House_Body` 新建材质 `M_Wall`，设置 Base Color 为浅暖灰。
2. 降低 Roughness 到 `0.35~0.5`，使墙体有轻微反射。
3. 为 `House_Roof` 新建材质 `M_Roof`，色彩偏深，Roughness 提高到 `0.6+`。
4. 为 `Ground` 新建材质 `M_Ground`，加入 Noise Texture 驱动粗糙度变化。
5. 通过 UV Editor 快速检查是否有明显拉伸。

## 验收标准

- 至少 3 个对象拥有独立材质槽
- 墙体、屋顶、地面视觉差异明显
- 没有极端过曝或纯黑区域

## 常见问题

- 材质发灰：检查 Color Management（建议 Filmic）
- 纹理拉伸：重新展开 UV 或调整 Mapping 比例

## 可复用 Prompt

> 给我的低模场景做基础 PBR 材质，优先保证层次感和可读性。
