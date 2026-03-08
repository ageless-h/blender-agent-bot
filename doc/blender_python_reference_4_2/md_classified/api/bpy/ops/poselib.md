Contents

Menu

Expand

Light mode

Dark mode

Auto light/dark mode

[ ]
[ ]

Hide navigation sidebar

Hide table of contents sidebar

Toggle site navigation sidebar

[Blender Python API](../../../meta/index.md)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

[![Logo](_static/blender_logo.svg)

Blender Python API](index.md)

Documentation

* [Quickstart](../../../guides/quickstart.md)
* [API Overview](../../../guides/overview.md)
* [API Reference Usage](../../../guides/api_reference.md)
* [Best Practice](../../../guides/best_practice.md)
* [Tips and Tricks](../../../guides/tips_and_tricks.md)
* [Gotchas](../../../guides/gotchas/index.md)
* [Advanced](../../../guides/advanced/index.md)[ ]
* [Change Log](../../../guides/change_log.md)

Application Modules

* [Context Access (bpy.context)](../context/index.md)
* [Data Access (bpy.data)](../data/index.md)
* [Message Bus (bpy.msgbus)](../msgbus/index.md)
* [Operators (bpy.ops)](index.md)[x]
* [Types (bpy.types)](../types/index.md)[ ]
* [Utilities (bpy.utils)](../utils/index.md)[ ]
* [Path Utilities (bpy.path)](../path/index.md)
* [Application Data (bpy.app)](../app/index.md)[ ]

  Toggle navigation of Application Data (bpy.app)

  + [Application Handlers (bpy.app.handlers)](../app/handlers.md)
  + [Application Translations (bpy.app.translations)](../app/translations.md)
  + [Application Icons (bpy.app.icons)](../app/icons.md)
  + [Application Timers (bpy.app.timers)](../app/timers.md)
* [Property Definitions (bpy.props)](../props/index.md)

Standalone Modules

* [Audio System (aud)](../../aud/index.md)
* [OpenGL Wrapper (bgl)](../../bgl/index.md)
* [Additional Math Functions (bl\_math)](../../bl_math/index.md)
* [Font Drawing (blf)](../../blf/index.md)
* [BMesh Module (bmesh)](../../bmesh/index.md)[ ]

  Toggle navigation of BMesh Module (bmesh)

  + [BMesh Operators (bmesh.ops)](../../bmesh/ops/index.md)
  + [BMesh Types (bmesh.types)](../../bmesh/types/index.md)
  + [BMesh Utilities (bmesh.utils)](../../bmesh/utils/index.md)
  + [BMesh Geometry Utilities (bmesh.geometry)](../../bmesh/geometry/index.md)
* [Extra Utilities (bpy\_extras)](../../bpy_extras/index.md)[ ]

  Toggle navigation of Extra Utilities (bpy\_extras)

  + [bpy\_extras submodule (bpy\_extras.anim\_utils)](../../bpy_extras/anim_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.asset\_utils)](../../bpy_extras/asset_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.object\_utils)](../../bpy_extras/object_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.io\_utils)](../../bpy_extras/io_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.image\_utils)](../../bpy_extras/image_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.keyconfig\_utils)](../../bpy_extras/keyconfig_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.mesh\_utils)](../../bpy_extras/mesh_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.node\_utils)](../../bpy_extras/node_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.view3d\_utils)](../../bpy_extras/view3d_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.id\_map\_utils)](../../bpy_extras/id_map_utils/index.md)
* [Freestyle Module (freestyle)](../../freestyle/index.md)[ ]

  Toggle navigation of Freestyle Module (freestyle)

  + [Freestyle Types (freestyle.types)](../../freestyle/types/index.md)
  + [Freestyle Predicates (freestyle.predicates)](../../freestyle/predicates/index.md)
  + [Freestyle Functions (freestyle.functions)](../../freestyle/functions/index.md)
  + [Freestyle Chaining Iterators (freestyle.chainingiterators)](../../freestyle/chainingiterators/index.md)
  + [Freestyle Shaders (freestyle.shaders)](../../freestyle/shaders/index.md)
  + [Freestyle Utilities (freestyle.utils)](../../freestyle/utils/index.md)[ ]

    Toggle navigation of Freestyle Utilities (freestyle.utils)

    - [freestyle.utils submodule (freestyle.utils.ContextFunctions)](../../freestyle/utils/ContextFunctions.md)
* [GPU Module (gpu)](../../gpu/index.md)[ ]

  Toggle navigation of GPU Module (gpu)

  + [GPU Types (gpu.types)](../../gpu/types/index.md)
  + [GPU Matrix Utilities (gpu.matrix)](../../gpu/matrix/index.md)
  + [GPU Select Utilities (gpu.select)](../../gpu/select/index.md)
  + [GPU Shader Utilities (gpu.shader)](../../gpu/shader/index.md)
  + [GPU State Utilities (gpu.state)](../../gpu/state/index.md)
  + [GPU Texture Utilities (gpu.texture)](../../gpu/texture/index.md)
  + [GPU Platform Utilities (gpu.platform)](../../gpu/platform/index.md)
  + [GPU Capabilities Utilities (gpu.capabilities)](../../gpu/capabilities/index.md)
* [GPU Utilities (gpu\_extras)](../../gpu_extras/index.md)[ ]

  Toggle navigation of GPU Utilities (gpu\_extras)

  + [gpu\_extras submodule (gpu\_extras.batch)](../../gpu_extras/batch/index.md)
  + [gpu\_extras submodule (gpu\_extras.presets)](../../gpu_extras/presets/index.md)
