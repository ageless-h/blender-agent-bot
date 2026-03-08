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
* [Types (bpy.types)](index.md)[x]
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

# Brush(ID)[#](#brush-id "Link to this heading")

base classes — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct"), [`ID`](ID.md#bpy.types.ID "bpy.types.ID")

*class* bpy.types.Brush(*ID*)[#](#bpy.types.Brush "Link to this definition")
:   Brush data-block for storing brush settings for painting and sculpting

    area\_radius\_factor[#](#bpy.types.Brush.area_radius_factor "Link to this definition")
    :   Ratio between the brush radius and the radius that is going to be used to sample the area center

        Type:
        :   float in [0, 2], default 0.5

    auto\_smooth\_factor[#](#bpy.types.Brush.auto_smooth_factor "Link to this definition")
    :   Amount of smoothing to automatically apply to each stroke

        Type:
        :   float in [0, 1], default 0.0

    automasking\_boundary\_edges\_propagation\_steps[#](#bpy.types.Brush.automasking_boundary_edges_propagation_steps "Link to this definition")
    :   Distance where boundary edge automasking is going to protect vertices from the fully masked edge

        Type:
        :   int in [1, 20], default 1

    automasking\_cavity\_blur\_steps[#](#bpy.types.Brush.automasking_cavity_blur_steps "Link to this definition")
    :   The number of times the cavity mask is blurred

        Type:
        :   int in [0, 25], default 0

    automasking\_cavity\_curve[#](#bpy.types.Brush.automasking_cavity_curve "Link to this definition")
    :   Curve used for the sensitivity

        Type:
        :   [`CurveMapping`](CurveMapping.md#bpy.types.CurveMapping "bpy.types.CurveMapping"), (readonly)

    automasking\_cavity\_factor[#](#bpy.types.Brush.automasking_cavity_factor "Link to this definition")
    :   The contrast of the cavity mask

        Type:
        :   float in [0, 5], default 1.0

    automasking\_start\_normal\_falloff[#](#bpy.types.Brush.automasking_start_normal_falloff "Link to this definition")
    :   Extend the angular range with a falloff gradient

        Type:
        :   float in [0.0001, 1], default 0.25

    automasking\_start\_normal\_limit[#](#bpy.types.Brush.automasking_start_normal_limit "Link to this definition")
    :   The range of angles that will be affected

        Type:
        :   float in [0.0001, 3.14159], default 0.349066

    automasking\_view\_normal\_falloff[#](#bpy.types.Brush.automasking_view_normal_falloff "Link to this definition")
    :   Extend the angular range with a falloff gradient

        Type:
        :   float in [0.0001, 1], default 0.25

    automasking\_view\_normal\_limit[#](#bpy.types.Brush.automasking_view_normal_limit "Link to this definition")
    :   The range of angles that will be affected

        Type:
        :   float in [0.0001, 3.14159], default 1.5708

    blend[#](#bpy.types.Brush.blend "Link to this definition")
    :   Brush blending mode

        * `MIX`
          Mix – Use Mix blending mode while painting.
        * `DARKEN`
          Darken – Use Darken blending mode while painting.
        * `MUL`
          Multiply – Use Multiply blending mode while painting.
        * `COLORBURN`
          Color Burn – Use Color Burn blending mode while painting.
        * `LINEARBURN`
          Linear Burn – Use Linear Burn blending mode while painting.
        * `LIGHTEN`
          Lighten – Use Lighten blending mode while painting.
        * `SCREEN`
          Screen – Use Screen blending mode while painting.
        * `COLORDODGE`
          Color Dodge – Use Color Dodge blending mode while painting.
        * `ADD`
          Add – Use Add blending mode while painting.
        * `OVERLAY`
          Overlay – Use Overlay blending mode while painting.
        * `SOFTLIGHT`
          Soft Light – Use Soft Light blending mode while painting.
        * `HARDLIGHT`
          Hard Light – Use Hard Light blending mode while painting.
        * `VIVIDLIGHT`
          Vivid Light – Use Vivid Light blending mode while painting.
        * `LINEARLIGHT`
          Linear Light – Use Linear Light blending mode while painting.
        * `PINLIGHT`
          Pin Light – Use Pin Light blending mode while painting.
        * `DIFFERENCE`
          Difference – Use Difference blending mode while painting.
        * `EXCLUSION`
          Exclusion – Use Exclusion blending mode while painting.
        * `SUB`
          Subtract – Use Subtract blending mode while painting.
        * `HUE`
          Hue – Use Hue blending mode while painting.
        * `SATURATION`
          Saturation – Use Saturation blending mode while painting.
        * `COLOR`
          Color – Use Color blending mode while painting.
        * `LUMINOSITY`
          Value – Use Value blending mode while painting.
        * `ERASE_ALPHA`
          Erase Alpha – Erase alpha while painting.
        * `ADD_ALPHA`
          Add Alpha – Add alpha while painting.

        Type:
        :   enum in [‘MIX’, ‘DARKEN’, ‘MUL’, ‘COLORBURN’, ‘LINEARBURN’, ‘LIGHTEN’, ‘SCREEN’, ‘COLORDODGE’, ‘ADD’, ‘OVERLAY’, ‘SOFTLIGHT’, ‘HARDLIGHT’, ‘VIVIDLIGHT’, ‘LINEARLIGHT’, ‘PINLIGHT’, ‘DIFFERENCE’, ‘EXCLUSION’, ‘SUB’, ‘HUE’, ‘SATURATION’, ‘COLOR’, ‘LUMINOSITY’, ‘ERASE\_ALPHA’, ‘ADD\_ALPHA’], default ‘MIX’

    blur\_kernel\_radius[#](#bpy.types.Brush.blur_kernel_radius "Link to this definition")
    :   Radius of kernel used for soften and sharpen in pixels

        Type:
        :   int in [1, 10000], default 2

    blur\_mode[#](#bpy.types.Brush.blur_mode "Link to this definition")
    :   Type:
        :   enum in [‘BOX’, ‘GAUSSIAN’], default ‘GAUSSIAN’

    boundary\_deform\_type[#](#bpy.types.Brush.boundary_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        Type:
        :   enum in [‘BEND’, ‘EXPAND’, ‘INFLATE’, ‘GRAB’, ‘TWIST’, ‘SMOOTH’], default ‘BEND’

    boundary\_falloff\_type[#](#bpy.types.Brush.boundary_falloff_type "Link to this definition")
    :   How the brush falloff is applied across the boundary

        * `CONSTANT`
          Constant – Applies the same deformation in the entire boundary.
        * `RADIUS`
          Brush Radius – Applies the deformation in a localized area limited by the brush radius.
        * `LOOP`
          Loop – Applies the brush falloff in a loop pattern.
        * `LOOP_INVERT`
          Loop and Invert – Applies the falloff radius in a loop pattern, inverting the displacement direction in each pattern repetition.

        Type:
        :   enum in [‘CONSTANT’, ‘RADIUS’, ‘LOOP’, ‘LOOP\_INVERT’], default ‘CONSTANT’

    boundary\_offset[#](#bpy.types.Brush.boundary_offset "Link to this definition")
    :   Offset of the boundary origin in relation to the brush radius

        Type:
        :   float in [0, 30], default 0.0

    brush\_capabilities[#](#bpy.types.Brush.brush_capabilities "Link to this definition")
    :   Brush’s capabilities

        Type:
        :   [`BrushCapabilities`](BrushCapabilities.md#bpy.types.BrushCapabilities "bpy.types.BrushCapabilities"), (readonly, never None)

    clone\_alpha[#](#bpy.types.Brush.clone_alpha "Link to this definition")
    :   Opacity of clone image display

        Type:
        :   float in [0, 1], default 0.5

    clone\_image[#](#bpy.types.Brush.clone_image "Link to this definition")
    :   Image for clone tool

        Type:
        :   [`Image`](Image.md#bpy.types.Image "bpy.types.Image")

    clone\_offset[#](#bpy.types.Brush.clone_offset "Link to this definition")
    :   Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], default (0.0, 0.0)

    cloth\_constraint\_softbody\_strength[#](#bpy.types.Brush.cloth_constraint_softbody_strength "Link to this definition")
    :   How much the cloth preserves the original shape, acting as a soft body

        Type:
        :   float in [0, 1], default 0.0

    cloth\_damping[#](#bpy.types.Brush.cloth_damping "Link to this definition")
    :   How much the applied forces are propagated through the cloth

        Type:
        :   float in [0.01, 1], default 0.01

    cloth\_deform\_type[#](#bpy.types.Brush.cloth_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        Type:
        :   enum in [‘DRAG’, ‘PUSH’, ‘PINCH\_POINT’, ‘PINCH\_PERPENDICULAR’, ‘INFLATE’, ‘GRAB’, ‘EXPAND’, ‘SNAKE\_HOOK’], default ‘DRAG’

    cloth\_force\_falloff\_type[#](#bpy.types.Brush.cloth_force_falloff_type "Link to this definition")
    :   Shape used in the brush to apply force to the cloth

        Type:
        :   enum in [‘RADIAL’, ‘PLANE’], default ‘RADIAL’

    cloth\_mass[#](#bpy.types.Brush.cloth_mass "Link to this definition")
    :   Mass of each simulation particle

        Type:
        :   float in [0.01, 2], default 1.0

    cloth\_sim\_falloff[#](#bpy.types.Brush.cloth_sim_falloff "Link to this definition")
    :   Area to apply deformation falloff to the effects of the simulation

        Type:
        :   float in [0, 1], default 0.75

    cloth\_sim\_limit[#](#bpy.types.Brush.cloth_sim_limit "Link to this definition")
    :   Factor added relative to the size of the radius to limit the cloth simulation effects

        Type:
        :   float in [0.1, 10], default 2.5

    cloth\_simulation\_area\_type[#](#bpy.types.Brush.cloth_simulation_area_type "Link to this definition")
    :   Part of the mesh that is going to be simulated when the stroke is active

        * `LOCAL`
          Local – Simulates only a specific area around the brush limited by a fixed radius.
        * `GLOBAL`
          Global – Simulates the entire mesh.
        * `DYNAMIC`
          Dynamic – The active simulation area moves with the brush.

        Type:
        :   enum in [‘LOCAL’, ‘GLOBAL’, ‘DYNAMIC’], default ‘LOCAL’

    color[#](#bpy.types.Brush.color "Link to this definition")
    :   Type:
        :   [`mathutils.Color`](../../mathutils/index.md#mathutils.Color "mathutils.Color") of 3 items in [0, 1], default (1.0, 1.0, 1.0)

    color\_type[#](#bpy.types.Brush.color_type "Link to this definition")
    :   Use single color or gradient when painting

        * `COLOR`
          Color – Paint with a single color.
        * `GRADIENT`
          Gradient – Paint with a gradient.

        Type:
        :   enum in [‘COLOR’, ‘GRADIENT’], default ‘COLOR’

    crease\_pinch\_factor[#](#bpy.types.Brush.crease_pinch_factor "Link to this definition")
    :   How much the crease brush pinches

        Type:
        :   float in [0, 1], default 0.5

    cursor\_color\_add[#](#bpy.types.Brush.cursor_color_add "Link to this definition")
    :   Color of cursor when adding

        Type:
        :   float array of 4 items in [0, inf], default (1.0, 0.39, 0.39, 0.9)

    cursor\_color\_subtract[#](#bpy.types.Brush.cursor_color_subtract "Link to this definition")
    :   Color of cursor when subtracting

        Type:
        :   float array of 4 items in [0, inf], default (0.39, 0.39, 1.0, 0.9)

    cursor\_overlay\_alpha[#](#bpy.types.Brush.cursor_overlay_alpha "Link to this definition")
    :   Type:
        :   int in [0, 100], default 33

    curve[#](#bpy.types.Brush.curve "Link to this definition")
    :   Editable falloff curve

        Type:
        :   [`CurveMapping`](CurveMapping.md#bpy.types.CurveMapping "bpy.types.CurveMapping"), (readonly, never None)

    curve\_preset[#](#bpy.types.Brush.curve_preset "Link to this definition")
    :   Type:
        :   enum in [Brush Curve Preset Items](../../../appendix/bpy_types_enum_items/brush_curve_preset_items.md#rna-enum-brush-curve-preset-items), default ‘CUSTOM’

    curves\_sculpt\_settings[#](#bpy.types.Brush.curves_sculpt_settings "Link to this definition")
    :   Type:
        :   [`BrushCurvesSculptSettings`](BrushCurvesSculptSettings.md#bpy.types.BrushCurvesSculptSettings "bpy.types.BrushCurvesSculptSettings"), (readonly)

    curves\_sculpt\_tool[#](#bpy.types.Brush.curves_sculpt_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Curves Sculpt Tool Items](../../../appendix/bpy_types_enum_items/brush_curves_sculpt_tool_items.md#rna-enum-brush-curves-sculpt-tool-items), default ‘COMB’

    dash\_ratio[#](#bpy.types.Brush.dash_ratio "Link to this definition")
    :   Ratio of samples in a cycle that the brush is enabled

        Type:
        :   float in [0, 1], default 1.0

    dash\_samples[#](#bpy.types.Brush.dash_samples "Link to this definition")
    :   Length of a dash cycle measured in stroke samples

        Type:
        :   int in [1, 10000], default 20

    deform\_target[#](#bpy.types.Brush.deform_target "Link to this definition")
    :   How the deformation of the brush will affect the object

        * `GEOMETRY`
          Geometry – Brush deformation displaces the vertices of the mesh.
        * `CLOTH_SIM`
          Cloth Simulation – Brush deforms the mesh by deforming the constraints of a cloth simulation.

        Type:
        :   enum in [‘GEOMETRY’, ‘CLOTH\_SIM’], default ‘GEOMETRY’

    density[#](#bpy.types.Brush.density "Link to this definition")
    :   Amount of random elements that are going to be affected by the brush

        Type:
        :   float in [0, 1], default 0.0

    direction[#](#bpy.types.Brush.direction "Link to this definition")
    :   * `ADD`
          Add – Add effect of brush.
        * `SUBTRACT`
          Subtract – Subtract effect of brush.

        Type:
        :   enum in [‘ADD’, ‘SUBTRACT’], default ‘ADD’

    disconnected\_distance\_max[#](#bpy.types.Brush.disconnected_distance_max "Link to this definition")
    :   Maximum distance to search for disconnected loose parts in the mesh

        Type:
        :   float in [0, 10], default 0.1

    elastic\_deform\_type[#](#bpy.types.Brush.elastic_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        Type:
        :   enum in [‘GRAB’, ‘GRAB\_BISCALE’, ‘GRAB\_TRISCALE’, ‘SCALE’, ‘TWIST’], default ‘GRAB’

    elastic\_deform\_volume\_preservation[#](#bpy.types.Brush.elastic_deform_volume_preservation "Link to this definition")
    :   Poisson ratio for elastic deformation. Higher values preserve volume more, but also lead to more bulging

        Type:
        :   float in [0, 0.9], default 0.0

    falloff\_angle[#](#bpy.types.Brush.falloff_angle "Link to this definition")
    :   Paint most on faces pointing towards the view according to this angle

        Type:
        :   float in [0, 1.5708], default 0.0

    falloff\_shape[#](#bpy.types.Brush.falloff_shape "Link to this definition")
    :   Use projected or spherical falloff

        * `SPHERE`
          Sphere – Apply brush influence in a Sphere, outwards from the center.
        * `PROJECTED`
          Projected – Apply brush influence in a 2D circle, projected from the view.

        Type:
        :   enum in [‘SPHERE’, ‘PROJECTED’], default ‘SPHERE’

    fill\_threshold[#](#bpy.types.Brush.fill_threshold "Link to this definition")
    :   Threshold above which filling is not propagated

        Type:
        :   float in [0, 100], default 0.2

    flow[#](#bpy.types.Brush.flow "Link to this definition")
    :   Amount of paint that is applied per stroke sample

        Type:
        :   float in [0, 1], default 0.0

    gpencil\_sculpt\_tool[#](#bpy.types.Brush.gpencil_sculpt_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Gpencil Sculpt Types Items](../../../appendix/bpy_types_enum_items/brush_gpencil_sculpt_types_items.md#rna-enum-brush-gpencil-sculpt-types-items), default ‘SMOOTH’

    gpencil\_settings[#](#bpy.types.Brush.gpencil_settings "Link to this definition")
    :   Type:
        :   [`BrushGpencilSettings`](BrushGpencilSettings.md#bpy.types.BrushGpencilSettings "bpy.types.BrushGpencilSettings"), (readonly)

    gpencil\_tool[#](#bpy.types.Brush.gpencil_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Gpencil Types Items](../../../appendix/bpy_types_enum_items/brush_gpencil_types_items.md#rna-enum-brush-gpencil-types-items), default ‘DRAW’

    gpencil\_vertex\_tool[#](#bpy.types.Brush.gpencil_vertex_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Gpencil Vertex Types Items](../../../appendix/bpy_types_enum_items/brush_gpencil_vertex_types_items.md#rna-enum-brush-gpencil-vertex-types-items), default ‘DRAW’

    gpencil\_weight\_tool[#](#bpy.types.Brush.gpencil_weight_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Gpencil Weight Types Items](../../../appendix/bpy_types_enum_items/brush_gpencil_weight_types_items.md#rna-enum-brush-gpencil-weight-types-items), default ‘WEIGHT’

    grad\_spacing[#](#bpy.types.Brush.grad_spacing "Link to this definition")
    :   Spacing before brush gradient goes full circle

        Type:
        :   int in [1, 10000], default 0

    gradient[#](#bpy.types.Brush.gradient "Link to this definition")
    :   Type:
        :   [`ColorRamp`](ColorRamp.md#bpy.types.ColorRamp "bpy.types.ColorRamp"), (readonly)

    gradient\_fill\_mode[#](#bpy.types.Brush.gradient_fill_mode "Link to this definition")
    :   Type:
        :   enum in [‘LINEAR’, ‘RADIAL’], default ‘LINEAR’

    gradient\_stroke\_mode[#](#bpy.types.Brush.gradient_stroke_mode "Link to this definition")
    :   Type:
        :   enum in [‘PRESSURE’, ‘SPACING\_REPEAT’, ‘SPACING\_CLAMP’], default ‘PRESSURE’

    hardness[#](#bpy.types.Brush.hardness "Link to this definition")
    :   How close the brush falloff starts from the edge of the brush

        Type:
        :   float in [0, 1], default 0.0

    height[#](#bpy.types.Brush.height "Link to this definition")
    :   Affectable height of brush (i.e. the layer height for the layer tool)

        Type:
        :   float in [0, 1], default 0.5

    icon\_filepath[#](#bpy.types.Brush.icon_filepath "Link to this definition")
    :   File path to brush icon

        Type:
        :   string, default “”, (never None)

    image\_paint\_capabilities[#](#bpy.types.Brush.image_paint_capabilities "Link to this definition")
    :   Type:
        :   [`BrushCapabilitiesImagePaint`](BrushCapabilitiesImagePaint.md#bpy.types.BrushCapabilitiesImagePaint "bpy.types.BrushCapabilitiesImagePaint"), (readonly, never None)

    image\_tool[#](#bpy.types.Brush.image_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Image Tool Items](../../../appendix/bpy_types_enum_items/brush_image_tool_items.md#rna-enum-brush-image-tool-items), default ‘DRAW’

    input\_samples[#](#bpy.types.Brush.input_samples "Link to this definition")
    :   Number of input samples to average together to smooth the brush stroke

        Type:
        :   int in [1, 64], default 1

    invert\_density\_pressure[#](#bpy.types.Brush.invert_density_pressure "Link to this definition")
    :   Invert the modulation of pressure in density

        Type:
        :   boolean, default False

    invert\_flow\_pressure[#](#bpy.types.Brush.invert_flow_pressure "Link to this definition")
    :   Invert the modulation of pressure in flow

        Type:
        :   boolean, default False

    invert\_hardness\_pressure[#](#bpy.types.Brush.invert_hardness_pressure "Link to this definition")
    :   Invert the modulation of pressure in hardness

        Type:
        :   boolean, default False

    invert\_to\_scrape\_fill[#](#bpy.types.Brush.invert_to_scrape_fill "Link to this definition")
    :   Use Scrape or Fill tool when inverting this brush instead of inverting its displacement direction

        Type:
        :   boolean, default False

    invert\_wet\_mix\_pressure[#](#bpy.types.Brush.invert_wet_mix_pressure "Link to this definition")
    :   Invert the modulation of pressure in wet mix

        Type:
        :   boolean, default False

    invert\_wet\_persistence\_pressure[#](#bpy.types.Brush.invert_wet_persistence_pressure "Link to this definition")
    :   Invert the modulation of pressure in wet persistence

        Type:
        :   boolean, default False

    jitter[#](#bpy.types.Brush.jitter "Link to this definition")
    :   Jitter the position of the brush while painting

        Type:
        :   float in [0, 1000], default 0.0

    jitter\_absolute[#](#bpy.types.Brush.jitter_absolute "Link to this definition")
    :   Jitter the position of the brush in pixels while painting

        Type:
        :   int in [0, 1000000], default 0

    jitter\_unit[#](#bpy.types.Brush.jitter_unit "Link to this definition")
    :   Jitter in screen space or relative to brush size

        * `VIEW`
          View – Jittering happens in screen space, in pixels.
        * `BRUSH`
          Brush – Jittering happens relative to the brush size.

        Type:
        :   enum in [‘VIEW’, ‘BRUSH’], default ‘BRUSH’

    mask\_overlay\_alpha[#](#bpy.types.Brush.mask_overlay_alpha "Link to this definition")
    :   Type:
        :   int in [0, 100], default 33

    mask\_stencil\_dimension[#](#bpy.types.Brush.mask_stencil_dimension "Link to this definition")
    :   Dimensions of mask stencil in viewport

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], default (0.0, 0.0)

    mask\_stencil\_pos[#](#bpy.types.Brush.mask_stencil_pos "Link to this definition")
    :   Position of mask stencil in viewport

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], default (0.0, 0.0)

    mask\_texture[#](#bpy.types.Brush.mask_texture "Link to this definition")
    :   Type:
        :   [`Texture`](Texture.md#bpy.types.Texture "bpy.types.Texture")

    mask\_texture\_slot[#](#bpy.types.Brush.mask_texture_slot "Link to this definition")
    :   Type:
        :   [`BrushTextureSlot`](BrushTextureSlot.md#bpy.types.BrushTextureSlot "bpy.types.BrushTextureSlot"), (readonly)

    mask\_tool[#](#bpy.types.Brush.mask_tool "Link to this definition")
    :   Type:
        :   enum in [‘DRAW’, ‘SMOOTH’], default ‘DRAW’

    multiplane\_scrape\_angle[#](#bpy.types.Brush.multiplane_scrape_angle "Link to this definition")
    :   Angle between the planes of the crease

        Type:
        :   float in [0, 160], default 0.0

    normal\_radius\_factor[#](#bpy.types.Brush.normal_radius_factor "Link to this definition")
    :   Ratio between the brush radius and the radius that is going to be used to sample the normal

        Type:
        :   float in [0, 2], default 0.5

    normal\_weight[#](#bpy.types.Brush.normal_weight "Link to this definition")
    :   How much grab will pull vertices out of surface during a grab

        Type:
        :   float in [0, 1], default 0.0

    paint\_curve[#](#bpy.types.Brush.paint_curve "Link to this definition")
    :   Active paint curve

        Type:
        :   [`PaintCurve`](PaintCurve.md#bpy.types.PaintCurve "bpy.types.PaintCurve")

    plane\_offset[#](#bpy.types.Brush.plane_offset "Link to this definition")
    :   Adjust plane on which the brush acts towards or away from the object surface

        Type:
        :   float in [-2, 2], default 0.0

    plane\_trim[#](#bpy.types.Brush.plane_trim "Link to this definition")
    :   If a vertex is further away from offset plane than this, then it is not affected

        Type:
        :   float in [0, 1], default 0.5

    pose\_deform\_type[#](#bpy.types.Brush.pose_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        Type:
        :   enum in [‘ROTATE\_TWIST’, ‘SCALE\_TRANSLATE’, ‘SQUASH\_STRETCH’], default ‘ROTATE\_TWIST’

    pose\_ik\_segments[#](#bpy.types.Brush.pose_ik_segments "Link to this definition")
    :   Number of segments of the inverse kinematics chain that will deform the mesh

        Type:
        :   int in [1, 20], default 1

    pose\_offset[#](#bpy.types.Brush.pose_offset "Link to this definition")
    :   Offset of the pose origin in relation to the brush radius

        Type:
        :   float in [0, 2], default 0.0

    pose\_origin\_type[#](#bpy.types.Brush.pose_origin_type "Link to this definition")
    :   Method to set the rotation origins for the segments of the brush

        * `TOPOLOGY`
          Topology – Sets the rotation origin automatically using the topology and shape of the mesh as a guide.
        * `FACE_SETS`
          Face Sets – Creates a pose segment per face sets, starting from the active face set.
        * `FACE_SETS_FK`
          Face Sets FK – Simulates an FK deformation using the Face Set under the cursor as control.

        Type:
        :   enum in [‘TOPOLOGY’, ‘FACE\_SETS’, ‘FACE\_SETS\_FK’], default ‘TOPOLOGY’

    pose\_smooth\_iterations[#](#bpy.types.Brush.pose_smooth_iterations "Link to this definition")
    :   Smooth iterations applied after calculating the pose factor of each vertex

        Type:
        :   int in [0, 100], default 4

    rake\_factor[#](#bpy.types.Brush.rake_factor "Link to this definition")
    :   How much grab will follow cursor rotation

        Type:
        :   float in [0, 10], default 0.0

    rate[#](#bpy.types.Brush.rate "Link to this definition")
    :   Interval between paints for Airbrush

        Type:
        :   float in [0.0001, 10000], default 0.1

    sculpt\_capabilities[#](#bpy.types.Brush.sculpt_capabilities "Link to this definition")
    :   Type:
        :   [`BrushCapabilitiesSculpt`](BrushCapabilitiesSculpt.md#bpy.types.BrushCapabilitiesSculpt "bpy.types.BrushCapabilitiesSculpt"), (readonly, never None)

    sculpt\_plane[#](#bpy.types.Brush.sculpt_plane "Link to this definition")
    :   Type:
        :   enum in [‘AREA’, ‘VIEW’, ‘X’, ‘Y’, ‘Z’], default ‘AREA’

    sculpt\_tool[#](#bpy.types.Brush.sculpt_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Sculpt Tool Items](../../../appendix/bpy_types_enum_items/brush_sculpt_tool_items.md#rna-enum-brush-sculpt-tool-items), default ‘DRAW’

    secondary\_color[#](#bpy.types.Brush.secondary_color "Link to this definition")
    :   Type:
        :   [`mathutils.Color`](../../mathutils/index.md#mathutils.Color "mathutils.Color") of 3 items in [0, 1], default (0.0, 0.0, 0.0)

    sharp\_threshold[#](#bpy.types.Brush.sharp_threshold "Link to this definition")
    :   Threshold below which, no sharpening is done

        Type:
        :   float in [0, 100], default 0.0

    show\_multiplane\_scrape\_planes\_preview[#](#bpy.types.Brush.show_multiplane_scrape_planes_preview "Link to this definition")
    :   Preview the scrape planes in the cursor during the stroke

        Type:
        :   boolean, default False

    size[#](#bpy.types.Brush.size "Link to this definition")
    :   Radius of the brush in pixels

        Type:
        :   int in [1, 5000], default 35

    slide\_deform\_type[#](#bpy.types.Brush.slide_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        Type:
        :   enum in [‘DRAG’, ‘PINCH’, ‘EXPAND’], default ‘DRAG’

    smear\_deform\_type[#](#bpy.types.Brush.smear_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        Type:
        :   enum in [‘DRAG’, ‘PINCH’, ‘EXPAND’], default ‘DRAG’

    smooth\_deform\_type[#](#bpy.types.Brush.smooth_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        * `LAPLACIAN`
          Laplacian – Smooths the surface and the volume.
        * `SURFACE`
          Surface – Smooths the surface of the mesh, preserving the volume.

        Type:
        :   enum in [‘LAPLACIAN’, ‘SURFACE’], default ‘LAPLACIAN’

    smooth\_stroke\_factor[#](#bpy.types.Brush.smooth_stroke_factor "Link to this definition")
    :   Higher values give a smoother stroke

        Type:
        :   float in [0.5, 0.99], default 0.9

    smooth\_stroke\_radius[#](#bpy.types.Brush.smooth_stroke_radius "Link to this definition")
    :   Minimum distance from last point before stroke continues

        Type:
        :   int in [10, 200], default 75

    snake\_hook\_deform\_type[#](#bpy.types.Brush.snake_hook_deform_type "Link to this definition")
    :   Deformation type that is used in the brush

        * `FALLOFF`
          Radius Falloff – Applies the brush falloff in the tip of the brush.
        * `ELASTIC`
          Elastic – Modifies the entire mesh using elastic deform.

        Type:
        :   enum in [‘FALLOFF’, ‘ELASTIC’], default ‘FALLOFF’

    spacing[#](#bpy.types.Brush.spacing "Link to this definition")
    :   Spacing between brush daubs as a percentage of brush diameter

        Type:
        :   int in [1, 1000], default 10

    stencil\_dimension[#](#bpy.types.Brush.stencil_dimension "Link to this definition")
    :   Dimensions of stencil in viewport

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], default (256.0, 256.0)

    stencil\_pos[#](#bpy.types.Brush.stencil_pos "Link to this definition")
    :   Position of stencil in viewport

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], default (256.0, 256.0)

    strength[#](#bpy.types.Brush.strength "Link to this definition")
    :   How powerful the effect of the brush is when applied

        Type:
        :   float in [0, 10], default 1.0

    stroke\_method[#](#bpy.types.Brush.stroke_method "Link to this definition")
    :   * `DOTS`
          Dots – Apply paint on each mouse move step.
        * `DRAG_DOT`
          Drag Dot – Allows a single dot to be carefully positioned.
        * `SPACE`
          Space – Limit brush application to the distance specified by spacing.
        * `AIRBRUSH`
          Airbrush – Keep applying paint effect while holding mouse (spray).
        * `ANCHORED`
          Anchored – Keep the brush anchored to the initial location.
        * `LINE`
          Line – Draw a line with dabs separated according to spacing.
        * `CURVE`
          Curve – Define the stroke curve with a Bézier curve (dabs are separated according to spacing).

        Type:
        :   enum in [‘DOTS’, ‘DRAG\_DOT’, ‘SPACE’, ‘AIRBRUSH’, ‘ANCHORED’, ‘LINE’, ‘CURVE’], default ‘DOTS’

    surface\_smooth\_current\_vertex[#](#bpy.types.Brush.surface_smooth_current_vertex "Link to this definition")
    :   How much the position of each individual vertex influences the final result

        Type:
        :   float in [0, 1], default 0.0

    surface\_smooth\_iterations[#](#bpy.types.Brush.surface_smooth_iterations "Link to this definition")
    :   Number of smoothing iterations per brush step

        Type:
        :   int in [1, 10], default 0

    surface\_smooth\_shape\_preservation[#](#bpy.types.Brush.surface_smooth_shape_preservation "Link to this definition")
    :   How much of the original shape is preserved when smoothing

        Type:
        :   float in [0, 1], default 0.0

    texture[#](#bpy.types.Brush.texture "Link to this definition")
    :   Type:
        :   [`Texture`](Texture.md#bpy.types.Texture "bpy.types.Texture")

    texture\_overlay\_alpha[#](#bpy.types.Brush.texture_overlay_alpha "Link to this definition")
    :   Type:
        :   int in [0, 100], default 33

    texture\_sample\_bias[#](#bpy.types.Brush.texture_sample_bias "Link to this definition")
    :   Value added to texture samples

        Type:
        :   float in [-1, 1], default 0.0

    texture\_slot[#](#bpy.types.Brush.texture_slot "Link to this definition")
    :   Type:
        :   [`BrushTextureSlot`](BrushTextureSlot.md#bpy.types.BrushTextureSlot "bpy.types.BrushTextureSlot"), (readonly)

    tilt\_strength\_factor[#](#bpy.types.Brush.tilt_strength_factor "Link to this definition")
    :   How much the tilt of the pen will affect the brush

        Type:
        :   float in [0, 1], default 0.0

    tip\_roundness[#](#bpy.types.Brush.tip_roundness "Link to this definition")
    :   Roundness of the brush tip

        Type:
        :   float in [0, 1], default 1.0

    tip\_scale\_x[#](#bpy.types.Brush.tip_scale_x "Link to this definition")
    :   Scale of the brush tip in the X axis

        Type:
        :   float in [0, 1], default 1.0

    topology\_rake\_factor[#](#bpy.types.Brush.topology_rake_factor "Link to this definition")
    :   Automatically align edges to the brush direction to generate cleaner topology and define sharp features. Best used on low-poly meshes as it has a performance impact

        Type:
        :   float in [0, 1], default 0.0

    unprojected\_radius[#](#bpy.types.Brush.unprojected_radius "Link to this definition")
    :   Radius of brush in Blender units

        Type:
        :   float in [0.001, inf], default 0.0

    use\_accumulate[#](#bpy.types.Brush.use_accumulate "Link to this definition")
    :   Accumulate stroke daubs on top of each other

        Type:
        :   boolean, default False

    use\_adaptive\_space[#](#bpy.types.Brush.use_adaptive_space "Link to this definition")
    :   Space daubs according to surface orientation instead of screen space

        Type:
        :   boolean, default False

    use\_airbrush[#](#bpy.types.Brush.use_airbrush "Link to this definition")
    :   Keep applying paint effect while holding mouse (spray)

        Type:
        :   boolean, default False

    use\_alpha[#](#bpy.types.Brush.use_alpha "Link to this definition")
    :   When this is disabled, lock alpha while painting

        Type:
        :   boolean, default False

    use\_anchor[#](#bpy.types.Brush.use_anchor "Link to this definition")
    :   Keep the brush anchored to the initial location

        Type:
        :   boolean, default False

    use\_automasking\_boundary\_edges[#](#bpy.types.Brush.use_automasking_boundary_edges "Link to this definition")
    :   Do not affect non manifold boundary edges

        Type:
        :   boolean, default False

    use\_automasking\_boundary\_face\_sets[#](#bpy.types.Brush.use_automasking_boundary_face_sets "Link to this definition")
    :   Do not affect vertices that belong to a Face Set boundary

        Type:
        :   boolean, default False

    use\_automasking\_cavity[#](#bpy.types.Brush.use_automasking_cavity "Link to this definition")
    :   Do not affect vertices on peaks, based on the surface curvature

        Type:
        :   boolean, default False

    use\_automasking\_cavity\_inverted[#](#bpy.types.Brush.use_automasking_cavity_inverted "Link to this definition")
    :   Do not affect vertices within crevices, based on the surface curvature

        Type:
        :   boolean, default False

    use\_automasking\_custom\_cavity\_curve[#](#bpy.types.Brush.use_automasking_custom_cavity_curve "Link to this definition")
    :   Use custom curve

        Type:
        :   boolean, default False

    use\_automasking\_face\_sets[#](#bpy.types.Brush.use_automasking_face_sets "Link to this definition")
    :   Affect only vertices that share Face Sets with the active vertex

        Type:
        :   boolean, default False

    use\_automasking\_start\_normal[#](#bpy.types.Brush.use_automasking_start_normal "Link to this definition")
    :   Affect only vertices with a similar normal to where the stroke starts

        Type:
        :   boolean, default False

    use\_automasking\_topology[#](#bpy.types.Brush.use_automasking_topology "Link to this definition")
    :   Affect only vertices connected to the active vertex under the brush

        Type:
        :   boolean, default False

    use\_automasking\_view\_normal[#](#bpy.types.Brush.use_automasking_view_normal "Link to this definition")
    :   Affect only vertices with a normal that faces the viewer

        Type:
        :   boolean, default False

    use\_automasking\_view\_occlusion[#](#bpy.types.Brush.use_automasking_view_occlusion "Link to this definition")
    :   Only affect vertices that are not occluded by other faces. (Slower performance)

        Type:
        :   boolean, default False

    use\_cloth\_collision[#](#bpy.types.Brush.use_cloth_collision "Link to this definition")
    :   Collide with objects during the simulation

        Type:
        :   boolean, default False

    use\_cloth\_pin\_simulation\_boundary[#](#bpy.types.Brush.use_cloth_pin_simulation_boundary "Link to this definition")
    :   Lock the position of the vertices in the simulation falloff area to avoid artifacts and create a softer transition with unaffected areas

        Type:
        :   boolean, default False

    use\_color\_as\_displacement[#](#bpy.types.Brush.use_color_as_displacement "Link to this definition")
    :   Handles each pixel color as individual vector for displacement. Works only with area plane mapping

        Type:
        :   boolean, default False

    use\_connected\_only[#](#bpy.types.Brush.use_connected_only "Link to this definition")
    :   Affect only topologically connected elements

        Type:
        :   boolean, default False

    use\_cursor\_overlay[#](#bpy.types.Brush.use_cursor_overlay "Link to this definition")
    :   Show cursor in viewport

        Type:
        :   boolean, default False

    use\_cursor\_overlay\_override[#](#bpy.types.Brush.use_cursor_overlay_override "Link to this definition")
    :   Don’t show overlay during a stroke

        Type:
        :   boolean, default False

    use\_curve[#](#bpy.types.Brush.use_curve "Link to this definition")
    :   Define the stroke curve with a Bézier curve. Dabs are separated according to spacing

        Type:
        :   boolean, default False

    use\_custom\_icon[#](#bpy.types.Brush.use_custom_icon "Link to this definition")
    :   Set the brush icon from an image file

        Type:
        :   boolean, default False

    use\_density\_pressure[#](#bpy.types.Brush.use_density_pressure "Link to this definition")
    :   Use pressure to modulate density

        Type:
        :   boolean, default False

    use\_edge\_to\_edge[#](#bpy.types.Brush.use_edge_to_edge "Link to this definition")
    :   Drag anchor brush from edge-to-edge

        Type:
        :   boolean, default False

    use\_flow\_pressure[#](#bpy.types.Brush.use_flow_pressure "Link to this definition")
    :   Use pressure to modulate flow

        Type:
        :   boolean, default False

    use\_frontface[#](#bpy.types.Brush.use_frontface "Link to this definition")
    :   Brush only affects vertices that face the viewer

        Type:
        :   boolean, default False

    use\_frontface\_falloff[#](#bpy.types.Brush.use_frontface_falloff "Link to this definition")
    :   Blend brush influence by how much they face the front

        Type:
        :   boolean, default False

    use\_grab\_active\_vertex[#](#bpy.types.Brush.use_grab_active_vertex "Link to this definition")
    :   Apply the maximum grab strength to the active vertex instead of the cursor location

        Type:
        :   boolean, default False

    use\_grab\_silhouette[#](#bpy.types.Brush.use_grab_silhouette "Link to this definition")
    :   Grabs trying to automask the silhouette of the object

        Type:
        :   boolean, default False

    use\_hardness\_pressure[#](#bpy.types.Brush.use_hardness_pressure "Link to this definition")
    :   Use pressure to modulate hardness

        Type:
        :   boolean, default False

    use\_inverse\_smooth\_pressure[#](#bpy.types.Brush.use_inverse_smooth_pressure "Link to this definition")
    :   Lighter pressure causes more smoothing to be applied

        Type:
        :   boolean, default False

    use\_line[#](#bpy.types.Brush.use_line "Link to this definition")
    :   Draw a line with dabs separated according to spacing

        Type:
        :   boolean, default False

    use\_locked\_size[#](#bpy.types.Brush.use_locked_size "Link to this definition")
    :   Measure brush size relative to the view or the scene

        * `VIEW`
          View – Measure brush size relative to the view.
        * `SCENE`
          Scene – Measure brush size relative to the scene.

        Type:
        :   enum in [‘VIEW’, ‘SCENE’], default ‘VIEW’

    use\_multiplane\_scrape\_dynamic[#](#bpy.types.Brush.use_multiplane_scrape_dynamic "Link to this definition")
    :   The angle between the planes changes during the stroke to fit the surface under the cursor

        Type:
        :   boolean, default False

    use\_offset\_pressure[#](#bpy.types.Brush.use_offset_pressure "Link to this definition")
    :   Enable tablet pressure sensitivity for offset

        Type:
        :   boolean, default False

    use\_original\_normal[#](#bpy.types.Brush.use_original_normal "Link to this definition")
    :   When locked keep using normal of surface where stroke was initiated

        Type:
        :   boolean, default False

    use\_original\_plane[#](#bpy.types.Brush.use_original_plane "Link to this definition")
    :   When locked keep using the plane origin of surface where stroke was initiated

        Type:
        :   boolean, default False

    use\_paint\_antialiasing[#](#bpy.types.Brush.use_paint_antialiasing "Link to this definition")
    :   Smooths the edges of the strokes

        Type:
        :   boolean, default True

    use\_paint\_grease\_pencil[#](#bpy.types.Brush.use_paint_grease_pencil "Link to this definition")
    :   Use this brush in grease pencil drawing mode

        Type:
        :   boolean, default False

    use\_paint\_image[#](#bpy.types.Brush.use_paint_image "Link to this definition")
    :   Use this brush in texture paint mode

        Type:
        :   boolean, default True

    use\_paint\_sculpt[#](#bpy.types.Brush.use_paint_sculpt "Link to this definition")
    :   Use this brush in sculpt mode

        Type:
        :   boolean, default True

    use\_paint\_sculpt\_curves[#](#bpy.types.Brush.use_paint_sculpt_curves "Link to this definition")
    :   Use this brush in sculpt curves mode

        Type:
        :   boolean, default False

    use\_paint\_uv\_sculpt[#](#bpy.types.Brush.use_paint_uv_sculpt "Link to this definition")
    :   Use this brush in UV sculpt mode

        Type:
        :   boolean, default False

    use\_paint\_vertex[#](#bpy.types.Brush.use_paint_vertex "Link to this definition")
    :   Use this brush in vertex paint mode

        Type:
        :   boolean, default True

    use\_paint\_weight[#](#bpy.types.Brush.use_paint_weight "Link to this definition")
    :   Use this brush in weight paint mode

        Type:
        :   boolean, default True

    use\_persistent[#](#bpy.types.Brush.use_persistent "Link to this definition")
    :   Sculpt on a persistent layer of the mesh

        Type:
        :   boolean, default False

    use\_plane\_trim[#](#bpy.types.Brush.use_plane_trim "Link to this definition")
    :   Limit the distance from the offset plane that a vertex can be affected

        Type:
        :   boolean, default False

    use\_pose\_ik\_anchored[#](#bpy.types.Brush.use_pose_ik_anchored "Link to this definition")
    :   Keep the position of the last segment in the IK chain fixed

        Type:
        :   boolean, default False

    use\_pose\_lock\_rotation[#](#bpy.types.Brush.use_pose_lock_rotation "Link to this definition")
    :   Do not rotate the segment when using the scale deform mode

        Type:
        :   boolean, default False

    use\_pressure\_area\_radius[#](#bpy.types.Brush.use_pressure_area_radius "Link to this definition")
    :   Enable tablet pressure sensitivity for area radius

        Type:
        :   boolean, default False

    use\_pressure\_jitter[#](#bpy.types.Brush.use_pressure_jitter "Link to this definition")
    :   Enable tablet pressure sensitivity for jitter

        Type:
        :   boolean, default False

    use\_pressure\_masking[#](#bpy.types.Brush.use_pressure_masking "Link to this definition")
    :   Pen pressure makes texture influence smaller

        Type:
        :   enum in [‘NONE’, ‘RAMP’, ‘CUTOFF’], default ‘NONE’

    use\_pressure\_size[#](#bpy.types.Brush.use_pressure_size "Link to this definition")
    :   Enable tablet pressure sensitivity for size

        Type:
        :   boolean, default False

    use\_pressure\_spacing[#](#bpy.types.Brush.use_pressure_spacing "Link to this definition")
    :   Enable tablet pressure sensitivity for spacing

        Type:
        :   boolean, default False

    use\_pressure\_strength[#](#bpy.types.Brush.use_pressure_strength "Link to this definition")
    :   Enable tablet pressure sensitivity for strength

        Type:
        :   boolean, default True

    use\_primary\_overlay[#](#bpy.types.Brush.use_primary_overlay "Link to this definition")
    :   Show texture in viewport

        Type:
        :   boolean, default False

    use\_primary\_overlay\_override[#](#bpy.types.Brush.use_primary_overlay_override "Link to this definition")
    :   Don’t show overlay during a stroke

        Type:
        :   boolean, default False

    use\_restore\_mesh[#](#bpy.types.Brush.use_restore_mesh "Link to this definition")
    :   Allow a single dot to be carefully positioned

        Type:
        :   boolean, default False

    use\_scene\_spacing[#](#bpy.types.Brush.use_scene_spacing "Link to this definition")
    :   Calculate the brush spacing using view or scene distance

        * `VIEW`
          View – Calculate brush spacing relative to the view.
        * `SCENE`
          Scene – Calculate brush spacing relative to the scene using the stroke location.

        Type:
        :   enum in [‘VIEW’, ‘SCENE’], default ‘VIEW’

    use\_secondary\_overlay[#](#bpy.types.Brush.use_secondary_overlay "Link to this definition")
    :   Show texture in viewport

        Type:
        :   boolean, default False

    use\_secondary\_overlay\_override[#](#bpy.types.Brush.use_secondary_overlay_override "Link to this definition")
    :   Don’t show overlay during a stroke

        Type:
        :   boolean, default False

    use\_smooth\_stroke[#](#bpy.types.Brush.use_smooth_stroke "Link to this definition")
    :   Brush lags behind mouse and follows a smoother path

        Type:
        :   boolean, default False

    use\_space[#](#bpy.types.Brush.use_space "Link to this definition")
    :   Limit brush application to the distance specified by spacing

        Type:
        :   boolean, default True

    use\_space\_attenuation[#](#bpy.types.Brush.use_space_attenuation "Link to this definition")
    :   Automatically adjust strength to give consistent results for different spacings

        Type:
        :   boolean, default True

    use\_vertex\_grease\_pencil[#](#bpy.types.Brush.use_vertex_grease_pencil "Link to this definition")
    :   Use this brush in grease pencil vertex color mode

        Type:
        :   boolean, default False

    use\_wet\_mix\_pressure[#](#bpy.types.Brush.use_wet_mix_pressure "Link to this definition")
    :   Use pressure to modulate wet mix

        Type:
        :   boolean, default False

    use\_wet\_persistence\_pressure[#](#bpy.types.Brush.use_wet_persistence_pressure "Link to this definition")
    :   Use pressure to modulate wet persistence

        Type:
        :   boolean, default False

    vertex\_paint\_capabilities[#](#bpy.types.Brush.vertex_paint_capabilities "Link to this definition")
    :   Type:
        :   [`BrushCapabilitiesVertexPaint`](BrushCapabilitiesVertexPaint.md#bpy.types.BrushCapabilitiesVertexPaint "bpy.types.BrushCapabilitiesVertexPaint"), (readonly, never None)

    vertex\_tool[#](#bpy.types.Brush.vertex_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Vertex Tool Items](../../../appendix/bpy_types_enum_items/brush_vertex_tool_items.md#rna-enum-brush-vertex-tool-items), default ‘DRAW’

    weight[#](#bpy.types.Brush.weight "Link to this definition")
    :   Vertex weight when brush is applied

        Type:
        :   float in [0, 1], default 1.0

    weight\_paint\_capabilities[#](#bpy.types.Brush.weight_paint_capabilities "Link to this definition")
    :   Type:
        :   [`BrushCapabilitiesWeightPaint`](BrushCapabilitiesWeightPaint.md#bpy.types.BrushCapabilitiesWeightPaint "bpy.types.BrushCapabilitiesWeightPaint"), (readonly, never None)

    weight\_tool[#](#bpy.types.Brush.weight_tool "Link to this definition")
    :   Type:
        :   enum in [Brush Weight Tool Items](../../../appendix/bpy_types_enum_items/brush_weight_tool_items.md#rna-enum-brush-weight-tool-items), default ‘DRAW’

    wet\_mix[#](#bpy.types.Brush.wet_mix "Link to this definition")
    :   Amount of paint that is picked from the surface into the brush color

        Type:
        :   float in [0, 1], default 0.0

    wet\_paint\_radius\_factor[#](#bpy.types.Brush.wet_paint_radius_factor "Link to this definition")
    :   Ratio between the brush radius and the radius that is going to be used to sample the color to blend in wet paint

        Type:
        :   float in [0, 2], default 0.5

    wet\_persistence[#](#bpy.types.Brush.wet_persistence "Link to this definition")
    :   Amount of wet paint that stays in the brush after applying paint to the surface

        Type:
        :   float in [0, 1], default 0.0

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.Brush.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.Brush.bl_rna_get_subclass_py "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The class or default when not found.

        Return type:
        :   type

## Inherited Properties[#](#inherited-properties "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.id_data`](bpy_struct.md#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data") * [`ID.name`](ID.md#bpy.types.ID.name "bpy.types.ID.name") * [`ID.name_full`](ID.md#bpy.types.ID.name_full "bpy.types.ID.name_full") * [`ID.id_type`](ID.md#bpy.types.ID.id_type "bpy.types.ID.id_type") * [`ID.session_uid`](ID.md#bpy.types.ID.session_uid "bpy.types.ID.session_uid") * [`ID.is_evaluated`](ID.md#bpy.types.ID.is_evaluated "bpy.types.ID.is_evaluated") * [`ID.original`](ID.md#bpy.types.ID.original "bpy.types.ID.original") * [`ID.users`](ID.md#bpy.types.ID.users "bpy.types.ID.users") * [`ID.use_fake_user`](ID.md#bpy.types.ID.use_fake_user "bpy.types.ID.use_fake_user") * [`ID.use_extra_user`](ID.md#bpy.types.ID.use_extra_user "bpy.types.ID.use_extra_user") * [`ID.is_embedded_data`](ID.md#bpy.types.ID.is_embedded_data "bpy.types.ID.is_embedded_data") | * [`ID.is_missing`](ID.md#bpy.types.ID.is_missing "bpy.types.ID.is_missing") * [`ID.is_runtime_data`](ID.md#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data") * [`ID.is_editable`](ID.md#bpy.types.ID.is_editable "bpy.types.ID.is_editable") * [`ID.tag`](ID.md#bpy.types.ID.tag "bpy.types.ID.tag") * [`ID.is_library_indirect`](ID.md#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect") * [`ID.library`](ID.md#bpy.types.ID.library "bpy.types.ID.library") * [`ID.library_weak_reference`](ID.md#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference") * [`ID.asset_data`](ID.md#bpy.types.ID.asset_data "bpy.types.ID.asset_data") * [`ID.override_library`](ID.md#bpy.types.ID.override_library "bpy.types.ID.override_library") * [`ID.preview`](ID.md#bpy.types.ID.preview "bpy.types.ID.preview") |

## Inherited Functions[#](#inherited-functions "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.as_pointer`](bpy_struct.md#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer") * [`bpy_struct.driver_add`](bpy_struct.md#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add") * [`bpy_struct.driver_remove`](bpy_struct.md#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove") * [`bpy_struct.get`](bpy_struct.md#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get") * [`bpy_struct.id_properties_clear`](bpy_struct.md#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear") * [`bpy_struct.id_properties_ensure`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure") * [`bpy_struct.id_properties_ui`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui") * [`bpy_struct.is_property_hidden`](bpy_struct.md#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden") * [`bpy_struct.is_property_overridable_library`](bpy_struct.md#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library") * [`bpy_struct.is_property_readonly`](bpy_struct.md#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly") * [`bpy_struct.is_property_set`](bpy_struct.md#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set") * [`bpy_struct.items`](bpy_struct.md#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items") * [`bpy_struct.keyframe_delete`](bpy_struct.md#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete") * [`bpy_struct.keyframe_insert`](bpy_struct.md#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert") * [`bpy_struct.keys`](bpy_struct.md#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys") * [`bpy_struct.path_from_id`](bpy_struct.md#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id") * [`bpy_struct.path_resolve`](bpy_struct.md#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve") * [`bpy_struct.pop`](bpy_struct.md#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop") * [`bpy_struct.property_overridable_library_set`](bpy_struct.md#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set") * [`bpy_struct.property_unset`](bpy_struct.md#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset") | * [`bpy_struct.type_recast`](bpy_struct.md#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast") * [`bpy_struct.values`](bpy_struct.md#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values") * [`ID.evaluated_get`](ID.md#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get") * [`ID.copy`](ID.md#bpy.types.ID.copy "bpy.types.ID.copy") * [`ID.asset_mark`](ID.md#bpy.types.ID.asset_mark "bpy.types.ID.asset_mark") * [`ID.asset_clear`](ID.md#bpy.types.ID.asset_clear "bpy.types.ID.asset_clear") * [`ID.asset_generate_preview`](ID.md#bpy.types.ID.asset_generate_preview "bpy.types.ID.asset_generate_preview") * [`ID.override_create`](ID.md#bpy.types.ID.override_create "bpy.types.ID.override_create") * [`ID.override_hierarchy_create`](ID.md#bpy.types.ID.override_hierarchy_create "bpy.types.ID.override_hierarchy_create") * [`ID.user_clear`](ID.md#bpy.types.ID.user_clear "bpy.types.ID.user_clear") * [`ID.user_remap`](ID.md#bpy.types.ID.user_remap "bpy.types.ID.user_remap") * [`ID.make_local`](ID.md#bpy.types.ID.make_local "bpy.types.ID.make_local") * [`ID.user_of_id`](ID.md#bpy.types.ID.user_of_id "bpy.types.ID.user_of_id") * [`ID.animation_data_create`](ID.md#bpy.types.ID.animation_data_create "bpy.types.ID.animation_data_create") * [`ID.animation_data_clear`](ID.md#bpy.types.ID.animation_data_clear "bpy.types.ID.animation_data_clear") * [`ID.update_tag`](ID.md#bpy.types.ID.update_tag "bpy.types.ID.update_tag") * [`ID.preview_ensure`](ID.md#bpy.types.ID.preview_ensure "bpy.types.ID.preview_ensure") * [`ID.bl_rna_get_subclass`](ID.md#bpy.types.ID.bl_rna_get_subclass "bpy.types.ID.bl_rna_get_subclass") * [`ID.bl_rna_get_subclass_py`](ID.md#bpy.types.ID.bl_rna_get_subclass_py "bpy.types.ID.bl_rna_get_subclass_py") |

## References[#](#references "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy.context.brush`](../context/index.md#bpy.context.brush "bpy.context.brush") * [`BlendData.brushes`](BlendData.md#bpy.types.BlendData.brushes "bpy.types.BlendData.brushes") * [`BlendDataBrushes.create_gpencil_data`](BlendDataBrushes.md#bpy.types.BlendDataBrushes.create_gpencil_data "bpy.types.BlendDataBrushes.create_gpencil_data") * [`BlendDataBrushes.new`](BlendDataBrushes.md#bpy.types.BlendDataBrushes.new "bpy.types.BlendDataBrushes.new") | * [`BlendDataBrushes.remove`](BlendDataBrushes.md#bpy.types.BlendDataBrushes.remove "bpy.types.BlendDataBrushes.remove") * [`Paint.brush`](Paint.md#bpy.types.Paint.brush "bpy.types.Paint.brush") * [`PaintToolSlot.brush`](PaintToolSlot.md#bpy.types.PaintToolSlot.brush "bpy.types.PaintToolSlot.brush") |

[Next

BrushCapabilities(bpy\_struct)](BrushCapabilities.md)
[Previous

BrightContrastModifier(SequenceModifier)](BrightContrastModifier.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.Brush.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.Brush.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Brush(ID)
  + [`Brush`](#bpy.types.Brush)
    - [`Brush.area_radius_factor`](#bpy.types.Brush.area_radius_factor)
    - [`Brush.auto_smooth_factor`](#bpy.types.Brush.auto_smooth_factor)
    - [`Brush.automasking_boundary_edges_propagation_steps`](#bpy.types.Brush.automasking_boundary_edges_propagation_steps)
    - [`Brush.automasking_cavity_blur_steps`](#bpy.types.Brush.automasking_cavity_blur_steps)
    - [`Brush.automasking_cavity_curve`](#bpy.types.Brush.automasking_cavity_curve)
    - [`Brush.automasking_cavity_factor`](#bpy.types.Brush.automasking_cavity_factor)
    - [`Brush.automasking_start_normal_falloff`](#bpy.types.Brush.automasking_start_normal_falloff)
    - [`Brush.automasking_start_normal_limit`](#bpy.types.Brush.automasking_start_normal_limit)
    - [`Brush.automasking_view_normal_falloff`](#bpy.types.Brush.automasking_view_normal_falloff)
    - [`Brush.automasking_view_normal_limit`](#bpy.types.Brush.automasking_view_normal_limit)
    - [`Brush.blend`](#bpy.types.Brush.blend)
    - [`Brush.blur_kernel_radius`](#bpy.types.Brush.blur_kernel_radius)
    - [`Brush.blur_mode`](#bpy.types.Brush.blur_mode)
    - [`Brush.boundary_deform_type`](#bpy.types.Brush.boundary_deform_type)
    - [`Brush.boundary_falloff_type`](#bpy.types.Brush.boundary_falloff_type)
    - [`Brush.boundary_offset`](#bpy.types.Brush.boundary_offset)
    - [`Brush.brush_capabilities`](#bpy.types.Brush.brush_capabilities)
    - [`Brush.clone_alpha`](#bpy.types.Brush.clone_alpha)
    - [`Brush.clone_image`](#bpy.types.Brush.clone_image)
    - [`Brush.clone_offset`](#bpy.types.Brush.clone_offset)
    - [`Brush.cloth_constraint_softbody_strength`](#bpy.types.Brush.cloth_constraint_softbody_strength)
    - [`Brush.cloth_damping`](#bpy.types.Brush.cloth_damping)
    - [`Brush.cloth_deform_type`](#bpy.types.Brush.cloth_deform_type)
    - [`Brush.cloth_force_falloff_type`](#bpy.types.Brush.cloth_force_falloff_type)
    - [`Brush.cloth_mass`](#bpy.types.Brush.cloth_mass)
    - [`Brush.cloth_sim_falloff`](#bpy.types.Brush.cloth_sim_falloff)
    - [`Brush.cloth_sim_limit`](#bpy.types.Brush.cloth_sim_limit)
    - [`Brush.cloth_simulation_area_type`](#bpy.types.Brush.cloth_simulation_area_type)
    - [`Brush.color`](#bpy.types.Brush.color)
    - [`Brush.color_type`](#bpy.types.Brush.color_type)
    - [`Brush.crease_pinch_factor`](#bpy.types.Brush.crease_pinch_factor)
    - [`Brush.cursor_color_add`](#bpy.types.Brush.cursor_color_add)
    - [`Brush.cursor_color_subtract`](#bpy.types.Brush.cursor_color_subtract)
    - [`Brush.cursor_overlay_alpha`](#bpy.types.Brush.cursor_overlay_alpha)
    - [`Brush.curve`](#bpy.types.Brush.curve)
    - [`Brush.curve_preset`](#bpy.types.Brush.curve_preset)
    - [`Brush.curves_sculpt_settings`](#bpy.types.Brush.curves_sculpt_settings)
    - [`Brush.curves_sculpt_tool`](#bpy.types.Brush.curves_sculpt_tool)
    - [`Brush.dash_ratio`](#bpy.types.Brush.dash_ratio)
    - [`Brush.dash_samples`](#bpy.types.Brush.dash_samples)
    - [`Brush.deform_target`](#bpy.types.Brush.deform_target)
    - [`Brush.density`](#bpy.types.Brush.density)
    - [`Brush.direction`](#bpy.types.Brush.direction)
    - [`Brush.disconnected_distance_max`](#bpy.types.Brush.disconnected_distance_max)
    - [`Brush.elastic_deform_type`](#bpy.types.Brush.elastic_deform_type)
    - [`Brush.elastic_deform_volume_preservation`](#bpy.types.Brush.elastic_deform_volume_preservation)
    - [`Brush.falloff_angle`](#bpy.types.Brush.falloff_angle)
    - [`Brush.falloff_shape`](#bpy.types.Brush.falloff_shape)
    - [`Brush.fill_threshold`](#bpy.types.Brush.fill_threshold)
    - [`Brush.flow`](#bpy.types.Brush.flow)
    - [`Brush.gpencil_sculpt_tool`](#bpy.types.Brush.gpencil_sculpt_tool)
    - [`Brush.gpencil_settings`](#bpy.types.Brush.gpencil_settings)
    - [`Brush.gpencil_tool`](#bpy.types.Brush.gpencil_tool)
    - [`Brush.gpencil_vertex_tool`](#bpy.types.Brush.gpencil_vertex_tool)
    - [`Brush.gpencil_weight_tool`](#bpy.types.Brush.gpencil_weight_tool)
    - [`Brush.grad_spacing`](#bpy.types.Brush.grad_spacing)
    - [`Brush.gradient`](#bpy.types.Brush.gradient)
    - [`Brush.gradient_fill_mode`](#bpy.types.Brush.gradient_fill_mode)
    - [`Brush.gradient_stroke_mode`](#bpy.types.Brush.gradient_stroke_mode)
    - [`Brush.hardness`](#bpy.types.Brush.hardness)
    - [`Brush.height`](#bpy.types.Brush.height)
    - [`Brush.icon_filepath`](#bpy.types.Brush.icon_filepath)
    - [`Brush.image_paint_capabilities`](#bpy.types.Brush.image_paint_capabilities)
    - [`Brush.image_tool`](#bpy.types.Brush.image_tool)
    - [`Brush.input_samples`](#bpy.types.Brush.input_samples)
    - [`Brush.invert_density_pressure`](#bpy.types.Brush.invert_density_pressure)
    - [`Brush.invert_flow_pressure`](#bpy.types.Brush.invert_flow_pressure)
    - [`Brush.invert_hardness_pressure`](#bpy.types.Brush.invert_hardness_pressure)
    - [`Brush.invert_to_scrape_fill`](#bpy.types.Brush.invert_to_scrape_fill)
    - [`Brush.invert_wet_mix_pressure`](#bpy.types.Brush.invert_wet_mix_pressure)
    - [`Brush.invert_wet_persistence_pressure`](#bpy.types.Brush.invert_wet_persistence_pressure)
    - [`Brush.jitter`](#bpy.types.Brush.jitter)
    - [`Brush.jitter_absolute`](#bpy.types.Brush.jitter_absolute)
    - [`Brush.jitter_unit`](#bpy.types.Brush.jitter_unit)
    - [`Brush.mask_overlay_alpha`](#bpy.types.Brush.mask_overlay_alpha)
    - [`Brush.mask_stencil_dimension`](#bpy.types.Brush.mask_stencil_dimension)
    - [`Brush.mask_stencil_pos`](#bpy.types.Brush.mask_stencil_pos)
    - [`Brush.mask_texture`](#bpy.types.Brush.mask_texture)
    - [`Brush.mask_texture_slot`](#bpy.types.Brush.mask_texture_slot)
    - [`Brush.mask_tool`](#bpy.types.Brush.mask_tool)
    - [`Brush.multiplane_scrape_angle`](#bpy.types.Brush.multiplane_scrape_angle)
    - [`Brush.normal_radius_factor`](#bpy.types.Brush.normal_radius_factor)
    - [`Brush.normal_weight`](#bpy.types.Brush.normal_weight)
    - [`Brush.paint_curve`](#bpy.types.Brush.paint_curve)
    - [`Brush.plane_offset`](#bpy.types.Brush.plane_offset)
    - [`Brush.plane_trim`](#bpy.types.Brush.plane_trim)
    - [`Brush.pose_deform_type`](#bpy.types.Brush.pose_deform_type)
    - [`Brush.pose_ik_segments`](#bpy.types.Brush.pose_ik_segments)
    - [`Brush.pose_offset`](#bpy.types.Brush.pose_offset)
    - [`Brush.pose_origin_type`](#bpy.types.Brush.pose_origin_type)
    - [`Brush.pose_smooth_iterations`](#bpy.types.Brush.pose_smooth_iterations)
    - [`Brush.rake_factor`](#bpy.types.Brush.rake_factor)
    - [`Brush.rate`](#bpy.types.Brush.rate)
    - [`Brush.sculpt_capabilities`](#bpy.types.Brush.sculpt_capabilities)
    - [`Brush.sculpt_plane`](#bpy.types.Brush.sculpt_plane)
    - [`Brush.sculpt_tool`](#bpy.types.Brush.sculpt_tool)
    - [`Brush.secondary_color`](#bpy.types.Brush.secondary_color)
    - [`Brush.sharp_threshold`](#bpy.types.Brush.sharp_threshold)
    - [`Brush.show_multiplane_scrape_planes_preview`](#bpy.types.Brush.show_multiplane_scrape_planes_preview)
    - [`Brush.size`](#bpy.types.Brush.size)
    - [`Brush.slide_deform_type`](#bpy.types.Brush.slide_deform_type)
    - [`Brush.smear_deform_type`](#bpy.types.Brush.smear_deform_type)
    - [`Brush.smooth_deform_type`](#bpy.types.Brush.smooth_deform_type)
    - [`Brush.smooth_stroke_factor`](#bpy.types.Brush.smooth_stroke_factor)
    - [`Brush.smooth_stroke_radius`](#bpy.types.Brush.smooth_stroke_radius)
    - [`Brush.snake_hook_deform_type`](#bpy.types.Brush.snake_hook_deform_type)
    - [`Brush.spacing`](#bpy.types.Brush.spacing)
    - [`Brush.stencil_dimension`](#bpy.types.Brush.stencil_dimension)
    - [`Brush.stencil_pos`](#bpy.types.Brush.stencil_pos)
    - [`Brush.strength`](#bpy.types.Brush.strength)
    - [`Brush.stroke_method`](#bpy.types.Brush.stroke_method)
    - [`Brush.surface_smooth_current_vertex`](#bpy.types.Brush.surface_smooth_current_vertex)
    - [`Brush.surface_smooth_iterations`](#bpy.types.Brush.surface_smooth_iterations)
    - [`Brush.surface_smooth_shape_preservation`](#bpy.types.Brush.surface_smooth_shape_preservation)
    - [`Brush.texture`](#bpy.types.Brush.texture)
    - [`Brush.texture_overlay_alpha`](#bpy.types.Brush.texture_overlay_alpha)
    - [`Brush.texture_sample_bias`](#bpy.types.Brush.texture_sample_bias)
    - [`Brush.texture_slot`](#bpy.types.Brush.texture_slot)
    - [`Brush.tilt_strength_factor`](#bpy.types.Brush.tilt_strength_factor)
    - [`Brush.tip_roundness`](#bpy.types.Brush.tip_roundness)
    - [`Brush.tip_scale_x`](#bpy.types.Brush.tip_scale_x)
    - [`Brush.topology_rake_factor`](#bpy.types.Brush.topology_rake_factor)
    - [`Brush.unprojected_radius`](#bpy.types.Brush.unprojected_radius)
    - [`Brush.use_accumulate`](#bpy.types.Brush.use_accumulate)
    - [`Brush.use_adaptive_space`](#bpy.types.Brush.use_adaptive_space)
    - [`Brush.use_airbrush`](#bpy.types.Brush.use_airbrush)
    - [`Brush.use_alpha`](#bpy.types.Brush.use_alpha)
    - [`Brush.use_anchor`](#bpy.types.Brush.use_anchor)
    - [`Brush.use_automasking_boundary_edges`](#bpy.types.Brush.use_automasking_boundary_edges)
    - [`Brush.use_automasking_boundary_face_sets`](#bpy.types.Brush.use_automasking_boundary_face_sets)
    - [`Brush.use_automasking_cavity`](#bpy.types.Brush.use_automasking_cavity)
    - [`Brush.use_automasking_cavity_inverted`](#bpy.types.Brush.use_automasking_cavity_inverted)
    - [`Brush.use_automasking_custom_cavity_curve`](#bpy.types.Brush.use_automasking_custom_cavity_curve)
    - [`Brush.use_automasking_face_sets`](#bpy.types.Brush.use_automasking_face_sets)
    - [`Brush.use_automasking_start_normal`](#bpy.types.Brush.use_automasking_start_normal)
    - [`Brush.use_automasking_topology`](#bpy.types.Brush.use_automasking_topology)
    - [`Brush.use_automasking_view_normal`](#bpy.types.Brush.use_automasking_view_normal)
    - [`Brush.use_automasking_view_occlusion`](#bpy.types.Brush.use_automasking_view_occlusion)
    - [`Brush.use_cloth_collision`](#bpy.types.Brush.use_cloth_collision)
    - [`Brush.use_cloth_pin_simulation_boundary`](#bpy.types.Brush.use_cloth_pin_simulation_boundary)
    - [`Brush.use_color_as_displacement`](#bpy.types.Brush.use_color_as_displacement)
    - [`Brush.use_connected_only`](#bpy.types.Brush.use_connected_only)
    - [`Brush.use_cursor_overlay`](#bpy.types.Brush.use_cursor_overlay)
    - [`Brush.use_cursor_overlay_override`](#bpy.types.Brush.use_cursor_overlay_override)
    - [`Brush.use_curve`](#bpy.types.Brush.use_curve)
    - [`Brush.use_custom_icon`](#bpy.types.Brush.use_custom_icon)
    - [`Brush.use_density_pressure`](#bpy.types.Brush.use_density_pressure)
    - [`Brush.use_edge_to_edge`](#bpy.types.Brush.use_edge_to_edge)
    - [`Brush.use_flow_pressure`](#bpy.types.Brush.use_flow_pressure)
    - [`Brush.use_frontface`](#bpy.types.Brush.use_frontface)
    - [`Brush.use_frontface_falloff`](#bpy.types.Brush.use_frontface_falloff)
    - [`Brush.use_grab_active_vertex`](#bpy.types.Brush.use_grab_active_vertex)
    - [`Brush.use_grab_silhouette`](#bpy.types.Brush.use_grab_silhouette)
    - [`Brush.use_hardness_pressure`](#bpy.types.Brush.use_hardness_pressure)
    - [`Brush.use_inverse_smooth_pressure`](#bpy.types.Brush.use_inverse_smooth_pressure)
    - [`Brush.use_line`](#bpy.types.Brush.use_line)
    - [`Brush.use_locked_size`](#bpy.types.Brush.use_locked_size)
    - [`Brush.use_multiplane_scrape_dynamic`](#bpy.types.Brush.use_multiplane_scrape_dynamic)
    - [`Brush.use_offset_pressure`](#bpy.types.Brush.use_offset_pressure)
    - [`Brush.use_original_normal`](#bpy.types.Brush.use_original_normal)
    - [`Brush.use_original_plane`](#bpy.types.Brush.use_original_plane)
    - [`Brush.use_paint_antialiasing`](#bpy.types.Brush.use_paint_antialiasing)
    - [`Brush.use_paint_grease_pencil`](#bpy.types.Brush.use_paint_grease_pencil)
    - [`Brush.use_paint_image`](#bpy.types.Brush.use_paint_image)
    - [`Brush.use_paint_sculpt`](#bpy.types.Brush.use_paint_sculpt)
    - [`Brush.use_paint_sculpt_curves`](#bpy.types.Brush.use_paint_sculpt_curves)
    - [`Brush.use_paint_uv_sculpt`](#bpy.types.Brush.use_paint_uv_sculpt)
    - [`Brush.use_paint_vertex`](#bpy.types.Brush.use_paint_vertex)
    - [`Brush.use_paint_weight`](#bpy.types.Brush.use_paint_weight)
    - [`Brush.use_persistent`](#bpy.types.Brush.use_persistent)
    - [`Brush.use_plane_trim`](#bpy.types.Brush.use_plane_trim)
    - [`Brush.use_pose_ik_anchored`](#bpy.types.Brush.use_pose_ik_anchored)
    - [`Brush.use_pose_lock_rotation`](#bpy.types.Brush.use_pose_lock_rotation)
    - [`Brush.use_pressure_area_radius`](#bpy.types.Brush.use_pressure_area_radius)
    - [`Brush.use_pressure_jitter`](#bpy.types.Brush.use_pressure_jitter)
    - [`Brush.use_pressure_masking`](#bpy.types.Brush.use_pressure_masking)
    - [`Brush.use_pressure_size`](#bpy.types.Brush.use_pressure_size)
    - [`Brush.use_pressure_spacing`](#bpy.types.Brush.use_pressure_spacing)
    - [`Brush.use_pressure_strength`](#bpy.types.Brush.use_pressure_strength)
    - [`Brush.use_primary_overlay`](#bpy.types.Brush.use_primary_overlay)
    - [`Brush.use_primary_overlay_override`](#bpy.types.Brush.use_primary_overlay_override)
    - [`Brush.use_restore_mesh`](#bpy.types.Brush.use_restore_mesh)
    - [`Brush.use_scene_spacing`](#bpy.types.Brush.use_scene_spacing)
    - [`Brush.use_secondary_overlay`](#bpy.types.Brush.use_secondary_overlay)
    - [`Brush.use_secondary_overlay_override`](#bpy.types.Brush.use_secondary_overlay_override)
    - [`Brush.use_smooth_stroke`](#bpy.types.Brush.use_smooth_stroke)
    - [`Brush.use_space`](#bpy.types.Brush.use_space)
    - [`Brush.use_space_attenuation`](#bpy.types.Brush.use_space_attenuation)
    - [`Brush.use_vertex_grease_pencil`](#bpy.types.Brush.use_vertex_grease_pencil)
    - [`Brush.use_wet_mix_pressure`](#bpy.types.Brush.use_wet_mix_pressure)
    - [`Brush.use_wet_persistence_pressure`](#bpy.types.Brush.use_wet_persistence_pressure)
    - [`Brush.vertex_paint_capabilities`](#bpy.types.Brush.vertex_paint_capabilities)
    - [`Brush.vertex_tool`](#bpy.types.Brush.vertex_tool)
    - [`Brush.weight`](#bpy.types.Brush.weight)
    - [`Brush.weight_paint_capabilities`](#bpy.types.Brush.weight_paint_capabilities)
    - [`Brush.weight_tool`](#bpy.types.Brush.weight_tool)
    - [`Brush.wet_mix`](#bpy.types.Brush.wet_mix)
    - [`Brush.wet_paint_radius_factor`](#bpy.types.Brush.wet_paint_radius_factor)
    - [`Brush.wet_persistence`](#bpy.types.Brush.wet_persistence)
    - [`Brush.bl_rna_get_subclass()`](#bpy.types.Brush.bl_rna_get_subclass)
    - [`Brush.bl_rna_get_subclass_py()`](#bpy.types.Brush.bl_rna_get_subclass_py)
  + [Inherited Properties](#inherited-properties)
  + [Inherited Functions](#inherited-functions)
  + [References](#references)