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
* [Freestyle Module (freestyle)](../../../meta/index.md)[x]

  Toggle navigation of Freestyle Module (freestyle)

  + [Freestyle Types (freestyle.types)](../types/index.md)
  + [Freestyle Predicates (freestyle.predicates)](../predicates/index.md)
  + [Freestyle Functions (freestyle.functions)](../functions/index.md)
  + [Freestyle Chaining Iterators (freestyle.chainingiterators)](../chainingiterators/index.md)
  + Freestyle Shaders (freestyle.shaders)
  + [Freestyle Utilities (freestyle.utils)](../utils/index.md)[ ]

    Toggle navigation of Freestyle Utilities (freestyle.utils)

    - [freestyle.utils submodule (freestyle.utils.ContextFunctions)](../utils/ContextFunctions.md)
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

# Freestyle Shaders (freestyle.shaders)[#](#module-freestyle.shaders "Link to this heading")

This module contains stroke shaders used for creation of stylized
strokes. It is also intended to be a collection of examples for
shader definition in Python.

User-defined stroke shaders inherit the
[`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") class.

*class* freestyle.shaders.BackboneStretcherShader[#](#freestyle.shaders.BackboneStretcherShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`BackboneStretcherShader`](#freestyle.shaders.BackboneStretcherShader "freestyle.shaders.BackboneStretcherShader")

    [Geometry shader]

    \_\_init\_\_(*amount=2.0*)[#](#freestyle.shaders.BackboneStretcherShader.__init__ "Link to this definition")
    :   Builds a BackboneStretcherShader object.

        Parameters:
        :   **amount** (*float*) – The stretching amount value.

    shade(*stroke*)[#](#freestyle.shaders.BackboneStretcherShader.shade "Link to this definition")
    :   Stretches the stroke at its two extremities and following the
        respective directions: v(1)v(0) and v(n-1)v(n).

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.BezierCurveShader[#](#freestyle.shaders.BezierCurveShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`BezierCurveShader`](#freestyle.shaders.BezierCurveShader "freestyle.shaders.BezierCurveShader")

    [Geometry shader]

    \_\_init\_\_(*error=4.0*)[#](#freestyle.shaders.BezierCurveShader.__init__ "Link to this definition")
    :   Builds a BezierCurveShader object.

        Parameters:
        :   **error** (*float*) – The error we’re allowing for the approximation. This
            error is the max distance allowed between the new curve and the
            original geometry.

    shade(*stroke*)[#](#freestyle.shaders.BezierCurveShader.shade "Link to this definition")
    :   Transforms the stroke backbone geometry so that it corresponds to a
        Bezier Curve approximation of the original backbone geometry.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.BlenderTextureShader[#](#freestyle.shaders.BlenderTextureShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`BlenderTextureShader`](#freestyle.shaders.BlenderTextureShader "freestyle.shaders.BlenderTextureShader")

    [Texture shader]

    \_\_init\_\_(*texture*)[#](#freestyle.shaders.BlenderTextureShader.__init__ "Link to this definition")
    :   Builds a BlenderTextureShader object.

        Parameters:
        :   **texture** ([`bpy.types.LineStyleTextureSlot`](../../bpy/types/LineStyleTextureSlot.md#bpy.types.LineStyleTextureSlot "bpy.types.LineStyleTextureSlot") or
            [`bpy.types.ShaderNodeTree`](../../bpy/types/ShaderNodeTree.md#bpy.types.ShaderNodeTree "bpy.types.ShaderNodeTree")) – A line style texture slot or a shader node tree to define
            a set of textures.

    shade(*stroke*)[#](#freestyle.shaders.BlenderTextureShader.shade "Link to this definition")
    :   Assigns a blender texture slot to the stroke shading in order to
        simulate marks.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.CalligraphicShader[#](#freestyle.shaders.CalligraphicShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`CalligraphicShader`](#freestyle.shaders.CalligraphicShader "freestyle.shaders.CalligraphicShader")

    [Thickness Shader]

    \_\_init\_\_(*thickness\_min*, *thickness\_max*, *orientation*, *clamp*)[#](#freestyle.shaders.CalligraphicShader.__init__ "Link to this definition")
    :   Builds a CalligraphicShader object.

        Parameters:
        :   * **thickness\_min** (*float*) – The minimum thickness in the direction
              perpendicular to the main direction.
            * **thickness\_max** (*float*) – The maximum thickness in the main direction.
            * **orientation** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")) – The 2D vector giving the main direction.
            * **clamp** (*bool*) – If true, the strokes are drawn in black when the stroke
              direction is between -90 and 90 degrees with respect to the main
              direction and drawn in white otherwise. If false, the strokes
              are always drawn in black.

    shade(*stroke*)[#](#freestyle.shaders.CalligraphicShader.shade "Link to this definition")
    :   Assigns thicknesses to the stroke vertices so that the stroke looks
        like made with a calligraphic tool, i.e. the stroke will be the
        thickest in a main direction, and the thinnest in the direction
        perpendicular to this one, and an interpolation in between.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.ColorNoiseShader[#](#freestyle.shaders.ColorNoiseShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`ColorNoiseShader`](#freestyle.shaders.ColorNoiseShader "freestyle.shaders.ColorNoiseShader")

    [Color shader]

    \_\_init\_\_(*amplitude*, *period*)[#](#freestyle.shaders.ColorNoiseShader.__init__ "Link to this definition")
    :   Builds a ColorNoiseShader object.

        Parameters:
        :   * **amplitude** (*float*) – The amplitude of the noise signal.
            * **period** (*float*) – The period of the noise signal.

    shade(*stroke*)[#](#freestyle.shaders.ColorNoiseShader.shade "Link to this definition")
    :   Shader to add noise to the stroke colors.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.ConstantColorShader[#](#freestyle.shaders.ConstantColorShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`ConstantColorShader`](#freestyle.shaders.ConstantColorShader "freestyle.shaders.ConstantColorShader")

    [Color shader]

    \_\_init\_\_(*red*, *green*, *blue*, *alpha=1.0*)[#](#freestyle.shaders.ConstantColorShader.__init__ "Link to this definition")
    :   Builds a ConstantColorShader object.

        Parameters:
        :   * **red** (*float*) – The red component.
            * **green** (*float*) – The green component.
            * **blue** (*float*) – The blue component.
            * **alpha** (*float*) – The alpha value.

    shade(*stroke*)[#](#freestyle.shaders.ConstantColorShader.shade "Link to this definition")
    :   Assigns a constant color to every vertex of the Stroke.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.ConstantThicknessShader[#](#freestyle.shaders.ConstantThicknessShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`ConstantThicknessShader`](#freestyle.shaders.ConstantThicknessShader "freestyle.shaders.ConstantThicknessShader")

    [Thickness shader]

    \_\_init\_\_(*thickness*)[#](#freestyle.shaders.ConstantThicknessShader.__init__ "Link to this definition")
    :   Builds a ConstantThicknessShader object.

        Parameters:
        :   **thickness** (*float*) – The thickness that must be assigned to the stroke.

    shade(*stroke*)[#](#freestyle.shaders.ConstantThicknessShader.shade "Link to this definition")
    :   Assigns an absolute constant thickness to every vertex of the Stroke.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.ConstrainedIncreasingThicknessShader[#](#freestyle.shaders.ConstrainedIncreasingThicknessShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`ConstrainedIncreasingThicknessShader`](#freestyle.shaders.ConstrainedIncreasingThicknessShader "freestyle.shaders.ConstrainedIncreasingThicknessShader")

    [Thickness shader]

    \_\_init\_\_(*thickness\_min*, *thickness\_max*, *ratio*)[#](#freestyle.shaders.ConstrainedIncreasingThicknessShader.__init__ "Link to this definition")
    :   Builds a ConstrainedIncreasingThicknessShader object.

        Parameters:
        :   * **thickness\_min** (*float*) – The minimum thickness.
            * **thickness\_max** (*float*) – The maximum thickness.
            * **ratio** (*float*) – The thickness/length ratio that we don’t want to exceed.

    shade(*stroke*)[#](#freestyle.shaders.ConstrainedIncreasingThicknessShader.shade "Link to this definition")
    :   Same as the [`IncreasingThicknessShader`](#freestyle.shaders.IncreasingThicknessShader "freestyle.shaders.IncreasingThicknessShader"), but here we allow
        the user to control the thickness/length ratio so that we don’t get
        fat short lines.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.GuidingLinesShader[#](#freestyle.shaders.GuidingLinesShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`GuidingLinesShader`](#freestyle.shaders.GuidingLinesShader "freestyle.shaders.GuidingLinesShader")

    [Geometry shader]

    \_\_init\_\_(*offset*)[#](#freestyle.shaders.GuidingLinesShader.__init__ "Link to this definition")
    :   Builds a GuidingLinesShader object.

        Parameters:
        :   **offset** (*float*) – The line that replaces the stroke is initially in the
            middle of the initial stroke bounding box. offset is the value
            of the displacement which is applied to this line along its
            normal.

    shade(*stroke*)[#](#freestyle.shaders.GuidingLinesShader.shade "Link to this definition")
    :   Shader to modify the Stroke geometry so that it corresponds to its
        main direction line. This shader must be used together with the
        splitting operator using the curvature criterion. Indeed, the
        precision of the approximation will depend on the size of the
        stroke’s pieces. The bigger the pieces are, the rougher the
        approximation is.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.IncreasingColorShader[#](#freestyle.shaders.IncreasingColorShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`IncreasingColorShader`](#freestyle.shaders.IncreasingColorShader "freestyle.shaders.IncreasingColorShader")

    [Color shader]

    \_\_init\_\_(*red\_min*, *green\_min*, *blue\_min*, *alpha\_min*, *red\_max*, *green\_max*, *blue\_max*, *alpha\_max*)[#](#freestyle.shaders.IncreasingColorShader.__init__ "Link to this definition")
    :   Builds an IncreasingColorShader object.

        Parameters:
        :   * **red\_min** (*float*) – The first color red component.
            * **green\_min** (*float*) – The first color green component.
            * **blue\_min** (*float*) – The first color blue component.
            * **alpha\_min** (*float*) – The first color alpha value.
            * **red\_max** (*float*) – The second color red component.
            * **green\_max** (*float*) – The second color green component.
            * **blue\_max** (*float*) – The second color blue component.
            * **alpha\_max** (*float*) – The second color alpha value.

    shade(*stroke*)[#](#freestyle.shaders.IncreasingColorShader.shade "Link to this definition")
    :   Assigns a varying color to the stroke. The user specifies two
        colors A and B. The stroke color will change linearly from A to B
        between the first and the last vertex.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.IncreasingThicknessShader[#](#freestyle.shaders.IncreasingThicknessShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`IncreasingThicknessShader`](#freestyle.shaders.IncreasingThicknessShader "freestyle.shaders.IncreasingThicknessShader")

    [Thickness shader]

    \_\_init\_\_(*thickness\_A*, *thickness\_B*)[#](#freestyle.shaders.IncreasingThicknessShader.__init__ "Link to this definition")
    :   Builds an IncreasingThicknessShader object.

        Parameters:
        :   * **thickness\_A** (*float*) – The first thickness value.
            * **thickness\_B** (*float*) – The second thickness value.

    shade(*stroke*)[#](#freestyle.shaders.IncreasingThicknessShader.shade "Link to this definition")
    :   Assigns thicknesses values such as the thickness increases from a
        thickness value A to a thickness value B between the first vertex
        to the midpoint vertex and then decreases from B to a A between
        this midpoint vertex and the last vertex. The thickness is
        linearly interpolated from A to B.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.PolygonalizationShader[#](#freestyle.shaders.PolygonalizationShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`PolygonalizationShader`](#freestyle.shaders.PolygonalizationShader "freestyle.shaders.PolygonalizationShader")

    [Geometry shader]

    \_\_init\_\_(*error*)[#](#freestyle.shaders.PolygonalizationShader.__init__ "Link to this definition")
    :   Builds a PolygonalizationShader object.

        Parameters:
        :   **error** (*float*) – The error we want our polygonal approximation to have
            with respect to the original geometry. The smaller, the closer
            the new stroke is to the original one. This error corresponds to
            the maximum distance between the new stroke and the old one.

    shade(*stroke*)[#](#freestyle.shaders.PolygonalizationShader.shade "Link to this definition")
    :   Modifies the Stroke geometry so that it looks more “polygonal”.
        The basic idea is to start from the minimal stroke approximation
        consisting in a line joining the first vertex to the last one and
        to subdivide using the original stroke vertices until a certain
        error is reached.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.RoundCapShader[#](#freestyle.shaders.RoundCapShader "Link to this definition")
:   round\_cap\_thickness(*x*)[#](#freestyle.shaders.RoundCapShader.round_cap_thickness "Link to this definition")

    shade(*stroke*)[#](#freestyle.shaders.RoundCapShader.shade "Link to this definition")

*class* freestyle.shaders.SamplingShader[#](#freestyle.shaders.SamplingShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`SamplingShader`](#freestyle.shaders.SamplingShader "freestyle.shaders.SamplingShader")

    [Geometry shader]

    \_\_init\_\_(*sampling*)[#](#freestyle.shaders.SamplingShader.__init__ "Link to this definition")
    :   Builds a SamplingShader object.

        Parameters:
        :   **sampling** (*float*) – The sampling to use for the stroke resampling.

    shade(*stroke*)[#](#freestyle.shaders.SamplingShader.shade "Link to this definition")
    :   Resamples the stroke.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.SmoothingShader[#](#freestyle.shaders.SmoothingShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`SmoothingShader`](#freestyle.shaders.SmoothingShader "freestyle.shaders.SmoothingShader")

    [Geometry shader]

    \_\_init\_\_(*num\_iterations=100*, *factor\_point=0.1*, *factor\_curvature=0.0*, *factor\_curvature\_difference=0.2*, *aniso\_point=0.0*, *aniso\_normal=0.0*, *aniso\_curvature=0.0*, *carricature\_factor=1.0*)[#](#freestyle.shaders.SmoothingShader.__init__ "Link to this definition")
    :   Builds a SmoothingShader object.

        Parameters:
        :   * **num\_iterations** (*int*) – The number of iterations.
            * **factor\_point** (*float*) – 0.1
            * **factor\_curvature** (*float*) – 0.0
            * **factor\_curvature\_difference** (*float*) – 0.2
            * **aniso\_point** (*float*) – 0.0
            * **aniso\_normal** (*float*) – 0.0
            * **aniso\_curvature** (*float*) – 0.0
            * **carricature\_factor** (*float*) – 1.0

    shade(*stroke*)[#](#freestyle.shaders.SmoothingShader.shade "Link to this definition")
    :   Smooths the stroke by moving the vertices to make the stroke
        smoother. Uses curvature flow to converge towards a curve of
        constant curvature. The diffusion method we use is anisotropic to
        prevent the diffusion across corners.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.SpatialNoiseShader[#](#freestyle.shaders.SpatialNoiseShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`SpatialNoiseShader`](#freestyle.shaders.SpatialNoiseShader "freestyle.shaders.SpatialNoiseShader")

    [Geometry shader]

    \_\_init\_\_(*amount*, *scale*, *num\_octaves*, *smooth*, *pure\_random*)[#](#freestyle.shaders.SpatialNoiseShader.__init__ "Link to this definition")
    :   Builds a SpatialNoiseShader object.

        Parameters:
        :   * **amount** (*float*) – The amplitude of the noise.
            * **scale** (*float*) – The noise frequency.
            * **num\_octaves** (*int*) – The number of octaves
            * **smooth** (*bool*) – True if you want the noise to be smooth.
            * **pure\_random** (*bool*) – True if you don’t want any coherence.

    shade(*stroke*)[#](#freestyle.shaders.SpatialNoiseShader.shade "Link to this definition")
    :   Spatial Noise stroke shader. Moves the vertices to make the stroke
        more noisy.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.SquareCapShader[#](#freestyle.shaders.SquareCapShader "Link to this definition")
:   shade(*stroke*)[#](#freestyle.shaders.SquareCapShader.shade "Link to this definition")

*class* freestyle.shaders.StrokeTextureStepShader[#](#freestyle.shaders.StrokeTextureStepShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`StrokeTextureStepShader`](#freestyle.shaders.StrokeTextureStepShader "freestyle.shaders.StrokeTextureStepShader")

    [Texture shader]

    \_\_init\_\_(*step*)[#](#freestyle.shaders.StrokeTextureStepShader.__init__ "Link to this definition")
    :   Builds a StrokeTextureStepShader object.

        Parameters:
        :   **step** (*float*) – The spacing along the stroke.

    shade(*stroke*)[#](#freestyle.shaders.StrokeTextureStepShader.shade "Link to this definition")
    :   Assigns a spacing factor to the texture coordinates of the Stroke.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.ThicknessNoiseShader[#](#freestyle.shaders.ThicknessNoiseShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`ThicknessNoiseShader`](#freestyle.shaders.ThicknessNoiseShader "freestyle.shaders.ThicknessNoiseShader")

    [Thickness shader]

    \_\_init\_\_(*amplitude*, *period*)[#](#freestyle.shaders.ThicknessNoiseShader.__init__ "Link to this definition")
    :   Builds a ThicknessNoiseShader object.

        Parameters:
        :   * **amplitude** (*float*) – The amplitude of the noise signal.
            * **period** (*float*) – The period of the noise signal.

    shade(*stroke*)[#](#freestyle.shaders.ThicknessNoiseShader.shade "Link to this definition")
    :   Adds some noise to the stroke thickness.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.TipRemoverShader[#](#freestyle.shaders.TipRemoverShader "Link to this definition")
:   Class hierarchy: [`freestyle.types.StrokeShader`](../types/index.md#freestyle.types.StrokeShader "freestyle.types.StrokeShader") > [`TipRemoverShader`](#freestyle.shaders.TipRemoverShader "freestyle.shaders.TipRemoverShader")

    [Geometry shader]

    \_\_init\_\_(*tip\_length*)[#](#freestyle.shaders.TipRemoverShader.__init__ "Link to this definition")
    :   Builds a TipRemoverShader object.

        Parameters:
        :   **tip\_length** (*float*) – The length of the piece of stroke we want to remove
            at each extremity.

    shade(*stroke*)[#](#freestyle.shaders.TipRemoverShader.shade "Link to this definition")
    :   Removes the stroke’s extremities.

        Parameters:
        :   **stroke** ([`freestyle.types.Stroke`](../types/index.md#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

*class* freestyle.shaders.py2DCurvatureColorShader[#](#freestyle.shaders.py2DCurvatureColorShader "Link to this definition")
:   Assigns a color (grayscale) to the stroke based on the curvature.
    A higher curvature will yield a brighter color.

    shade(*stroke*)[#](#freestyle.shaders.py2DCurvatureColorShader.shade "Link to this definition")

*class* freestyle.shaders.pyBackboneStretcherNoCuspShader[#](#freestyle.shaders.pyBackboneStretcherNoCuspShader "Link to this definition")
:   Stretches the stroke’s backbone, excluding cusp vertices (end junctions).

    shade(*stroke*)[#](#freestyle.shaders.pyBackboneStretcherNoCuspShader.shade "Link to this definition")

*class* freestyle.shaders.pyBackboneStretcherShader[#](#freestyle.shaders.pyBackboneStretcherShader "Link to this definition")
:   Stretches the stroke’s backbone by a given length (in pixels).

    shade(*stroke*)[#](#freestyle.shaders.pyBackboneStretcherShader.shade "Link to this definition")

*class* freestyle.shaders.pyBluePrintCirclesShader[#](#freestyle.shaders.pyBluePrintCirclesShader "Link to this definition")
:   Draws the silhouette of the object as a circle.

    shade(*stroke*)[#](#freestyle.shaders.pyBluePrintCirclesShader.shade "Link to this definition")

*class* freestyle.shaders.pyBluePrintDirectedSquaresShader[#](#freestyle.shaders.pyBluePrintDirectedSquaresShader "Link to this definition")
:   Replaces the stroke with a directed square.

    shade(*stroke*)[#](#freestyle.shaders.pyBluePrintDirectedSquaresShader.shade "Link to this definition")

*class* freestyle.shaders.pyBluePrintEllipsesShader[#](#freestyle.shaders.pyBluePrintEllipsesShader "Link to this definition")
:   shade(*stroke*)[#](#freestyle.shaders.pyBluePrintEllipsesShader.shade "Link to this definition")

*class* freestyle.shaders.pyBluePrintSquaresShader[#](#freestyle.shaders.pyBluePrintSquaresShader "Link to this definition")
:   shade(*stroke*)[#](#freestyle.shaders.pyBluePrintSquaresShader.shade "Link to this definition")

*class* freestyle.shaders.pyConstantColorShader[#](#freestyle.shaders.pyConstantColorShader "Link to this definition")
:   Assigns a constant color to the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyConstantColorShader.shade "Link to this definition")

*class* freestyle.shaders.pyConstantThicknessShader[#](#freestyle.shaders.pyConstantThicknessShader "Link to this definition")
:   Assigns a constant thickness along the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyConstantThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyConstrainedIncreasingThicknessShader[#](#freestyle.shaders.pyConstrainedIncreasingThicknessShader "Link to this definition")
:   Increasingly thickens the stroke, constrained by a ratio of the
    stroke’s length.

    shade(*stroke*)[#](#freestyle.shaders.pyConstrainedIncreasingThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyDecreasingThicknessShader[#](#freestyle.shaders.pyDecreasingThicknessShader "Link to this definition")
:   Inverse of pyIncreasingThicknessShader, decreasingly thickens the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyDecreasingThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyDepthDiscontinuityThicknessShader[#](#freestyle.shaders.pyDepthDiscontinuityThicknessShader "Link to this definition")
:   Assigns a thickness to the stroke based on the stroke’s distance
    to the camera (Z-value).

    shade(*stroke*)[#](#freestyle.shaders.pyDepthDiscontinuityThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyDiffusion2Shader[#](#freestyle.shaders.pyDiffusion2Shader "Link to this definition")
:   Iteratively adds an offset to the position of each stroke vertex
    in the direction perpendicular to the stroke direction at the
    point. The offset is scaled by the 2D curvature (i.e. how quickly
    the stroke curve is) at the point.

    shade(*stroke*)[#](#freestyle.shaders.pyDiffusion2Shader.shade "Link to this definition")

*class* freestyle.shaders.pyFXSVaryingThicknessWithDensityShader[#](#freestyle.shaders.pyFXSVaryingThicknessWithDensityShader "Link to this definition")
:   Assigns thickness to a stroke based on the density of the diffuse map.

    shade(*stroke*)[#](#freestyle.shaders.pyFXSVaryingThicknessWithDensityShader.shade "Link to this definition")

*class* freestyle.shaders.pyGuidingLineShader[#](#freestyle.shaders.pyGuidingLineShader "Link to this definition")
:   shade(*stroke*)[#](#freestyle.shaders.pyGuidingLineShader.shade "Link to this definition")

*class* freestyle.shaders.pyHLRShader[#](#freestyle.shaders.pyHLRShader "Link to this definition")
:   Controls visibility based upon the quantitative invisibility (QI)
    based on hidden line removal (HLR).

    shade(*stroke*)[#](#freestyle.shaders.pyHLRShader.shade "Link to this definition")

*class* freestyle.shaders.pyImportance2DThicknessShader[#](#freestyle.shaders.pyImportance2DThicknessShader "Link to this definition")
:   Assigns thickness based on distance to a given point in 2D space.
    the thickness is inverted, so the vertices closest to the
    specified point have the lowest thickness.

    shade(*stroke*)[#](#freestyle.shaders.pyImportance2DThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyImportance3DThicknessShader[#](#freestyle.shaders.pyImportance3DThicknessShader "Link to this definition")
:   Assigns thickness based on distance to a given point in 3D space.

    shade(*stroke*)[#](#freestyle.shaders.pyImportance3DThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyIncreasingColorShader[#](#freestyle.shaders.pyIncreasingColorShader "Link to this definition")
:   Fades from one color to another along the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyIncreasingColorShader.shade "Link to this definition")

*class* freestyle.shaders.pyIncreasingThicknessShader[#](#freestyle.shaders.pyIncreasingThicknessShader "Link to this definition")
:   Increasingly thickens the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyIncreasingThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyInterpolateColorShader[#](#freestyle.shaders.pyInterpolateColorShader "Link to this definition")
:   Fades from one color to another and back.

    shade(*stroke*)[#](#freestyle.shaders.pyInterpolateColorShader.shade "Link to this definition")

*class* freestyle.shaders.pyLengthDependingBackboneStretcherShader[#](#freestyle.shaders.pyLengthDependingBackboneStretcherShader "Link to this definition")
:   Stretches the stroke’s backbone proportional to the stroke’s length
    NOTE: you’ll probably want an l somewhere between (0.5 - 0). A value that
    is too high may yield unexpected results.

    shade(*stroke*)[#](#freestyle.shaders.pyLengthDependingBackboneStretcherShader.shade "Link to this definition")

*class* freestyle.shaders.pyMaterialColorShader[#](#freestyle.shaders.pyMaterialColorShader "Link to this definition")
:   Assigns the color of the underlying material to the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyMaterialColorShader.shade "Link to this definition")

*class* freestyle.shaders.pyModulateAlphaShader[#](#freestyle.shaders.pyModulateAlphaShader "Link to this definition")
:   Limits the stroke’s alpha between a min and max value.

    shade(*stroke*)[#](#freestyle.shaders.pyModulateAlphaShader.shade "Link to this definition")

*class* freestyle.shaders.pyNonLinearVaryingThicknessShader[#](#freestyle.shaders.pyNonLinearVaryingThicknessShader "Link to this definition")
:   Assigns thickness to a stroke based on an exponential function.

    shade(*stroke*)[#](#freestyle.shaders.pyNonLinearVaryingThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pyPerlinNoise1DShader[#](#freestyle.shaders.pyPerlinNoise1DShader "Link to this definition")
:   Displaces the stroke using the curvilinear abscissa. This means
    that lines with the same length and sampling interval will be
    identically distorted.

    shade(*stroke*)[#](#freestyle.shaders.pyPerlinNoise1DShader.shade "Link to this definition")

*class* freestyle.shaders.pyPerlinNoise2DShader[#](#freestyle.shaders.pyPerlinNoise2DShader "Link to this definition")
:   Displaces the stroke using the strokes coordinates. This means
    that in a scene no strokes will be distorted identically.

    More information on the noise shaders can be found at:
    <https://freestyleintegration.wordpress.com/2011/09/25/development-updates-on-september-25/>

    shade(*stroke*)[#](#freestyle.shaders.pyPerlinNoise2DShader.shade "Link to this definition")

*class* freestyle.shaders.pyRandomColorShader[#](#freestyle.shaders.pyRandomColorShader "Link to this definition")
:   Assigns a color to the stroke based on given seed.

    shade(*stroke*)[#](#freestyle.shaders.pyRandomColorShader.shade "Link to this definition")

*class* freestyle.shaders.pySLERPThicknessShader[#](#freestyle.shaders.pySLERPThicknessShader "Link to this definition")
:   Assigns thickness to a stroke based on spherical linear interpolation.

    shade(*stroke*)[#](#freestyle.shaders.pySLERPThicknessShader.shade "Link to this definition")

*class* freestyle.shaders.pySamplingShader[#](#freestyle.shaders.pySamplingShader "Link to this definition")
:   Resamples the stroke, which gives the stroke the amount of
    vertices specified.

    shade(*stroke*)[#](#freestyle.shaders.pySamplingShader.shade "Link to this definition")

*class* freestyle.shaders.pySinusDisplacementShader[#](#freestyle.shaders.pySinusDisplacementShader "Link to this definition")
:   Displaces the stroke in the shape of a sine wave.

    shade(*stroke*)[#](#freestyle.shaders.pySinusDisplacementShader.shade "Link to this definition")

*class* freestyle.shaders.pyTVertexRemoverShader[#](#freestyle.shaders.pyTVertexRemoverShader "Link to this definition")
:   Removes t-vertices from the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyTVertexRemoverShader.shade "Link to this definition")

*class* freestyle.shaders.pyTVertexThickenerShader[#](#freestyle.shaders.pyTVertexThickenerShader "Link to this definition")
:   Thickens TVertices (visual intersections between two edges).

    shade(*stroke*)[#](#freestyle.shaders.pyTVertexThickenerShader.shade "Link to this definition")

*class* freestyle.shaders.pyTimeColorShader[#](#freestyle.shaders.pyTimeColorShader "Link to this definition")
:   Assigns a grayscale value that increases for every vertex.
    The brightness will increase along the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyTimeColorShader.shade "Link to this definition")

*class* freestyle.shaders.pyTipRemoverShader[#](#freestyle.shaders.pyTipRemoverShader "Link to this definition")
:   Removes the tips of the stroke.

    shade(*stroke*)[#](#freestyle.shaders.pyTipRemoverShader.shade "Link to this definition")

    Undocumented

*class* freestyle.shaders.pyZDependingThicknessShader[#](#freestyle.shaders.pyZDependingThicknessShader "Link to this definition")
:   Assigns thickness based on an object’s local Z depth (point
    closest to camera is 1, point furthest from camera is zero).

    shade(*stroke*)[#](#freestyle.shaders.pyZDependingThicknessShader.shade "Link to this definition")

[Next

Freestyle Utilities (freestyle.utils)](../utils/index.md)
[Previous

Freestyle Chaining Iterators (freestyle.chainingiterators)](../chainingiterators/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60freestyle.shaders.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Ffreestyle.shaders.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Freestyle Shaders (freestyle.shaders)
  + [`BackboneStretcherShader`](#freestyle.shaders.BackboneStretcherShader)
    - [`BackboneStretcherShader.__init__()`](#freestyle.shaders.BackboneStretcherShader.__init__)
    - [`BackboneStretcherShader.shade()`](#freestyle.shaders.BackboneStretcherShader.shade)
  + [`BezierCurveShader`](#freestyle.shaders.BezierCurveShader)
    - [`BezierCurveShader.__init__()`](#freestyle.shaders.BezierCurveShader.__init__)
    - [`BezierCurveShader.shade()`](#freestyle.shaders.BezierCurveShader.shade)
  + [`BlenderTextureShader`](#freestyle.shaders.BlenderTextureShader)
    - [`BlenderTextureShader.__init__()`](#freestyle.shaders.BlenderTextureShader.__init__)
    - [`BlenderTextureShader.shade()`](#freestyle.shaders.BlenderTextureShader.shade)
  + [`CalligraphicShader`](#freestyle.shaders.CalligraphicShader)
    - [`CalligraphicShader.__init__()`](#freestyle.shaders.CalligraphicShader.__init__)
    - [`CalligraphicShader.shade()`](#freestyle.shaders.CalligraphicShader.shade)
  + [`ColorNoiseShader`](#freestyle.shaders.ColorNoiseShader)
    - [`ColorNoiseShader.__init__()`](#freestyle.shaders.ColorNoiseShader.__init__)
    - [`ColorNoiseShader.shade()`](#freestyle.shaders.ColorNoiseShader.shade)
  + [`ConstantColorShader`](#freestyle.shaders.ConstantColorShader)
    - [`ConstantColorShader.__init__()`](#freestyle.shaders.ConstantColorShader.__init__)
    - [`ConstantColorShader.shade()`](#freestyle.shaders.ConstantColorShader.shade)
  + [`ConstantThicknessShader`](#freestyle.shaders.ConstantThicknessShader)
    - [`ConstantThicknessShader.__init__()`](#freestyle.shaders.ConstantThicknessShader.__init__)
    - [`ConstantThicknessShader.shade()`](#freestyle.shaders.ConstantThicknessShader.shade)
  + [`ConstrainedIncreasingThicknessShader`](#freestyle.shaders.ConstrainedIncreasingThicknessShader)
    - [`ConstrainedIncreasingThicknessShader.__init__()`](#freestyle.shaders.ConstrainedIncreasingThicknessShader.__init__)
    - [`ConstrainedIncreasingThicknessShader.shade()`](#freestyle.shaders.ConstrainedIncreasingThicknessShader.shade)
  + [`GuidingLinesShader`](#freestyle.shaders.GuidingLinesShader)
    - [`GuidingLinesShader.__init__()`](#freestyle.shaders.GuidingLinesShader.__init__)
    - [`GuidingLinesShader.shade()`](#freestyle.shaders.GuidingLinesShader.shade)
  + [`IncreasingColorShader`](#freestyle.shaders.IncreasingColorShader)
    - [`IncreasingColorShader.__init__()`](#freestyle.shaders.IncreasingColorShader.__init__)
    - [`IncreasingColorShader.shade()`](#freestyle.shaders.IncreasingColorShader.shade)
  + [`IncreasingThicknessShader`](#freestyle.shaders.IncreasingThicknessShader)
    - [`IncreasingThicknessShader.__init__()`](#freestyle.shaders.IncreasingThicknessShader.__init__)
    - [`IncreasingThicknessShader.shade()`](#freestyle.shaders.IncreasingThicknessShader.shade)
  + [`PolygonalizationShader`](#freestyle.shaders.PolygonalizationShader)
    - [`PolygonalizationShader.__init__()`](#freestyle.shaders.PolygonalizationShader.__init__)
    - [`PolygonalizationShader.shade()`](#freestyle.shaders.PolygonalizationShader.shade)
  + [`RoundCapShader`](#freestyle.shaders.RoundCapShader)
    - [`RoundCapShader.round_cap_thickness()`](#freestyle.shaders.RoundCapShader.round_cap_thickness)
    - [`RoundCapShader.shade()`](#freestyle.shaders.RoundCapShader.shade)
  + [`SamplingShader`](#freestyle.shaders.SamplingShader)
    - [`SamplingShader.__init__()`](#freestyle.shaders.SamplingShader.__init__)
    - [`SamplingShader.shade()`](#freestyle.shaders.SamplingShader.shade)
  + [`SmoothingShader`](#freestyle.shaders.SmoothingShader)
    - [`SmoothingShader.__init__()`](#freestyle.shaders.SmoothingShader.__init__)
    - [`SmoothingShader.shade()`](#freestyle.shaders.SmoothingShader.shade)
  + [`SpatialNoiseShader`](#freestyle.shaders.SpatialNoiseShader)
    - [`SpatialNoiseShader.__init__()`](#freestyle.shaders.SpatialNoiseShader.__init__)
    - [`SpatialNoiseShader.shade()`](#freestyle.shaders.SpatialNoiseShader.shade)
  + [`SquareCapShader`](#freestyle.shaders.SquareCapShader)
    - [`SquareCapShader.shade()`](#freestyle.shaders.SquareCapShader.shade)
  + [`StrokeTextureStepShader`](#freestyle.shaders.StrokeTextureStepShader)
    - [`StrokeTextureStepShader.__init__()`](#freestyle.shaders.StrokeTextureStepShader.__init__)
    - [`StrokeTextureStepShader.shade()`](#freestyle.shaders.StrokeTextureStepShader.shade)
  + [`ThicknessNoiseShader`](#freestyle.shaders.ThicknessNoiseShader)
    - [`ThicknessNoiseShader.__init__()`](#freestyle.shaders.ThicknessNoiseShader.__init__)
    - [`ThicknessNoiseShader.shade()`](#freestyle.shaders.ThicknessNoiseShader.shade)
  + [`TipRemoverShader`](#freestyle.shaders.TipRemoverShader)
    - [`TipRemoverShader.__init__()`](#freestyle.shaders.TipRemoverShader.__init__)
    - [`TipRemoverShader.shade()`](#freestyle.shaders.TipRemoverShader.shade)
  + [`py2DCurvatureColorShader`](#freestyle.shaders.py2DCurvatureColorShader)
    - [`py2DCurvatureColorShader.shade()`](#freestyle.shaders.py2DCurvatureColorShader.shade)
  + [`pyBackboneStretcherNoCuspShader`](#freestyle.shaders.pyBackboneStretcherNoCuspShader)
    - [`pyBackboneStretcherNoCuspShader.shade()`](#freestyle.shaders.pyBackboneStretcherNoCuspShader.shade)
  + [`pyBackboneStretcherShader`](#freestyle.shaders.pyBackboneStretcherShader)
    - [`pyBackboneStretcherShader.shade()`](#freestyle.shaders.pyBackboneStretcherShader.shade)
  + [`pyBluePrintCirclesShader`](#freestyle.shaders.pyBluePrintCirclesShader)
    - [`pyBluePrintCirclesShader.shade()`](#freestyle.shaders.pyBluePrintCirclesShader.shade)
  + [`pyBluePrintDirectedSquaresShader`](#freestyle.shaders.pyBluePrintDirectedSquaresShader)
    - [`pyBluePrintDirectedSquaresShader.shade()`](#freestyle.shaders.pyBluePrintDirectedSquaresShader.shade)
  + [`pyBluePrintEllipsesShader`](#freestyle.shaders.pyBluePrintEllipsesShader)
    - [`pyBluePrintEllipsesShader.shade()`](#freestyle.shaders.pyBluePrintEllipsesShader.shade)
  + [`pyBluePrintSquaresShader`](#freestyle.shaders.pyBluePrintSquaresShader)
    - [`pyBluePrintSquaresShader.shade()`](#freestyle.shaders.pyBluePrintSquaresShader.shade)
  + [`pyConstantColorShader`](#freestyle.shaders.pyConstantColorShader)
    - [`pyConstantColorShader.shade()`](#freestyle.shaders.pyConstantColorShader.shade)
  + [`pyConstantThicknessShader`](#freestyle.shaders.pyConstantThicknessShader)
    - [`pyConstantThicknessShader.shade()`](#freestyle.shaders.pyConstantThicknessShader.shade)
  + [`pyConstrainedIncreasingThicknessShader`](#freestyle.shaders.pyConstrainedIncreasingThicknessShader)
    - [`pyConstrainedIncreasingThicknessShader.shade()`](#freestyle.shaders.pyConstrainedIncreasingThicknessShader.shade)
  + [`pyDecreasingThicknessShader`](#freestyle.shaders.pyDecreasingThicknessShader)
    - [`pyDecreasingThicknessShader.shade()`](#freestyle.shaders.pyDecreasingThicknessShader.shade)
  + [`pyDepthDiscontinuityThicknessShader`](#freestyle.shaders.pyDepthDiscontinuityThicknessShader)
    - [`pyDepthDiscontinuityThicknessShader.shade()`](#freestyle.shaders.pyDepthDiscontinuityThicknessShader.shade)
  + [`pyDiffusion2Shader`](#freestyle.shaders.pyDiffusion2Shader)
    - [`pyDiffusion2Shader.shade()`](#freestyle.shaders.pyDiffusion2Shader.shade)
  + [`pyFXSVaryingThicknessWithDensityShader`](#freestyle.shaders.pyFXSVaryingThicknessWithDensityShader)
    - [`pyFXSVaryingThicknessWithDensityShader.shade()`](#freestyle.shaders.pyFXSVaryingThicknessWithDensityShader.shade)
  + [`pyGuidingLineShader`](#freestyle.shaders.pyGuidingLineShader)
    - [`pyGuidingLineShader.shade()`](#freestyle.shaders.pyGuidingLineShader.shade)
  + [`pyHLRShader`](#freestyle.shaders.pyHLRShader)
    - [`pyHLRShader.shade()`](#freestyle.shaders.pyHLRShader.shade)
  + [`pyImportance2DThicknessShader`](#freestyle.shaders.pyImportance2DThicknessShader)
    - [`pyImportance2DThicknessShader.shade()`](#freestyle.shaders.pyImportance2DThicknessShader.shade)
  + [`pyImportance3DThicknessShader`](#freestyle.shaders.pyImportance3DThicknessShader)
    - [`pyImportance3DThicknessShader.shade()`](#freestyle.shaders.pyImportance3DThicknessShader.shade)
  + [`pyIncreasingColorShader`](#freestyle.shaders.pyIncreasingColorShader)
    - [`pyIncreasingColorShader.shade()`](#freestyle.shaders.pyIncreasingColorShader.shade)
  + [`pyIncreasingThicknessShader`](#freestyle.shaders.pyIncreasingThicknessShader)
    - [`pyIncreasingThicknessShader.shade()`](#freestyle.shaders.pyIncreasingThicknessShader.shade)
  + [`pyInterpolateColorShader`](#freestyle.shaders.pyInterpolateColorShader)
    - [`pyInterpolateColorShader.shade()`](#freestyle.shaders.pyInterpolateColorShader.shade)
  + [`pyLengthDependingBackboneStretcherShader`](#freestyle.shaders.pyLengthDependingBackboneStretcherShader)
    - [`pyLengthDependingBackboneStretcherShader.shade()`](#freestyle.shaders.pyLengthDependingBackboneStretcherShader.shade)
  + [`pyMaterialColorShader`](#freestyle.shaders.pyMaterialColorShader)
    - [`pyMaterialColorShader.shade()`](#freestyle.shaders.pyMaterialColorShader.shade)
  + [`pyModulateAlphaShader`](#freestyle.shaders.pyModulateAlphaShader)
    - [`pyModulateAlphaShader.shade()`](#freestyle.shaders.pyModulateAlphaShader.shade)
  + [`pyNonLinearVaryingThicknessShader`](#freestyle.shaders.pyNonLinearVaryingThicknessShader)
    - [`pyNonLinearVaryingThicknessShader.shade()`](#freestyle.shaders.pyNonLinearVaryingThicknessShader.shade)
  + [`pyPerlinNoise1DShader`](#freestyle.shaders.pyPerlinNoise1DShader)
    - [`pyPerlinNoise1DShader.shade()`](#freestyle.shaders.pyPerlinNoise1DShader.shade)
  + [`pyPerlinNoise2DShader`](#freestyle.shaders.pyPerlinNoise2DShader)
    - [`pyPerlinNoise2DShader.shade()`](#freestyle.shaders.pyPerlinNoise2DShader.shade)
  + [`pyRandomColorShader`](#freestyle.shaders.pyRandomColorShader)
    - [`pyRandomColorShader.shade()`](#freestyle.shaders.pyRandomColorShader.shade)
  + [`pySLERPThicknessShader`](#freestyle.shaders.pySLERPThicknessShader)
    - [`pySLERPThicknessShader.shade()`](#freestyle.shaders.pySLERPThicknessShader.shade)
  + [`pySamplingShader`](#freestyle.shaders.pySamplingShader)
    - [`pySamplingShader.shade()`](#freestyle.shaders.pySamplingShader.shade)
  + [`pySinusDisplacementShader`](#freestyle.shaders.pySinusDisplacementShader)
    - [`pySinusDisplacementShader.shade()`](#freestyle.shaders.pySinusDisplacementShader.shade)
  + [`pyTVertexRemoverShader`](#freestyle.shaders.pyTVertexRemoverShader)
    - [`pyTVertexRemoverShader.shade()`](#freestyle.shaders.pyTVertexRemoverShader.shade)
  + [`pyTVertexThickenerShader`](#freestyle.shaders.pyTVertexThickenerShader)
    - [`pyTVertexThickenerShader.shade()`](#freestyle.shaders.pyTVertexThickenerShader.shade)
  + [`pyTimeColorShader`](#freestyle.shaders.pyTimeColorShader)
    - [`pyTimeColorShader.shade()`](#freestyle.shaders.pyTimeColorShader.shade)
  + [`pyTipRemoverShader`](#freestyle.shaders.pyTipRemoverShader)
    - [`pyTipRemoverShader.shade()`](#freestyle.shaders.pyTipRemoverShader.shade)
  + [`pyZDependingThicknessShader`](#freestyle.shaders.pyZDependingThicknessShader)
    - [`pyZDependingThicknessShader.shade()`](#freestyle.shaders.pyZDependingThicknessShader.shade)