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

# View2D Operators[#](#module-bpy.ops.view2d "Link to this heading")

bpy.ops.view2d.edge\_pan(*inside\_padding=1.0*, *outside\_padding=0.0*, *speed\_ramp=1.0*, *max\_speed=500.0*, *delay=1.0*, *zoom\_influence=0.0*)[#](#bpy.ops.view2d.edge_pan "Link to this definition")
:   Pan the view when the mouse is held at an edge

    Parameters:
    :   * **inside\_padding** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
        * **outside\_padding** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
        * **speed\_ramp** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
        * **max\_speed** (*float in* *[**0**,* *10000**]**,* *(**optional**)*) – Max Speed, Maximum speed in UI units per second
        * **delay** (*float in* *[**0**,* *10**]**,* *(**optional**)*) – Delay, Delay in seconds before maximum speed is reached
        * **zoom\_influence** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Zoom Influence, Influence of the zoom factor on scroll speed

bpy.ops.view2d.ndof()[#](#bpy.ops.view2d.ndof "Link to this definition")
:   Use a 3D mouse device to pan/zoom the view

bpy.ops.view2d.pan(*deltax=0*, *deltay=0*)[#](#bpy.ops.view2d.pan "Link to this definition")
:   Pan the view

    Parameters:
    :   * **deltax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta X
        * **deltay** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta Y

bpy.ops.view2d.reset()[#](#bpy.ops.view2d.reset "Link to this definition")
:   Reset the view

bpy.ops.view2d.scroll\_down(*deltax=0*, *deltay=0*, *page=False*)[#](#bpy.ops.view2d.scroll_down "Link to this definition")
:   Scroll the view down

    Parameters:
    :   * **deltax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta X
        * **deltay** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta Y
        * **page** (*boolean**,* *(**optional**)*) – Page, Scroll down one page

bpy.ops.view2d.scroll\_left(*deltax=0*, *deltay=0*)[#](#bpy.ops.view2d.scroll_left "Link to this definition")
:   Scroll the view left

    Parameters:
    :   * **deltax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta X
        * **deltay** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta Y

bpy.ops.view2d.scroll\_right(*deltax=0*, *deltay=0*)[#](#bpy.ops.view2d.scroll_right "Link to this definition")
:   Scroll the view right

    Parameters:
    :   * **deltax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta X
        * **deltay** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta Y

bpy.ops.view2d.scroll\_up(*deltax=0*, *deltay=0*, *page=False*)[#](#bpy.ops.view2d.scroll_up "Link to this definition")
:   Scroll the view up

    Parameters:
    :   * **deltax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta X
        * **deltay** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta Y
        * **page** (*boolean**,* *(**optional**)*) – Page, Scroll up one page

bpy.ops.view2d.scroller\_activate()[#](#bpy.ops.view2d.scroller_activate "Link to this definition")
:   Scroll view by mouse click and drag

bpy.ops.view2d.smoothview(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*)[#](#bpy.ops.view2d.smoothview "Link to this definition")
:   Undocumented, consider [contributing](https://developer.blender.org/).

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.view2d.zoom(*deltax=0.0*, *deltay=0.0*, *use\_cursor\_init=True*)[#](#bpy.ops.view2d.zoom "Link to this definition")
:   Zoom in/out the view

    Parameters:
    :   * **deltax** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta X
        * **deltay** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta Y
        * **use\_cursor\_init** (*boolean**,* *(**optional**)*) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.view2d.zoom\_border(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *zoom\_out=False*)[#](#bpy.ops.view2d.zoom_border "Link to this definition")
:   Zoom in the view to the nearest item contained in the border

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **zoom\_out** (*boolean**,* *(**optional**)*) – Zoom Out

bpy.ops.view2d.zoom\_in(*zoomfacx=0.0*, *zoomfacy=0.0*)[#](#bpy.ops.view2d.zoom_in "Link to this definition")
:   Zoom in the view

    Parameters:
    :   * **zoomfacx** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Zoom Factor X
        * **zoomfacy** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Zoom Factor Y

bpy.ops.view2d.zoom\_out(*zoomfacx=0.0*, *zoomfacy=0.0*)[#](#bpy.ops.view2d.zoom_out "Link to this definition")
:   Zoom out the view

    Parameters:
    :   * **zoomfacx** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Zoom Factor X
        * **zoomfacy** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Zoom Factor Y

[Next

View3D Operators](view3d.md)
[Previous

Uv Operators](uv.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.view2d.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.view2d.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* View2D Operators
  + [`edge_pan()`](#bpy.ops.view2d.edge_pan)
  + [`ndof()`](#bpy.ops.view2d.ndof)
  + [`pan()`](#bpy.ops.view2d.pan)
  + [`reset()`](#bpy.ops.view2d.reset)
  + [`scroll_down()`](#bpy.ops.view2d.scroll_down)
  + [`scroll_left()`](#bpy.ops.view2d.scroll_left)
  + [`scroll_right()`](#bpy.ops.view2d.scroll_right)
  + [`scroll_up()`](#bpy.ops.view2d.scroll_up)
  + [`scroller_activate()`](#bpy.ops.view2d.scroller_activate)
  + [`smoothview()`](#bpy.ops.view2d.smoothview)
  + [`zoom()`](#bpy.ops.view2d.zoom)
  + [`zoom_border()`](#bpy.ops.view2d.zoom_border)
  + [`zoom_in()`](#bpy.ops.view2d.zoom_in)
  + [`zoom_out()`](#bpy.ops.view2d.zoom_out)