* [ID Property Access (idprop.types)](../../idprop/types/index.md)
* [Image Buffer (imbuf)](../../imbuf/index.md)[ ]

  Toggle navigation of Image Buffer (imbuf)

  + [Image Buffer Types (imbuf.types)](../../imbuf/types/index.md)
* [Math Types & Utilities (mathutils)](../../mathutils/index.md)[ ]

  Toggle navigation of Math Types & Utilities (mathutils)

  + [Geometry Utilities (mathutils.geometry)](../../mathutils/geometry/index.md)
  + [BVHTree Utilities (mathutils.bvhtree)](../../mathutils/bvhtree/index.md)
  + [KDTree Utilities (mathutils.kdtree)](../../mathutils/kdtree/index.md)
  + [Interpolation Utilities (mathutils.interpolate)](../../mathutils/interpolate/index.md)
  + [Noise Utilities (mathutils.noise)](../../mathutils/noise/index.md)

* 4.2

  Versions

  + Loading...

Note

You are not using the most up to date version of the documentation.
 is the newest version.

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Poselib Operators[#](#module-bpy.ops.poselib "Link to this heading")

bpy.ops.poselib.apply\_pose\_asset(*blend\_factor=1.0*, *flipped=False*)[#](#bpy.ops.poselib.apply_pose_asset "Link to this definition")
:   Apply the given Pose Action to the rig

    Parameters:
    :   * **blend\_factor** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
        * **flipped** (*boolean**,* *(**optional**)*) – Apply Flipped, When enabled, applies the pose flipped over the X-axis

bpy.ops.poselib.blend\_pose\_asset(*blend\_factor=0.0*, *flipped=False*, *release\_confirm=False*)[#](#bpy.ops.poselib.blend_pose_asset "Link to this definition")
:   Blend the given Pose Action to the rig

    Parameters:
    :   * **blend\_factor** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Blend Factor, Amount that the pose is applied on top of the existing poses. A negative value will subtract the pose instead of adding it
        * **flipped** (*boolean**,* *(**optional**)*) – Apply Flipped, When enabled, applies the pose flipped over the X-axis
        * **release\_confirm** (*boolean**,* *(**optional**)*) – Confirm on Release, Always confirm operation when releasing button

bpy.ops.poselib.convert\_old\_object\_poselib()[#](#bpy.ops.poselib.convert_old_object_poselib "Link to this definition")
:   Create a pose asset for each pose marker in this legacy pose library data-block

    File:
    :   [addons\_core/pose\_library/operators.py:435](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L435)

bpy.ops.poselib.convert\_old\_poselib()[#](#bpy.ops.poselib.convert_old_poselib "Link to this definition")
:   Create a pose asset for each pose marker in the current action

    File:
    :   [addons\_core/pose\_library/operators.py:401](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L401)

bpy.ops.poselib.copy\_as\_asset()[#](#bpy.ops.poselib.copy_as_asset "Link to this definition")
:   Create a new pose asset on the clipboard, to be pasted into an Asset Browser

    File:
    :   [addons\_core/pose\_library/operators.py:211](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L211)

bpy.ops.poselib.create\_pose\_asset(*pose\_name=''*, *activate\_new\_action=True*)[#](#bpy.ops.poselib.create_pose_asset "Link to this definition")
:   Create a new Action that contains the pose of the selected bones, and mark it as Asset. The asset will be stored in the current blend file

    Parameters:
    :   * **pose\_name** (*string**,* *(**optional**,* *never None**)*) – Pose Name
        * **activate\_new\_action** (*boolean**,* *(**optional**)*) – Activate New Action

    File:
    :   [addons\_core/pose\_library/operators.py:84](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L84)

bpy.ops.poselib.paste\_asset()[#](#bpy.ops.poselib.paste_asset "Link to this definition")
:   Paste the Asset that was previously copied using Copy As Asset

    File:
    :   [addons\_core/pose\_library/operators.py:283](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L283)

bpy.ops.poselib.pose\_asset\_select\_bones(*select=True*, *flipped=False*)[#](#bpy.ops.poselib.pose_asset_select_bones "Link to this definition")
:   Select those bones that are used in this pose

    Parameters:
    :   * **select** (*boolean**,* *(**optional**)*) – Select
        * **flipped** (*boolean**,* *(**optional**)*) – Flipped

    File:
    :   [addons\_core/pose\_library/operators.py:321](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L321)

bpy.ops.poselib.restore\_previous\_action()[#](#bpy.ops.poselib.restore_previous_action "Link to this definition")
:   Switch back to the previous Action, after creating a pose asset

    File:
    :   [addons\_core/pose\_library/operators.py:160](https://projects.blender.org/blender/blender-addons/addons_core/pose_library/operators.py#L160)

[Next

Preferences Operators](preferences.md)
[Previous

Pose Operators](pose.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.poselib.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.poselib.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Poselib Operators
  + [`apply_pose_asset()`](#bpy.ops.poselib.apply_pose_asset)
  + [`blend_pose_asset()`](#bpy.ops.poselib.blend_pose_asset)
  + [`convert_old_object_poselib()`](#bpy.ops.poselib.convert_old_object_poselib)
  + [`convert_old_poselib()`](#bpy.ops.poselib.convert_old_poselib)
  + [`copy_as_asset()`](#bpy.ops.poselib.copy_as_asset)
  + [`create_pose_asset()`](#bpy.ops.poselib.create_pose_asset)
  + [`paste_asset()`](#bpy.ops.poselib.paste_asset)
  + [`pose_asset_select_bones()`](#bpy.ops.poselib.pose_asset_select_bones)
  + [`restore_previous_action()`](#bpy.ops.poselib.restore_previous_action)