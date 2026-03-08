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
* [Extra Utilities (bpy\_extras)](../../../meta/index.md)[x]

  Toggle navigation of Extra Utilities (bpy\_extras)

  + [bpy\_extras submodule (bpy\_extras.anim\_utils)](../anim_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.asset\_utils)](../asset_utils/index.md)
  + bpy\_extras submodule (bpy\_extras.object\_utils)
  + [bpy\_extras submodule (bpy\_extras.io\_utils)](../io_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.image\_utils)](../image_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.keyconfig\_utils)](../keyconfig_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.mesh\_utils)](../mesh_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.node\_utils)](../node_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.view3d\_utils)](../view3d_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.id\_map\_utils)](../id_map_utils/index.md)
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

# bpy\_extras submodule (bpy\_extras.object\_utils)[#](#module-bpy_extras.object_utils "Link to this heading")

bpy\_extras.object\_utils.add\_object\_align\_init(*context*, *operator*)[#](#bpy_extras.object_utils.add_object_align_init "Link to this definition")
:   Return a matrix using the operator settings and view context.

    Parameters:
    :   * **context** ([`bpy.types.Context`](../../bpy/types/Context.md#bpy.types.Context "bpy.types.Context")) – The context to use.
        * **operator** ([`bpy.types.Operator`](../../bpy/types/Operator.md#bpy.types.Operator "bpy.types.Operator")) – The operator, checked for location and rotation properties.

    Returns:
    :   the matrix from the context and settings.

    Return type:
    :   [`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")

bpy\_extras.object\_utils.object\_data\_add(*context*, *obdata*, *operator=None*, *name=None*)[#](#bpy_extras.object_utils.object_data_add "Link to this definition")
:   Add an object using the view context and preference to initialize the
    location, rotation and layer.

    Parameters:
    :   * **context** ([`bpy.types.Context`](../../bpy/types/Context.md#bpy.types.Context "bpy.types.Context")) – The context to use.
        * **obdata** (*valid object data type* *or* *None.*) – the data used for the new object.
        * **operator** ([`bpy.types.Operator`](../../bpy/types/Operator.md#bpy.types.Operator "bpy.types.Operator")) – The operator, checked for location and rotation properties.
        * **name** (*string*) – Optional name

    Returns:
    :   the newly created object in the scene.

    Return type:
    :   [`bpy.types.Object`](../../bpy/types/Object.md#bpy.types.Object "bpy.types.Object")

bpy\_extras.object\_utils.object\_add\_grid\_scale(*context*)[#](#bpy_extras.object_utils.object_add_grid_scale "Link to this definition")
:   Return scale which should be applied on object
    data to align it to grid scale

bpy\_extras.object\_utils.object\_add\_grid\_scale\_apply\_operator(*operator*, *context*)[#](#bpy_extras.object_utils.object_add_grid_scale_apply_operator "Link to this definition")
:   Scale an operators distance values by the grid size.

bpy\_extras.object\_utils.world\_to\_camera\_view(*scene*, *obj*, *coord*)[#](#bpy_extras.object_utils.world_to_camera_view "Link to this definition")
:   Returns the camera space coords for a 3d point.
    (also known as: normalized device coordinates - NDC).

    Where (0, 0) is the bottom left and (1, 1)
    is the top right of the camera frame.
    values outside 0-1 are also supported.
    A negative ‘z’ value means the point is behind the camera.

    Takes shift-x/y, lens angle and sensor size into account
    as well as perspective/ortho projections.

    Parameters:
    :   * **scene** ([`bpy.types.Scene`](../../bpy/types/Scene.md#bpy.types.Scene "bpy.types.Scene")) – Scene to use for frame size.
        * **obj** ([`bpy.types.Object`](../../bpy/types/Object.md#bpy.types.Object "bpy.types.Object")) – Camera object.
        * **coord** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")) – World space location.

    Returns:
    :   a vector where X and Y map to the view plane and
        Z is the depth on the view axis.

    Return type:
    :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

bpy\_extras.object\_utils.object\_report\_if\_active\_shape\_key\_is\_locked(*obj*, *operator*)[#](#bpy_extras.object_utils.object_report_if_active_shape_key_is_locked "Link to this definition")
:   Checks if the active shape key of the specified object is locked, and reports an error if so.

    If the object has no shape keys, there is nothing to lock, and the function returns False.

    Parameters:
    :   * **obj** ([`bpy.types.Object`](../../bpy/types/Object.md#bpy.types.Object "bpy.types.Object")) – Object to check.
        * **operator** ([`bpy.types.Operator`](../../bpy/types/Operator.md#bpy.types.Operator "bpy.types.Operator")) – Currently running operator to report the error through. Use None to suppress emitting the message.

    Returns:
    :   True if the shape key was locked.

*class* bpy\_extras.object\_utils.AddObjectHelper[#](#bpy_extras.object_utils.AddObjectHelper "Link to this definition")
:   align\_update\_callback(*\_context*)[#](#bpy_extras.object_utils.AddObjectHelper.align_update_callback "Link to this definition")

[Next

bpy\_extras submodule (bpy\_extras.io\_utils)](../io_utils/index.md)
[Previous

bpy\_extras submodule (bpy\_extras.asset\_utils)](../asset_utils/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy_extras.object_utils.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy_extras.object_utils.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* bpy\_extras submodule (bpy\_extras.object\_utils)
  + [`add_object_align_init()`](#bpy_extras.object_utils.add_object_align_init)
  + [`object_data_add()`](#bpy_extras.object_utils.object_data_add)
  + [`object_add_grid_scale()`](#bpy_extras.object_utils.object_add_grid_scale)
  + [`object_add_grid_scale_apply_operator()`](#bpy_extras.object_utils.object_add_grid_scale_apply_operator)
  + [`world_to_camera_view()`](#bpy_extras.object_utils.world_to_camera_view)
  + [`object_report_if_active_shape_key_is_locked()`](#bpy_extras.object_utils.object_report_if_active_shape_key_is_locked)
  + [`AddObjectHelper`](#bpy_extras.object_utils.AddObjectHelper)
    - [`AddObjectHelper.align_update_callback()`](#bpy_extras.object_utils.AddObjectHelper.align_update_callback)