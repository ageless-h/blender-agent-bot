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

# Gpencil Operators[#](#module-bpy.ops.gpencil "Link to this heading")

bpy.ops.gpencil.active\_frame\_delete()[#](#bpy.ops.gpencil.active_frame_delete "Link to this definition")
:   Delete the active frame for the active Grease Pencil Layer

bpy.ops.gpencil.active\_frames\_delete\_all()[#](#bpy.ops.gpencil.active_frames_delete_all "Link to this definition")
:   Delete the active frame(s) of all editable Grease Pencil layers

bpy.ops.gpencil.annotate(*mode='DRAW'*, *arrowstyle\_start='NONE'*, *arrowstyle\_end='NONE'*, *use\_stabilizer=False*, *stabilizer\_factor=0.75*, *stabilizer\_radius=35*, *stroke=None*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.annotate "Link to this definition")
:   Make annotations on the active data

    Parameters:
    :   * **mode** (*enum in* *[**'DRAW'**,* *'DRAW\_STRAIGHT'**,* *'DRAW\_POLY'**,* *'ERASER'**]**,* *(**optional**)*) –

          Mode, Way to interpret mouse movements

          + `DRAW`
            Draw Freehand – Draw freehand stroke(s).
          + `DRAW_STRAIGHT`
            Draw Straight Lines – Draw straight line segment(s).
          + `DRAW_POLY`
            Draw Poly Line – Click to place endpoints of straight line segments (connected).
          + `ERASER`
            Eraser – Erase Annotation strokes.
        * **arrowstyle\_start** (*enum in* *[**'NONE'**,* *'ARROW'**,* *'ARROW\_OPEN'**,* *'ARROW\_OPEN\_INVERTED'**,* *'DIAMOND'**]**,* *(**optional**)*) –

          Start Arrow Style, Stroke start style

          + `NONE`
            None – Don’t use any arrow/style in corner.
          + `ARROW`
            Arrow – Use closed arrow style.
          + `ARROW_OPEN`
            Open Arrow – Use open arrow style.
          + `ARROW_OPEN_INVERTED`
            Segment – Use perpendicular segment style.
          + `DIAMOND`
            Square – Use square style.
        * **arrowstyle\_end** (*enum in* *[**'NONE'**,* *'ARROW'**,* *'ARROW\_OPEN'**,* *'ARROW\_OPEN\_INVERTED'**,* *'DIAMOND'**]**,* *(**optional**)*) –

          End Arrow Style, Stroke end style

          + `NONE`
            None – Don’t use any arrow/style in corner.
          + `ARROW`
            Arrow – Use closed arrow style.
          + `ARROW_OPEN`
            Open Arrow – Use open arrow style.
          + `ARROW_OPEN_INVERTED`
            Segment – Use perpendicular segment style.
          + `DIAMOND`
            Square – Use square style.
        * **use\_stabilizer** (*boolean**,* *(**optional**)*) – Stabilize Stroke, Helper to draw smooth and clean lines. Press Shift for an invert effect (even if this option is not active)
        * **stabilizer\_factor** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Stabilizer Stroke Factor, Higher values gives a smoother stroke
        * **stabilizer\_radius** (*int in* *[**0**,* *200**]**,* *(**optional**)*) – Stabilizer Stroke Radius, Minimum distance from last point before stroke continues
        * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input, Wait for first click instead of painting immediately

bpy.ops.gpencil.annotation\_active\_frame\_delete()[#](#bpy.ops.gpencil.annotation_active_frame_delete "Link to this definition")
:   Delete the active frame for the active Annotation Layer

bpy.ops.gpencil.annotation\_add()[#](#bpy.ops.gpencil.annotation_add "Link to this definition")
:   Add new Annotation data-block

bpy.ops.gpencil.bake\_grease\_pencil\_animation(*frame\_start=1*, *frame\_end=250*, *step=1*, *only\_selected=False*, *frame\_target=1*, *project\_type='KEEP'*)[#](#bpy.ops.gpencil.bake_grease_pencil_animation "Link to this definition")
:   Bake grease pencil object transform to grease pencil keyframes

    Parameters:
    :   * **frame\_start** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – Start Frame, The start frame
        * **frame\_end** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – End Frame, The end frame of animation
        * **step** (*int in* *[**1**,* *100**]**,* *(**optional**)*) – Step, Step between generated frames
        * **only\_selected** (*boolean**,* *(**optional**)*) – Only Selected Keyframes, Convert only selected keyframes
        * **frame\_target** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – Target Frame, Destination frame
        * **project\_type** (*enum in* *[**'KEEP'**,* *'FRONT'**,* *'SIDE'**,* *'TOP'**,* *'VIEW'**,* *'CURSOR'**]**,* *(**optional**)*) –

          Projection Type

          + `KEEP`
            No Reproject.
          + `FRONT`
            Front – Reproject the strokes using the X-Z plane.
          + `SIDE`
            Side – Reproject the strokes using the Y-Z plane.
          + `TOP`
            Top – Reproject the strokes using the X-Y plane.
          + `VIEW`
            View – Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using ‘Cursor’ Stroke Placement.
          + `CURSOR`
            Cursor – Reproject the strokes using the orientation of 3D cursor.

bpy.ops.gpencil.bake\_mesh\_animation(*target='NEW'*, *frame\_start=1*, *frame\_end=250*, *step=1*, *thickness=1*, *angle=1.22173*, *offset=0.001*, *seams=False*, *faces=True*, *only\_selected=False*, *frame\_target=1*, *project\_type='VIEW'*)[#](#bpy.ops.gpencil.bake_mesh_animation "Link to this definition")
:   Bake mesh animation to grease pencil strokes

    Parameters:
    :   * **target** (*enum in* *[**'NEW'**,* *'SELECTED'**]**,* *(**optional**)*) – Target Object, Target grease pencil
        * **frame\_start** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – Start Frame, The start frame
        * **frame\_end** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – End Frame, The end frame of animation
        * **step** (*int in* *[**1**,* *100**]**,* *(**optional**)*) – Step, Step between generated frames
        * **thickness** (*int in* *[**1**,* *100**]**,* *(**optional**)*) – Thickness
        * **angle** (*float in* *[**0**,* *3.14159**]**,* *(**optional**)*) – Threshold Angle, Threshold to determine ends of the strokes
        * **offset** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Stroke Offset, Offset strokes from fill
        * **seams** (*boolean**,* *(**optional**)*) – Only Seam Edges, Convert only seam edges
        * **faces** (*boolean**,* *(**optional**)*) – Export Faces, Export faces as filled strokes
        * **only\_selected** (*boolean**,* *(**optional**)*) – Only Selected Keyframes, Convert only selected keyframes
        * **frame\_target** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – Target Frame, Destination frame
        * **project\_type** (*enum in* *[**'KEEP'**,* *'FRONT'**,* *'SIDE'**,* *'TOP'**,* *'VIEW'**,* *'CURSOR'**]**,* *(**optional**)*) –

          Projection Type

          + `KEEP`
            No Reproject.
          + `FRONT`
            Front – Reproject the strokes using the X-Z plane.
          + `SIDE`
            Side – Reproject the strokes using the Y-Z plane.
          + `TOP`
            Top – Reproject the strokes using the X-Y plane.
          + `VIEW`
            View – Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using ‘Cursor’ Stroke Placement.
          + `CURSOR`
            Cursor – Reproject the strokes using the orientation of 3D cursor.

bpy.ops.gpencil.blank\_frame\_add(*all\_layers=False*)[#](#bpy.ops.gpencil.blank_frame_add "Link to this definition")
:   Insert a blank frame on the current frame (all subsequently existing frames, if any, are shifted right by one frame)

    Parameters:
    :   **all\_layers** (*boolean**,* *(**optional**)*) – All Layers, Create blank frame in all layers, not only active

bpy.ops.gpencil.brush\_reset()[#](#bpy.ops.gpencil.brush_reset "Link to this definition")
:   Reset brush to default parameters

bpy.ops.gpencil.brush\_reset\_all()[#](#bpy.ops.gpencil.brush_reset_all "Link to this definition")
:   Delete all mode brushes and recreate a default set

bpy.ops.gpencil.convert(*type='PATH'*, *bevel\_depth=0.0*, *bevel\_resolution=0*, *use\_normalize\_weights=True*, *radius\_multiplier=1.0*, *use\_link\_strokes=False*, *timing\_mode='FULL'*, *frame\_range=100*, *start\_frame=1*, *use\_realtime=False*, *end\_frame=250*, *gap\_duration=0.0*, *gap\_randomness=0.0*, *seed=0*, *use\_timing\_data=False*)[#](#bpy.ops.gpencil.convert "Link to this definition")
:   Convert the active Grease Pencil layer to a new Curve Object

    Parameters:
    :   * **type** (*enum in* *[**'PATH'**,* *'CURVE'**,* *'POLY'**]**,* *(**optional**)*) –

          Type, Which type of curve to convert to

          + `PATH`
            Path – Animation path.
          + `CURVE`
            Bézier Curve – Smooth Bézier curve.
          + `POLY`
            Polygon Curve – Bézier curve with straight-line segments (vector handles).
        * **bevel\_depth** (*float in* *[**0**,* *1000**]**,* *(**optional**)*) – Bevel Depth
        * **bevel\_resolution** (*int in* *[**0**,* *32**]**,* *(**optional**)*) – Bevel Resolution, Bevel resolution when depth is non-zero
        * **use\_normalize\_weights** (*boolean**,* *(**optional**)*) – Normalize Weight, Normalize weight (set from stroke width)
        * **radius\_multiplier** (*float in* *[**0**,* *1000**]**,* *(**optional**)*) – Radius Factor, Multiplier for the points’ radii (set from stroke width)
        * **use\_link\_strokes** (*boolean**,* *(**optional**)*) – Link Strokes, Whether to link strokes with zero-radius sections of curves
        * **timing\_mode** (*enum in* *[**'NONE'**,* *'LINEAR'**,* *'FULL'**,* *'CUSTOMGAP'**]**,* *(**optional**)*) –

          Timing Mode, How to use timing data stored in strokes

          + `NONE`
            No Timing – Ignore timing.
          + `LINEAR`
            Linear – Simple linear timing.
          + `FULL`
            Original – Use the original timing, gaps included.
          + `CUSTOMGAP`
            Custom Gaps – Use the original timing, but with custom gap lengths (in frames).
        * **frame\_range** (*int in* *[**1**,* *10000**]**,* *(**optional**)*) – Frame Range, The duration of evaluation of the path control curve
        * **start\_frame** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – Start Frame, The start frame of the path control curve
        * **use\_realtime** (*boolean**,* *(**optional**)*) – Realtime, Whether the path control curve reproduces the drawing in realtime, starting from Start Frame
        * **end\_frame** (*int in* *[**1**,* *100000**]**,* *(**optional**)*) – End Frame, The end frame of the path control curve (if Realtime is not set)
        * **gap\_duration** (*float in* *[**0**,* *10000**]**,* *(**optional**)*) – Gap Duration, Custom Gap mode: (Average) length of gaps, in frames (Note: Realtime value, will be scaled if Realtime is not set)
        * **gap\_randomness** (*float in* *[**0**,* *10000**]**,* *(**optional**)*) – Gap Randomness, Custom Gap mode: Number of frames that gap lengths can vary
        * **seed** (*int in* *[**0**,* *1000**]**,* *(**optional**)*) – Random Seed, Custom Gap mode: Random generator seed
        * **use\_timing\_data** (*boolean**,* *(**optional**)*) – Has Valid Timing, Whether the converted Grease Pencil layer has valid timing data (internal use)

bpy.ops.gpencil.convert\_old\_files(*annotation=False*)[#](#bpy.ops.gpencil.convert_old_files "Link to this definition")
:   Convert 2.7x grease pencil files to 2.80

    Parameters:
    :   **annotation** (*boolean**,* *(**optional**)*) – Annotation, Convert to Annotations

bpy.ops.gpencil.copy()[#](#bpy.ops.gpencil.copy "Link to this definition")
:   Copy selected Grease Pencil points and strokes

bpy.ops.gpencil.data\_unlink()[#](#bpy.ops.gpencil.data_unlink "Link to this definition")
:   Unlink active Annotation data-block

bpy.ops.gpencil.delete(*type='POINTS'*)[#](#bpy.ops.gpencil.delete "Link to this definition")
:   Delete selected Grease Pencil strokes, vertices, or frames

    Parameters:
    :   **type** (*enum in* *[**'POINTS'**,* *'STROKES'**,* *'FRAME'**]**,* *(**optional**)*) –

        Type, Method used for deleting Grease Pencil data

        * `POINTS`
          Points – Delete selected points and split strokes into segments.
        * `STROKES`
          Strokes – Delete selected strokes.
        * `FRAME`
          Frame – Delete active frame.

bpy.ops.gpencil.dissolve(*type='POINTS'*)[#](#bpy.ops.gpencil.dissolve "Link to this definition")
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

bpy.ops.gpencil.draw(*mode='DRAW'*, *stroke=None*, *wait\_for\_input=True*, *disable\_straight=False*, *disable\_fill=False*, *disable\_stabilizer=False*, *guide\_last\_angle=0.0*)[#](#bpy.ops.gpencil.draw "Link to this definition")
:   Draw a new stroke in the active Grease Pencil object

    Parameters:
    :   * **mode** (*enum in* *[**'DRAW'**,* *'DRAW\_STRAIGHT'**,* *'ERASER'**]**,* *(**optional**)*) –

          Mode, Way to interpret mouse movements

          + `DRAW`
            Draw Freehand – Draw freehand stroke(s).
          + `DRAW_STRAIGHT`
            Draw Straight Lines – Draw straight line segment(s).
          + `ERASER`
            Eraser – Erase Grease Pencil strokes.
        * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input, Wait for first click instead of painting immediately
        * **disable\_straight** (*boolean**,* *(**optional**)*) – No Straight lines, Disable key for straight lines
        * **disable\_fill** (*boolean**,* *(**optional**)*) – No Fill Areas, Disable fill to use stroke as fill boundary
        * **disable\_stabilizer** (*boolean**,* *(**optional**)*) – No Stabilizer
        * **guide\_last\_angle** (*float in* *[**-10000**,* *10000**]**,* *(**optional**)*) – Angle, Speed guide angle

bpy.ops.gpencil.duplicate()[#](#bpy.ops.gpencil.duplicate "Link to this definition")
:   Duplicate the selected Grease Pencil strokes

bpy.ops.gpencil.duplicate\_move(*GPENCIL\_OT\_duplicate=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.gpencil.duplicate_move "Link to this definition")
:   Make copies of the selected Grease Pencil strokes and move them

    Parameters:
    :   * **GPENCIL\_OT\_duplicate** (`GPENCIL_OT_duplicate`, (optional)) – Duplicate Strokes, Duplicate the selected Grease Pencil strokes
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.gpencil.editmode\_toggle(*back=False*)[#](#bpy.ops.gpencil.editmode_toggle "Link to this definition")
:   Enter/Exit edit mode for Grease Pencil strokes

    Parameters:
    :   **back** (*boolean**,* *(**optional**)*) – Return to Previous Mode, Return to previous mode

bpy.ops.gpencil.extract\_palette\_vertex(*selected=False*, *threshold=1*)[#](#bpy.ops.gpencil.extract_palette_vertex "Link to this definition")
:   Extract all colors used in Grease Pencil Vertex and create a Palette

    Parameters:
    :   * **selected** (*boolean**,* *(**optional**)*) – Only Selected, Convert only selected strokes
        * **threshold** (*int in* *[**1**,* *4**]**,* *(**optional**)*) – Threshold

bpy.ops.gpencil.extrude()[#](#bpy.ops.gpencil.extrude "Link to this definition")
:   Extrude the selected Grease Pencil points

bpy.ops.gpencil.extrude\_move(*GPENCIL\_OT\_extrude=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.gpencil.extrude_move "Link to this definition")
:   Extrude selected points and move them

    Parameters:
    :   * **GPENCIL\_OT\_extrude** (`GPENCIL_OT_extrude`, (optional)) – Extrude Stroke Points, Extrude the selected Grease Pencil points
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.gpencil.fill(*on\_back=False*)[#](#bpy.ops.gpencil.fill "Link to this definition")
:   Fill with color the shape formed by strokes

    Parameters:
    :   **on\_back** (*boolean**,* *(**optional**)*) – Draw on Back, Send new stroke to back

bpy.ops.gpencil.frame\_clean\_duplicate(*type='ALL'*)[#](#bpy.ops.gpencil.frame_clean_duplicate "Link to this definition")
:   Remove duplicate keyframes

    Parameters:
    :   **type** (*enum in* *[**'ALL'**,* *'SELECTED'**]**,* *(**optional**)*) – Type

bpy.ops.gpencil.frame\_clean\_fill(*mode='ACTIVE'*)[#](#bpy.ops.gpencil.frame_clean_fill "Link to this definition")
:   Remove ‘no fill’ boundary strokes

    Parameters:
    :   **mode** (*enum in* *[**'ACTIVE'**,* *'ALL'**]**,* *(**optional**)*) –

        Mode

        * `ACTIVE`
          Active Frame Only – Clean active frame only.
        * `ALL`
          All Frames – Clean all frames in all layers.

bpy.ops.gpencil.frame\_clean\_loose(*limit=1*)[#](#bpy.ops.gpencil.frame_clean_loose "Link to this definition")
:   Remove loose points

    Parameters:
    :   **limit** (*int in* *[**1**,* *inf**]**,* *(**optional**)*) – Limit, Number of points to consider stroke as loose

bpy.ops.gpencil.frame\_duplicate(*mode='ACTIVE'*)[#](#bpy.ops.gpencil.frame_duplicate "Link to this definition")
:   Make a copy of the active Grease Pencil Frame

    Parameters:
    :   **mode** (*enum in* *[**'ACTIVE'**,* *'ALL'**]**,* *(**optional**)*) –

        Mode

        * `ACTIVE`
          Active – Duplicate frame in active layer only.
        * `ALL`
          All – Duplicate active frames in all layers.

bpy.ops.gpencil.generate\_weights(*mode='NAME'*, *armature='DEFAULT'*, *ratio=0.1*, *decay=0.8*)[#](#bpy.ops.gpencil.generate_weights "Link to this definition")
:   Generate automatic weights for armatures (requires armature modifier)

    Parameters:
    :   * **mode** (*enum in* *[**'NAME'**,* *'AUTO'**]**,* *(**optional**)*) – Mode
        * **armature** (*enum in* *[**'DEFAULT'**]**,* *(**optional**)*) – Armature, Armature to use
        * **ratio** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Ratio, Ratio between bone length and influence radius
        * **decay** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Decay, Factor to reduce influence depending of distance to bone axis

bpy.ops.gpencil.guide\_rotate(*increment=True*, *angle=0.0*)[#](#bpy.ops.gpencil.guide_rotate "Link to this definition")
:   Rotate guide angle

    Parameters:
    :   * **increment** (*boolean**,* *(**optional**)*) – Increment, Increment angle
        * **angle** (*float in* *[**-10000**,* *10000**]**,* *(**optional**)*) – Angle, Guide angle

bpy.ops.gpencil.hide(*unselected=False*)[#](#bpy.ops.gpencil.hide "Link to this definition")
:   Hide selected/unselected Grease Pencil layers

    Parameters:
    :   **unselected** (*boolean**,* *(**optional**)*) – Unselected, Hide unselected rather than selected layers

bpy.ops.gpencil.image\_to\_grease\_pencil(*size=0.005*, *mask=False*)[#](#bpy.ops.gpencil.image_to_grease_pencil "Link to this definition")
:   Generate a Grease Pencil Object using Image as source

    Parameters:
    :   * **size** (*float in* *[**0.0001**,* *10**]**,* *(**optional**)*) – Point Size, Size used for grease pencil points
        * **mask** (*boolean**,* *(**optional**)*) – Generate Mask, Create an inverted image for masking using alpha channel

bpy.ops.gpencil.interpolate(*shift=0.0*, *layers='ACTIVE'*, *interpolate\_selected\_only=False*, *exclude\_breakdowns=False*, *flip='AUTO'*, *smooth\_steps=1*, *smooth\_factor=0.0*, *release\_confirm=False*)[#](#bpy.ops.gpencil.interpolate "Link to this definition")
:   Interpolate grease pencil strokes between frames

    Parameters:
    :   * **shift** (*float in* *[**-1**,* *1**]**,* *(**optional**)*) – Shift, Bias factor for which frame has more influence on the interpolated strokes
        * **layers** (*enum in* *[**'ACTIVE'**,* *'ALL'**]**,* *(**optional**)*) – Layer, Layers included in the interpolation
        * **interpolate\_selected\_only** (*boolean**,* *(**optional**)*) – Only Selected, Interpolate only selected strokes
        * **exclude\_breakdowns** (*boolean**,* *(**optional**)*) – Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes
        * **flip** (*enum in* *[**'NOFLIP'**,* *'FLIP'**,* *'AUTO'**]**,* *(**optional**)*) – Flip Mode, Invert destination stroke to match start and end with source stroke
        * **smooth\_steps** (*int in* *[**1**,* *3**]**,* *(**optional**)*) – Iterations, Number of times to smooth newly created strokes
        * **smooth\_factor** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
        * **release\_confirm** (*boolean**,* *(**optional**)*) – Confirm on Release

bpy.ops.gpencil.interpolate\_reverse()[#](#bpy.ops.gpencil.interpolate_reverse "Link to this definition")
:   Remove breakdown frames generated by interpolating between two Grease Pencil frames

bpy.ops.gpencil.interpolate\_sequence(*step=1*, *layers='ACTIVE'*, *interpolate\_selected\_only=False*, *exclude\_breakdowns=False*, *flip='AUTO'*, *smooth\_steps=1*, *smooth\_factor=0.0*, *type='LINEAR'*, *easing='AUTO'*, *back=1.702*, *amplitude=0.15*, *period=0.15*)[#](#bpy.ops.gpencil.interpolate_sequence "Link to this definition")
:   Generate ‘in-betweens’ to smoothly interpolate between Grease Pencil frames

    Parameters:
    :   * **step** (*int in* *[**1**,* *1048574**]**,* *(**optional**)*) – Step, Number of frames between generated interpolated frames
        * **layers** (*enum in* *[**'ACTIVE'**,* *'ALL'**]**,* *(**optional**)*) – Layer, Layers included in the interpolation
        * **interpolate\_selected\_only** (*boolean**,* *(**optional**)*) – Only Selected, Interpolate only selected strokes
        * **exclude\_breakdowns** (*boolean**,* *(**optional**)*) – Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes
        * **flip** (*enum in* *[**'NOFLIP'**,* *'FLIP'**,* *'AUTO'**]**,* *(**optional**)*) – Flip Mode, Invert destination stroke to match start and end with source stroke
        * **smooth\_steps** (*int in* *[**1**,* *3**]**,* *(**optional**)*) – Iterations, Number of times to smooth newly created strokes
        * **smooth\_factor** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
        * **type** (*enum in* *[**'LINEAR'**,* *'CUSTOM'**,* *'SINE'**,* *'QUAD'**,* *'CUBIC'**,* *'QUART'**,* *'QUINT'**,* *'EXPO'**,* *'CIRC'**,* *'BACK'**,* *'BOUNCE'**,* *'ELASTIC'**]**,* *(**optional**)*) –

          Type, Interpolation method to use the next time ‘Interpolate Sequence’ is run

          + `LINEAR`
            Linear – Straight-line interpolation between A and B (i.e. no ease in/out).
          + `CUSTOM`
            Custom – Custom interpolation defined using a curve map.
          + `SINE`
            Sinusoidal – Sinusoidal easing (weakest, almost linear but with a slight curvature).
          + `QUAD`
            Quadratic – Quadratic easing.
          + `CUBIC`
            Cubic – Cubic easing.
          + `QUART`
            Quartic – Quartic easing.
          + `QUINT`
            Quintic – Quintic easing.
          + `EXPO`
            Exponential – Exponential easing (dramatic).
          + `CIRC`
            Circular – Circular easing (strongest and most dynamic).
          + `BACK`
            Back – Cubic easing with overshoot and settle.
          + `BOUNCE`
            Bounce – Exponentially decaying parabolic bounce, like when objects collide.
          + `ELASTIC`
            Elastic – Exponentially decaying sine wave, like an elastic band.
        * **easing** (*enum in* *[**'AUTO'**,* *'EASE\_IN'**,* *'EASE\_OUT'**,* *'EASE\_IN\_OUT'**]**,* *(**optional**)*) –

          Easing, Which ends of the segment between the preceding and following grease pencil frames easing interpolation is applied to

          + `AUTO`
            Automatic Easing – Easing type is chosen automatically based on what the type of interpolation used (e.g. ‘Ease In’ for transitional types, and ‘Ease Out’ for dynamic effects).
          + `EASE_IN`
            Ease In – Only on the end closest to the next keyframe.
          + `EASE_OUT`
            Ease Out – Only on the end closest to the first keyframe.
          + `EASE_IN_OUT`
            Ease In and Out – Segment between both keyframes.
        * **back** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Back, Amount of overshoot for ‘back’ easing
        * **amplitude** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Amplitude, Amount to boost elastic bounces for ‘elastic’ easing
        * **period** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Period, Time between bounces for elastic easing

bpy.ops.gpencil.layer\_active(*layer=0*)[#](#bpy.ops.gpencil.layer_active "Link to this definition")
:   Active Grease Pencil layer

    Parameters:
    :   **layer** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Grease Pencil Layer

bpy.ops.gpencil.layer\_add(*layer=0*, *new\_layer\_name=''*)[#](#bpy.ops.gpencil.layer_add "Link to this definition")
:   Add new layer or note for the active data-block

    Parameters:
    :   * **layer** (*int in* *[**-1**,* *inf**]**,* *(**optional**)*) – Grease Pencil Layer
        * **new\_layer\_name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the newly added layer

bpy.ops.gpencil.layer\_annotation\_add()[#](#bpy.ops.gpencil.layer_annotation_add "Link to this definition")
:   Add new Annotation layer or note for the active data-block

bpy.ops.gpencil.layer\_annotation\_move(*type='UP'*)[#](#bpy.ops.gpencil.layer_annotation_move "Link to this definition")
:   Move the active Annotation layer up/down in the list

    Parameters:
    :   **type** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Type

bpy.ops.gpencil.layer\_annotation\_remove()[#](#bpy.ops.gpencil.layer_annotation_remove "Link to this definition")
:   Remove active Annotation layer

bpy.ops.gpencil.layer\_change(*layer='DEFAULT'*)[#](#bpy.ops.gpencil.layer_change "Link to this definition")
:   Change active Grease Pencil layer

    Parameters:
    :   **layer** (*enum in* *[**'DEFAULT'**]**,* *(**optional**)*) – Grease Pencil Layer

bpy.ops.gpencil.layer\_duplicate(*mode='ALL'*)[#](#bpy.ops.gpencil.layer_duplicate "Link to this definition")
:   Make a copy of the active Grease Pencil layer

    Parameters:
    :   **mode** (*enum in* *[**'ALL'**,* *'EMPTY'**]**,* *(**optional**)*) – Mode

bpy.ops.gpencil.layer\_duplicate\_object(*mode='ALL'*, *only\_active=True*)[#](#bpy.ops.gpencil.layer_duplicate_object "Link to this definition")
:   Make a copy of the active Grease Pencil layer to selected object

    Parameters:
    :   * **mode** (*enum in* *[**'ALL'**,* *'ACTIVE'**]**,* *(**optional**)*) – Mode
        * **only\_active** (*boolean**,* *(**optional**)*) – Only Active, Copy only active Layer, uncheck to append all layers

bpy.ops.gpencil.layer\_isolate(*affect\_visibility=False*)[#](#bpy.ops.gpencil.layer_isolate "Link to this definition")
:   Toggle whether the active layer is the only one that can be edited and/or visible

    Parameters:
    :   **affect\_visibility** (*boolean**,* *(**optional**)*) – Affect Visibility, In addition to toggling the editability, also affect the visibility

bpy.ops.gpencil.layer\_mask\_add(*name=''*)[#](#bpy.ops.gpencil.layer_mask_add "Link to this definition")
:   Add new layer as masking

    Parameters:
    :   **name** (*string**,* *(**optional**,* *never None**)*) – Layer, Name of the layer

bpy.ops.gpencil.layer\_mask\_move(*type='UP'*)[#](#bpy.ops.gpencil.layer_mask_move "Link to this definition")
:   Move the active Grease Pencil mask layer up/down in the list

    Parameters:
    :   **type** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Type

bpy.ops.gpencil.layer\_mask\_remove()[#](#bpy.ops.gpencil.layer_mask_remove "Link to this definition")
:   Remove Layer Mask

bpy.ops.gpencil.layer\_merge(*mode='ACTIVE'*)[#](#bpy.ops.gpencil.layer_merge "Link to this definition")
:   Combine Layers

    Parameters:
    :   **mode** (*enum in* *[**'ACTIVE'**,* *'ALL'**]**,* *(**optional**)*) –

        Mode

        * `ACTIVE`
          Active – Combine active layer into the layer below.
        * `ALL`
          All – Combine all layers into the active layer.

bpy.ops.gpencil.layer\_move(*type='UP'*)[#](#bpy.ops.gpencil.layer_move "Link to this definition")
:   Move the active Grease Pencil layer up/down in the list

    Parameters:
    :   **type** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Type

bpy.ops.gpencil.layer\_remove()[#](#bpy.ops.gpencil.layer_remove "Link to this definition")
:   Remove active Grease Pencil layer

bpy.ops.gpencil.lock\_all()[#](#bpy.ops.gpencil.lock_all "Link to this definition")
:   Lock all Grease Pencil layers to prevent them from being accidentally modified

bpy.ops.gpencil.lock\_layer()[#](#bpy.ops.gpencil.lock_layer "Link to this definition")
:   Lock and hide any color not used in any layer

bpy.ops.gpencil.material\_hide(*unselected=False*)[#](#bpy.ops.gpencil.material_hide "Link to this definition")
:   Hide selected/unselected Grease Pencil materials

    Parameters:
    :   **unselected** (*boolean**,* *(**optional**)*) – Unselected, Hide unselected rather than selected colors

bpy.ops.gpencil.material\_isolate(*affect\_visibility=False*)[#](#bpy.ops.gpencil.material_isolate "Link to this definition")
:   Toggle whether the active material is the only one that is editable and/or visible

    Parameters:
    :   **affect\_visibility** (*boolean**,* *(**optional**)*) – Affect Visibility, In addition to toggling the editability, also affect the visibility

bpy.ops.gpencil.material\_lock\_all()[#](#bpy.ops.gpencil.material_lock_all "Link to this definition")
:   Lock all Grease Pencil materials to prevent them from being accidentally modified

bpy.ops.gpencil.material\_lock\_unused()[#](#bpy.ops.gpencil.material_lock_unused "Link to this definition")
:   Lock any material not used in any selected stroke

bpy.ops.gpencil.material\_reveal()[#](#bpy.ops.gpencil.material_reveal "Link to this definition")
:   Unhide all hidden Grease Pencil materials

bpy.ops.gpencil.material\_select(*deselect=False*)[#](#bpy.ops.gpencil.material_select "Link to this definition")
:   Select/Deselect all Grease Pencil strokes using current material

    Parameters:
    :   **deselect** (*boolean**,* *(**optional**)*) – Deselect, Unselect strokes

bpy.ops.gpencil.material\_set(*slot='DEFAULT'*)[#](#bpy.ops.gpencil.material_set "Link to this definition")
:   Set active material

    Parameters:
    :   **slot** (*enum in* *[**'DEFAULT'**]**,* *(**optional**)*) – Material Slot

bpy.ops.gpencil.material\_to\_vertex\_color(*remove=True*, *palette=True*, *selected=False*, *threshold=3*)[#](#bpy.ops.gpencil.material_to_vertex_color "Link to this definition")
:   Replace materials in strokes with Vertex Color

    Parameters:
    :   * **remove** (*boolean**,* *(**optional**)*) – Remove Unused Materials, Remove any unused material after the conversion
        * **palette** (*boolean**,* *(**optional**)*) – Create Palette, Create a new palette with colors
        * **selected** (*boolean**,* *(**optional**)*) – Only Selected, Convert only selected strokes
        * **threshold** (*int in* *[**1**,* *4**]**,* *(**optional**)*) – Threshold

bpy.ops.gpencil.material\_unlock\_all()[#](#bpy.ops.gpencil.material_unlock_all "Link to this definition")
:   Unlock all Grease Pencil materials so that they can be edited

bpy.ops.gpencil.materials\_copy\_to\_object(*only\_active=True*)[#](#bpy.ops.gpencil.materials_copy_to_object "Link to this definition")
:   Append Materials of the active Grease Pencil to other object

    Parameters:
    :   **only\_active** (*boolean**,* *(**optional**)*) – Only Active, Append only active material, uncheck to append all materials

bpy.ops.gpencil.move\_to\_layer(*layer=0*, *new\_layer\_name=''*)[#](#bpy.ops.gpencil.move_to_layer "Link to this definition")
:   Move selected strokes to another layer

    Parameters:
    :   * **layer** (*int in* *[**-1**,* *inf**]**,* *(**optional**)*) – Grease Pencil Layer
        * **new\_layer\_name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the newly added layer

bpy.ops.gpencil.paintmode\_toggle(*back=False*)[#](#bpy.ops.gpencil.paintmode_toggle "Link to this definition")
:   Enter/Exit paint mode for Grease Pencil strokes

    Parameters:
    :   **back** (*boolean**,* *(**optional**)*) – Return to Previous Mode, Return to previous mode

bpy.ops.gpencil.paste(*type='ACTIVE'*, *paste\_back=False*)[#](#bpy.ops.gpencil.paste "Link to this definition")
:   Paste previously copied strokes to active layer or to original layer

    Parameters:
    :   * **type** (*enum in* *[**'ACTIVE'**,* *'LAYER'**]**,* *(**optional**)*) – Type
        * **paste\_back** (*boolean**,* *(**optional**)*) – Paste on Back, Add pasted strokes behind all strokes

bpy.ops.gpencil.primitive\_box(*subdivision=3*, *edges=1*, *type='BOX'*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.primitive_box "Link to this definition")
:   Create predefined grease pencil stroke box shapes

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *128**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **edges** (*int in* *[**1**,* *128**]**,* *(**optional**)*) – Edges, Number of points per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.primitive\_circle(*subdivision=94*, *edges=1*, *type='CIRCLE'*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.primitive_circle "Link to this definition")
:   Create predefined grease pencil stroke circle shapes

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *128**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **edges** (*int in* *[**1**,* *128**]**,* *(**optional**)*) – Edges, Number of points per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.primitive\_curve(*subdivision=62*, *edges=1*, *type='CURVE'*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.primitive_curve "Link to this definition")
:   Create predefined grease pencil stroke curve shapes

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *128**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **edges** (*int in* *[**1**,* *128**]**,* *(**optional**)*) – Edges, Number of points per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.primitive\_line(*subdivision=6*, *edges=1*, *type='LINE'*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.primitive_line "Link to this definition")
:   Create predefined grease pencil stroke lines

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *128**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **edges** (*int in* *[**1**,* *128**]**,* *(**optional**)*) – Edges, Number of points per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.primitive\_polyline(*subdivision=6*, *edges=1*, *type='POLYLINE'*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.primitive_polyline "Link to this definition")
:   Create predefined grease pencil stroke polylines

    Parameters:
    :   * **subdivision** (*int in* *[**0**,* *128**]**,* *(**optional**)*) – Subdivisions, Number of subdivisions per segment
        * **edges** (*int in* *[**1**,* *128**]**,* *(**optional**)*) – Edges, Number of points per segment
        * **type** (*enum in* *[**'BOX'**,* *'LINE'**,* *'POLYLINE'**,* *'CIRCLE'**,* *'ARC'**,* *'CURVE'**]**,* *(**optional**)*) – Type, Type of shape
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.recalc\_geometry()[#](#bpy.ops.gpencil.recalc_geometry "Link to this definition")
:   Update all internal geometry data

bpy.ops.gpencil.reproject(*type='VIEW'*, *keep\_original=False*, *offset=0.0*)[#](#bpy.ops.gpencil.reproject "Link to this definition")
:   Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

    Parameters:
    :   * **type** (*enum in* *[**'FRONT'**,* *'SIDE'**,* *'TOP'**,* *'VIEW'**,* *'SURFACE'**,* *'CURSOR'**]**,* *(**optional**)*) –

          Projection Type

          + `FRONT`
            Front – Reproject the strokes using the X-Z plane.
          + `SIDE`
            Side – Reproject the strokes using the Y-Z plane.
          + `TOP`
            Top – Reproject the strokes using the X-Y plane.
          + `VIEW`
            View – Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using ‘Cursor’ Stroke Placement.
          + `SURFACE`
            Surface – Reproject the strokes on to the scene geometry, as if drawn using ‘Surface’ placement.
          + `CURSOR`
            Cursor – Reproject the strokes using the orientation of 3D cursor.
        * **keep\_original** (*boolean**,* *(**optional**)*) – Keep Original, Keep original strokes and create a copy before reprojecting
        * **offset** (*float in* *[**0**,* *10**]**,* *(**optional**)*) – Surface Offset

bpy.ops.gpencil.reset\_transform\_fill(*mode='ALL'*)[#](#bpy.ops.gpencil.reset_transform_fill "Link to this definition")
:   Reset any UV transformation and back to default values

    Parameters:
    :   **mode** (*enum in* *[**'ALL'**,* *'TRANSLATE'**,* *'ROTATE'**,* *'SCALE'**]**,* *(**optional**)*) – Mode

bpy.ops.gpencil.reveal(*select=True*)[#](#bpy.ops.gpencil.reveal "Link to this definition")
:   Show all Grease Pencil layers

    Parameters:
    :   **select** (*boolean**,* *(**optional**)*) – Select

bpy.ops.gpencil.sculpt\_paint(*stroke=None*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.sculpt_paint "Link to this definition")
:   Apply tweaks to strokes by painting over the strokes

    Parameters:
    :   * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input, Enter a mini ‘sculpt-mode’ if enabled, otherwise, exit after drawing a single stroke

bpy.ops.gpencil.sculptmode\_toggle(*back=False*)[#](#bpy.ops.gpencil.sculptmode_toggle "Link to this definition")
:   Enter/Exit sculpt mode for Grease Pencil strokes

    Parameters:
    :   **back** (*boolean**,* *(**optional**)*) – Return to Previous Mode, Return to previous mode

bpy.ops.gpencil.segment\_add(*modifier=''*)[#](#bpy.ops.gpencil.segment_add "Link to this definition")
:   Add a segment to the dash modifier

    Parameters:
    :   **modifier** (*string**,* *(**optional**,* *never None**)*) – Modifier, Name of the modifier to edit

bpy.ops.gpencil.segment\_move(*modifier=''*, *type='UP'*)[#](#bpy.ops.gpencil.segment_move "Link to this definition")
:   Move the active dash segment up or down

    Parameters:
    :   * **modifier** (*string**,* *(**optional**,* *never None**)*) – Modifier, Name of the modifier to edit
        * **type** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Type

bpy.ops.gpencil.segment\_remove(*modifier=''*, *index=0*)[#](#bpy.ops.gpencil.segment_remove "Link to this definition")
:   Remove the active segment from the dash modifier

    Parameters:
    :   * **modifier** (*string**,* *(**optional**,* *never None**)*) – Modifier, Name of the modifier to edit
        * **index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Index, Index of the segment to remove

bpy.ops.gpencil.select(*extend=False*, *deselect=False*, *toggle=False*, *deselect\_all=False*, *select\_passthrough=False*, *entire\_strokes=False*, *location=(0, 0)*, *use\_shift\_extend=False*)[#](#bpy.ops.gpencil.select "Link to this definition")
:   Select Grease Pencil strokes and/or stroke points

    Parameters:
    :   * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection instead of deselecting everything first
        * **deselect** (*boolean**,* *(**optional**)*) – Deselect, Remove from selection
        * **toggle** (*boolean**,* *(**optional**)*) – Toggle Selection, Toggle the selection
        * **deselect\_all** (*boolean**,* *(**optional**)*) – Deselect On Nothing, Deselect all when nothing under the cursor
        * **select\_passthrough** (*boolean**,* *(**optional**)*) – Only Select Unselected, Ignore the select action when the element is already selected
        * **entire\_strokes** (*boolean**,* *(**optional**)*) – Entire Strokes, Select entire strokes instead of just the nearest stroke vertex
        * **location** (*int array* *of* *2 items in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Location, Mouse location
        * **use\_shift\_extend** (*boolean**,* *(**optional**)*) – Extend

bpy.ops.gpencil.select\_all(*action='TOGGLE'*)[#](#bpy.ops.gpencil.select_all "Link to this definition")
:   Change selection of all Grease Pencil strokes currently visible

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

bpy.ops.gpencil.select\_alternate(*unselect\_ends=False*)[#](#bpy.ops.gpencil.select_alternate "Link to this definition")
:   Select alternative points in same strokes as already selected points

    Parameters:
    :   **unselect\_ends** (*boolean**,* *(**optional**)*) – Unselect Ends, Do not select the first and last point of the stroke

bpy.ops.gpencil.select\_box(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.gpencil.select_box "Link to this definition")
:   Select Grease Pencil strokes within a rectangular region

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**,* *'XOR'**,* *'AND'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.
          + `XOR`
            Difference – Invert existing selection.
          + `AND`
            Intersect – Intersect existing selection.

bpy.ops.gpencil.select\_circle(*x=0*, *y=0*, *radius=25*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.gpencil.select_circle "Link to this definition")
:   Select Grease Pencil strokes using brush selection

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

bpy.ops.gpencil.select\_first(*only\_selected\_strokes=False*, *extend=False*)[#](#bpy.ops.gpencil.select_first "Link to this definition")
:   Select first point in Grease Pencil strokes

    Parameters:
    :   * **only\_selected\_strokes** (*boolean**,* *(**optional**)*) – Selected Strokes Only, Only select the first point of strokes that already have points selected
        * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection instead of deselecting all other selected points

bpy.ops.gpencil.select\_grouped(*type='LAYER'*)[#](#bpy.ops.gpencil.select_grouped "Link to this definition")
:   Select all strokes with similar characteristics

    Parameters:
    :   **type** (*enum in* *[**'LAYER'**,* *'MATERIAL'**]**,* *(**optional**)*) –

        Type

        * `LAYER`
          Layer – Shared layers.
        * `MATERIAL`
          Material – Shared materials.

bpy.ops.gpencil.select\_lasso(*mode='SET'*, *path=None*)[#](#bpy.ops.gpencil.select_lasso "Link to this definition")
:   Select Grease Pencil strokes using lasso selection

    Parameters:
    :   * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**,* *'XOR'**,* *'AND'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.
          + `XOR`
            Difference – Invert existing selection.
          + `AND`
            Intersect – Intersect existing selection.
        * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path

bpy.ops.gpencil.select\_last(*only\_selected\_strokes=False*, *extend=False*)[#](#bpy.ops.gpencil.select_last "Link to this definition")
:   Select last point in Grease Pencil strokes

    Parameters:
    :   * **only\_selected\_strokes** (*boolean**,* *(**optional**)*) – Selected Strokes Only, Only select the last point of strokes that already have points selected
        * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection instead of deselecting all other selected points

bpy.ops.gpencil.select\_less()[#](#bpy.ops.gpencil.select_less "Link to this definition")
:   Shrink sets of selected Grease Pencil points

bpy.ops.gpencil.select\_linked()[#](#bpy.ops.gpencil.select_linked "Link to this definition")
:   Select all points in same strokes as already selected points

bpy.ops.gpencil.select\_more()[#](#bpy.ops.gpencil.select_more "Link to this definition")
:   Grow sets of selected Grease Pencil points

bpy.ops.gpencil.select\_random(*ratio=0.5*, *seed=0*, *action='SELECT'*, *unselect\_ends=False*)[#](#bpy.ops.gpencil.select_random "Link to this definition")
:   Select random points for non selected strokes

    Parameters:
    :   * **ratio** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Ratio, Portion of items to select randomly
        * **seed** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Random Seed, Seed for the random number generator
        * **action** (*enum in* *[**'SELECT'**,* *'DESELECT'**]**,* *(**optional**)*) –

          Action, Selection action to execute

          + `SELECT`
            Select – Select all elements.
          + `DESELECT`
            Deselect – Deselect all elements.
        * **unselect\_ends** (*boolean**,* *(**optional**)*) – Unselect Ends, Do not select the first and last point of the stroke

bpy.ops.gpencil.select\_vertex\_color(*threshold=0*)[#](#bpy.ops.gpencil.select_vertex_color "Link to this definition")
:   Select all points with similar vertex color of current selected

    Parameters:
    :   **threshold** (*int in* *[**0**,* *5**]**,* *(**optional**)*) – Threshold, Tolerance of the selection. Higher values select a wider range of similar colors

bpy.ops.gpencil.selection\_opacity\_toggle()[#](#bpy.ops.gpencil.selection_opacity_toggle "Link to this definition")
:   Hide/Unhide selected points for Grease Pencil strokes setting alpha factor

bpy.ops.gpencil.selectmode\_toggle(*mode=0*)[#](#bpy.ops.gpencil.selectmode_toggle "Link to this definition")
:   Set selection mode for Grease Pencil strokes

    Parameters:
    :   **mode** (*int in* *[**0**,* *2**]**,* *(**optional**)*) – Select Mode, Select mode

bpy.ops.gpencil.set\_active\_material()[#](#bpy.ops.gpencil.set_active_material "Link to this definition")
:   Set the selected stroke material as the active material

bpy.ops.gpencil.snap\_cursor\_to\_selected()[#](#bpy.ops.gpencil.snap_cursor_to_selected "Link to this definition")
:   Snap cursor to center of selected points

bpy.ops.gpencil.snap\_to\_cursor(*use\_offset=True*)[#](#bpy.ops.gpencil.snap_to_cursor "Link to this definition")
:   Snap selected points/strokes to the cursor

    Parameters:
    :   **use\_offset** (*boolean**,* *(**optional**)*) – With Offset, Offset the entire stroke instead of selected points only

bpy.ops.gpencil.snap\_to\_grid()[#](#bpy.ops.gpencil.snap_to_grid "Link to this definition")
:   Snap selected points to the nearest grid points

bpy.ops.gpencil.stroke\_apply\_thickness()[#](#bpy.ops.gpencil.stroke_apply_thickness "Link to this definition")
:   Apply the thickness change of the layer to its strokes

bpy.ops.gpencil.stroke\_arrange(*direction='UP'*)[#](#bpy.ops.gpencil.stroke_arrange "Link to this definition")
:   Arrange selected strokes up/down in the display order of the active layer

    Parameters:
    :   **direction** (*enum in* *[**'TOP'**,* *'UP'**,* *'DOWN'**,* *'BOTTOM'**]**,* *(**optional**)*) – Direction

bpy.ops.gpencil.stroke\_caps\_set(*type='TOGGLE'*)[#](#bpy.ops.gpencil.stroke_caps_set "Link to this definition")
:   Change stroke caps mode (rounded or flat)

    Parameters:
    :   **type** (*enum in* *[**'TOGGLE'**,* *'START'**,* *'END'**,* *'DEFAULT'**]**,* *(**optional**)*) –

        Type

        * `TOGGLE`
          Both.
        * `START`
          Start.
        * `END`
          End.
        * `DEFAULT`
          Default – Set as default rounded.

bpy.ops.gpencil.stroke\_change\_color(*material=''*)[#](#bpy.ops.gpencil.stroke_change_color "Link to this definition")
:   Move selected strokes to active material

    Parameters:
    :   **material** (*string**,* *(**optional**,* *never None**)*) – Material, Name of the material

bpy.ops.gpencil.stroke\_cutter(*path=None*, *flat\_caps=False*)[#](#bpy.ops.gpencil.stroke_cutter "Link to this definition")
:   Select section and cut

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **flat\_caps** (*boolean**,* *(**optional**)*) – Flat Caps

bpy.ops.gpencil.stroke\_cyclical\_set(*type='TOGGLE'*, *geometry=False*)[#](#bpy.ops.gpencil.stroke_cyclical_set "Link to this definition")
:   Close or open the selected stroke adding a segment from last to first point

    Parameters:
    :   * **type** (*enum in* *[**'CLOSE'**,* *'OPEN'**,* *'TOGGLE'**]**,* *(**optional**)*) – Type
        * **geometry** (*boolean**,* *(**optional**)*) – Create Geometry, Create new geometry for closing stroke

bpy.ops.gpencil.stroke\_editcurve\_set\_handle\_type(*type='AUTOMATIC'*)[#](#bpy.ops.gpencil.stroke_editcurve_set_handle_type "Link to this definition")
:   Set the type of an edit curve handle

    Parameters:
    :   **type** (*enum in* *[**'FREE'**,* *'AUTOMATIC'**,* *'VECTOR'**,* *'ALIGNED'**]**,* *(**optional**)*) – Type, Spline type

bpy.ops.gpencil.stroke\_enter\_editcurve\_mode(*error\_threshold=0.1*)[#](#bpy.ops.gpencil.stroke_enter_editcurve_mode "Link to this definition")
:   Called to transform a stroke into a curve

    Parameters:
    :   **error\_threshold** (*float in* *[**1.17549e-38**,* *100**]**,* *(**optional**)*) – Error Threshold, Threshold on the maximum deviation from the actual stroke

bpy.ops.gpencil.stroke\_flip()[#](#bpy.ops.gpencil.stroke_flip "Link to this definition")
:   Change direction of the points of the selected strokes

bpy.ops.gpencil.stroke\_join(*type='JOIN'*, *leave\_gaps=False*)[#](#bpy.ops.gpencil.stroke_join "Link to this definition")
:   Join selected strokes (optionally as new stroke)

    Parameters:
    :   * **type** (*enum in* *[**'JOIN'**,* *'JOINCOPY'**]**,* *(**optional**)*) – Type
        * **leave\_gaps** (*boolean**,* *(**optional**)*) – Leave Gaps, Leave gaps between joined strokes instead of linking them

bpy.ops.gpencil.stroke\_merge(*mode='STROKE'*, *back=False*, *additive=False*, *cyclic=False*, *clear\_point=False*, *clear\_stroke=False*)[#](#bpy.ops.gpencil.stroke_merge "Link to this definition")
:   Create a new stroke with the selected stroke points

    Parameters:
    :   * **mode** (*enum in* *[**'STROKE'**,* *'POINT'**]**,* *(**optional**)*) – Mode
        * **back** (*boolean**,* *(**optional**)*) – Draw on Back, Draw new stroke below all previous strokes
        * **additive** (*boolean**,* *(**optional**)*) – Additive Drawing, Add to previous drawing
        * **cyclic** (*boolean**,* *(**optional**)*) – Cyclic, Close new stroke
        * **clear\_point** (*boolean**,* *(**optional**)*) – Dissolve Points, Dissolve old selected points
        * **clear\_stroke** (*boolean**,* *(**optional**)*) – Delete Strokes, Delete old selected strokes

bpy.ops.gpencil.stroke\_merge\_by\_distance(*threshold=0.001*, *use\_unselected=False*)[#](#bpy.ops.gpencil.stroke_merge_by_distance "Link to this definition")
:   Merge points by distance

    Parameters:
    :   * **threshold** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Threshold
        * **use\_unselected** (*boolean**,* *(**optional**)*) – Unselected, Use whole stroke, not only selected points

bpy.ops.gpencil.stroke\_merge\_material(*hue\_threshold=0.001*, *sat\_threshold=0.001*, *val\_threshold=0.001*)[#](#bpy.ops.gpencil.stroke_merge_material "Link to this definition")
:   Replace materials in strokes merging similar

    Parameters:
    :   * **hue\_threshold** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Hue Threshold
        * **sat\_threshold** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Saturation Threshold
        * **val\_threshold** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Value Threshold

bpy.ops.gpencil.stroke\_normalize(*mode='THICKNESS'*, *factor=1.0*, *value=10*)[#](#bpy.ops.gpencil.stroke_normalize "Link to this definition")
:   Normalize stroke attributes

    Parameters:
    :   * **mode** (*enum in* *[**'THICKNESS'**,* *'OPACITY'**]**,* *(**optional**)*) –

          Mode, Attribute to be normalized

          + `THICKNESS`
            Thickness – Normalizes the stroke thickness by making all points use the same thickness value.
          + `OPACITY`
            Opacity – Normalizes the stroke opacity by making all points use the same opacity value.
        * **factor** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Factor
        * **value** (*int in* *[**0**,* *1000**]**,* *(**optional**)*) – Value, Value

bpy.ops.gpencil.stroke\_outline(*view\_mode='VIEW'*, *material\_mode='ACTIVE'*, *thickness=1*, *keep=True*, *subdivisions=3*, *length=0.0*)[#](#bpy.ops.gpencil.stroke_outline "Link to this definition")
:   Convert stroke to perimeter

    Parameters:
    :   * **view\_mode** (*enum in* *[**'VIEW'**,* *'FRONT'**,* *'SIDE'**,* *'TOP'**,* *'CAMERA'**]**,* *(**optional**)*) – View
        * **material\_mode** (*enum in* *[**'ACTIVE'**,* *'KEEP'**,* *'NEW'**]**,* *(**optional**)*) –

          Material Mode

          + `ACTIVE`
            Active Material.
          + `KEEP`
            Keep Material – Keep current stroke material.
          + `NEW`
            New Material.
        * **thickness** (*int in* *[**1**,* *1000**]**,* *(**optional**)*) – Thickness, Thickness of the stroke perimeter
        * **keep** (*boolean**,* *(**optional**)*) – Keep Shape, Try to keep global shape when the stroke thickness change
        * **subdivisions** (*int in* *[**0**,* *10**]**,* *(**optional**)*) – Subdivisions
        * **length** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Sample Length

bpy.ops.gpencil.stroke\_reset\_vertex\_color(*mode='BOTH'*)[#](#bpy.ops.gpencil.stroke_reset_vertex_color "Link to this definition")
:   Reset vertex color for all or selected strokes

    Parameters:
    :   **mode** (*enum in* *[**'STROKE'**,* *'FILL'**,* *'BOTH'**]**,* *(**optional**)*) –

        Mode

        * `STROKE`
          Stroke – Reset Vertex Color to Stroke only.
        * `FILL`
          Fill – Reset Vertex Color to Fill only.
        * `BOTH`
          Stroke & Fill – Reset Vertex Color to Stroke and Fill.

bpy.ops.gpencil.stroke\_sample(*length=0.1*, *sharp\_threshold=0.1*)[#](#bpy.ops.gpencil.stroke_sample "Link to this definition")
:   Sample stroke points to predefined segment length

    Parameters:
    :   * **length** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Length
        * **sharp\_threshold** (*float in* *[**0**,* *3.14159**]**,* *(**optional**)*) – Sharp Threshold

bpy.ops.gpencil.stroke\_separate(*mode='POINT'*)[#](#bpy.ops.gpencil.stroke_separate "Link to this definition")
:   Separate the selected strokes or layer in a new grease pencil object

    Parameters:
    :   **mode** (*enum in* *[**'POINT'**,* *'STROKE'**,* *'LAYER'**]**,* *(**optional**)*) –

        Mode

        * `POINT`
          Selected Points – Separate the selected points.
        * `STROKE`
          Selected Strokes – Separate the selected strokes.
        * `LAYER`
          Active Layer – Separate the strokes of the current layer.

bpy.ops.gpencil.stroke\_simplify(*factor=0.0*)[#](#bpy.ops.gpencil.stroke_simplify "Link to this definition")
:   Simplify selected strokes, reducing number of points

    Parameters:
    :   **factor** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Factor

bpy.ops.gpencil.stroke\_simplify\_fixed(*step=1*)[#](#bpy.ops.gpencil.stroke_simplify_fixed "Link to this definition")
:   Simplify selected strokes, reducing number of points using fixed algorithm

    Parameters:
    :   **step** (*int in* *[**1**,* *100**]**,* *(**optional**)*) – Steps, Number of simplify steps

bpy.ops.gpencil.stroke\_smooth(*repeat=2*, *factor=1.0*, *only\_selected=True*, *smooth\_position=True*, *smooth\_thickness=True*, *smooth\_strength=False*, *smooth\_uv=False*)[#](#bpy.ops.gpencil.stroke_smooth "Link to this definition")
:   Smooth selected strokes

    Parameters:
    :   * **repeat** (*int in* *[**1**,* *1000**]**,* *(**optional**)*) – Repeat
        * **factor** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Factor
        * **only\_selected** (*boolean**,* *(**optional**)*) – Selected Points, Smooth only selected points in the stroke
        * **smooth\_position** (*boolean**,* *(**optional**)*) – Position
        * **smooth\_thickness** (*boolean**,* *(**optional**)*) – Thickness
        * **smooth\_strength** (*boolean**,* *(**optional**)*) – Strength
        * **smooth\_uv** (*boolean**,* *(**optional**)*) – UV

bpy.ops.gpencil.stroke\_split()[#](#bpy.ops.gpencil.stroke_split "Link to this definition")
:   Split selected points as new stroke on same frame

bpy.ops.gpencil.stroke\_start\_set()[#](#bpy.ops.gpencil.stroke_start_set "Link to this definition")
:   Set start point for cyclic strokes

bpy.ops.gpencil.stroke\_subdivide(*number\_cuts=1*, *factor=0.0*, *repeat=1*, *only\_selected=True*, *smooth\_position=True*, *smooth\_thickness=True*, *smooth\_strength=False*, *smooth\_uv=False*)[#](#bpy.ops.gpencil.stroke_subdivide "Link to this definition")
:   Subdivide between continuous selected points of the stroke adding a point half way between them

    Parameters:
    :   * **number\_cuts** (*int in* *[**1**,* *10**]**,* *(**optional**)*) – Number of Cuts
        * **factor** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Smooth
        * **repeat** (*int in* *[**1**,* *10**]**,* *(**optional**)*) – Repeat
        * **only\_selected** (*boolean**,* *(**optional**)*) – Selected Points, Smooth only selected points in the stroke
        * **smooth\_position** (*boolean**,* *(**optional**)*) – Position
        * **smooth\_thickness** (*boolean**,* *(**optional**)*) – Thickness
        * **smooth\_strength** (*boolean**,* *(**optional**)*) – Strength
        * **smooth\_uv** (*boolean**,* *(**optional**)*) – UV

bpy.ops.gpencil.stroke\_trim()[#](#bpy.ops.gpencil.stroke_trim "Link to this definition")
:   Trim selected stroke to first loop or intersection

bpy.ops.gpencil.time\_segment\_add(*modifier=''*)[#](#bpy.ops.gpencil.time_segment_add "Link to this definition")
:   Add a segment to the time modifier

    Parameters:
    :   **modifier** (*string**,* *(**optional**,* *never None**)*) – Modifier, Name of the modifier to edit

bpy.ops.gpencil.time\_segment\_move(*modifier=''*, *type='UP'*)[#](#bpy.ops.gpencil.time_segment_move "Link to this definition")
:   Move the active time segment up or down

    Parameters:
    :   * **modifier** (*string**,* *(**optional**,* *never None**)*) – Modifier, Name of the modifier to edit
        * **type** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Type

bpy.ops.gpencil.time\_segment\_remove(*modifier=''*, *index=0*)[#](#bpy.ops.gpencil.time_segment_remove "Link to this definition")
:   Remove the active segment from the time modifier

    Parameters:
    :   * **modifier** (*string**,* *(**optional**,* *never None**)*) – Modifier, Name of the modifier to edit
        * **index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Index, Index of the segment to remove

bpy.ops.gpencil.tint\_flip()[#](#bpy.ops.gpencil.tint_flip "Link to this definition")
:   Switch tint colors

    File:
    :   [startup/bl\_ui/properties\_grease\_pencil\_common.py:943](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_ui/properties_grease_pencil_common.py#L943)

bpy.ops.gpencil.trace\_image(*target='NEW'*, *thickness=10*, *resolution=5*, *scale=1.0*, *sample=0.0*, *threshold=0.5*, *turnpolicy='MINORITY'*, *mode='SINGLE'*, *use\_current\_frame=True*, *frame\_number=0*)[#](#bpy.ops.gpencil.trace_image "Link to this definition")
:   Extract Grease Pencil strokes from image

    Parameters:
    :   * **target** (*enum in* *[**'NEW'**,* *'SELECTED'**]**,* *(**optional**)*) – Target Object, Target grease pencil
        * **thickness** (*int in* *[**1**,* *1000**]**,* *(**optional**)*) – Thickness
        * **resolution** (*int in* *[**1**,* *20**]**,* *(**optional**)*) – Resolution, Resolution of the generated curves
        * **scale** (*float in* *[**0.001**,* *100**]**,* *(**optional**)*) – Scale, Scale of the final stroke
        * **sample** (*float in* *[**0**,* *100**]**,* *(**optional**)*) – Sample, Distance to sample points, zero to disable
        * **threshold** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Color Threshold, Determine the lightness threshold above which strokes are generated
        * **turnpolicy** (*enum in* *[**'BLACK'**,* *'WHITE'**,* *'LEFT'**,* *'RIGHT'**,* *'MINORITY'**,* *'MAJORITY'**,* *'RANDOM'**]**,* *(**optional**)*) –

          Turn Policy, Determines how to resolve ambiguities during decomposition of bitmaps into paths

          + `BLACK`
            Black – Prefers to connect black (foreground) components.
          + `WHITE`
            White – Prefers to connect white (background) components.
          + `LEFT`
            Left – Always take a left turn.
          + `RIGHT`
            Right – Always take a right turn.
          + `MINORITY`
            Minority – Prefers to connect the color (black or white) that occurs least frequently in the local neighborhood of the current position.
          + `MAJORITY`
            Majority – Prefers to connect the color (black or white) that occurs most frequently in the local neighborhood of the current position.
          + `RANDOM`
            Random – Choose pseudo-randomly.
        * **mode** (*enum in* *[**'SINGLE'**,* *'SEQUENCE'**]**,* *(**optional**)*) –

          Mode, Determines if trace simple image or full sequence

          + `SINGLE`
            Single – Trace the current frame of the image.
          + `SEQUENCE`
            Sequence – Trace full sequence.
        * **use\_current\_frame** (*boolean**,* *(**optional**)*) – Start At Current Frame, Trace Image starting in current image frame
        * **frame\_number** (*int in* *[**0**,* *9999**]**,* *(**optional**)*) – Trace Frame, Used to trace only one frame of the image sequence, set to zero to trace all

bpy.ops.gpencil.transform\_fill(*mode='ROTATE'*, *location=(0.0, 0.0)*, *rotation=0.0*, *scale=0.0*, *release\_confirm=False*)[#](#bpy.ops.gpencil.transform_fill "Link to this definition")
:   Transform grease pencil stroke fill

    Parameters:
    :   * **mode** (*enum in* *[**'TRANSLATE'**,* *'ROTATE'**,* *'SCALE'**]**,* *(**optional**)*) – Mode
        * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location
        * **rotation** (*float in* *[**-6.28319**,* *6.28319**]**,* *(**optional**)*) – Rotation
        * **scale** (*float in* *[**0.001**,* *100**]**,* *(**optional**)*) – Scale
        * **release\_confirm** (*boolean**,* *(**optional**)*) – Confirm on Release

bpy.ops.gpencil.unlock\_all()[#](#bpy.ops.gpencil.unlock_all "Link to this definition")
:   Unlock all Grease Pencil layers so that they can be edited

bpy.ops.gpencil.vertex\_color\_brightness\_contrast(*mode='BOTH'*, *brightness=0.0*, *contrast=0.0*)[#](#bpy.ops.gpencil.vertex_color_brightness_contrast "Link to this definition")
:   Adjust vertex color brightness/contrast

    Parameters:
    :   * **mode** (*enum in* *[**'STROKE'**,* *'FILL'**,* *'BOTH'**]**,* *(**optional**)*) – Mode
        * **brightness** (*float in* *[**-100**,* *100**]**,* *(**optional**)*) – Brightness
        * **contrast** (*float in* *[**-100**,* *100**]**,* *(**optional**)*) – Contrast

bpy.ops.gpencil.vertex\_color\_hsv(*mode='BOTH'*, *h=0.5*, *s=1.0*, *v=1.0*)[#](#bpy.ops.gpencil.vertex_color_hsv "Link to this definition")
:   Adjust vertex color HSV values

    Parameters:
    :   * **mode** (*enum in* *[**'STROKE'**,* *'FILL'**,* *'BOTH'**]**,* *(**optional**)*) – Mode
        * **h** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Hue
        * **s** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Saturation
        * **v** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Value

bpy.ops.gpencil.vertex\_color\_invert(*mode='BOTH'*)[#](#bpy.ops.gpencil.vertex_color_invert "Link to this definition")
:   Invert RGB values

    Parameters:
    :   **mode** (*enum in* *[**'STROKE'**,* *'FILL'**,* *'BOTH'**]**,* *(**optional**)*) – Mode

bpy.ops.gpencil.vertex\_color\_levels(*mode='BOTH'*, *offset=0.0*, *gain=1.0*)[#](#bpy.ops.gpencil.vertex_color_levels "Link to this definition")
:   Adjust levels of vertex colors

    Parameters:
    :   * **mode** (*enum in* *[**'STROKE'**,* *'FILL'**,* *'BOTH'**]**,* *(**optional**)*) – Mode
        * **offset** (*float in* *[**-1**,* *1**]**,* *(**optional**)*) – Offset, Value to add to colors
        * **gain** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Gain, Value to multiply colors by

bpy.ops.gpencil.vertex\_color\_set(*mode='BOTH'*, *factor=1.0*)[#](#bpy.ops.gpencil.vertex_color_set "Link to this definition")
:   Set active color to all selected vertex

    Parameters:
    :   * **mode** (*enum in* *[**'STROKE'**,* *'FILL'**,* *'BOTH'**]**,* *(**optional**)*) – Mode
        * **factor** (*float in* *[**0.001**,* *1**]**,* *(**optional**)*) – Factor, Mix Factor

bpy.ops.gpencil.vertex\_group\_assign()[#](#bpy.ops.gpencil.vertex_group_assign "Link to this definition")
:   Assign the selected vertices to the active vertex group

bpy.ops.gpencil.vertex\_group\_deselect()[#](#bpy.ops.gpencil.vertex_group_deselect "Link to this definition")
:   Deselect all selected vertices assigned to the active vertex group

bpy.ops.gpencil.vertex\_group\_invert()[#](#bpy.ops.gpencil.vertex_group_invert "Link to this definition")
:   Invert weights to the active vertex group

bpy.ops.gpencil.vertex\_group\_normalize()[#](#bpy.ops.gpencil.vertex_group_normalize "Link to this definition")
:   Normalize weights to the active vertex group

bpy.ops.gpencil.vertex\_group\_normalize\_all(*lock\_active=True*)[#](#bpy.ops.gpencil.vertex_group_normalize_all "Link to this definition")
:   Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    Parameters:
    :   **lock\_active** (*boolean**,* *(**optional**)*) – Lock Active, Keep the values of the active group while normalizing others

bpy.ops.gpencil.vertex\_group\_remove\_from()[#](#bpy.ops.gpencil.vertex_group_remove_from "Link to this definition")
:   Remove the selected vertices from active or all vertex group(s)

bpy.ops.gpencil.vertex\_group\_select()[#](#bpy.ops.gpencil.vertex_group_select "Link to this definition")
:   Select all the vertices assigned to the active vertex group

bpy.ops.gpencil.vertex\_group\_smooth(*factor=0.5*, *repeat=1*)[#](#bpy.ops.gpencil.vertex_group_smooth "Link to this definition")
:   Smooth weights to the active vertex group

    Parameters:
    :   * **factor** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Factor
        * **repeat** (*int in* *[**1**,* *10000**]**,* *(**optional**)*) – Iterations

bpy.ops.gpencil.vertex\_paint(*stroke=None*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.vertex_paint "Link to this definition")
:   Paint stroke points with a color

    Parameters:
    :   * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.vertexmode\_toggle(*back=False*)[#](#bpy.ops.gpencil.vertexmode_toggle "Link to this definition")
:   Enter/Exit vertex paint mode for Grease Pencil strokes

    Parameters:
    :   **back** (*boolean**,* *(**optional**)*) – Return to Previous Mode, Return to previous mode

bpy.ops.gpencil.weight\_paint(*stroke=None*, *wait\_for\_input=True*)[#](#bpy.ops.gpencil.weight_paint "Link to this definition")
:   Draw weight on stroke points

    Parameters:
    :   * **stroke** (`bpy_prop_collection` of `OperatorStrokeElement`, (optional)) – Stroke
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input

bpy.ops.gpencil.weight\_sample()[#](#bpy.ops.gpencil.weight_sample "Link to this definition")
:   Use the mouse to sample a weight in the 3D view

bpy.ops.gpencil.weight\_toggle\_direction()[#](#bpy.ops.gpencil.weight_toggle_direction "Link to this definition")
:   Toggle Add/Subtract for the weight paint draw tool

bpy.ops.gpencil.weightmode\_toggle(*back=False*)[#](#bpy.ops.gpencil.weightmode_toggle "Link to this definition")
:   Enter/Exit weight paint mode for Grease Pencil strokes

    Parameters:
    :   **back** (*boolean**,* *(**optional**)*) – Return to Previous Mode, Return to previous mode

[Next

Graph Operators](graph.md)
[Previous

Gizmogroup Operators](gizmogroup.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.gpencil.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.gpencil.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Gpencil Operators
  + [`active_frame_delete()`](#bpy.ops.gpencil.active_frame_delete)
  + [`active_frames_delete_all()`](#bpy.ops.gpencil.active_frames_delete_all)
  + [`annotate()`](#bpy.ops.gpencil.annotate)
  + [`annotation_active_frame_delete()`](#bpy.ops.gpencil.annotation_active_frame_delete)
  + [`annotation_add()`](#bpy.ops.gpencil.annotation_add)
  + [`bake_grease_pencil_animation()`](#bpy.ops.gpencil.bake_grease_pencil_animation)
  + [`bake_mesh_animation()`](#bpy.ops.gpencil.bake_mesh_animation)
  + [`blank_frame_add()`](#bpy.ops.gpencil.blank_frame_add)
  + [`brush_reset()`](#bpy.ops.gpencil.brush_reset)
  + [`brush_reset_all()`](#bpy.ops.gpencil.brush_reset_all)
  + [`convert()`](#bpy.ops.gpencil.convert)
  + [`convert_old_files()`](#bpy.ops.gpencil.convert_old_files)
  + [`copy()`](#bpy.ops.gpencil.copy)
  + [`data_unlink()`](#bpy.ops.gpencil.data_unlink)
  + [`delete()`](#bpy.ops.gpencil.delete)
  + [`dissolve()`](#bpy.ops.gpencil.dissolve)
  + [`draw()`](#bpy.ops.gpencil.draw)
  + [`duplicate()`](#bpy.ops.gpencil.duplicate)
  + [`duplicate_move()`](#bpy.ops.gpencil.duplicate_move)
  + [`editmode_toggle()`](#bpy.ops.gpencil.editmode_toggle)
  + [`extract_palette_vertex()`](#bpy.ops.gpencil.extract_palette_vertex)
  + [`extrude()`](#bpy.ops.gpencil.extrude)
  + [`extrude_move()`](#bpy.ops.gpencil.extrude_move)
  + [`fill()`](#bpy.ops.gpencil.fill)
  + [`frame_clean_duplicate()`](#bpy.ops.gpencil.frame_clean_duplicate)
  + [`frame_clean_fill()`](#bpy.ops.gpencil.frame_clean_fill)
  + [`frame_clean_loose()`](#bpy.ops.gpencil.frame_clean_loose)
  + [`frame_duplicate()`](#bpy.ops.gpencil.frame_duplicate)
  + [`generate_weights()`](#bpy.ops.gpencil.generate_weights)
  + [`guide_rotate()`](#bpy.ops.gpencil.guide_rotate)
  + [`hide()`](#bpy.ops.gpencil.hide)
  + [`image_to_grease_pencil()`](#bpy.ops.gpencil.image_to_grease_pencil)
  + [`interpolate()`](#bpy.ops.gpencil.interpolate)
  + [`interpolate_reverse()`](#bpy.ops.gpencil.interpolate_reverse)
  + [`interpolate_sequence()`](#bpy.ops.gpencil.interpolate_sequence)
  + [`layer_active()`](#bpy.ops.gpencil.layer_active)
  + [`layer_add()`](#bpy.ops.gpencil.layer_add)
  + [`layer_annotation_add()`](#bpy.ops.gpencil.layer_annotation_add)
  + [`layer_annotation_move()`](#bpy.ops.gpencil.layer_annotation_move)
  + [`layer_annotation_remove()`](#bpy.ops.gpencil.layer_annotation_remove)
  + [`layer_change()`](#bpy.ops.gpencil.layer_change)
  + [`layer_duplicate()`](#bpy.ops.gpencil.layer_duplicate)
  + [`layer_duplicate_object()`](#bpy.ops.gpencil.layer_duplicate_object)
  + [`layer_isolate()`](#bpy.ops.gpencil.layer_isolate)
  + [`layer_mask_add()`](#bpy.ops.gpencil.layer_mask_add)
  + [`layer_mask_move()`](#bpy.ops.gpencil.layer_mask_move)
  + [`layer_mask_remove()`](#bpy.ops.gpencil.layer_mask_remove)
  + [`layer_merge()`](#bpy.ops.gpencil.layer_merge)
  + [`layer_move()`](#bpy.ops.gpencil.layer_move)
  + [`layer_remove()`](#bpy.ops.gpencil.layer_remove)
  + [`lock_all()`](#bpy.ops.gpencil.lock_all)
  + [`lock_layer()`](#bpy.ops.gpencil.lock_layer)
  + [`material_hide()`](#bpy.ops.gpencil.material_hide)
  + [`material_isolate()`](#bpy.ops.gpencil.material_isolate)
  + [`material_lock_all()`](#bpy.ops.gpencil.material_lock_all)
  + [`material_lock_unused()`](#bpy.ops.gpencil.material_lock_unused)
  + [`material_reveal()`](#bpy.ops.gpencil.material_reveal)
  + [`material_select()`](#bpy.ops.gpencil.material_select)
  + [`material_set()`](#bpy.ops.gpencil.material_set)
  + [`material_to_vertex_color()`](#bpy.ops.gpencil.material_to_vertex_color)
  + [`material_unlock_all()`](#bpy.ops.gpencil.material_unlock_all)
  + [`materials_copy_to_object()`](#bpy.ops.gpencil.materials_copy_to_object)
  + [`move_to_layer()`](#bpy.ops.gpencil.move_to_layer)
  + [`paintmode_toggle()`](#bpy.ops.gpencil.paintmode_toggle)
  + [`paste()`](#bpy.ops.gpencil.paste)
  + [`primitive_box()`](#bpy.ops.gpencil.primitive_box)
  + [`primitive_circle()`](#bpy.ops.gpencil.primitive_circle)
  + [`primitive_curve()`](#bpy.ops.gpencil.primitive_curve)
  + [`primitive_line()`](#bpy.ops.gpencil.primitive_line)
  + [`primitive_polyline()`](#bpy.ops.gpencil.primitive_polyline)
  + [`recalc_geometry()`](#bpy.ops.gpencil.recalc_geometry)
  + [`reproject()`](#bpy.ops.gpencil.reproject)
  + [`reset_transform_fill()`](#bpy.ops.gpencil.reset_transform_fill)
  + [`reveal()`](#bpy.ops.gpencil.reveal)
  + [`sculpt_paint()`](#bpy.ops.gpencil.sculpt_paint)
  + [`sculptmode_toggle()`](#bpy.ops.gpencil.sculptmode_toggle)
  + [`segment_add()`](#bpy.ops.gpencil.segment_add)
  + [`segment_move()`](#bpy.ops.gpencil.segment_move)
  + [`segment_remove()`](#bpy.ops.gpencil.segment_remove)
  + [`select()`](#bpy.ops.gpencil.select)
  + [`select_all()`](#bpy.ops.gpencil.select_all)
  + [`select_alternate()`](#bpy.ops.gpencil.select_alternate)
  + [`select_box()`](#bpy.ops.gpencil.select_box)
  + [`select_circle()`](#bpy.ops.gpencil.select_circle)
  + [`select_first()`](#bpy.ops.gpencil.select_first)
  + [`select_grouped()`](#bpy.ops.gpencil.select_grouped)
  + [`select_lasso()`](#bpy.ops.gpencil.select_lasso)
  + [`select_last()`](#bpy.ops.gpencil.select_last)
  + [`select_less()`](#bpy.ops.gpencil.select_less)
  + [`select_linked()`](#bpy.ops.gpencil.select_linked)
  + [`select_more()`](#bpy.ops.gpencil.select_more)
  + [`select_random()`](#bpy.ops.gpencil.select_random)
  + [`select_vertex_color()`](#bpy.ops.gpencil.select_vertex_color)
  + [`selection_opacity_toggle()`](#bpy.ops.gpencil.selection_opacity_toggle)
  + [`selectmode_toggle()`](#bpy.ops.gpencil.selectmode_toggle)
  + [`set_active_material()`](#bpy.ops.gpencil.set_active_material)
  + [`snap_cursor_to_selected()`](#bpy.ops.gpencil.snap_cursor_to_selected)
  + [`snap_to_cursor()`](#bpy.ops.gpencil.snap_to_cursor)
  + [`snap_to_grid()`](#bpy.ops.gpencil.snap_to_grid)
  + [`stroke_apply_thickness()`](#bpy.ops.gpencil.stroke_apply_thickness)
  + [`stroke_arrange()`](#bpy.ops.gpencil.stroke_arrange)
  + [`stroke_caps_set()`](#bpy.ops.gpencil.stroke_caps_set)
  + [`stroke_change_color()`](#bpy.ops.gpencil.stroke_change_color)
  + [`stroke_cutter()`](#bpy.ops.gpencil.stroke_cutter)
  + [`stroke_cyclical_set()`](#bpy.ops.gpencil.stroke_cyclical_set)
  + [`stroke_editcurve_set_handle_type()`](#bpy.ops.gpencil.stroke_editcurve_set_handle_type)
  + [`stroke_enter_editcurve_mode()`](#bpy.ops.gpencil.stroke_enter_editcurve_mode)
  + [`stroke_flip()`](#bpy.ops.gpencil.stroke_flip)
  + [`stroke_join()`](#bpy.ops.gpencil.stroke_join)
  + [`stroke_merge()`](#bpy.ops.gpencil.stroke_merge)
  + [`stroke_merge_by_distance()`](#bpy.ops.gpencil.stroke_merge_by_distance)
  + [`stroke_merge_material()`](#bpy.ops.gpencil.stroke_merge_material)
  + [`stroke_normalize()`](#bpy.ops.gpencil.stroke_normalize)
  + [`stroke_outline()`](#bpy.ops.gpencil.stroke_outline)
  + [`stroke_reset_vertex_color()`](#bpy.ops.gpencil.stroke_reset_vertex_color)
  + [`stroke_sample()`](#bpy.ops.gpencil.stroke_sample)
  + [`stroke_separate()`](#bpy.ops.gpencil.stroke_separate)
  + [`stroke_simplify()`](#bpy.ops.gpencil.stroke_simplify)
  + [`stroke_simplify_fixed()`](#bpy.ops.gpencil.stroke_simplify_fixed)
  + [`stroke_smooth()`](#bpy.ops.gpencil.stroke_smooth)
  + [`stroke_split()`](#bpy.ops.gpencil.stroke_split)
  + [`stroke_start_set()`](#bpy.ops.gpencil.stroke_start_set)
  + [`stroke_subdivide()`](#bpy.ops.gpencil.stroke_subdivide)
  + [`stroke_trim()`](#bpy.ops.gpencil.stroke_trim)
  + [`time_segment_add()`](#bpy.ops.gpencil.time_segment_add)
  + [`time_segment_move()`](#bpy.ops.gpencil.time_segment_move)
  + [`time_segment_remove()`](#bpy.ops.gpencil.time_segment_remove)
  + [`tint_flip()`](#bpy.ops.gpencil.tint_flip)
  + [`trace_image()`](#bpy.ops.gpencil.trace_image)
  + [`transform_fill()`](#bpy.ops.gpencil.transform_fill)
  + [`unlock_all()`](#bpy.ops.gpencil.unlock_all)
  + [`vertex_color_brightness_contrast()`](#bpy.ops.gpencil.vertex_color_brightness_contrast)
  + [`vertex_color_hsv()`](#bpy.ops.gpencil.vertex_color_hsv)
  + [`vertex_color_invert()`](#bpy.ops.gpencil.vertex_color_invert)
  + [`vertex_color_levels()`](#bpy.ops.gpencil.vertex_color_levels)
  + [`vertex_color_set()`](#bpy.ops.gpencil.vertex_color_set)
  + [`vertex_group_assign()`](#bpy.ops.gpencil.vertex_group_assign)
  + [`vertex_group_deselect()`](#bpy.ops.gpencil.vertex_group_deselect)
  + [`vertex_group_invert()`](#bpy.ops.gpencil.vertex_group_invert)
  + [`vertex_group_normalize()`](#bpy.ops.gpencil.vertex_group_normalize)
  + [`vertex_group_normalize_all()`](#bpy.ops.gpencil.vertex_group_normalize_all)
  + [`vertex_group_remove_from()`](#bpy.ops.gpencil.vertex_group_remove_from)
  + [`vertex_group_select()`](#bpy.ops.gpencil.vertex_group_select)
  + [`vertex_group_smooth()`](#bpy.ops.gpencil.vertex_group_smooth)
  + [`vertex_paint()`](#bpy.ops.gpencil.vertex_paint)
  + [`vertexmode_toggle()`](#bpy.ops.gpencil.vertexmode_toggle)
  + [`weight_paint()`](#bpy.ops.gpencil.weight_paint)
  + [`weight_sample()`](#bpy.ops.gpencil.weight_sample)
  + [`weight_toggle_direction()`](#bpy.ops.gpencil.weight_toggle_direction)
  + [`weightmode_toggle()`](#bpy.ops.gpencil.weightmode_toggle)