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

# Sculpt Operators[#](#module-bpy.ops.sculpt "Link to this heading")

bpy.ops.sculpt.brush\_stroke(*stroke=None*, *mode='NORMAL'*, *pen\_flip=False*, *ignore\_background\_click=False*)[#](#bpy.ops.sculpt.brush_stroke "Link to this definition")
:   Sculpt a stroke into the geometry

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
        * **ignore\_background\_click** (*boolean**,* *(**optional**)*) – Ignore Background Click, Clicks on the background do not start the stroke

bpy.ops.sculpt.cloth\_filter(*start\_mouse=(0, 0)*, *area\_normal\_radius=0.25*, *strength=1.0*, *iteration\_count=1*, *event\_history=None*, *type='GRAVITY'*, *force\_axis={'X', 'Y', 'Z'}*, *orientation='LOCAL'*, *cloth\_mass=1.0*, *cloth\_damping=0.0*, *use\_face\_sets=False*, *use\_collisions=False*)[#](#bpy.ops.sculpt.cloth_filter "Link to this definition")
:   Applies a cloth simulation deformation to the entire mesh

    Parameters:
    :   * **start\_mouse** (*int array* *of* *2 items in* *[**0**,* *16384**]**,* *(**optional**)*) – Starting Mouse
        * **area\_normal\_radius** (*float in* *[**0.001**,* *5**]**,* *(**optional**)*) – Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        * **strength** (*float in* *[**-10**,* *10**]**,* *(**optional**)*) – Strength, Filter strength
        * **iteration\_count** (*int in* *[**1**,* *10000**]**,* *(**optional**)*) – Repeat, How many times to repeat the filter
        * **type** (*enum in* *[**'GRAVITY'**,* *'INFLATE'**,* *'EXPAND'**,* *'PINCH'**,* *'SCALE'**]**,* *(**optional**)*) –

          Filter Type, Operation that is going to be applied to the mesh

          + `GRAVITY`
            Gravity – Applies gravity to the simulation.
          + `INFLATE`
            Inflate – Inflates the cloth.
          + `EXPAND`
            Expand – Expands the cloth’s dimensions.
          + `PINCH`
            Pinch – Pulls the cloth to the cursor’s start position.
          + `SCALE`
            Scale – Scales the mesh as a soft body using the origin of the object as scale.
        * **force\_axis** (*enum set in {'X'**,* *'Y'**,* *'Z'}**,* *(**optional**)*) –

          Force Axis, Apply the force in the selected axis

          + `X`
            X – Apply force in the X axis.
          + `Y`
            Y – Apply force in the Y axis.
          + `Z`
            Z – Apply force in the Z axis.
        * **orientation** (*enum in* *[**'LOCAL'**,* *'WORLD'**,* *'VIEW'**]**,* *(**optional**)*) –

          Orientation, Orientation of the axis to limit the filter force

          + `LOCAL`
            Local – Use the local axis to limit the force and set the gravity direction.
          + `WORLD`
            World – Use the global axis to limit the force and set the gravity direction.
          + `VIEW`
            View – Use the view axis to limit the force and set the gravity direction.
        * **cloth\_mass** (*float in* *[**0**,* *2**]**,* *(**optional**)*) – Cloth Mass, Mass of each simulation particle
        * **cloth\_damping** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Cloth Damping, How much the applied forces are propagated through the cloth
        * **use\_face\_sets** (*boolean**,* *(**optional**)*) – Use Face Sets, Apply the filter only to the Face Set under the cursor
        * **use\_collisions** (*boolean**,* *(**optional**)*) – Use Collisions, Collide with other collider objects in the scene

bpy.ops.sculpt.color\_filter(*start\_mouse=(0, 0)*, *area\_normal\_radius=0.25*, *strength=1.0*, *iteration\_count=1*, *event\_history=None*, *type='FILL'*, *fill\_color=(1.0, 1.0, 1.0)*)[#](#bpy.ops.sculpt.color_filter "Link to this definition")
:   Applies a filter to modify the active color attribute

    Parameters:
    :   * **start\_mouse** (*int array* *of* *2 items in* *[**0**,* *16384**]**,* *(**optional**)*) – Starting Mouse
        * **area\_normal\_radius** (*float in* *[**0.001**,* *5**]**,* *(**optional**)*) – Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        * **strength** (*float in* *[**-10**,* *10**]**,* *(**optional**)*) – Strength, Filter strength
        * **iteration\_count** (*int in* *[**1**,* *10000**]**,* *(**optional**)*) – Repeat, How many times to repeat the filter
        * **type** (*enum in* *[**'FILL'**,* *'HUE'**,* *'SATURATION'**,* *'VALUE'**,* *'BRIGHTNESS'**,* *'CONTRAST'**,* *'SMOOTH'**,* *'RED'**,* *'GREEN'**,* *'BLUE'**]**,* *(**optional**)*) –

          Filter Type

          + `FILL`
            Fill – Fill with a specific color.
          + `HUE`
            Hue – Change hue.
          + `SATURATION`
            Saturation – Change saturation.
          + `VALUE`
            Value – Change value.
          + `BRIGHTNESS`
            Brightness – Change brightness.
          + `CONTRAST`
            Contrast – Change contrast.
          + `SMOOTH`
            Smooth – Smooth colors.
          + `RED`
            Red – Change red channel.
          + `GREEN`
            Green – Change green channel.
          + `BLUE`
            Blue – Change blue channel.
        * **fill\_color** ([`mathutils.Color`](../../mathutils/index.md#mathutils.Color "mathutils.Color") of 3 items in [0, inf], (optional)) – Fill Color

bpy.ops.sculpt.detail\_flood\_fill()[#](#bpy.ops.sculpt.detail_flood_fill "Link to this definition")
:   Flood fill the mesh with the selected detail setting

bpy.ops.sculpt.dynamic\_topology\_toggle()[#](#bpy.ops.sculpt.dynamic_topology_toggle "Link to this definition")
:   Dynamic topology alters the mesh topology while sculpting

bpy.ops.sculpt.dyntopo\_detail\_size\_edit()[#](#bpy.ops.sculpt.dyntopo_detail_size_edit "Link to this definition")
:   Modify the detail size of dyntopo interactively

bpy.ops.sculpt.expand(*target='MASK'*, *falloff\_type='GEODESIC'*, *invert=False*, *use\_mask\_preserve=False*, *use\_falloff\_gradient=False*, *use\_modify\_active=False*, *use\_reposition\_pivot=True*, *max\_geodesic\_move\_preview=10000*, *use\_auto\_mask=False*, *normal\_falloff\_smooth=2*)[#](#bpy.ops.sculpt.expand "Link to this definition")
:   Generic sculpt expand operator

    Parameters:
    :   * **target** (*enum in* *[**'MASK'**,* *'FACE\_SETS'**,* *'COLOR'**]**,* *(**optional**)*) – Data Target, Data that is going to be modified in the expand operation
        * **falloff\_type** (*enum in* *[**'GEODESIC'**,* *'TOPOLOGY'**,* *'TOPOLOGY\_DIAGONALS'**,* *'NORMALS'**,* *'SPHERICAL'**,* *'BOUNDARY\_TOPOLOGY'**,* *'BOUNDARY\_FACE\_SET'**,* *'ACTIVE\_FACE\_SET'**]**,* *(**optional**)*) – Falloff Type, Initial falloff of the expand operation
        * **invert** (*boolean**,* *(**optional**)*) – Invert, Invert the expand active elements
        * **use\_mask\_preserve** (*boolean**,* *(**optional**)*) – Preserve Previous, Preserve the previous state of the target data
        * **use\_falloff\_gradient** (*boolean**,* *(**optional**)*) – Falloff Gradient, Expand Using a linear falloff
        * **use\_modify\_active** (*boolean**,* *(**optional**)*) – Modify Active, Modify the active Face Set instead of creating a new one
        * **use\_reposition\_pivot** (*boolean**,* *(**optional**)*) – Reposition Pivot, Reposition the sculpt transform pivot to the boundary of the expand active area
        * **max\_geodesic\_move\_preview** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Max Vertex Count for Geodesic Move Preview, Maximum number of vertices in the mesh for using geodesic falloff when moving the origin of expand. If the total number of vertices is greater than this value, the falloff will be set to spherical when moving
        * **use\_auto\_mask** (*boolean**,* *(**optional**)*) – Auto Create, Fill in mask if nothing is already masked
        * **normal\_falloff\_smooth** (*int in* *[**0**,* *10**]**,* *(**optional**)*) – Normal Smooth, Blurring steps for normal falloff

bpy.ops.sculpt.face\_set\_box\_gesture(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *use\_front\_faces\_only=False*)[#](#bpy.ops.sculpt.face_set_box_gesture "Link to this definition")
:   Add a face set in a rectangle defined by the cursor

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.sculpt.face\_set\_change\_visibility(*mode='TOGGLE'*)[#](#bpy.ops.sculpt.face_set_change_visibility "Link to this definition")
:   Change the visibility of the Face Sets of the sculpt

    Parameters:
    :   **mode** (*enum in* *[**'TOGGLE'**,* *'SHOW\_ACTIVE'**,* *'HIDE\_ACTIVE'**]**,* *(**optional**)*) –

        Mode

        * `TOGGLE`
          Toggle Visibility – Hide all Face Sets except for the active one.
        * `SHOW_ACTIVE`
          Show Active Face Set – Show Active Face Set.
        * `HIDE_ACTIVE`
          Hide Active Face Sets – Hide Active Face Sets.

bpy.ops.sculpt.face\_set\_edit(*active\_face\_set=1*, *mode='GROW'*, *strength=1.0*, *modify\_hidden=False*)[#](#bpy.ops.sculpt.face_set_edit "Link to this definition")
:   Edits the current active Face Set

    Parameters:
    :   * **active\_face\_set** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Active Face Set
        * **mode** (*enum in* *[**'GROW'**,* *'SHRINK'**,* *'DELETE\_GEOMETRY'**,* *'FAIR\_POSITIONS'**,* *'FAIR\_TANGENCY'**]**,* *(**optional**)*) –

          Mode

          + `GROW`
            Grow Face Set – Grows the Face Sets boundary by one face based on mesh topology.
          + `SHRINK`
            Shrink Face Set – Shrinks the Face Sets boundary by one face based on mesh topology.
          + `DELETE_GEOMETRY`
            Delete Geometry – Deletes the faces that are assigned to the Face Set.
          + `FAIR_POSITIONS`
            Fair Positions – Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex positions.
          + `FAIR_TANGENCY`
            Fair Tangency – Creates a smooth as possible geometry patch from the Face Set minimizing changes in vertex tangents.
        * **strength** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Strength
        * **modify\_hidden** (*boolean**,* *(**optional**)*) – Modify Hidden, Apply the edit operation to hidden geometry

bpy.ops.sculpt.face\_set\_lasso\_gesture(*path=None*, *use\_front\_faces\_only=False*)[#](#bpy.ops.sculpt.face_set_lasso_gesture "Link to this definition")
:   Add a face set in a shape defined by the cursor

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.sculpt.face\_set\_line\_gesture(*xstart=0*, *xend=0*, *ystart=0*, *yend=0*, *flip=False*, *cursor=5*, *use\_front\_faces\_only=False*, *use\_limit\_to\_segment=False*)[#](#bpy.ops.sculpt.face_set_line_gesture "Link to this definition")
:   Add a face set to one side of a line defined by the cursor

    Parameters:
    :   * **xstart** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Start
        * **xend** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X End
        * **ystart** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Start
        * **yend** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y End
        * **flip** (*boolean**,* *(**optional**)*) – Flip
        * **cursor** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Cursor, Mouse cursor style to use during the modal operator
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view
        * **use\_limit\_to\_segment** (*boolean**,* *(**optional**)*) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

bpy.ops.sculpt.face\_set\_polyline\_gesture(*path=None*, *use\_front\_faces\_only=False*)[#](#bpy.ops.sculpt.face_set_polyline_gesture "Link to this definition")
:   Add a face set in a shape defined by the cursor

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view

bpy.ops.sculpt.face\_sets\_create(*mode='MASKED'*)[#](#bpy.ops.sculpt.face_sets_create "Link to this definition")
:   Create a new Face Set

    Parameters:
    :   **mode** (*enum in* *[**'MASKED'**,* *'VISIBLE'**,* *'ALL'**,* *'SELECTION'**]**,* *(**optional**)*) –

        Mode

        * `MASKED`
          Face Set from Masked – Create a new Face Set from the masked faces.
        * `VISIBLE`
          Face Set from Visible – Create a new Face Set from the visible vertices.
        * `ALL`
          Face Set Full Mesh – Create an unique Face Set with all faces in the sculpt.
        * `SELECTION`
          Face Set from Edit Mode Selection – Create an Face Set corresponding to the Edit Mode face selection.

bpy.ops.sculpt.face\_sets\_init(*mode='LOOSE\_PARTS'*, *threshold=0.5*)[#](#bpy.ops.sculpt.face_sets_init "Link to this definition")
:   Initializes all Face Sets in the mesh

    Parameters:
    :   * **mode** (*enum in* *[**'LOOSE\_PARTS'**,* *'MATERIALS'**,* *'NORMALS'**,* *'UV\_SEAMS'**,* *'CREASES'**,* *'BEVEL\_WEIGHT'**,* *'SHARP\_EDGES'**,* *'FACE\_SET\_BOUNDARIES'**]**,* *(**optional**)*) –

          Mode

          + `LOOSE_PARTS`
            Face Sets from Loose Parts – Create a Face Set per loose part in the mesh.
          + `MATERIALS`
            Face Sets from Material Slots – Create a Face Set per Material Slot.
          + `NORMALS`
            Face Sets from Mesh Normals – Create Face Sets for Faces that have similar normal.
          + `UV_SEAMS`
            Face Sets from UV Seams – Create Face Sets using UV Seams as boundaries.
          + `CREASES`
            Face Sets from Edge Creases – Create Face Sets using Edge Creases as boundaries.
          + `BEVEL_WEIGHT`
            Face Sets from Bevel Weight – Create Face Sets using Bevel Weights as boundaries.
          + `SHARP_EDGES`
            Face Sets from Sharp Edges – Create Face Sets using Sharp Edges as boundaries.
          + `FACE_SET_BOUNDARIES`
            Face Sets from Face Set Boundaries – Create a Face Set per isolated Face Set.
        * **threshold** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Threshold, Minimum value to consider a certain attribute a boundary when creating the Face Sets

bpy.ops.sculpt.face\_sets\_randomize\_colors()[#](#bpy.ops.sculpt.face_sets_randomize_colors "Link to this definition")
:   Generates a new set of random colors to render the Face Sets in the viewport

bpy.ops.sculpt.mask\_by\_color(*contiguous=False*, *invert=False*, *preserve\_previous\_mask=False*, *threshold=0.35*)[#](#bpy.ops.sculpt.mask_by_color "Link to this definition")
:   Creates a mask based on the active color attribute

    Parameters:
    :   * **contiguous** (*boolean**,* *(**optional**)*) – Contiguous, Mask only contiguous color areas
        * **invert** (*boolean**,* *(**optional**)*) – Invert, Invert the generated mask
        * **preserve\_previous\_mask** (*boolean**,* *(**optional**)*) – Preserve Previous Mask, Preserve the previous mask and add or subtract the new one generated by the colors
        * **threshold** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Threshold, How much changes in color affect the mask generation

bpy.ops.sculpt.mask\_filter(*filter\_type='SMOOTH'*, *iterations=1*, *auto\_iteration\_count=True*)[#](#bpy.ops.sculpt.mask_filter "Link to this definition")
:   Applies a filter to modify the current mask

    Parameters:
    :   * **filter\_type** (*enum in* *[**'SMOOTH'**,* *'SHARPEN'**,* *'GROW'**,* *'SHRINK'**,* *'CONTRAST\_INCREASE'**,* *'CONTRAST\_DECREASE'**]**,* *(**optional**)*) – Type, Filter that is going to be applied to the mask
        * **iterations** (*int in* *[**1**,* *100**]**,* *(**optional**)*) – Iterations, Number of times that the filter is going to be applied
        * **auto\_iteration\_count** (*boolean**,* *(**optional**)*) – Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt

bpy.ops.sculpt.mask\_from\_cavity(*mix\_mode='MIX'*, *mix\_factor=1.0*, *settings\_source='OPERATOR'*, *factor=0.5*, *blur\_steps=2*, *use\_curve=False*, *invert=False*)[#](#bpy.ops.sculpt.mask_from_cavity "Link to this definition")
:   Creates a mask based on the curvature of the surface

    Parameters:
    :   * **mix\_mode** (*enum in* *[**'MIX'**,* *'MULTIPLY'**,* *'DIVIDE'**,* *'ADD'**,* *'SUBTRACT'**]**,* *(**optional**)*) – Mode, Mix mode
        * **mix\_factor** (*float in* *[**0**,* *5**]**,* *(**optional**)*) – Mix Factor
        * **settings\_source** (*enum in* *[**'OPERATOR'**,* *'BRUSH'**,* *'SCENE'**]**,* *(**optional**)*) –

          Settings, Use settings from here

          + `OPERATOR`
            Operator – Use settings from operator properties.
          + `BRUSH`
            Brush – Use settings from brush.
          + `SCENE`
            Scene – Use settings from scene.
        * **factor** (*float in* *[**0**,* *5**]**,* *(**optional**)*) – Factor, The contrast of the cavity mask
        * **blur\_steps** (*int in* *[**0**,* *25**]**,* *(**optional**)*) – Blur, The number of times the cavity mask is blurred
        * **use\_curve** (*boolean**,* *(**optional**)*) – Custom Curve
        * **invert** (*boolean**,* *(**optional**)*) – Cavity (Inverted)

bpy.ops.sculpt.mask\_init(*mode='RANDOM\_PER\_VERTEX'*)[#](#bpy.ops.sculpt.mask_init "Link to this definition")
:   Creates a new mask for the entire mesh

    Parameters:
    :   **mode** (*enum in* *[**'RANDOM\_PER\_VERTEX'**,* *'RANDOM\_PER\_FACE\_SET'**,* *'RANDOM\_PER\_LOOSE\_PART'**]**,* *(**optional**)*) – Mode

bpy.ops.sculpt.mesh\_filter(*start\_mouse=(0, 0)*, *area\_normal\_radius=0.25*, *strength=1.0*, *iteration\_count=1*, *event\_history=None*, *type='INFLATE'*, *deform\_axis={'X', 'Y', 'Z'}*, *orientation='LOCAL'*, *surface\_smooth\_shape\_preservation=0.5*, *surface\_smooth\_current\_vertex=0.5*, *sharpen\_smooth\_ratio=0.35*, *sharpen\_intensify\_detail\_strength=0.0*, *sharpen\_curvature\_smooth\_iterations=0*)[#](#bpy.ops.sculpt.mesh_filter "Link to this definition")
:   Applies a filter to modify the current mesh

    Parameters:
    :   * **start\_mouse** (*int array* *of* *2 items in* *[**0**,* *16384**]**,* *(**optional**)*) – Starting Mouse
        * **area\_normal\_radius** (*float in* *[**0.001**,* *5**]**,* *(**optional**)*) – Normal Radius, Radius used for calculating area normal on initial click,in percentage of brush radius
        * **strength** (*float in* *[**-10**,* *10**]**,* *(**optional**)*) – Strength, Filter strength
        * **iteration\_count** (*int in* *[**1**,* *10000**]**,* *(**optional**)*) – Repeat, How many times to repeat the filter
        * **type** (*enum in* *[**'SMOOTH'**,* *'SCALE'**,* *'INFLATE'**,* *'SPHERE'**,* *'RANDOM'**,* *'RELAX'**,* *'RELAX\_FACE\_SETS'**,* *'SURFACE\_SMOOTH'**,* *'SHARPEN'**,* *'ENHANCE\_DETAILS'**,* *'ERASE\_DISCPLACEMENT'**]**,* *(**optional**)*) –

          Filter Type, Operation that is going to be applied to the mesh

          + `SMOOTH`
            Smooth – Smooth mesh.
          + `SCALE`
            Scale – Scale mesh.
          + `INFLATE`
            Inflate – Inflate mesh.
          + `SPHERE`
            Sphere – Morph into sphere.
          + `RANDOM`
            Random – Randomize vertex positions.
          + `RELAX`
            Relax – Relax mesh.
          + `RELAX_FACE_SETS`
            Relax Face Sets – Smooth the edges of all the Face Sets.
          + `SURFACE_SMOOTH`
            Surface Smooth – Smooth the surface of the mesh, preserving the volume.
          + `SHARPEN`
            Sharpen – Sharpen the cavities of the mesh.
          + `ENHANCE_DETAILS`
            Enhance Details – Enhance the high frequency surface detail.
          + `ERASE_DISCPLACEMENT`
            Erase Displacement – Deletes the displacement of the Multires Modifier.
        * **deform\_axis** (*enum set in {'X'**,* *'Y'**,* *'Z'}**,* *(**optional**)*) –

          Deform Axis, Apply the deformation in the selected axis

          + `X`
            X – Deform in the X axis.
          + `Y`
            Y – Deform in the Y axis.
          + `Z`
            Z – Deform in the Z axis.
        * **orientation** (*enum in* *[**'LOCAL'**,* *'WORLD'**,* *'VIEW'**]**,* *(**optional**)*) –

          Orientation, Orientation of the axis to limit the filter displacement

          + `LOCAL`
            Local – Use the local axis to limit the displacement.
          + `WORLD`
            World – Use the global axis to limit the displacement.
          + `VIEW`
            View – Use the view axis to limit the displacement.
        * **surface\_smooth\_shape\_preservation** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Shape Preservation, How much of the original shape is preserved when smoothing
        * **surface\_smooth\_current\_vertex** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Per Vertex Displacement, How much the position of each individual vertex influences the final result
        * **sharpen\_smooth\_ratio** (*float in* *[**0**,* *1**]**,* *(**optional**)*) – Smooth Ratio, How much smoothing is applied to polished surfaces
        * **sharpen\_intensify\_detail\_strength** (*float in* *[**0**,* *10**]**,* *(**optional**)*) – Intensify Details, How much creases and valleys are intensified
        * **sharpen\_curvature\_smooth\_iterations** (*int in* *[**0**,* *10**]**,* *(**optional**)*) – Curvature Smooth Iterations, How much smooth the resulting shape is, ignoring high frequency details

bpy.ops.sculpt.optimize()[#](#bpy.ops.sculpt.optimize "Link to this definition")
:   Recalculate the sculpt BVH to improve performance

bpy.ops.sculpt.project\_line\_gesture(*xstart=0*, *xend=0*, *ystart=0*, *yend=0*, *flip=False*, *cursor=5*, *use\_front\_faces\_only=False*, *use\_limit\_to\_segment=False*)[#](#bpy.ops.sculpt.project_line_gesture "Link to this definition")
:   Project the geometry onto a plane defined by a line

    Parameters:
    :   * **xstart** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Start
        * **xend** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X End
        * **ystart** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Start
        * **yend** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y End
        * **flip** (*boolean**,* *(**optional**)*) – Flip
        * **cursor** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Cursor, Mouse cursor style to use during the modal operator
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view
        * **use\_limit\_to\_segment** (*boolean**,* *(**optional**)*) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line

bpy.ops.sculpt.sample\_color()[#](#bpy.ops.sculpt.sample_color "Link to this definition")
:   Sample the vertex color of the active vertex

bpy.ops.sculpt.sample\_detail\_size(*location=(0, 0)*, *mode='DYNTOPO'*)[#](#bpy.ops.sculpt.sample_detail_size "Link to this definition")
:   Sample the mesh detail on clicked point

    Parameters:
    :   * **location** (*int array* *of* *2 items in* *[**0**,* *32767**]**,* *(**optional**)*) – Location, Screen coordinates of sampling
        * **mode** (*enum in* *[**'DYNTOPO'**,* *'VOXEL'**]**,* *(**optional**)*) –

          Detail Mode, Target sculpting workflow that is going to use the sampled size

          + `DYNTOPO`
            Dyntopo – Sample dyntopo detail.
          + `VOXEL`
            Voxel – Sample mesh voxel size.

bpy.ops.sculpt.sculptmode\_toggle()[#](#bpy.ops.sculpt.sculptmode_toggle "Link to this definition")
:   Toggle sculpt mode in 3D view

bpy.ops.sculpt.set\_persistent\_base()[#](#bpy.ops.sculpt.set_persistent_base "Link to this definition")
:   Reset the copy of the mesh that is being sculpted on

bpy.ops.sculpt.set\_pivot\_position(*mode='UNMASKED'*, *mouse\_x=0.0*, *mouse\_y=0.0*)[#](#bpy.ops.sculpt.set_pivot_position "Link to this definition")
:   Sets the sculpt transform pivot position

    Parameters:
    :   * **mode** (*enum in* *[**'ORIGIN'**,* *'UNMASKED'**,* *'BORDER'**,* *'ACTIVE'**,* *'SURFACE'**]**,* *(**optional**)*) –

          Mode

          + `ORIGIN`
            Origin – Sets the pivot to the origin of the sculpt.
          + `UNMASKED`
            Unmasked – Sets the pivot position to the average position of the unmasked vertices.
          + `BORDER`
            Mask Border – Sets the pivot position to the center of the border of the mask.
          + `ACTIVE`
            Active Vertex – Sets the pivot position to the active vertex position.
          + `SURFACE`
            Surface – Sets the pivot position to the surface under the cursor.
        * **mouse\_x** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Mouse Position X, Position of the mouse used for “Surface” mode
        * **mouse\_y** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Mouse Position Y, Position of the mouse used for “Surface” mode

bpy.ops.sculpt.symmetrize(*merge\_tolerance=0.0005*)[#](#bpy.ops.sculpt.symmetrize "Link to this definition")
:   Symmetrize the topology modifications

    Parameters:
    :   **merge\_tolerance** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Merge Distance, Distance within which symmetrical vertices are merged

bpy.ops.sculpt.trim\_box\_gesture(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *use\_front\_faces\_only=False*, *location=(0, 0)*, *trim\_mode='DIFFERENCE'*, *use\_cursor\_depth=False*, *trim\_orientation='VIEW'*, *trim\_extrude\_mode='FIXED'*, *trim\_solver='FAST'*)[#](#bpy.ops.sculpt.trim_box_gesture "Link to this definition")
:   Execute a boolean operation on the mesh and a rectangle defined by the cursor

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view
        * **location** (*int array* *of* *2 items in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Location, Mouse location
        * **trim\_mode** (*enum in* *[**'DIFFERENCE'**,* *'UNION'**,* *'JOIN'**]**,* *(**optional**)*) –

          Trim Mode

          + `DIFFERENCE`
            Difference – Use a difference boolean operation.
          + `UNION`
            Union – Use a union boolean operation.
          + `JOIN`
            Join – Join the new mesh as separate geometry, without performing any boolean operation.
        * **use\_cursor\_depth** (*boolean**,* *(**optional**)*) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        * **trim\_orientation** (*enum in* *[**'VIEW'**,* *'SURFACE'**]**,* *(**optional**)*) –

          Shape Orientation

          + `VIEW`
            View – Use the view to orientate the trimming shape.
          + `SURFACE`
            Surface – Use the surface normal to orientate the trimming shape.
        * **trim\_extrude\_mode** (*enum in* *[**'PROJECT'**,* *'FIXED'**]**,* *(**optional**)*) –

          Extrude Mode

          + `PROJECT`
            Project – Align trim geometry with the perspective of the current view for a tapered shape.
          + `FIXED`
            Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.
        * **trim\_solver** (*enum in* *[**'EXACT'**,* *'FAST'**]**,* *(**optional**)*) –

          Solver

          + `EXACT`
            Exact – Use the exact boolean solver.
          + `FAST`
            Fast – Use the fast float boolean solver.

bpy.ops.sculpt.trim\_lasso\_gesture(*path=None*, *use\_front\_faces\_only=False*, *location=(0, 0)*, *trim\_mode='DIFFERENCE'*, *use\_cursor\_depth=False*, *trim\_orientation='VIEW'*, *trim\_extrude\_mode='FIXED'*, *trim\_solver='FAST'*)[#](#bpy.ops.sculpt.trim_lasso_gesture "Link to this definition")
:   Execute a boolean operation on the mesh and a shape defined by the cursor

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view
        * **location** (*int array* *of* *2 items in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Location, Mouse location
        * **trim\_mode** (*enum in* *[**'DIFFERENCE'**,* *'UNION'**,* *'JOIN'**]**,* *(**optional**)*) –

          Trim Mode

          + `DIFFERENCE`
            Difference – Use a difference boolean operation.
          + `UNION`
            Union – Use a union boolean operation.
          + `JOIN`
            Join – Join the new mesh as separate geometry, without performing any boolean operation.
        * **use\_cursor\_depth** (*boolean**,* *(**optional**)*) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        * **trim\_orientation** (*enum in* *[**'VIEW'**,* *'SURFACE'**]**,* *(**optional**)*) –

          Shape Orientation

          + `VIEW`
            View – Use the view to orientate the trimming shape.
          + `SURFACE`
            Surface – Use the surface normal to orientate the trimming shape.
        * **trim\_extrude\_mode** (*enum in* *[**'PROJECT'**,* *'FIXED'**]**,* *(**optional**)*) –

          Extrude Mode

          + `PROJECT`
            Project – Align trim geometry with the perspective of the current view for a tapered shape.
          + `FIXED`
            Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.
        * **trim\_solver** (*enum in* *[**'EXACT'**,* *'FAST'**]**,* *(**optional**)*) –

          Solver

          + `EXACT`
            Exact – Use the exact boolean solver.
          + `FAST`
            Fast – Use the fast float boolean solver.

bpy.ops.sculpt.trim\_line\_gesture(*xstart=0*, *xend=0*, *ystart=0*, *yend=0*, *flip=False*, *cursor=5*, *use\_front\_faces\_only=False*, *use\_limit\_to\_segment=False*, *location=(0, 0)*, *trim\_mode='DIFFERENCE'*, *use\_cursor\_depth=False*, *trim\_orientation='VIEW'*, *trim\_extrude\_mode='FIXED'*, *trim\_solver='FAST'*)[#](#bpy.ops.sculpt.trim_line_gesture "Link to this definition")
:   Remove a portion of the mesh on one side of a line

    Parameters:
    :   * **xstart** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Start
        * **xend** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X End
        * **ystart** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Start
        * **yend** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y End
        * **flip** (*boolean**,* *(**optional**)*) – Flip
        * **cursor** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Cursor, Mouse cursor style to use during the modal operator
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view
        * **use\_limit\_to\_segment** (*boolean**,* *(**optional**)*) – Limit to Segment, Apply the gesture action only to the area that is contained within the segment without extending its effect to the entire line
        * **location** (*int array* *of* *2 items in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Location, Mouse location
        * **trim\_mode** (*enum in* *[**'DIFFERENCE'**,* *'UNION'**,* *'JOIN'**]**,* *(**optional**)*) –

          Trim Mode

          + `DIFFERENCE`
            Difference – Use a difference boolean operation.
          + `UNION`
            Union – Use a union boolean operation.
          + `JOIN`
            Join – Join the new mesh as separate geometry, without performing any boolean operation.
        * **use\_cursor\_depth** (*boolean**,* *(**optional**)*) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        * **trim\_orientation** (*enum in* *[**'VIEW'**,* *'SURFACE'**]**,* *(**optional**)*) –

          Shape Orientation

          + `VIEW`
            View – Use the view to orientate the trimming shape.
          + `SURFACE`
            Surface – Use the surface normal to orientate the trimming shape.
        * **trim\_extrude\_mode** (*enum in* *[**'PROJECT'**,* *'FIXED'**]**,* *(**optional**)*) –

          Extrude Mode

          + `PROJECT`
            Project – Align trim geometry with the perspective of the current view for a tapered shape.
          + `FIXED`
            Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.
        * **trim\_solver** (*enum in* *[**'EXACT'**,* *'FAST'**]**,* *(**optional**)*) –

          Solver

          + `EXACT`
            Exact – Use the exact boolean solver.
          + `FAST`
            Fast – Use the fast float boolean solver.

bpy.ops.sculpt.trim\_polyline\_gesture(*path=None*, *use\_front\_faces\_only=False*, *location=(0, 0)*, *trim\_mode='DIFFERENCE'*, *use\_cursor\_depth=False*, *trim\_orientation='VIEW'*, *trim\_extrude\_mode='FIXED'*, *trim\_solver='FAST'*)[#](#bpy.ops.sculpt.trim_polyline_gesture "Link to this definition")
:   Execute a boolean operation on the mesh and a polygonal shape defined by the cursor

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **use\_front\_faces\_only** (*boolean**,* *(**optional**)*) – Front Faces Only, Affect only faces facing towards the view
        * **location** (*int array* *of* *2 items in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Location, Mouse location
        * **trim\_mode** (*enum in* *[**'DIFFERENCE'**,* *'UNION'**,* *'JOIN'**]**,* *(**optional**)*) –

          Trim Mode

          + `DIFFERENCE`
            Difference – Use a difference boolean operation.
          + `UNION`
            Union – Use a union boolean operation.
          + `JOIN`
            Join – Join the new mesh as separate geometry, without performing any boolean operation.
        * **use\_cursor\_depth** (*boolean**,* *(**optional**)*) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape
        * **trim\_orientation** (*enum in* *[**'VIEW'**,* *'SURFACE'**]**,* *(**optional**)*) –

          Shape Orientation

          + `VIEW`
            View – Use the view to orientate the trimming shape.
          + `SURFACE`
            Surface – Use the surface normal to orientate the trimming shape.
        * **trim\_extrude\_mode** (*enum in* *[**'PROJECT'**,* *'FIXED'**]**,* *(**optional**)*) –

          Extrude Mode

          + `PROJECT`
            Project – Align trim geometry with the perspective of the current view for a tapered shape.
          + `FIXED`
            Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.
        * **trim\_solver** (*enum in* *[**'EXACT'**,* *'FAST'**]**,* *(**optional**)*) –

          Solver

          + `EXACT`
            Exact – Use the exact boolean solver.
          + `FAST`
            Fast – Use the fast float boolean solver.

bpy.ops.sculpt.uv\_sculpt\_grab(*use\_invert=False*)[#](#bpy.ops.sculpt.uv_sculpt_grab "Link to this definition")
:   Grab UVs

    Parameters:
    :   **use\_invert** (*boolean**,* *(**optional**)*) – Invert, Invert action for the duration of the stroke

bpy.ops.sculpt.uv\_sculpt\_pinch(*use\_invert=False*)[#](#bpy.ops.sculpt.uv_sculpt_pinch "Link to this definition")
:   Pinch UVs

    Parameters:
    :   **use\_invert** (*boolean**,* *(**optional**)*) – Invert, Invert action for the duration of the stroke

bpy.ops.sculpt.uv\_sculpt\_relax(*use\_invert=False*, *relax\_method='COTAN'*)[#](#bpy.ops.sculpt.uv_sculpt_relax "Link to this definition")
:   Relax UVs

    Parameters:
    :   * **use\_invert** (*boolean**,* *(**optional**)*) – Invert, Invert action for the duration of the stroke
        * **relax\_method** (*enum in* *[**'LAPLACIAN'**,* *'HC'**,* *'COTAN'**]**,* *(**optional**)*) –

          Relax Method, Algorithm used for UV relaxation

          + `LAPLACIAN`
            Laplacian – Use Laplacian method for relaxation.
          + `HC`
            HC – Use HC method for relaxation.
          + `COTAN`
            Geometry – Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.

[Next

Sculpt Curves Operators](sculpt_curves.md)
[Previous

Script Operators](script.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.sculpt.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.sculpt.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Sculpt Operators
  + [`brush_stroke()`](#bpy.ops.sculpt.brush_stroke)
  + [`cloth_filter()`](#bpy.ops.sculpt.cloth_filter)
  + [`color_filter()`](#bpy.ops.sculpt.color_filter)
  + [`detail_flood_fill()`](#bpy.ops.sculpt.detail_flood_fill)
  + [`dynamic_topology_toggle()`](#bpy.ops.sculpt.dynamic_topology_toggle)
  + [`dyntopo_detail_size_edit()`](#bpy.ops.sculpt.dyntopo_detail_size_edit)
  + [`expand()`](#bpy.ops.sculpt.expand)
  + [`face_set_box_gesture()`](#bpy.ops.sculpt.face_set_box_gesture)
  + [`face_set_change_visibility()`](#bpy.ops.sculpt.face_set_change_visibility)
  + [`face_set_edit()`](#bpy.ops.sculpt.face_set_edit)
  + [`face_set_lasso_gesture()`](#bpy.ops.sculpt.face_set_lasso_gesture)
  + [`face_set_line_gesture()`](#bpy.ops.sculpt.face_set_line_gesture)
  + [`face_set_polyline_gesture()`](#bpy.ops.sculpt.face_set_polyline_gesture)
  + [`face_sets_create()`](#bpy.ops.sculpt.face_sets_create)
  + [`face_sets_init()`](#bpy.ops.sculpt.face_sets_init)
  + [`face_sets_randomize_colors()`](#bpy.ops.sculpt.face_sets_randomize_colors)
  + [`mask_by_color()`](#bpy.ops.sculpt.mask_by_color)
  + [`mask_filter()`](#bpy.ops.sculpt.mask_filter)
  + [`mask_from_cavity()`](#bpy.ops.sculpt.mask_from_cavity)
  + [`mask_init()`](#bpy.ops.sculpt.mask_init)
  + [`mesh_filter()`](#bpy.ops.sculpt.mesh_filter)
  + [`optimize()`](#bpy.ops.sculpt.optimize)
  + [`project_line_gesture()`](#bpy.ops.sculpt.project_line_gesture)
  + [`sample_color()`](#bpy.ops.sculpt.sample_color)
  + [`sample_detail_size()`](#bpy.ops.sculpt.sample_detail_size)
  + [`sculptmode_toggle()`](#bpy.ops.sculpt.sculptmode_toggle)
  + [`set_persistent_base()`](#bpy.ops.sculpt.set_persistent_base)
  + [`set_pivot_position()`](#bpy.ops.sculpt.set_pivot_position)
  + [`symmetrize()`](#bpy.ops.sculpt.symmetrize)
  + [`trim_box_gesture()`](#bpy.ops.sculpt.trim_box_gesture)
  + [`trim_lasso_gesture()`](#bpy.ops.sculpt.trim_lasso_gesture)
  + [`trim_line_gesture()`](#bpy.ops.sculpt.trim_line_gesture)
  + [`trim_polyline_gesture()`](#bpy.ops.sculpt.trim_polyline_gesture)
  + [`uv_sculpt_grab()`](#bpy.ops.sculpt.uv_sculpt_grab)
  + [`uv_sculpt_pinch()`](#bpy.ops.sculpt.uv_sculpt_pinch)
  + [`uv_sculpt_relax()`](#bpy.ops.sculpt.uv_sculpt_relax)