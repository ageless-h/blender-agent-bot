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

# Grease Pencil Operators[#](#module-bpy.ops.grease_pencil "Link to this heading")

bpy.ops.grease\_pencil.brush\_stroke(*stroke=None*, *mode='NORMAL'*, *pen\_flip=False*)[#](#bpy.ops.grease_pencil.brush_stroke "Link to this definition")
:   Draw a new stroke in the active Grease Pencil object

    Parameters:
    :   * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **mode** (*enum in* *[**'NORMAL'**,* *'INVERT'**,* *'SMOOTH'**]**,* *(**optional**)*) –

          Stroke Mode, Action taken when a paint stroke is made

          + `NORMAL`
            Regular – Apply brush normally.
          + `INVERT`
            Invert – Invert action of brush for duration of stroke.
          + `SMOOTH`
            Smooth – Switch brush to smooth mode for duration of stroke.
        * **pen\_flip** (*boolean**,* *(**optional**)*) – Pen Flip, Whether a tablet’s eraser mode is being used

bpy.ops.grease\_pencil.caps\_set(*type='ROUND'*)[#](#bpy.ops.grease_pencil.caps_set "Link to this definition")
:   Change curve caps mode (rounded or flat)

    Parameters:
    :   **type** (*enum in* *[**'ROUND'**,* *'FLAT'**,* *'START'**,* *'END'**]**,* *(**optional**)*) –

        Type

        * `ROUND`
          Rounded – Set as default rounded.
        * `FLAT`
          Flat.
        * `START`
          Toggle Start.
        * `END`
          Toggle End.

bpy.ops.grease\_pencil.clean\_loose(*limit=1*)[#](#bpy.ops.grease_pencil.clean_loose "Link to this definition")
:   Remove loose points

    Parameters:
    :   **limit** (*int in* *[**1**,* *inf**]**,* *(**optional**)*) – Limit, Number of points to consider stroke as loose

bpy.ops.grease\_pencil.copy()[#](#bpy.ops.grease_pencil.copy "Link to this definition")
:   Copy the selected Grease Pencil points or strokes to the internal clipboard

bpy.ops.grease\_pencil.cyclical\_set(*type='TOGGLE'*)[#](#bpy.ops.grease_pencil.cyclical_set "Link to this definition")
:   Close or open the selected stroke adding a segment from last to first point

    Parameters:
    :   **type** (*enum in* *[**'CLOSE'**,* *'OPEN'**,* *'TOGGLE'**]**,* *(**optional**)*) – Type

bpy.ops.grease\_pencil.delete()[#](#bpy.ops.grease_pencil.delete "Link to this definition")
:   Delete selected strokes or points

bpy.ops.grease\_pencil.delete\_frame(*type='ACTIVE\_FRAME'*)[#](#bpy.ops.grease_pencil.delete_frame "Link to this definition")
:   Delete Grease Pencil Frame(s)

    Parameters:
    :   **type** (*enum in* *[**'ACTIVE\_FRAME'**,* *'ALL\_FRAMES'**]**,* *(**optional**)*) –

        Type, Method used for deleting Grease Pencil frames

        * `ACTIVE_FRAME`
          Active Frame – Deletes current frame in the active layer.
        * `ALL_FRAMES`
          All Active Frames – Delete active frames for all layers.

bpy.ops.grease\_pencil.dissolve(*type='POINTS'*)[#](#bpy.ops.grease_pencil.dissolve "Link to this definition")
:   Delete selected points without splitting strokes

    Parameters:
    :   **type** (*enum in* *[**'POINTS'**,* *'BETWEEN'**,* *'UNSELECT'**]**,* *(**optional**)*) –

        Type, Method used for dissolving stroke points

        * `POINTS`
          Dissolve – Dissolve selected points.
        * `BETWEEN`
          Dissolve Between – Dissolve points between selected points.
        * `UNSELECT`
          Dissolve Unselect – Dissolve all unselected points.

bpy.ops.grease\_pencil.duplicate()[#](#bpy.ops.grease_pencil.duplicate "Link to this definition")
:   Duplicate the selected points

bpy.ops.grease\_pencil.duplicate\_move(*GREASE\_PENCIL\_OT\_duplicate=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.grease_pencil.duplicate_move "Link to this definition")
:   Make copies of the selected Grease Pencil strokes and move them

    Parameters:
    :   * **GREASE\_PENCIL\_OT\_duplicate** (`GREASE_PENCIL_OT_duplicate`, (optional)) – Duplicate, Duplicate the selected points
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.grease\_pencil.extrude()[#](#bpy.ops.grease_pencil.extrude "Link to this definition")
:   Extrude the selected points

bpy.ops.grease\_pencil.extrude\_move(*GREASE\_PENCIL\_OT\_extrude=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.grease_pencil.extrude_move "Link to this definition")
:   Extrude selected points and move them

    Parameters:
    :   * **GREASE\_PENCIL\_OT\_extrude** (`GREASE_PENCIL_OT_extrude`, (optional)) – Extrude Stroke Points, Extrude the selected points
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.grease\_pencil.fill(*on\_back=False*, *invert=False*, *precision=False*)[#](#bpy.ops.grease_pencil.fill "Link to this definition")
:   Fill with color the shape formed by strokes

    Parameters:
    :   * **on\_back** (*boolean**,* *(**optional**)*) – Draw on Back, Send new stroke to back
        * **invert** (*boolean**,* *(**optional**)*) – Invert, Find boundary of unfilled instead of filled regions
        * **precision** (*boolean**,* *(**optional**)*) – Precision, Use precision movement for extension lines

bpy.ops.grease\_pencil.insert\_blank\_frame(*all\_layers=False*, *duration=0*)[#](#bpy.ops.grease_pencil.insert_blank_frame "Link to this definition")
:   Insert a blank frame on the current scene frame

    Parameters:
    :   * **all\_layers** (*boolean**,* *(**optional**)*) – All Layers, Insert a blank frame in all editable layers
        * **duration** (*int in* *[**0**,* *1048574**]**,* *(**optional**)*) – Duration

bpy.ops.grease\_pencil.layer\_active(*layer=0*)[#](#bpy.ops.grease_pencil.layer_active "Link to this definition")
:   Set the active Grease Pencil layer

    Parameters:
    :   **layer** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Grease Pencil Layer

bpy.ops.grease\_pencil.layer\_add(*new\_layer\_name='Layer'*)[#](#bpy.ops.grease_pencil.layer_add "Link to this definition")
:   Add a new Grease Pencil layer in the active object

    Parameters:
    :   **new\_layer\_name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the new layer

bpy.ops.grease\_pencil.layer\_duplicate(*empty\_keyframes=False*)[#](#bpy.ops.grease_pencil.layer_duplicate "Link to this definition")
:   Make a copy of the active Grease Pencil layer

    Parameters:
    :   **empty\_keyframes** (*boolean**,* *(**optional**)*) – Empty Keyframes, Add Empty Keyframes

bpy.ops.grease\_pencil.layer\_group\_add(*new\_layer\_group\_name=''*)[#](#bpy.ops.grease_pencil.layer_group_add "Link to this definition")
:   Add a new Grease Pencil layer group in the active object

    Parameters:
    :   **new\_layer\_group\_name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the new layer group

bpy.ops.grease\_pencil.layer\_group\_remove(*keep\_children=False*)[#](#bpy.ops.grease_pencil.layer_group_remove "Link to this definition")
:   Remove Grease Pencil layer group in the active object

    Parameters:
    :   **keep\_children** (*boolean**,* *(**optional**)*) – Keep children nodes, Keep the children nodes of the group and only delete the group itself

bpy.ops.grease\_pencil.layer\_hide(*unselected=False*)[#](#bpy.ops.grease_pencil.layer_hide "Link to this definition")
:   Hide selected/unselected Grease Pencil layers

    Parameters:
    :   **unselected** (*boolean**,* *(**optional**)*) – Unselected, Hide unselected rather than selected layers

bpy.ops.grease\_pencil.layer\_isolate(*affect\_visibility=False*)[#](#bpy.ops.grease_pencil.layer_isolate "Link to this definition")
:   Make only active layer visible/editable

    Parameters:
    :   **affect\_visibility** (*boolean**,* *(**optional**)*) – Affect Visibility, Also affect the visibility

bpy.ops.grease\_pencil.layer\_lock\_all(*lock=True*)[#](#bpy.ops.grease_pencil.layer_lock_all "Link to this definition")
:   Lock all Grease Pencil layers to prevent them from being accidentally modified

    Parameters:
    :   **lock** (*boolean**,* *(**optional**)*) – Lock Value, Lock/Unlock all layers

bpy.ops.grease\_pencil.layer\_mask\_add(*name=''*)[#](#bpy.ops.grease_pencil.layer_mask_add "Link to this definition")
:   Add new layer as masking

    Parameters:
    :   **name** (*string**,* *(**optional**,* *never None**)*) – Layer, Name of the layer

bpy.ops.grease\_pencil.layer\_mask\_remove()[#](#bpy.ops.grease_pencil.layer_mask_remove "Link to this definition")
:   Remove Layer Mask

bpy.ops.grease\_pencil.layer\_mask\_reorder(*direction='UP'*)[#](#bpy.ops.grease_pencil.layer_mask_reorder "Link to this definition")
:   Reorder the active Grease Pencil mask layer up/down in the list

    Parameters:
    :   **direction** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Direction

bpy.ops.grease\_pencil.layer\_remove()[#](#bpy.ops.grease_pencil.layer_remove "Link to this definition")
:   Remove the active Grease Pencil layer

bpy.ops.grease\_pencil.layer\_reorder(*target\_layer\_name='Layer'*, *location='ABOVE'*)[#](#bpy.ops.grease_pencil.layer_reorder "Link to this definition")
:   Reorder the active Grease Pencil layer

    Parameters:
    :   * **target\_layer\_name** (*string**,* *(**optional**,* *never None**)*) – Target Name, Name of the target layer
        * **location** (*enum in* *[**'ABOVE'**,* *'BELOW'**]**,* *(**optional**)*) – Location

bpy.ops.grease\_pencil.layer\_reveal()[#](#bpy.ops.grease_pencil.layer_reveal "Link to this definition")
:   Show all Grease Pencil layers

bpy.ops.grease\_pencil.material\_copy\_to\_object(*only\_active=True*)[#](#bpy.ops.grease_pencil.material_copy_to_object "Link to this definition")
:   Append Materials of the active Grease Pencil to other object

    Parameters:
    :   **only\_active** (*boolean**,* *(**optional**)*) – Only Active, Append only active material, uncheck to append all materials

bpy.ops.grease\_pencil.material\_hide(*invert=False*)[#](#bpy.ops.grease_pencil.material_hide "Link to this definition")
:   Hide active/inactive Grease Pencil material(s)

    Parameters:
    :   **invert** (*boolean**,* *(**optional**)*) – Invert, Hide inactive materials instead of the active one

bpy.ops.grease\_pencil.material\_lock\_all()[#](#bpy.ops.grease_pencil.material_lock_all "Link to this definition")
:   Lock all Grease Pencil materials to prevent them from being accidentally modified

bpy.ops.grease\_pencil.material\_lock\_unselected()[#](#bpy.ops.grease_pencil.material_lock_unselected "Link to this definition")
:   Lock any material not used in any selected stroke

bpy.ops.grease\_pencil.material\_lock\_unused()[#](#bpy.ops.grease_pencil.material_lock_unused "Link to this definition")
:   Lock and hide any material not used

bpy.ops.grease\_pencil.material\_reveal()[#](#bpy.ops.grease_pencil.material_reveal "Link to this definition")
:   Unhide all hidden Grease Pencil materials

bpy.ops.grease\_pencil.material\_select(*deselect=False*)[#](#bpy.ops.grease_pencil.material_select "Link to this definition")
:   Select/Deselect all Grease Pencil strokes using current material

    Parameters:
    :   **deselect** (*boolean**,* *(**optional**)*) – Deselect, Unselect strokes

bpy.ops.grease\_pencil.material\_unlock\_all()[#](#bpy.ops.grease_pencil.material_unlock_all "Link to this definition")
:   Unlock all Grease Pencil materials so that they can be edited

bpy.ops.grease\_pencil.move\_to\_layer(*target\_layer\_name='Layer'*, *add\_new\_layer=False*)[#](#bpy.ops.grease_pencil.move_to_layer "Link to this definition")
:   Move selected strokes to another layer

    Parameters:
    :   * **target\_layer\_name** (*string**,* *(**optional**,* *never None**)*) – Name, Target Grease Pencil Layer
        * **add\_new\_layer** (*boolean**,* *(**optional**)*) – New Layer, Move selection to a new layer

bpy.ops.grease\_pencil.paste(*paste\_back=False*)[#](#bpy.ops.grease_pencil.paste "Link to this definition")
:   Paste Grease Pencil points or strokes from the internal clipboard to the active layer

    Parameters:
    :   **paste\_back** (*boolean**,* *(**optional**)*) – Paste on Back, Add pasted strokes behind all strokes

bpy.ops.grease\_pencil.primitive\_arc(*subdivision=62*, *type='ARC'*)[#](#bpy.ops.grease_pencil.primitive_arc "Link to this definition")
:   Create predefined grease pencil stroke arcs

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape

bpy.ops.grease\_pencil.primitive\_box(*subdivision=3*, *type='BOX'*)[#](#bpy.ops.grease_pencil.primitive_box "Link to this definition")
:   Create predefined grease pencil stroke boxes

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape

bpy.ops.grease\_pencil.primitive\_circle(*subdivision=94*, *type='CIRCLE'*)[#](#bpy.ops.grease_pencil.primitive_circle "Link to this definition")
:   Create predefined grease pencil stroke circles

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape

bpy.ops.grease\_pencil.primitive\_curve(*subdivision=62*, *type='CURVE'*)[#](#bpy.ops.grease_pencil.primitive_curve "Link to this definition")
:   Create predefined grease pencil stroke curve shapes

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape

bpy.ops.grease\_pencil.primitive\_line(*subdivision=6*, *type='LINE'*)[#](#bpy.ops.grease_pencil.primitive_line "Link to this definition")
:   Create predefined grease pencil stroke lines

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape

bpy.ops.grease\_pencil.primitive\_polyline(*subdivision=6*, *type='POLYLINE'*)[#](#bpy.ops.grease_pencil.primitive_polyline "Link to this definition")
:   Create predefined grease pencil stroke polylines

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape

bpy.ops.grease\_pencil.reorder(*direction='TOP'*)[#](#bpy.ops.grease_pencil.reorder "Link to this definition")
:   Change the display order of the selected strokes

    Parameters:
    :   **direction** (*enum in* *[**'TOP'**,* *'UP'**,* *'DOWN'**,* *'BOTTOM'**]**,* *(**optional**)*) – Direction

bpy.ops.grease\_pencil.sculpt\_paint(*stroke=None*, *mode='NORMAL'*, *pen\_flip=False*)[#](#bpy.ops.grease_pencil.sculpt_paint "Link to this definition")
:   Draw a new stroke in the active Grease Pencil object

    Parameters:
    :   * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **mode** (*enum in* *[**'NORMAL'**,* *'INVERT'**,* *'SMOOTH'**]**,* *(**optional**)*) –

          Stroke Mode, Action taken when a paint stroke is made

          + `NORMAL`
            Regular – Apply brush normally.
          + `INVERT`
            Invert – Invert action of brush for duration of stroke.
          + `SMOOTH`
            Smooth – Switch brush to smooth mode for duration of stroke.
        * **pen\_flip** (*boolean**,* *(**optional**)*) – Pen Flip, Whether a tablet’s eraser mode is being used

bpy.ops.grease\_pencil.select\_all(*action='TOGGLE'*)[#](#bpy.ops.grease_pencil.select_all "Link to this definition")
:   (De)select all visible strokes

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

bpy.ops.grease\_pencil.select\_alternate(*deselect\_ends=False*)[#](#bpy.ops.grease_pencil.select_alternate "Link to this definition")
:   Select alternated points in strokes with already selected points

    Parameters:
    :   **deselect\_ends** (*boolean**,* *(**optional**)*) – Deselect Ends, (De)select the first and last point of each stroke

bpy.ops.grease\_pencil.select\_ends(*amount\_start=0*, *amount\_end=1*)[#](#bpy.ops.grease_pencil.select_ends "Link to this definition")
:   Select end points of strokes

    Parameters:
    :   * **amount\_start** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Amount Start, Number of points to select from the start
        * **amount\_end** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Amount End, Number of points to select from the end

bpy.ops.grease\_pencil.select\_less()[#](#bpy.ops.grease_pencil.select_less "Link to this definition")
:   Shrink the selection by one point

bpy.ops.grease\_pencil.select\_linked()[#](#bpy.ops.grease_pencil.select_linked "Link to this definition")
:   Select all points in curves with any point selection

bpy.ops.grease\_pencil.select\_more()[#](#bpy.ops.grease_pencil.select_more "Link to this definition")
:   Grow the selection by one point

bpy.ops.grease\_pencil.select\_random(*ratio=0.5*, *seed=0*, *action='SELECT'*)[#](#bpy.ops.grease_pencil.select_random "Link to this definition")
:   Selects random points from the current strokes selection

    Parameters:
    :   * **ratio** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Ratio, Portion of items to select randomly
        * **seed** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Random Seed, Seed for the random number generator
        * **action** (*enum in* *[**'SELECT'**,* *'DESELECT'**]**,* *(**optional**)*) –

          Action, Selection action to execute

          + `SELECT`
            Select – Select all elements.
          + `DESELECT`
            Deselect – Deselect all elements.

bpy.ops.grease\_pencil.separate(*mode='SELECTED'*)[#](#bpy.ops.grease_pencil.separate "Link to this definition")
:   Separate the selected geometry into a new grease pencil object

    Parameters:
    :   **mode** (*enum in* *[**'SELECTED'**,* *'MATERIAL'**,* *'LAYER'**]**,* *(**optional**)*) –

        Mode

        * `SELECTED`
          Selection – Separate selected geometry.
        * `MATERIAL`
          By Material – Separate by material.
        * `LAYER`
          By Layer – Separate by layer.

bpy.ops.grease\_pencil.set\_active\_material()[#](#bpy.ops.grease_pencil.set_active_material "Link to this definition")
:   Set the selected stroke material as the active material

bpy.ops.grease\_pencil.set\_material(*slot='DEFAULT'*)[#](#bpy.ops.grease_pencil.set_material "Link to this definition")
:   Set active material

    Parameters:
    :   **slot** (*enum in* *[**'DEFAULT'**]**,* *(**optional**)*) – Material Slot

bpy.ops.grease\_pencil.set\_selection\_mode(*mode='POINT'*)[#](#bpy.ops.grease_pencil.set_selection_mode "Link to this definition")
:   Change the selection mode for Grease Pencil strokes

    Parameters:
    :   **mode** (enum in [Grease Pencil Selectmode Items](../../../appendix/bpy_types_enum_items/grease_pencil_selectmode_items.md#rna-enum-grease-pencil-selectmode-items), (optional)) – Mode

bpy.ops.grease\_pencil.set\_uniform\_opacity(*opacity=1.0*)[#](#bpy.ops.grease_pencil.set_uniform_opacity "Link to this definition")
:   Set all stroke points to same opacity

    Parameters:
    :   **opacity** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Opacity

bpy.ops.grease\_pencil.set\_uniform\_thickness(*thickness=0.1*)[#](#bpy.ops.grease_pencil.set_uniform_thickness "Link to this definition")
:   Set all stroke points to same thickness

    Parameters:
    :   **thickness** (*float in* *[**0**,* *1000**]**,* *(**optional**)*) – Thickness, Thickness

bpy.ops.grease\_pencil.snap\_cursor\_to\_selected()[#](#bpy.ops.grease_pencil.snap_cursor_to_selected "Link to this definition")
:   Snap cursor to center of selected points

bpy.ops.grease\_pencil.snap\_to\_cursor(*use\_offset=True*)[#](#bpy.ops.grease_pencil.snap_to_cursor "Link to this definition")
:   Snap selected points/strokes to the cursor

    Parameters:
    :   **use\_offset** (*boolean**,* *(**optional**)*) – With Offset, Offset the entire stroke instead of selected points only

bpy.ops.grease\_pencil.snap\_to\_grid()[#](#bpy.ops.grease_pencil.snap_to_grid "Link to this definition")
:   Snap selected points to the nearest grid points

bpy.ops.grease\_pencil.stroke\_cutter(*path=None*)[#](#bpy.ops.grease_pencil.stroke_cutter "Link to this definition")
:   Delete stroke points in between intersecting strokes

    Parameters:
    :   **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

bpy.ops.grease\_pencil.stroke\_material\_set(*material=''*)[#](#bpy.ops.grease_pencil.stroke_material_set "Link to this definition")
:   Assign the active material slot to the selected strokes

    Parameters:
    :   **material** (*string**,* *(**optional**,* *never None**)*) – Material, Name of the material

bpy.ops.grease\_pencil.stroke\_merge\_by\_distance(*threshold=0.001*, *use\_unselected=False*)[#](#bpy.ops.grease_pencil.stroke_merge_by_distance "Link to this definition")
:   Merge points by distance

    Parameters:
    :   * **threshold** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Threshold
        * **use\_unselected** (*boolean**,* *(**optional**)*) – Unselected, Use whole stroke, not only selected points

bpy.ops.grease\_pencil.stroke\_simplify(*factor=0.01*)[#](#bpy.ops.grease_pencil.stroke_simplify "Link to this definition")
:   Simplify selected strokes

    Parameters:
    :   **factor** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Factor

bpy.ops.grease\_pencil.stroke\_smooth(*iterations=10*, *factor=1.0*, *smooth\_ends=False*, *keep\_shape=False*, *smooth\_position=True*, *smooth\_radius=True*, *smooth\_opacity=False*)[#](#bpy.ops.grease_pencil.stroke_smooth "Link to this definition")
:   Smooth selected strokes

    Parameters:
    :   * **iterations** (*int in* *[**1**,* *100**]**,* *(**optional**)*) – Iterations
        * **factor** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Factor
        * **smooth\_ends** (*boolean**,* *(**optional**)*) – Smooth Endpoints
        * **keep\_shape** (*boolean**,* *(**optional**)*) – Keep Shape
        * **smooth\_position** (*boolean**,* *(**optional**)*) – Position
        * **smooth\_radius** (*boolean**,* *(**optional**)*) – Radius
        * **smooth\_opacity** (*boolean**,* *(**optional**)*) – Opacity

bpy.ops.grease\_pencil.stroke\_subdivide(*number\_cuts=1*, *only\_selected=True*)[#](#bpy.ops.grease_pencil.stroke_subdivide "Link to this definition")
:   Subdivide between continuous selected points of the stroke adding a point half way between them

    Parameters:
    :   * **number\_cuts** (*int in* *[**1**,* *32**]**,* *(**optional**)*) – Number of Cuts
        * **only\_selected** (*boolean**,* *(**optional**)*) – Selected Points, Smooth only selected points in the stroke

bpy.ops.grease\_pencil.stroke\_subdivide\_smooth(*GREASE\_PENCIL\_OT\_stroke\_subdivide=None*, *GREASE\_PENCIL\_OT\_stroke\_smooth=None*)[#](#bpy.ops.grease_pencil.stroke_subdivide_smooth "Link to this definition")
:   Subdivide strokes and smooth them

    Parameters:
    :   * **GREASE\_PENCIL\_OT\_stroke\_subdivide** (`GREASE_PENCIL_OT_stroke_subdivide`, (optional)) – Subdivide Stroke, Subdivide between continuous selected points of the stroke adding a point half way between them
        * **GREASE\_PENCIL\_OT\_stroke\_smooth** (`GREASE_PENCIL_OT_stroke_smooth`, (optional)) – Smooth Stroke, Smooth selected strokes

bpy.ops.grease\_pencil.stroke\_switch\_direction()[#](#bpy.ops.grease_pencil.stroke_switch_direction "Link to this definition")
:   Change direction of the points of the selected strokes

bpy.ops.grease\_pencil.weight\_brush\_stroke(*stroke=None*, *mode='NORMAL'*, *pen\_flip=False*)[#](#bpy.ops.grease_pencil.weight_brush_stroke "Link to this definition")
:   Draw weight on stroke points in the active Grease Pencil object

    Parameters:
    :   * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **mode** (*enum in* *[**'NORMAL'**,* *'INVERT'**,* *'SMOOTH'**]**,* *(**optional**)*) –

          Stroke Mode, Action taken when a paint stroke is made

          + `NORMAL`
            Regular – Apply brush normally.
          + `INVERT`
            Invert – Invert action of brush for duration of stroke.
          + `SMOOTH`
            Smooth – Switch brush to smooth mode for duration of stroke.
        * **pen\_flip** (*boolean**,* *(**optional**)*) – Pen Flip, Whether a tablet’s eraser mode is being used

bpy.ops.grease\_pencil.weight\_sample()[#](#bpy.ops.grease_pencil.weight_sample "Link to this definition")
:   Set the weight of the Draw tool to the weight of the vertex under the mouse cursor

bpy.ops.grease\_pencil.weight\_toggle\_direction()[#](#bpy.ops.grease_pencil.weight_toggle_direction "Link to this definition")
:   Toggle Add/Subtract for the weight paint draw tool

[Next

Image Operators](image.md)
[Previous

Graph Operators](graph.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.grease_pencil.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.grease_pencil.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Grease Pencil Operators
  + [`brush_stroke()`](#bpy.ops.grease_pencil.brush_stroke)
  + [`caps_set()`](#bpy.ops.grease_pencil.caps_set)
  + [`clean_loose()`](#bpy.ops.grease_pencil.clean_loose)
  + [`copy()`](#bpy.ops.grease_pencil.copy)
  + [`cyclical_set()`](#bpy.ops.grease_pencil.cyclical_set)
  + [`delete()`](#bpy.ops.grease_pencil.delete)
  + [`delete_frame()`](#bpy.ops.grease_pencil.delete_frame)
  + [`dissolve()`](#bpy.ops.grease_pencil.dissolve)
  + [`duplicate()`](#bpy.ops.grease_pencil.duplicate)
  + [`duplicate_move()`](#bpy.ops.grease_pencil.duplicate_move)
  + [`extrude()`](#bpy.ops.grease_pencil.extrude)
  + [`extrude_move()`](#bpy.ops.grease_pencil.extrude_move)
  + [`fill()`](#bpy.ops.grease_pencil.fill)
  + [`insert_blank_frame()`](#bpy.ops.grease_pencil.insert_blank_frame)
  + [`layer_active()`](#bpy.ops.grease_pencil.layer_active)
  + [`layer_add()`](#bpy.ops.grease_pencil.layer_add)
  + [`layer_duplicate()`](#bpy.ops.grease_pencil.layer_duplicate)
  + [`layer_group_add()`](#bpy.ops.grease_pencil.layer_group_add)
  + [`layer_group_remove()`](#bpy.ops.grease_pencil.layer_group_remove)
  + [`layer_hide()`](#bpy.ops.grease_pencil.layer_hide)
  + [`layer_isolate()`](#bpy.ops.grease_pencil.layer_isolate)
  + [`layer_lock_all()`](#bpy.ops.grease_pencil.layer_lock_all)
  + [`layer_mask_add()`](#bpy.ops.grease_pencil.layer_mask_add)
  + [`layer_mask_remove()`](#bpy.ops.grease_pencil.layer_mask_remove)
  + [`layer_mask_reorder()`](#bpy.ops.grease_pencil.layer_mask_reorder)
  + [`layer_remove()`](#bpy.ops.grease_pencil.layer_remove)
  + [`layer_reorder()`](#bpy.ops.grease_pencil.layer_reorder)
  + [`layer_reveal()`](#bpy.ops.grease_pencil.layer_reveal)
  + [`material_copy_to_object()`](#bpy.ops.grease_pencil.material_copy_to_object)
  + [`material_hide()`](#bpy.ops.grease_pencil.material_hide)
  + [`material_lock_all()`](#bpy.ops.grease_pencil.material_lock_all)
  + [`material_lock_unselected()`](#bpy.ops.grease_pencil.material_lock_unselected)
  + [`material_lock_unused()`](#bpy.ops.grease_pencil.material_lock_unused)
  + [`material_reveal()`](#bpy.ops.grease_pencil.material_reveal)
  + [`material_select()`](#bpy.ops.grease_pencil.material_select)
  + [`material_unlock_all()`](#bpy.ops.grease_pencil.material_unlock_all)
  + [`move_to_layer()`](#bpy.ops.grease_pencil.move_to_layer)
  + [`paste()`](#bpy.ops.grease_pencil.paste)
  + [`primitive_arc()`](#bpy.ops.grease_pencil.primitive_arc)
  + [`primitive_box()`](#bpy.ops.grease_pencil.primitive_box)
  + [`primitive_circle()`](#bpy.ops.grease_pencil.primitive_circle)
  + [`primitive_curve()`](#bpy.ops.grease_pencil.primitive_curve)
  + [`primitive_line()`](#bpy.ops.grease_pencil.primitive_line)
  + [`primitive_polyline()`](#bpy.ops.grease_pencil.primitive_polyline)
  + [`reorder()`](#bpy.ops.grease_pencil.reorder)
  + [`sculpt_paint()`](#bpy.ops.grease_pencil.sculpt_paint)
  + [`select_all()`](#bpy.ops.grease_pencil.select_all)
  + [`select_alternate()`](#bpy.ops.grease_pencil.select_alternate)
  + [`select_ends()`](#bpy.ops.grease_pencil.select_ends)
  + [`select_less()`](#bpy.ops.grease_pencil.select_less)
  + [`select_linked()`](#bpy.ops.grease_pencil.select_linked)
  + [`select_more()`](#bpy.ops.grease_pencil.select_more)
  + [`select_random()`](#bpy.ops.grease_pencil.select_random)
  + [`separate()`](#bpy.ops.grease_pencil.separate)
  + [`set_active_material()`](#bpy.ops.grease_pencil.set_active_material)
  + [`set_material()`](#bpy.ops.grease_pencil.set_material)
  + [`set_selection_mode()`](#bpy.ops.grease_pencil.set_selection_mode)
  + [`set_uniform_opacity()`](#bpy.ops.grease_pencil.set_uniform_opacity)
  + [`set_uniform_thickness()`](#bpy.ops.grease_pencil.set_uniform_thickness)
  + [`snap_cursor_to_selected()`](#bpy.ops.grease_pencil.snap_cursor_to_selected)
  + [`snap_to_cursor()`](#bpy.ops.grease_pencil.snap_to_cursor)
  + [`snap_to_grid()`](#bpy.ops.grease_pencil.snap_to_grid)
  + [`stroke_cutter()`](#bpy.ops.grease_pencil.stroke_cutter)
  + [`stroke_material_set()`](#bpy.ops.grease_pencil.stroke_material_set)
  + [`stroke_merge_by_distance()`](#bpy.ops.grease_pencil.stroke_merge_by_distance)
  + [`stroke_simplify()`](#bpy.ops.grease_pencil.stroke_simplify)
  + [`stroke_smooth()`](#bpy.ops.grease_pencil.stroke_smooth)
  + [`stroke_subdivide()`](#bpy.ops.grease_pencil.stroke_subdivide)
  + [`stroke_subdivide_smooth()`](#bpy.ops.grease_pencil.stroke_subdivide_smooth)
  + [`stroke_switch_direction()`](#bpy.ops.grease_pencil.stroke_switch_direction)
  + [`weight_brush_stroke()`](#bpy.ops.grease_pencil.weight_brush_stroke)
  + [`weight_sample()`](#bpy.ops.grease_pencil.weight_sample)
  + [`weight_toggle_direction()`](#bpy.ops.grease_pencil.weight_toggle_direction)