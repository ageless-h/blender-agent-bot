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
* [Operators (bpy.ops)](../ops/index.md)[ ]
* [Types (bpy.types)](../types/index.md)[ ]
* [Utilities (bpy.utils)](../utils/index.md)[ ]
* [Path Utilities (bpy.path)](../path/index.md)
* [Application Data (bpy.app)](index.md)[x]

  Toggle navigation of Application Data (bpy.app)

  + Application Handlers (bpy.app.handlers)
  + [Application Translations (bpy.app.translations)](translations.md)
  + [Application Icons (bpy.app.icons)](icons.md)
  + [Application Timers (bpy.app.timers)](timers.md)
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

# Application Handlers (bpy.app.handlers)[#](#module-bpy.app.handlers "Link to this heading")

This module contains callback lists

## Basic Handler Example[#](#basic-handler-example "Link to this heading")

This script shows the most simple example of adding a handler.

```
import bpy

def my_handler(scene):
    print("Frame Change", scene.frame_current)

bpy.app.handlers.frame_change_pre.append(my_handler)
```

## Persistent Handler Example[#](#persistent-handler-example "Link to this heading")

By default handlers are freed when loading new files, in some cases you may
want the handler stay running across multiple files (when the handler is
part of an add-on for example).

For this the [`bpy.app.handlers.persistent`](#bpy.app.handlers.persistent "bpy.app.handlers.persistent") decorator needs to be used.

```
import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler(dummy):
    print("Load Handler:", bpy.data.filepath)

bpy.app.handlers.load_post.append(load_handler)
```

## Note on Altering Data[#](#note-on-altering-data "Link to this heading")

Altering data from handlers should be done carefully. While rendering the
`frame_change_pre` and `frame_change_post` handlers are called from one
thread and the viewport updates from a different thread. If the handler changes
data that is accessed by the viewport, this can cause a crash of Blender. In
such cases, lock the interface (Render → Lock Interface or
[`bpy.types.RenderSettings.use_lock_interface`](../types/RenderSettings.md#bpy.types.RenderSettings.use_lock_interface "bpy.types.RenderSettings.use_lock_interface")) before starting a render.

Below is an example of a mesh that is altered from a handler:

```
def frame_change_pre(scene):
    # A triangle that shifts in the z direction
    zshift = scene.frame_current * 0.1
    vertices = [(-1, -1, zshift), (1, -1, zshift), (0, 1, zshift)]
    triangles = [(0, 1, 2)]

    object = bpy.data.objects["The Object"]
    object.data.clear_geometry()
    object.data.from_pydata(vertices, [], triangles)
```

bpy.app.handlers.animation\_playback\_post[#](#bpy.app.handlers.animation_playback_post "Link to this definition")
:   on ending animation playback

bpy.app.handlers.animation\_playback\_pre[#](#bpy.app.handlers.animation_playback_pre "Link to this definition")
:   on starting animation playback

bpy.app.handlers.annotation\_post[#](#bpy.app.handlers.annotation_post "Link to this definition")
:   on drawing an annotation (after)

bpy.app.handlers.annotation\_pre[#](#bpy.app.handlers.annotation_pre "Link to this definition")
:   on drawing an annotation (before)

bpy.app.handlers.composite\_cancel[#](#bpy.app.handlers.composite_cancel "Link to this definition")
:   on a compositing background job (cancel)

bpy.app.handlers.composite\_post[#](#bpy.app.handlers.composite_post "Link to this definition")
:   on a compositing background job (after)

bpy.app.handlers.composite\_pre[#](#bpy.app.handlers.composite_pre "Link to this definition")
:   on a compositing background job (before)

bpy.app.handlers.depsgraph\_update\_post[#](#bpy.app.handlers.depsgraph_update_post "Link to this definition")
:   on depsgraph update (post)

bpy.app.handlers.depsgraph\_update\_pre[#](#bpy.app.handlers.depsgraph_update_pre "Link to this definition")
:   on depsgraph update (pre)

bpy.app.handlers.frame\_change\_post[#](#bpy.app.handlers.frame_change_post "Link to this definition")
:   Called after frame change for playback and rendering, after the data has been evaluated for the new frame.

bpy.app.handlers.frame\_change\_pre[#](#bpy.app.handlers.frame_change_pre "Link to this definition")
:   Called after frame change for playback and rendering, before any data is evaluated for the new frame. This makes it possible to change data and relations (for example swap an object to another mesh) for the new frame. Note that this handler is **not** to be used as ‘before the frame changes’ event. The dependency graph is not available in this handler, as data and relations may have been altered and the dependency graph has not yet been updated for that.

bpy.app.handlers.load\_factory\_preferences\_post[#](#bpy.app.handlers.load_factory_preferences_post "Link to this definition")
:   on loading factory preferences (after)

bpy.app.handlers.load\_factory\_startup\_post[#](#bpy.app.handlers.load_factory_startup_post "Link to this definition")
:   on loading factory startup (after)

bpy.app.handlers.load\_post[#](#bpy.app.handlers.load_post "Link to this definition")
:   on loading a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.

bpy.app.handlers.load\_post\_fail[#](#bpy.app.handlers.load_post_fail "Link to this definition")
:   on failure to load a new blend file (after). Accepts one argument: the file being loaded, an empty string for the startup-file.

bpy.app.handlers.load\_pre[#](#bpy.app.handlers.load_pre "Link to this definition")
:   on loading a new blend file (before).Accepts one argument: the file being loaded, an empty string for the startup-file.

bpy.app.handlers.object\_bake\_cancel[#](#bpy.app.handlers.object_bake_cancel "Link to this definition")
:   on canceling a bake job; will be called in the main thread

bpy.app.handlers.object\_bake\_complete[#](#bpy.app.handlers.object_bake_complete "Link to this definition")
:   on completing a bake job; will be called in the main thread

bpy.app.handlers.object\_bake\_pre[#](#bpy.app.handlers.object_bake_pre "Link to this definition")
:   before starting a bake job

bpy.app.handlers.redo\_post[#](#bpy.app.handlers.redo_post "Link to this definition")
:   on loading a redo step (after)

bpy.app.handlers.redo\_pre[#](#bpy.app.handlers.redo_pre "Link to this definition")
:   on loading a redo step (before)

bpy.app.handlers.render\_cancel[#](#bpy.app.handlers.render_cancel "Link to this definition")
:   on canceling a render job

bpy.app.handlers.render\_complete[#](#bpy.app.handlers.render_complete "Link to this definition")
:   on completion of render job

bpy.app.handlers.render\_init[#](#bpy.app.handlers.render_init "Link to this definition")
:   on initialization of a render job

bpy.app.handlers.render\_post[#](#bpy.app.handlers.render_post "Link to this definition")
:   on render (after)

bpy.app.handlers.render\_pre[#](#bpy.app.handlers.render_pre "Link to this definition")
:   on render (before)

bpy.app.handlers.render\_stats[#](#bpy.app.handlers.render_stats "Link to this definition")
:   on printing render statistics. Accepts one argument: the render stats (render/saving time plus in background mode frame/used [peak] memory).

bpy.app.handlers.render\_write[#](#bpy.app.handlers.render_write "Link to this definition")
:   on writing a render frame (directly after the frame is written)

bpy.app.handlers.save\_post[#](#bpy.app.handlers.save_post "Link to this definition")
:   on saving a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.

bpy.app.handlers.save\_post\_fail[#](#bpy.app.handlers.save_post_fail "Link to this definition")
:   on failure to save a blend file (after). Accepts one argument: the file being saved, an empty string for the startup-file.

bpy.app.handlers.save\_pre[#](#bpy.app.handlers.save_pre "Link to this definition")
:   on saving a blend file (before). Accepts one argument: the file being saved, an empty string for the startup-file.

bpy.app.handlers.translation\_update\_post[#](#bpy.app.handlers.translation_update_post "Link to this definition")
:   on translation settings update

bpy.app.handlers.undo\_post[#](#bpy.app.handlers.undo_post "Link to this definition")
:   on loading an undo step (after)

bpy.app.handlers.undo\_pre[#](#bpy.app.handlers.undo_pre "Link to this definition")
:   on loading an undo step (before)

bpy.app.handlers.version\_update[#](#bpy.app.handlers.version_update "Link to this definition")
:   on ending the versioning code

bpy.app.handlers.xr\_session\_start\_pre[#](#bpy.app.handlers.xr_session_start_pre "Link to this definition")
:   on starting an xr session (before)

bpy.app.handlers.persistent[#](#bpy.app.handlers.persistent "Link to this definition")
:   Function decorator for callback functions not to be removed when loading new files

[Next

Application Translations (bpy.app.translations)](translations.md)
[Previous

Application Data (bpy.app)](index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.app.handlers.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.app.handlers.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Application Handlers (bpy.app.handlers)
  + [Basic Handler Example](#basic-handler-example)
  + [Persistent Handler Example](#persistent-handler-example)
  + [Note on Altering Data](#note-on-altering-data)
    - [`animation_playback_post`](#bpy.app.handlers.animation_playback_post)
    - [`animation_playback_pre`](#bpy.app.handlers.animation_playback_pre)
    - [`annotation_post`](#bpy.app.handlers.annotation_post)
    - [`annotation_pre`](#bpy.app.handlers.annotation_pre)
    - [`composite_cancel`](#bpy.app.handlers.composite_cancel)
    - [`composite_post`](#bpy.app.handlers.composite_post)
    - [`composite_pre`](#bpy.app.handlers.composite_pre)
    - [`depsgraph_update_post`](#bpy.app.handlers.depsgraph_update_post)
    - [`depsgraph_update_pre`](#bpy.app.handlers.depsgraph_update_pre)
    - [`frame_change_post`](#bpy.app.handlers.frame_change_post)
    - [`frame_change_pre`](#bpy.app.handlers.frame_change_pre)
    - [`load_factory_preferences_post`](#bpy.app.handlers.load_factory_preferences_post)
    - [`load_factory_startup_post`](#bpy.app.handlers.load_factory_startup_post)
    - [`load_post`](#bpy.app.handlers.load_post)
    - [`load_post_fail`](#bpy.app.handlers.load_post_fail)
    - [`load_pre`](#bpy.app.handlers.load_pre)
    - [`object_bake_cancel`](#bpy.app.handlers.object_bake_cancel)
    - [`object_bake_complete`](#bpy.app.handlers.object_bake_complete)
    - [`object_bake_pre`](#bpy.app.handlers.object_bake_pre)
    - [`redo_post`](#bpy.app.handlers.redo_post)
    - [`redo_pre`](#bpy.app.handlers.redo_pre)
    - [`render_cancel`](#bpy.app.handlers.render_cancel)
    - [`render_complete`](#bpy.app.handlers.render_complete)
    - [`render_init`](#bpy.app.handlers.render_init)
    - [`render_post`](#bpy.app.handlers.render_post)
    - [`render_pre`](#bpy.app.handlers.render_pre)
    - [`render_stats`](#bpy.app.handlers.render_stats)
    - [`render_write`](#bpy.app.handlers.render_write)
    - [`save_post`](#bpy.app.handlers.save_post)
    - [`save_post_fail`](#bpy.app.handlers.save_post_fail)
    - [`save_pre`](#bpy.app.handlers.save_pre)
    - [`translation_update_post`](#bpy.app.handlers.translation_update_post)
    - [`undo_post`](#bpy.app.handlers.undo_post)
    - [`undo_pre`](#bpy.app.handlers.undo_pre)
    - [`version_update`](#bpy.app.handlers.version_update)
    - [`xr_session_start_pre`](#bpy.app.handlers.xr_session_start_pre)
    - [`persistent`](#bpy.app.handlers.persistent)