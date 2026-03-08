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

* [Context Access (bpy.context)](../../bpy/context/index.md)
* [Data Access (bpy.data)](../../bpy/data/index.md)
* [Message Bus (bpy.msgbus)](../../bpy/msgbus/index.md)
* [Operators (bpy.ops)](../../bpy/ops/index.md)[ ]
* [Types (bpy.types)](../../bpy/types/index.md)[ ]
* [Utilities (bpy.utils)](../../bpy/utils/index.md)[ ]
* [Path Utilities (bpy.path)](../../bpy/path/index.md)
* [Application Data (bpy.app)](../../bpy/app/index.md)[ ]

  Toggle navigation of Application Data (bpy.app)

  + [Application Handlers (bpy.app.handlers)](../../bpy/app/handlers.md)
  + [Application Translations (bpy.app.translations)](../../bpy/app/translations.md)
  + [Application Icons (bpy.app.icons)](../../bpy/app/icons.md)
  + [Application Timers (bpy.app.timers)](../../bpy/app/timers.md)
* [Property Definitions (bpy.props)](../../bpy/props/index.md)

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
* [GPU Module (gpu)](../../../meta/index.md)[x]

  Toggle navigation of GPU Module (gpu)

  + [GPU Types (gpu.types)](../types/index.md)
  + GPU Matrix Utilities (gpu.matrix)
  + [GPU Select Utilities (gpu.select)](../select/index.md)
  + [GPU Shader Utilities (gpu.shader)](../shader/index.md)
  + [GPU State Utilities (gpu.state)](../state/index.md)
  + [GPU Texture Utilities (gpu.texture)](../texture/index.md)
  + [GPU Platform Utilities (gpu.platform)](../platform/index.md)
  + [GPU Capabilities Utilities (gpu.capabilities)](../capabilities/index.md)
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

# GPU Matrix Utilities (gpu.matrix)[#](#module-gpu.matrix "Link to this heading")

This module provides access to the matrix stack.

gpu.matrix.get\_model\_view\_matrix()[#](#gpu.matrix.get_model_view_matrix "Link to this definition")
:   Return a copy of the model-view matrix.

    Returns:
    :   A 4x4 view matrix.

    Return type:
    :   [`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")

gpu.matrix.get\_normal\_matrix()[#](#gpu.matrix.get_normal_matrix "Link to this definition")
:   Return a copy of the normal matrix.

    Returns:
    :   A 3x3 normal matrix.

    Return type:
    :   [`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")

gpu.matrix.get\_projection\_matrix()[#](#gpu.matrix.get_projection_matrix "Link to this definition")
:   Return a copy of the projection matrix.

    Returns:
    :   A 4x4 projection matrix.

    Return type:
    :   [`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")

gpu.matrix.load\_identity()[#](#gpu.matrix.load_identity "Link to this definition")
:   Load an identity matrix into the stack.

gpu.matrix.load\_matrix(*matrix*)[#](#gpu.matrix.load_matrix "Link to this definition")
:   Load a matrix into the stack.

    Parameters:
    :   **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – A 4x4 matrix.

gpu.matrix.load\_projection\_matrix(*matrix*)[#](#gpu.matrix.load_projection_matrix "Link to this definition")
:   Load a projection matrix into the stack.

    Parameters:
    :   **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – A 4x4 matrix.

gpu.matrix.multiply\_matrix(*matrix*)[#](#gpu.matrix.multiply_matrix "Link to this definition")
:   Multiply the current stack matrix.

    Parameters:
    :   **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – A 4x4 matrix.

gpu.matrix.pop()[#](#gpu.matrix.pop "Link to this definition")
:   Remove the last model-view matrix from the stack.

gpu.matrix.pop\_projection()[#](#gpu.matrix.pop_projection "Link to this definition")
:   Remove the last projection matrix from the stack.

gpu.matrix.push()[#](#gpu.matrix.push "Link to this definition")
:   Add to the model-view matrix stack.

gpu.matrix.push\_pop()[#](#gpu.matrix.push_pop "Link to this definition")
:   Context manager to ensure balanced push/pop calls, even in the case of an error.

gpu.matrix.push\_pop\_projection()[#](#gpu.matrix.push_pop_projection "Link to this definition")
:   Context manager to ensure balanced push/pop calls, even in the case of an error.

gpu.matrix.push\_projection()[#](#gpu.matrix.push_projection "Link to this definition")
:   Add to the projection matrix stack.

gpu.matrix.reset()[#](#gpu.matrix.reset "Link to this definition")
:   Empty stack and set to identity.

gpu.matrix.scale(*scale*)[#](#gpu.matrix.scale "Link to this definition")
:   Scale the current stack matrix.

    Parameters:
    :   **scale** (*sequence* *of* *2* *or* *3 floats*) – Scale the current stack matrix.

gpu.matrix.scale\_uniform(*scale*)[#](#gpu.matrix.scale_uniform "Link to this definition")
:   Parameters:
    :   **scale** (*float*) – Scale the current stack matrix.

gpu.matrix.translate(*offset*)[#](#gpu.matrix.translate "Link to this definition")
:   Scale the current stack matrix.

    Parameters:
    :   **offset** (*sequence* *of* *2* *or* *3 floats*) – Translate the current stack matrix.

[Next

GPU Select Utilities (gpu.select)](../select/index.md)
[Previous

GPU Types (gpu.types)](../types/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60gpu.matrix.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fgpu.matrix.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* GPU Matrix Utilities (gpu.matrix)
  + [`get_model_view_matrix()`](#gpu.matrix.get_model_view_matrix)
  + [`get_normal_matrix()`](#gpu.matrix.get_normal_matrix)
  + [`get_projection_matrix()`](#gpu.matrix.get_projection_matrix)
  + [`load_identity()`](#gpu.matrix.load_identity)
  + [`load_matrix()`](#gpu.matrix.load_matrix)
  + [`load_projection_matrix()`](#gpu.matrix.load_projection_matrix)
  + [`multiply_matrix()`](#gpu.matrix.multiply_matrix)
  + [`pop()`](#gpu.matrix.pop)
  + [`pop_projection()`](#gpu.matrix.pop_projection)
  + [`push()`](#gpu.matrix.push)
  + [`push_pop()`](#gpu.matrix.push_pop)
  + [`push_pop_projection()`](#gpu.matrix.push_pop_projection)
  + [`push_projection()`](#gpu.matrix.push_projection)
  + [`reset()`](#gpu.matrix.reset)
  + [`scale()`](#gpu.matrix.scale)
  + [`scale_uniform()`](#gpu.matrix.scale_uniform)
  + [`translate()`](#gpu.matrix.translate)