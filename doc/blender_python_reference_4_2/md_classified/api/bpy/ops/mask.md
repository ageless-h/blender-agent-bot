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

# Mask Operators[#](#module-bpy.ops.mask "Link to this heading")

bpy.ops.mask.add\_feather\_vertex(*location=(0.0, 0.0)*)[#](#bpy.ops.mask.add_feather_vertex "Link to this definition")
:   Add vertex to feather

    Parameters:
    :   **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of vertex in normalized space

bpy.ops.mask.add\_feather\_vertex\_slide(*MASK\_OT\_add\_feather\_vertex=None*, *MASK\_OT\_slide\_point=None*)[#](#bpy.ops.mask.add_feather_vertex_slide "Link to this definition")
:   Add new vertex to feather and slide it

    Parameters:
    :   * **MASK\_OT\_add\_feather\_vertex** (`MASK_OT_add_feather_vertex`, (optional)) – Add Feather Vertex, Add vertex to feather
        * **MASK\_OT\_slide\_point** (`MASK_OT_slide_point`, (optional)) – Slide Point, Slide control points

bpy.ops.mask.add\_vertex(*location=(0.0, 0.0)*)[#](#bpy.ops.mask.add_vertex "Link to this definition")
:   Add vertex to active spline

    Parameters:
    :   **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of vertex in normalized space

bpy.ops.mask.add\_vertex\_slide(*MASK\_OT\_add\_vertex=None*, *MASK\_OT\_slide\_point=None*)[#](#bpy.ops.mask.add_vertex_slide "Link to this definition")
:   Add new vertex and slide it

    Parameters:
    :   * **MASK\_OT\_add\_vertex** (`MASK_OT_add_vertex`, (optional)) – Add Vertex, Add vertex to active spline
        * **MASK\_OT\_slide\_point** (`MASK_OT_slide_point`, (optional)) – Slide Point, Slide control points

bpy.ops.mask.copy\_splines()[#](#bpy.ops.mask.copy_splines "Link to this definition")
:   Copy the selected splines to the internal clipboard

bpy.ops.mask.cyclic\_toggle()[#](#bpy.ops.mask.cyclic_toggle "Link to this definition")
:   Toggle cyclic for selected splines

bpy.ops.mask.delete(*confirm=True*)[#](#bpy.ops.mask.delete "Link to this definition")
:   Delete selected control points or splines

    Parameters:
    :   **confirm** (*boolean**,* *(**optional**)*) – Confirm, Prompt for confirmation

bpy.ops.mask.duplicate()[#](#bpy.ops.mask.duplicate "Link to this definition")
:   Duplicate selected control points and segments between them

bpy.ops.mask.duplicate\_move(*MASK\_OT\_duplicate=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.mask.duplicate_move "Link to this definition")
:   Duplicate mask and move

    Parameters:
    :   * **MASK\_OT\_duplicate** (`MASK_OT_duplicate`, (optional)) – Duplicate Mask, Duplicate selected control points and segments between them
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.mask.feather\_weight\_clear()[#](#bpy.ops.mask.feather_weight_clear "Link to this definition")
:   Reset the feather weight to zero

bpy.ops.mask.handle\_type\_set(*type='AUTO'*)[#](#bpy.ops.mask.handle_type_set "Link to this definition")
:   Set type of handles for selected control points

    Parameters:
    :   **type** (*enum in* *[**'AUTO'**,* *'VECTOR'**,* *'ALIGNED'**,* *'ALIGNED\_DOUBLESIDE'**,* *'FREE'**]**,* *(**optional**)*) – Type, Spline type

bpy.ops.mask.hide\_view\_clear(*select=True*)[#](#bpy.ops.mask.hide_view_clear "Link to this definition")
:   Reveal temporarily hidden mask layers

    Parameters:
    :   **select** (*boolean**,* *(**optional**)*) – Select

bpy.ops.mask.hide\_view\_set(*unselected=False*)[#](#bpy.ops.mask.hide_view_set "Link to this definition")
:   Temporarily hide mask layers

    Parameters:
    :   **unselected** (*boolean**,* *(**optional**)*) – Unselected, Hide unselected rather than selected layers

bpy.ops.mask.layer\_move(*direction='UP'*)[#](#bpy.ops.mask.layer_move "Link to this definition")
:   Move the active layer up/down in the list

    Parameters:
    :   **direction** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Direction, Direction to move the active layer

bpy.ops.mask.layer\_new(*name=''*)[#](#bpy.ops.mask.layer_new "Link to this definition")
:   Add new mask layer for masking

    Parameters:
    :   **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of new mask layer

bpy.ops.mask.layer\_remove()[#](#bpy.ops.mask.layer_remove "Link to this definition")
:   Remove mask layer

bpy.ops.mask.new(*name=''*)[#](#bpy.ops.mask.new "Link to this definition")
:   Create new mask

    Parameters:
    :   **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of new mask

bpy.ops.mask.normals\_make\_consistent()[#](#bpy.ops.mask.normals_make_consistent "Link to this definition")
:   Recalculate the direction of selected handles

bpy.ops.mask.parent\_clear()[#](#bpy.ops.mask.parent_clear "Link to this definition")
:   Clear the mask’s parenting

bpy.ops.mask.parent\_set()[#](#bpy.ops.mask.parent_set "Link to this definition")
:   Set the mask’s parenting

bpy.ops.mask.paste\_splines()[#](#bpy.ops.mask.paste_splines "Link to this definition")
:   Paste splines from the internal clipboard

bpy.ops.mask.primitive\_circle\_add(*size=100.0*, *location=(0.0, 0.0)*)[#](#bpy.ops.mask.primitive_circle_add "Link to this definition")
:   Add new circle-shaped spline

    Parameters:
    :   * **size** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Size, Size of new circle
        * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of new circle

bpy.ops.mask.primitive\_square\_add(*size=100.0*, *location=(0.0, 0.0)*)[#](#bpy.ops.mask.primitive_square_add "Link to this definition")
:   Add new square-shaped spline

    Parameters:
    :   * **size** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Size, Size of new circle
        * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of new circle

bpy.ops.mask.select(*extend=False*, *deselect=False*, *toggle=False*, *deselect\_all=False*, *select\_passthrough=False*, *location=(0.0, 0.0)*)[#](#bpy.ops.mask.select "Link to this definition")
:   Select spline points

    Parameters:
    :   * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection instead of deselecting everything first
        * **deselect** (*boolean**,* *(**optional**)*) – Deselect, Remove from selection
        * **toggle** (*boolean**,* *(**optional**)*) – Toggle Selection, Toggle the selection
        * **deselect\_all** (*boolean**,* *(**optional**)*) – Deselect On Nothing, Deselect all when nothing under the cursor
        * **select\_passthrough** (*boolean**,* *(**optional**)*) – Only Select Unselected, Ignore the select action when the element is already selected
        * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of vertex in normalized space

bpy.ops.mask.select\_all(*action='TOGGLE'*)[#](#bpy.ops.mask.select_all "Link to this definition")
:   Change selection of all curve points

    Parameters:
    :   **action** (*enum in* *[**'TOGGLE'**,* *'SELECT'**,* *'DESELECT'**,* *'INVERT'**]**,* *(**optional**)*) –

        Action, Selection action to execute

        * `TOGGLE`
          Toggle – Toggle selection for all elements.
        * `SELECT`
          Select – Select all elements.
        * `DESELECT`
          Deselect – Deselect all elements.
        * `INVERT`
          Invert – Invert selection of all elements.

bpy.ops.mask.select\_box(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.mask.select_box "Link to this definition")
:   Select curve points using box selection

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.

bpy.ops.mask.select\_circle(*x=0*, *y=0*, *radius=25*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.mask.select_circle "Link to this definition")
:   Select curve points using circle selection

    Parameters:
    :   * **x** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X
        * **y** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y
        * **radius** (*int in* *[**1**,* *inf**]**,* *(**optional**)*) – Radius
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.

bpy.ops.mask.select\_lasso(*path=None*, *mode='SET'*)[#](#bpy.ops.mask.select_lasso "Link to this definition")
:   Select curve points using lasso selection

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.

bpy.ops.mask.select\_less()[#](#bpy.ops.mask.select_less "Link to this definition")
:   Deselect spline points at the boundary of each selection region

bpy.ops.mask.select\_linked()[#](#bpy.ops.mask.select_linked "Link to this definition")
:   Select all curve points linked to already selected ones

bpy.ops.mask.select\_linked\_pick(*deselect=False*)[#](#bpy.ops.mask.select_linked_pick "Link to this definition")
:   (De)select all points linked to the curve under the mouse cursor

    Parameters:
    :   **deselect** (*boolean**,* *(**optional**)*) – Deselect

bpy.ops.mask.select\_more()[#](#bpy.ops.mask.select_more "Link to this definition")
:   Select more spline points connected to initial selection

bpy.ops.mask.shape\_key\_clear()[#](#bpy.ops.mask.shape_key_clear "Link to this definition")
:   Remove mask shape keyframe for active mask layer at the current frame

bpy.ops.mask.shape\_key\_feather\_reset()[#](#bpy.ops.mask.shape_key_feather_reset "Link to this definition")
:   Reset feather weights on all selected points animation values

bpy.ops.mask.shape\_key\_insert()[#](#bpy.ops.mask.shape_key_insert "Link to this definition")
:   Insert mask shape keyframe for active mask layer at the current frame

bpy.ops.mask.shape\_key\_rekey(*location=True*, *feather=True*)[#](#bpy.ops.mask.shape_key_rekey "Link to this definition")
:   Recalculate animation data on selected points for frames selected in the dopesheet

    Parameters:
    :   * **location** (*boolean**,* *(**optional**)*) – Location
        * **feather** (*boolean**,* *(**optional**)*) – Feather

bpy.ops.mask.slide\_point(*slide\_feather=False*, *is\_new\_point=False*)[#](#bpy.ops.mask.slide_point "Link to this definition")
:   Slide control points

    Parameters:
    :   * **slide\_feather** (*boolean**,* *(**optional**)*) – Slide Feather, First try to slide feather instead of vertex
        * **is\_new\_point** (*boolean**,* *(**optional**)*) – Slide New Point, Newly created vertex is being slid

bpy.ops.mask.slide\_spline\_curvature()[#](#bpy.ops.mask.slide_spline_curvature "Link to this definition")
:   Slide a point on the spline to define its curvature

bpy.ops.mask.switch\_direction()[#](#bpy.ops.mask.switch_direction "Link to this definition")
:   Switch direction of selected splines

[Next

Material Operators](material.md)
[Previous

Marker Operators](marker.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.mask.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.mask.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Mask Operators
  + [`add_feather_vertex()`](#bpy.ops.mask.add_feather_vertex)
  + [`add_feather_vertex_slide()`](#bpy.ops.mask.add_feather_vertex_slide)
  + [`add_vertex()`](#bpy.ops.mask.add_vertex)
  + [`add_vertex_slide()`](#bpy.ops.mask.add_vertex_slide)
  + [`copy_splines()`](#bpy.ops.mask.copy_splines)
  + [`cyclic_toggle()`](#bpy.ops.mask.cyclic_toggle)
  + [`delete()`](#bpy.ops.mask.delete)
  + [`duplicate()`](#bpy.ops.mask.duplicate)
  + [`duplicate_move()`](#bpy.ops.mask.duplicate_move)
  + [`feather_weight_clear()`](#bpy.ops.mask.feather_weight_clear)
  + [`handle_type_set()`](#bpy.ops.mask.handle_type_set)
  + [`hide_view_clear()`](#bpy.ops.mask.hide_view_clear)
  + [`hide_view_set()`](#bpy.ops.mask.hide_view_set)
  + [`layer_move()`](#bpy.ops.mask.layer_move)
  + [`layer_new()`](#bpy.ops.mask.layer_new)
  + [`layer_remove()`](#bpy.ops.mask.layer_remove)
  + [`new()`](#bpy.ops.mask.new)
  + [`normals_make_consistent()`](#bpy.ops.mask.normals_make_consistent)
  + [`parent_clear()`](#bpy.ops.mask.parent_clear)
  + [`parent_set()`](#bpy.ops.mask.parent_set)
  + [`paste_splines()`](#bpy.ops.mask.paste_splines)
  + [`primitive_circle_add()`](#bpy.ops.mask.primitive_circle_add)
  + [`primitive_square_add()`](#bpy.ops.mask.primitive_square_add)
  + [`select()`](#bpy.ops.mask.select)
  + [`select_all()`](#bpy.ops.mask.select_all)
  + [`select_box()`](#bpy.ops.mask.select_box)
  + [`select_circle()`](#bpy.ops.mask.select_circle)
  + [`select_lasso()`](#bpy.ops.mask.select_lasso)
  + [`select_less()`](#bpy.ops.mask.select_less)
  + [`select_linked()`](#bpy.ops.mask.select_linked)
  + [`select_linked_pick()`](#bpy.ops.mask.select_linked_pick)
  + [`select_more()`](#bpy.ops.mask.select_more)
  + [`shape_key_clear()`](#bpy.ops.mask.shape_key_clear)
  + [`shape_key_feather_reset()`](#bpy.ops.mask.shape_key_feather_reset)
  + [`shape_key_insert()`](#bpy.ops.mask.shape_key_insert)
  + [`shape_key_rekey()`](#bpy.ops.mask.shape_key_rekey)
  + [`slide_point()`](#bpy.ops.mask.slide_point)
  + [`slide_spline_curvature()`](#bpy.ops.mask.slide_spline_curvature)
  + [`switch_direction()`](#bpy.ops.mask.switch_direction)