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
  + [GPU Matrix Utilities (gpu.matrix)](../matrix/index.md)
  + [GPU Select Utilities (gpu.select)](../select/index.md)
  + [GPU Shader Utilities (gpu.shader)](../shader/index.md)
  + GPU State Utilities (gpu.state)
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

# GPU State Utilities (gpu.state)[#](#module-gpu.state "Link to this heading")

This module provides access to the gpu state.

gpu.state.active\_framebuffer\_get(*enable*)[#](#gpu.state.active_framebuffer_get "Link to this definition")
:   Return the active frame-buffer in context.

gpu.state.blend\_get()[#](#gpu.state.blend_get "Link to this definition")
:   Current blending equation.

gpu.state.blend\_set(*mode*)[#](#gpu.state.blend_set "Link to this definition")
:   Defines the fixed pipeline blending equation.

    Parameters:
    :   **mode** (*str*) – The type of blend mode.
        \* `NONE` No blending.
        \* `ALPHA` The original color channels are interpolated according to the alpha value.
        \* `ALPHA_PREMULT` The original color channels are interpolated according to the alpha value with the new colors pre-multiplied by this value.
        \* `ADDITIVE` The original color channels are added by the corresponding ones.
        \* `ADDITIVE_PREMULT` The original color channels are added by the corresponding ones that are pre-multiplied by the alpha value.
        \* `MULTIPLY` The original color channels are multiplied by the corresponding ones.
        \* `SUBTRACT` The original color channels are subtracted by the corresponding ones.
        \* `INVERT` The original color channels are replaced by its complementary color.

gpu.state.clip\_distances\_set(*distances\_enabled*)[#](#gpu.state.clip_distances_set "Link to this definition")
:   Sets the number of gl\_ClipDistance planes used for clip geometry.

    Parameters:
    :   **distances\_enabled** (*int*) – Number of clip distances enabled.

gpu.state.color\_mask\_set(*r*, *g*, *b*, *a*)[#](#gpu.state.color_mask_set "Link to this definition")
:   Enable or disable writing of frame buffer color components.

    Parameters:
    :   **a** (*r**,* *g**,* *b**,*) – components red, green, blue, and alpha.

gpu.state.depth\_mask\_get()[#](#gpu.state.depth_mask_get "Link to this definition")
:   Writing status in the depth component.

gpu.state.depth\_mask\_set(*value*)[#](#gpu.state.depth_mask_set "Link to this definition")
:   Write to depth component.

    Parameters:
    :   **value** – True for writing to the depth component.

gpu.state.depth\_test\_get()[#](#gpu.state.depth_test_get "Link to this definition")
:   Current depth\_test equation.

gpu.state.depth\_test\_set(*mode*)[#](#gpu.state.depth_test_set "Link to this definition")
:   Defines the depth\_test equation.

    Parameters:
    :   **mode** (*str*) – The depth test equation name.
        Possible values are NONE, ALWAYS, LESS, LESS\_EQUAL, EQUAL, GREATER and GREATER\_EQUAL.

gpu.state.face\_culling\_set(*culling*)[#](#gpu.state.face_culling_set "Link to this definition")
:   Specify whether none, front-facing or back-facing facets can be culled.

    Parameters:
    :   **mode** (*str*) – NONE, FRONT or BACK.

gpu.state.front\_facing\_set(*invert*)[#](#gpu.state.front_facing_set "Link to this definition")
:   Specifies the orientation of front-facing polygons.

    Parameters:
    :   **invert** – True for clockwise polygons as front-facing.

gpu.state.line\_width\_get()[#](#gpu.state.line_width_get "Link to this definition")
:   Current width of rasterized lines.

gpu.state.line\_width\_set(*width*)[#](#gpu.state.line_width_set "Link to this definition")
:   Specify the width of rasterized lines.

    Parameters:
    :   **size** – New width.

gpu.state.point\_size\_set(*size*)[#](#gpu.state.point_size_set "Link to this definition")
:   Specify the diameter of rasterized points.

    Parameters:
    :   **size** – New diameter.

gpu.state.program\_point\_size\_set(*enable*)[#](#gpu.state.program_point_size_set "Link to this definition")
:   If enabled, the derived point size is taken from the (potentially clipped) shader builtin gl\_PointSize.

    Parameters:
    :   **enable** (*bool*) – True for shader builtin gl\_PointSize.

gpu.state.scissor\_get()[#](#gpu.state.scissor_get "Link to this definition")
:   Retrieve the scissors of the active framebuffer.
    Note: Only valid between ‘scissor\_set’ and a framebuffer rebind.

    Returns:
    :   The scissor of the active framebuffer as a tuple
        (x, y, xsize, ysize).
        x, y: lower left corner of the scissor rectangle, in pixels.
        xsize, ysize: width and height of the scissor rectangle.

    Return type:
    :   tuple(int, int, int, int)

gpu.state.scissor\_set(*x*, *y*, *xsize*, *ysize*)[#](#gpu.state.scissor_set "Link to this definition")
:   Specifies the scissor area of the active framebuffer.
    Note: The scissor state is not saved upon framebuffer rebind.

    Parameters:
    :   * **y** (*x**,*) – lower left corner of the scissor rectangle, in pixels.
        * **ysize** (*xsize**,*) – width and height of the scissor rectangle.

gpu.state.scissor\_test\_set(*enable*)[#](#gpu.state.scissor_test_set "Link to this definition")
:   Enable/disable scissor testing on the active framebuffer.

    Parameters:
    :   **enable** (*bool*) – True - enable scissor testing.
        False - disable scissor testing.

gpu.state.viewport\_get()[#](#gpu.state.viewport_get "Link to this definition")
:   Viewport of the active framebuffer.

gpu.state.viewport\_set(*x*, *y*, *xsize*, *ysize*)[#](#gpu.state.viewport_set "Link to this definition")
:   Specifies the viewport of the active framebuffer.
    Note: The viewport state is not saved upon framebuffer rebind.

    Parameters:
    :   * **y** (*x**,*) – lower left corner of the viewport\_set rectangle, in pixels.
        * **ysize** (*xsize**,*) – width and height of the viewport\_set.

[Next

GPU Texture Utilities (gpu.texture)](../texture/index.md)
[Previous

GPU Shader Utilities (gpu.shader)](../shader/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60gpu.state.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fgpu.state.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* GPU State Utilities (gpu.state)
  + [`active_framebuffer_get()`](#gpu.state.active_framebuffer_get)
  + [`blend_get()`](#gpu.state.blend_get)
  + [`blend_set()`](#gpu.state.blend_set)
  + [`clip_distances_set()`](#gpu.state.clip_distances_set)
  + [`color_mask_set()`](#gpu.state.color_mask_set)
  + [`depth_mask_get()`](#gpu.state.depth_mask_get)
  + [`depth_mask_set()`](#gpu.state.depth_mask_set)
  + [`depth_test_get()`](#gpu.state.depth_test_get)
  + [`depth_test_set()`](#gpu.state.depth_test_set)
  + [`face_culling_set()`](#gpu.state.face_culling_set)
  + [`front_facing_set()`](#gpu.state.front_facing_set)
  + [`line_width_get()`](#gpu.state.line_width_get)
  + [`line_width_set()`](#gpu.state.line_width_set)
  + [`point_size_set()`](#gpu.state.point_size_set)
  + [`program_point_size_set()`](#gpu.state.program_point_size_set)
  + [`scissor_get()`](#gpu.state.scissor_get)
  + [`scissor_set()`](#gpu.state.scissor_set)
  + [`scissor_test_set()`](#gpu.state.scissor_test_set)
  + [`viewport_get()`](#gpu.state.viewport_get)
  + [`viewport_set()`](#gpu.state.viewport_set)