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
* [BMesh Module (bmesh)](../../../meta/index.md)[x]

  Toggle navigation of BMesh Module (bmesh)

  + BMesh Operators (bmesh.ops)
  + [BMesh Types (bmesh.types)](../types/index.md)
  + [BMesh Utilities (bmesh.utils)](../utils/index.md)
  + [BMesh Geometry Utilities (bmesh.geometry)](../geometry/index.md)
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

# BMesh Operators (bmesh.ops)[#](#module-bmesh.ops "Link to this heading")

This module gives access to low level bmesh operations.

Most operators take input and return output, they can be chained together
to perform useful operations.

## Operator Example[#](#operator-example "Link to this heading")

This script shows how operators can be used to model a link of a chain.

```
# This script uses bmesh operators to make 2 links of a chain.

import bpy
import bmesh
import math
import mathutils

# Make a new BMesh
bm = bmesh.new()

# Add a circle XXX, should return all geometry created, not just verts.
bmesh.ops.create_circle(
    bm,
    cap_ends=False,
    radius=0.2,
    segments=8)

# Spin and deal with geometry on side 'a'
edges_start_a = bm.edges[:]
geom_start_a = bm.verts[:] + edges_start_a
ret = bmesh.ops.spin(
    bm,
    geom=geom_start_a,
    angle=math.radians(180.0),
    steps=8,
    axis=(1.0, 0.0, 0.0),
    cent=(0.0, 1.0, 0.0))
edges_end_a = [ele for ele in ret["geom_last"]
               if isinstance(ele, bmesh.types.BMEdge)]
del ret

# Extrude and create geometry on side 'b'
ret = bmesh.ops.extrude_edge_only(
    bm,
    edges=edges_start_a)
geom_extrude_mid = ret["geom"]
del ret

# Collect the edges to spin XXX, 'extrude_edge_only' could return this.
verts_extrude_b = [ele for ele in geom_extrude_mid
                   if isinstance(ele, bmesh.types.BMVert)]
edges_extrude_b = [ele for ele in geom_extrude_mid
                   if isinstance(ele, bmesh.types.BMEdge) and ele.is_boundary]
bmesh.ops.translate(
    bm,
    verts=verts_extrude_b,
    vec=(0.0, 0.0, 1.0))

# Create the circle on side 'b'
ret = bmesh.ops.spin(
    bm,
    geom=verts_extrude_b + edges_extrude_b,
    angle=-math.radians(180.0),
    steps=8,
    axis=(1.0, 0.0, 0.0),
    cent=(0.0, 1.0, 1.0))
edges_end_b = [ele for ele in ret["geom_last"]
               if isinstance(ele, bmesh.types.BMEdge)]
del ret

# Bridge the resulting edge loops of both spins 'a & b'
bmesh.ops.bridge_loops(
    bm,
    edges=edges_end_a + edges_end_b)

# Now we have made a links of the chain, make a copy and rotate it
# (so this looks something like a chain)

ret = bmesh.ops.duplicate(
    bm,
    geom=bm.verts[:] + bm.edges[:] + bm.faces[:])
geom_dupe = ret["geom"]
verts_dupe = [ele for ele in geom_dupe if isinstance(ele, bmesh.types.BMVert)]
del ret

# position the new link
bmesh.ops.translate(
    bm,
    verts=verts_dupe,
    vec=(0.0, 0.0, 2.0))
bmesh.ops.rotate(
    bm,
    verts=verts_dupe,
    cent=(0.0, 1.0, 0.0),
    matrix=mathutils.Matrix.Rotation(math.radians(90.0), 3, 'Z'))

# Done with creating the mesh, simply link it into the scene so we can see it

# Finish up, write the bmesh into a new mesh
me = bpy.data.meshes.new("Mesh")
bm.to_mesh(me)
bm.free()

# Add the mesh to the scene
obj = bpy.data.objects.new("Object", me)
bpy.context.collection.objects.link(obj)

# Select and make active
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
```

bmesh.ops.smooth\_vert(*bm*, *verts=[]*, *factor=0*, *mirror\_clip\_x=False*, *mirror\_clip\_y=False*, *mirror\_clip\_z=False*, *clip\_dist=0*, *use\_axis\_x=False*, *use\_axis\_y=False*, *use\_axis\_z=False*)[#](#bmesh.ops.smooth_vert "Link to this definition")
:   Vertex Smooth.

    Smooths vertices by using a basic vertex averaging scheme.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **factor** (*float*) – smoothing factor
        * **mirror\_clip\_x** (*bool*) – set vertices close to the x axis before the operation to 0
        * **mirror\_clip\_y** (*bool*) – set vertices close to the y axis before the operation to 0
        * **mirror\_clip\_z** (*bool*) – set vertices close to the z axis before the operation to 0
        * **clip\_dist** (*float*) – clipping threshold for the above three slots
        * **use\_axis\_x** (*bool*) – smooth vertices along X axis
        * **use\_axis\_y** (*bool*) – smooth vertices along Y axis
        * **use\_axis\_z** (*bool*) – smooth vertices along Z axis

bmesh.ops.smooth\_laplacian\_vert(*bm*, *verts=[]*, *lambda\_factor=0*, *lambda\_border=0*, *use\_x=False*, *use\_y=False*, *use\_z=False*, *preserve\_volume=False*)[#](#bmesh.ops.smooth_laplacian_vert "Link to this definition")
:   Vertex Smooth Laplacian.

    Smooths vertices by using Laplacian smoothing propose by.
    Desbrun, et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **lambda\_factor** (*float*) – lambda param
        * **lambda\_border** (*float*) – lambda param in border
        * **use\_x** (*bool*) – Smooth object along X axis
        * **use\_y** (*bool*) – Smooth object along Y axis
        * **use\_z** (*bool*) – Smooth object along Z axis
        * **preserve\_volume** (*bool*) – Apply volume preservation after smooth

bmesh.ops.recalc\_face\_normals(*bm*, *faces=[]*)[#](#bmesh.ops.recalc_face_normals "Link to this definition")
:   Right-Hand Faces.

    Computes an “outside” normal for the specified input faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces

bmesh.ops.planar\_faces(*bm*, *faces=[]*, *iterations=0*, *factor=0*)[#](#bmesh.ops.planar_faces "Link to this definition")
:   Planar Faces.

    Iteratively flatten faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry.
        * **iterations** (*int*) – Number of times to flatten faces (for when connected faces are used)
        * **factor** (*float*) – Influence for making planar each iteration

    Returns:
    :   * `geom`: output slot, computed boundary geometry.

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.region\_extend(*bm*, *geom=[]*, *use\_contract=False*, *use\_faces=False*, *use\_face\_step=False*)[#](#bmesh.ops.region_extend "Link to this definition")
:   Region Extend.

    used to implement the select more/less tools.
    this puts some geometry surrounding regions of
    geometry in geom into geom.out.

    if use\_faces is 0 then geom.out spits out verts and edges,
    otherwise it spits out faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **use\_contract** (*bool*) – find boundary inside the regions, not outside.
        * **use\_faces** (*bool*) – extend from faces instead of edges
        * **use\_face\_step** (*bool*) – step over connected faces

    Returns:
    :   * `geom`: output slot, computed boundary geometry.

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.rotate\_edges(*bm*, *edges=[]*, *use\_ccw=False*)[#](#bmesh.ops.rotate_edges "Link to this definition")
:   Edge Rotate.

    Rotates edges topologically. Also known as “spin edge” to some people.
    Simple example: [/] becomes [|] then [].

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **use\_ccw** (*bool*) – rotate edge counter-clockwise if true, otherwise clockwise

    Returns:
    :   * `edges`: newly spun edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.reverse\_faces(*bm*, *faces=[]*, *flip\_multires=False*)[#](#bmesh.ops.reverse_faces "Link to this definition")
:   Reverse Faces.

    Reverses the winding (vertex order) of faces.
    This has the effect of flipping the normal.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **flip\_multires** (*bool*) – maintain multi-res offset

bmesh.ops.flip\_quad\_tessellation(*bm*, *faces=[]*)[#](#bmesh.ops.flip_quad_tessellation "Link to this definition")
:   Flip Quad Tessellation

    Flip the tessellation direction of the selected quads.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – Undocumented.

bmesh.ops.bisect\_edges(*bm*, *edges=[]*, *cuts=0*, *edge\_percents={}*)[#](#bmesh.ops.bisect_edges "Link to this definition")
:   Edge Bisect.

    Splits input edges (but doesn’t do anything else).
    This creates a 2-valence vert.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **cuts** (*int*) – number of cuts
        * **edge\_percents** (*dict mapping vert/edge/face types to float*) – Undocumented.

    Returns:
    :   * `geom_split`: newly created vertices and edges

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.mirror(*bm*, *geom=[]*, *matrix=mathutils.Matrix.Identity(4)*, *merge\_dist=0*, *axis='X'*, *mirror\_u=False*, *mirror\_v=False*, *mirror\_udim=False*, *use\_shapekey=False*)[#](#bmesh.ops.mirror "Link to this definition")
:   Mirror.

    Mirrors geometry along an axis. The resulting geometry is welded on using
    merge\_dist. Pairs of original/mirrored vertices are welded using the merge\_dist
    parameter (which defines the minimum distance for welding to happen).

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix defining the mirror transformation
        * **merge\_dist** (*float*) – maximum distance for merging. does no merging if 0.
        * **axis** (*enum in* *[**'X'**,* *'Y'**,* *'Z'**]**,* *default 'X'*) – the axis to use.
        * **mirror\_u** (*bool*) – mirror UVs across the u axis
        * **mirror\_v** (*bool*) – mirror UVs across the v axis
        * **mirror\_udim** (*bool*) – mirror UVs in each tile
        * **use\_shapekey** (*bool*) – Transform shape keys too.

    Returns:
    :   * `geom`: output geometry, mirrored

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.find\_doubles(*bm*, *verts=[]*, *keep\_verts=[]*, *dist=0*)[#](#bmesh.ops.find_doubles "Link to this definition")
:   Find Doubles.

    Takes input verts and find vertices they should weld to.
    Outputs a mapping slot suitable for use with the weld verts BMOP.

    If keep\_verts is used, vertices outside that set can only be merged
    with vertices in that set.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **keep\_verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – list of verts to keep
        * **dist** (*float*) – maximum distance

    Returns:
    :   * `targetmap`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")

    Return type:
    :   dict with string keys

bmesh.ops.remove\_doubles(*bm*, *verts=[]*, *dist=0*)[#](#bmesh.ops.remove_doubles "Link to this definition")
:   Remove Doubles.

    Finds groups of vertices closer than dist and merges them together,
    using the weld verts BMOP.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input verts
        * **dist** (*float*) – minimum distance

bmesh.ops.collapse(*bm*, *edges=[]*, *uvs=False*)[#](#bmesh.ops.collapse "Link to this definition")
:   Collapse Connected.

    Collapses connected vertices

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **uvs** (*bool*) – also collapse UVs and such

bmesh.ops.pointmerge\_facedata(*bm*, *verts=[]*, *vert\_snap*)[#](#bmesh.ops.pointmerge_facedata "Link to this definition")
:   Face-Data Point Merge.

    Merge uv/vcols at a specific vertex.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **vert\_snap** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – snap vertex

bmesh.ops.average\_vert\_facedata(*bm*, *verts=[]*)[#](#bmesh.ops.average_vert_facedata "Link to this definition")
:   Average Vertices Face-vert Data.

    Merge uv/vcols associated with the input vertices at
    the bounding box center. (I know, it’s not averaging but
    the vert\_snap\_to\_bb\_center is just too long).

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices

bmesh.ops.pointmerge(*bm*, *verts=[]*, *merge\_co=mathutils.Vector()*)[#](#bmesh.ops.pointmerge "Link to this definition")
:   Point Merge.

    Merge verts together at a point.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices (all verts will be merged into the first).
        * **merge\_co** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – Position to merge at.

bmesh.ops.collapse\_uvs(*bm*, *edges=[]*)[#](#bmesh.ops.collapse_uvs "Link to this definition")
:   Collapse Connected UVs.

    Collapses connected UV vertices.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges

bmesh.ops.weld\_verts(*bm*, *targetmap={}*)[#](#bmesh.ops.weld_verts "Link to this definition")
:   Weld Verts.

    Welds verts together (kind-of like remove doubles, merge, etc, all of which
    use or will use this BMOP). You pass in mappings from vertices to the vertices
    they weld with.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **targetmap** (dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")) – maps welded vertices to verts they should weld to

bmesh.ops.create\_vert(*bm*, *co=mathutils.Vector()*)[#](#bmesh.ops.create_vert "Link to this definition")
:   Make Vertex.

    Creates a single vertex; this BMOP was necessary
    for click-create-vertex.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **co** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – the coordinate of the new vert

    Returns:
    :   * `vert`: the new vert

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.join\_triangles(*bm*, *faces=[]*, *cmp\_seam=False*, *cmp\_sharp=False*, *cmp\_uvs=False*, *cmp\_vcols=False*, *cmp\_materials=False*, *angle\_face\_threshold=0*, *angle\_shape\_threshold=0*)[#](#bmesh.ops.join_triangles "Link to this definition")
:   Join Triangles.

    Tries to intelligently join triangles according
    to angle threshold and delimiters.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry.
        * **cmp\_seam** (*bool*) – Compare seam
        * **cmp\_sharp** (*bool*) – Compare sharp
        * **cmp\_uvs** (*bool*) – Compare UVs
        * **cmp\_vcols** (*bool*) – compare VCols
        * **cmp\_materials** (*bool*) – compare materials
        * **angle\_face\_threshold** (*float*) – Undocumented.
        * **angle\_shape\_threshold** (*float*) – Undocumented.

    Returns:
    :   * `faces`: joined faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.contextual\_create(*bm*, *geom=[]*, *mat\_nr=0*, *use\_smooth=False*)[#](#bmesh.ops.contextual_create "Link to this definition")
:   Contextual Create.

    This is basically F-key, it creates
    new faces from vertices, makes stuff from edge nets,
    makes wire edges, etc. It also dissolves faces.

    Three verts become a triangle, four become a quad. Two
    become a wire edge.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry.
        * **mat\_nr** (*int*) – material to use
        * **use\_smooth** (*bool*) – smooth to use

    Returns:
    :   * `faces`: newly-made face(s)

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `edges`: newly-made edge(s)

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.bridge\_loops(*bm*, *edges=[]*, *use\_pairs=False*, *use\_cyclic=False*, *use\_merge=False*, *merge\_factor=0*, *twist\_offset=0*)[#](#bmesh.ops.bridge_loops "Link to this definition")
:   Bridge edge loops with faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **use\_pairs** (*bool*) – Undocumented.
        * **use\_cyclic** (*bool*) – Undocumented.
        * **use\_merge** (*bool*) – merge rather than creating faces
        * **merge\_factor** (*float*) – merge factor
        * **twist\_offset** (*int*) – twist offset for closed loops

    Returns:
    :   * `faces`: new faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `edges`: new edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.grid\_fill(*bm*, *edges=[]*, *mat\_nr=0*, *use\_smooth=False*, *use\_interp\_simple=False*)[#](#bmesh.ops.grid_fill "Link to this definition")
:   Grid Fill.

    Create faces defined by 2 disconnected edge loops (which share edges).

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **mat\_nr** (*int*) – material to use
        * **use\_smooth** (*bool*) – smooth state to use
        * **use\_interp\_simple** (*bool*) – use simple interpolation

    Returns:
    :   * `faces`: new faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.holes\_fill(*bm*, *edges=[]*, *sides=0*)[#](#bmesh.ops.holes_fill "Link to this definition")
:   Fill Holes.

    Fill boundary edges with faces, copying surrounding customdata.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **sides** (*int*) – number of face sides to fill

    Returns:
    :   * `faces`: new faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.face\_attribute\_fill(*bm*, *faces=[]*, *use\_normals=False*, *use\_data=False*)[#](#bmesh.ops.face_attribute_fill "Link to this definition")
:   Face Attribute Fill.

    Fill in faces with data from adjacent faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **use\_normals** (*bool*) – copy face winding
        * **use\_data** (*bool*) – copy face data

    Returns:
    :   * `faces_fail`: faces that could not be handled

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.edgeloop\_fill(*bm*, *edges=[]*, *mat\_nr=0*, *use\_smooth=False*)[#](#bmesh.ops.edgeloop_fill "Link to this definition")
:   Edge Loop Fill.

    Create faces defined by one or more non overlapping edge loops.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **mat\_nr** (*int*) – material to use
        * **use\_smooth** (*bool*) – smooth state to use

    Returns:
    :   * `faces`: new faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.edgenet\_fill(*bm*, *edges=[]*, *mat\_nr=0*, *use\_smooth=False*, *sides=0*)[#](#bmesh.ops.edgenet_fill "Link to this definition")
:   Edge Net Fill.

    Create faces defined by enclosed edges.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **mat\_nr** (*int*) – material to use
        * **use\_smooth** (*bool*) – smooth state to use
        * **sides** (*int*) – number of sides

    Returns:
    :   * `faces`: new faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.edgenet\_prepare(*bm*, *edges=[]*)[#](#bmesh.ops.edgenet_prepare "Link to this definition")
:   Edge-net Prepare.

    Identifies several useful edge loop cases and modifies them so
    they’ll become a face when edgenet\_fill is called. The cases covered are:

    * One single loop; an edge is added to connect the ends
    * Two loops; two edges are added to connect the endpoints (based on the
      shortest distance between each endpoint).

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges

    Returns:
    :   * `edges`: new edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.rotate(*bm*, *cent=mathutils.Vector()*, *matrix=mathutils.Matrix.Identity(4)*, *verts=[]*, *space=mathutils.Matrix.Identity(4)*, *use\_shapekey=False*)[#](#bmesh.ops.rotate "Link to this definition")
:   Rotate.

    Rotate vertices around a center, using a 3x3 rotation matrix.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **cent** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – center of rotation
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix defining rotation
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **space** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to define the space (typically object matrix)
        * **use\_shapekey** (*bool*) – Transform shape keys too.

bmesh.ops.translate(*bm*, *vec=mathutils.Vector()*, *space=mathutils.Matrix.Identity(4)*, *verts=[]*, *use\_shapekey=False*)[#](#bmesh.ops.translate "Link to this definition")
:   Translate.

    Translate vertices by an offset.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **vec** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – translation offset
        * **space** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to define the space (typically object matrix)
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **use\_shapekey** (*bool*) – Transform shape keys too.

bmesh.ops.scale(*bm*, *vec=mathutils.Vector()*, *space=mathutils.Matrix.Identity(4)*, *verts=[]*, *use\_shapekey=False*)[#](#bmesh.ops.scale "Link to this definition")
:   Scale.

    Scales vertices by an offset.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **vec** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – scale factor
        * **space** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to define the space (typically object matrix)
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **use\_shapekey** (*bool*) – Transform shape keys too.

bmesh.ops.transform(*bm*, *matrix=mathutils.Matrix.Identity(4)*, *space=mathutils.Matrix.Identity(4)*, *verts=[]*, *use\_shapekey=False*)[#](#bmesh.ops.transform "Link to this definition")
:   Transform.

    Transforms a set of vertices by a matrix. Multiplies
    the vertex coordinates with the matrix.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – transform matrix
        * **space** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to define the space (typically object matrix)
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **use\_shapekey** (*bool*) – Transform shape keys too.

bmesh.ops.object\_load\_bmesh(*bm*, *scene*, *object*)[#](#bmesh.ops.object_load_bmesh "Link to this definition")
:   Object Load BMesh.

    Loads a bmesh into an object/mesh. This is a “private”
    BMOP.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **scene** ([`bpy.types.Scene`](../../bpy/types/Scene.md#bpy.types.Scene "bpy.types.Scene")) – pointer to an scene structure
        * **object** ([`bpy.types.Object`](../../bpy/types/Object.md#bpy.types.Object "bpy.types.Object")) – pointer to an object structure

bmesh.ops.bmesh\_to\_mesh(*bm*, *mesh*, *object*)[#](#bmesh.ops.bmesh_to_mesh "Link to this definition")
:   BMesh to Mesh.

    Converts a bmesh to a Mesh. This is reserved for exiting editmode.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **mesh** ([`bpy.types.Mesh`](../../bpy/types/Mesh.md#bpy.types.Mesh "bpy.types.Mesh")) – pointer to a mesh structure to fill in
        * **object** ([`bpy.types.Object`](../../bpy/types/Object.md#bpy.types.Object "bpy.types.Object")) – pointer to an object structure

bmesh.ops.mesh\_to\_bmesh(*bm*, *mesh*, *object*, *use\_shapekey=False*)[#](#bmesh.ops.mesh_to_bmesh "Link to this definition")
:   Mesh to BMesh.

    Load the contents of a mesh into the bmesh. this BMOP is private, it’s
    reserved exclusively for entering editmode.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **mesh** ([`bpy.types.Mesh`](../../bpy/types/Mesh.md#bpy.types.Mesh "bpy.types.Mesh")) – pointer to a Mesh structure
        * **object** ([`bpy.types.Object`](../../bpy/types/Object.md#bpy.types.Object "bpy.types.Object")) – pointer to an Object structure
        * **use\_shapekey** (*bool*) – load active shapekey coordinates into verts

bmesh.ops.extrude\_discrete\_faces(*bm*, *faces=[]*, *use\_normal\_flip=False*, *use\_select\_history=False*)[#](#bmesh.ops.extrude_discrete_faces "Link to this definition")
:   Individual Face Extrude.

    Extrudes faces individually.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **use\_normal\_flip** (*bool*) – Create faces with reversed direction.
        * **use\_select\_history** (*bool*) – pass to duplicate

    Returns:
    :   * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.extrude\_edge\_only(*bm*, *edges=[]*, *use\_normal\_flip=False*, *use\_select\_history=False*)[#](#bmesh.ops.extrude_edge_only "Link to this definition")
:   Extrude Only Edges.

    Extrudes Edges into faces, note that this is very simple, there’s no fancy
    winged extrusion.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input vertices
        * **use\_normal\_flip** (*bool*) – Create faces with reversed direction.
        * **use\_select\_history** (*bool*) – pass to duplicate

    Returns:
    :   * `geom`: output geometry

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.extrude\_vert\_indiv(*bm*, *verts=[]*, *use\_select\_history=False*)[#](#bmesh.ops.extrude_vert_indiv "Link to this definition")
:   Individual Vertex Extrude.

    Extrudes wire edges from vertices.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **use\_select\_history** (*bool*) – pass to duplicate

    Returns:
    :   * `edges`: output wire edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))
        * `verts`: output vertices

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.connect\_verts(*bm*, *verts=[]*, *faces\_exclude=[]*, *check\_degenerate=False*)[#](#bmesh.ops.connect_verts "Link to this definition")
:   Connect Verts.

    Split faces by adding edges that connect **verts**.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **faces\_exclude** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces to explicitly exclude from connecting
        * **check\_degenerate** (*bool*) – prevent splits with overlaps & intersections

    Returns:
    :   * `edges`:

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.connect\_verts\_concave(*bm*, *faces=[]*)[#](#bmesh.ops.connect_verts_concave "Link to this definition")
:   Connect Verts to form Convex Faces.

    Ensures all faces are convex **faces**.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces

    Returns:
    :   * `edges`:

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))
        * `faces`:

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.connect\_verts\_nonplanar(*bm*, *angle\_limit=0*, *faces=[]*)[#](#bmesh.ops.connect_verts_nonplanar "Link to this definition")
:   Connect Verts Across non Planer Faces.

    Split faces by connecting edges along non planer **faces**.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **angle\_limit** (*float*) – total rotation angle (radians)
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces

    Returns:
    :   * `edges`:

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))
        * `faces`:

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.connect\_vert\_pair(*bm*, *verts=[]*, *verts\_exclude=[]*, *faces\_exclude=[]*)[#](#bmesh.ops.connect_vert_pair "Link to this definition")
:   Connect Verts.

    Split faces by adding edges that connect **verts**.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **verts\_exclude** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices to explicitly exclude from connecting
        * **faces\_exclude** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces to explicitly exclude from connecting

    Returns:
    :   * `edges`:

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.extrude\_face\_region(*bm*, *geom=[]*, *edges\_exclude=set()*, *use\_keep\_orig=False*, *use\_normal\_flip=False*, *use\_normal\_from\_adjacent=False*, *use\_dissolve\_ortho\_edges=False*, *use\_select\_history=False*)[#](#bmesh.ops.extrude_face_region "Link to this definition")
:   Extrude Faces.

    Extrude operator (does not transform)

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – edges and faces
        * **edges\_exclude** (*set* *of* *vert/edge/face type*) – input edges to explicitly exclude from extrusion
        * **use\_keep\_orig** (*bool*) – keep original geometry (requires `geom` to include edges).
        * **use\_normal\_flip** (*bool*) – Create faces with reversed direction.
        * **use\_normal\_from\_adjacent** (*bool*) – Use winding from surrounding faces instead of this region.
        * **use\_dissolve\_ortho\_edges** (*bool*) – Dissolve edges whose faces form a flat surface.
        * **use\_select\_history** (*bool*) – pass to duplicate

    Returns:
    :   * `geom`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.dissolve\_verts(*bm*, *verts=[]*, *use\_face\_split=False*, *use\_boundary\_tear=False*)[#](#bmesh.ops.dissolve_verts "Link to this definition")
:   Dissolve Verts.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **use\_face\_split** (*bool*) – split off face corners to maintain surrounding geometry
        * **use\_boundary\_tear** (*bool*) – split off face corners instead of merging faces

bmesh.ops.dissolve\_edges(*bm*, *edges=[]*, *use\_verts=False*, *use\_face\_split=False*)[#](#bmesh.ops.dissolve_edges "Link to this definition")
:   Dissolve Edges.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **use\_verts** (*bool*) – dissolve verts left between only 2 edges.
        * **use\_face\_split** (*bool*) – split off face corners to maintain surrounding geometry

    Returns:
    :   * `region`:

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.dissolve\_faces(*bm*, *faces=[]*, *use\_verts=False*)[#](#bmesh.ops.dissolve_faces "Link to this definition")
:   Dissolve Faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **use\_verts** (*bool*) – dissolve verts left between only 2 edges.

    Returns:
    :   * `region`:

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.dissolve\_limit(*bm*, *angle\_limit=0*, *use\_dissolve\_boundaries=False*, *verts=[]*, *edges=[]*, *delimit=set()*)[#](#bmesh.ops.dissolve_limit "Link to this definition")
:   Limited Dissolve.

    Dissolve planar faces and co-linear edges.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **angle\_limit** (*float*) – total rotation angle (radians)
        * **use\_dissolve\_boundaries** (*bool*) – dissolve all vertices in between face boundaries
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **delimit** (*set* *of* *flags from* *[**'NORMAL'**,* *'MATERIAL'**,* *'SEAM'**,* *'SHARP'**,* *'UV'**]**,* *default set**(**)*) – delimit dissolve operation

    Returns:
    :   * `region`:

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.dissolve\_degenerate(*bm*, *dist=0*, *edges=[]*)[#](#bmesh.ops.dissolve_degenerate "Link to this definition")
:   Degenerate Dissolve.

    Dissolve edges with no length, faces with no area.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **dist** (*float*) – maximum distance to consider degenerate
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges

bmesh.ops.triangulate(*bm*, *faces=[]*, *quad\_method='BEAUTY'*, *ngon\_method='BEAUTY'*)[#](#bmesh.ops.triangulate "Link to this definition")
:   Triangulate.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **quad\_method** (*enum in* *[**'BEAUTY'**,* *'FIXED'**,* *'ALTERNATE'**,* *'SHORT\_EDGE'**,* *'LONG\_EDGE'**]**,* *default 'BEAUTY'*) – method for splitting the quads into triangles
        * **ngon\_method** (*enum in* *[**'BEAUTY'**,* *'EAR\_CLIP'**]**,* *default 'BEAUTY'*) – method for splitting the polygons into triangles

    Returns:
    :   * `edges`:

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))
        * `faces`:

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `face_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")
        * `face_map_double`: duplicate faces

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")

    Return type:
    :   dict with string keys

bmesh.ops.unsubdivide(*bm*, *verts=[]*, *iterations=0*)[#](#bmesh.ops.unsubdivide "Link to this definition")
:   Un-Subdivide.

    Reduce detail in geometry containing grids.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – input vertices
        * **iterations** (*int*) – number of times to unsubdivide

bmesh.ops.subdivide\_edges(*bm*, *edges=[]*, *smooth=0*, *smooth\_falloff='SMOOTH'*, *fractal=0*, *along\_normal=0*, *cuts=0*, *seed=0*, *custom\_patterns={}*, *edge\_percents={}*, *quad\_corner\_type='STRAIGHT\_CUT'*, *use\_grid\_fill=False*, *use\_single\_edge=False*, *use\_only\_quads=False*, *use\_sphere=False*, *use\_smooth\_even=False*)[#](#bmesh.ops.subdivide_edges "Link to this definition")
:   Subdivide Edges.

    Advanced operator for subdividing edges
    with options for face patterns, smoothing and randomization.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **smooth** (*float*) – smoothness factor
        * **smooth\_falloff** (*enum in* *[**'SMOOTH'**,* *'SPHERE'**,* *'ROOT'**,* *'SHARP'**,* *'LINEAR'**,* *'INVERSE\_SQUARE'**]**,* *default 'SMOOTH'*) – smooth falloff type
        * **fractal** (*float*) – fractal randomness factor
        * **along\_normal** (*float*) – apply fractal displacement along normal only
        * **cuts** (*int*) – number of cuts
        * **seed** (*int*) – seed for the random number generator
        * **custom\_patterns** (*dict mapping vert/edge/face types to unknown internal data**,* *not compatible with python*) – uses custom pointers
        * **edge\_percents** (*dict mapping vert/edge/face types to float*) – Undocumented.
        * **quad\_corner\_type** (*enum in* *[**'STRAIGHT\_CUT'**,* *'INNER\_VERT'**,* *'PATH'**,* *'FAN'**]**,* *default 'STRAIGHT\_CUT'*) – quad corner type
        * **use\_grid\_fill** (*bool*) – fill in fully-selected faces with a grid
        * **use\_single\_edge** (*bool*) – tessellate the case of one edge selected in a quad or triangle
        * **use\_only\_quads** (*bool*) – Only subdivide quads (for loop-cut).
        * **use\_sphere** (*bool*) – for making new primitives only
        * **use\_smooth\_even** (*bool*) – maintain even offset when smoothing

    Returns:
    :   * `geom_inner`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `geom_split`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `geom`: contains all output geometry

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.subdivide\_edgering(*bm*, *edges=[]*, *interp\_mode='LINEAR'*, *smooth=0*, *cuts=0*, *profile\_shape='SMOOTH'*, *profile\_shape\_factor=0*)[#](#bmesh.ops.subdivide_edgering "Link to this definition")
:   Subdivide Edge-Ring.

    Take an edge-ring, and subdivide with interpolation options.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input vertices
        * **interp\_mode** (*enum in* *[**'LINEAR'**,* *'PATH'**,* *'SURFACE'**]**,* *default 'LINEAR'*) – interpolation method
        * **smooth** (*float*) – smoothness factor
        * **cuts** (*int*) – number of cuts
        * **profile\_shape** (*enum in* *[**'SMOOTH'**,* *'SPHERE'**,* *'ROOT'**,* *'SHARP'**,* *'LINEAR'**,* *'INVERSE\_SQUARE'**]**,* *default 'SMOOTH'*) – profile shape type
        * **profile\_shape\_factor** (*float*) – how much intermediary new edges are shrunk/expanded

    Returns:
    :   * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.bisect\_plane(*bm*, *geom=[]*, *dist=0*, *plane\_co=mathutils.Vector()*, *plane\_no=mathutils.Vector()*, *use\_snap\_center=False*, *clear\_outer=False*, *clear\_inner=False*)[#](#bmesh.ops.bisect_plane "Link to this definition")
:   Bisect Plane.

    Bisects the mesh by a plane (cut the mesh in half).

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **dist** (*float*) – minimum distance when testing if a vert is exactly on the plane
        * **plane\_co** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – point on the plane
        * **plane\_no** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – direction of the plane
        * **use\_snap\_center** (*bool*) – snap axis aligned verts to the center
        * **clear\_outer** (*bool*) – when enabled. remove all geometry on the positive side of the plane
        * **clear\_inner** (*bool*) – when enabled. remove all geometry on the negative side of the plane

    Returns:
    :   * `geom_cut`: output geometry aligned with the plane (new and existing)

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))
        * `geom`: input and output geometry (result of cut).

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.delete(*bm*, *geom=[]*, *context='VERTS'*)[#](#bmesh.ops.delete "Link to this definition")
:   Delete Geometry.

    Utility operator to delete geometry.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **context** (*enum in* *[**'VERTS'**,* *'EDGES'**,* *'FACES\_ONLY'**,* *'EDGES\_FACES'**,* *'FACES'**,* *'FACES\_KEEP\_BOUNDARY'**,* *'TAGGED\_ONLY'**]**,* *default 'VERTS'*) – geometry types to delete

bmesh.ops.duplicate(*bm*, *geom=[]*, *dest=None*, *use\_select\_history=False*, *use\_edge\_flip\_from\_face=False*)[#](#bmesh.ops.duplicate "Link to this definition")
:   Duplicate Geometry.

    Utility operator to duplicate geometry,
    optionally into a destination mesh.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **dest** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – destination bmesh, if None will use current on
        * **use\_select\_history** (*bool*) – Undocumented.
        * **use\_edge\_flip\_from\_face** (*bool*) – Undocumented.

    Returns:
    :   * `geom_orig`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `geom`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `vert_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")
        * `edge_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")
        * `face_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")
        * `boundary_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")
        * `isovert_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")

    Return type:
    :   dict with string keys

bmesh.ops.split(*bm*, *geom=[]*, *dest=None*, *use\_only\_faces=False*)[#](#bmesh.ops.split "Link to this definition")
:   Split Off Geometry.

    Disconnect geometry from adjacent edges and faces,
    optionally into a destination mesh.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **dest** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – destination bmesh, if None will use current one
        * **use\_only\_faces** (*bool*) – when enabled. don’t duplicate loose verts/edges

    Returns:
    :   * `geom`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `boundary_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")
        * `isovert_map`:

          **type** dict mapping vert/edge/face types to [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")/[`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")/[`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")

    Return type:
    :   dict with string keys

bmesh.ops.spin(*bm*, *geom=[]*, *cent=mathutils.Vector()*, *axis=mathutils.Vector()*, *dvec=mathutils.Vector()*, *angle=0*, *space=mathutils.Matrix.Identity(4)*, *steps=0*, *use\_merge=False*, *use\_normal\_flip=False*, *use\_duplicate=False*)[#](#bmesh.ops.spin "Link to this definition")
:   Spin.

    Extrude or duplicate geometry a number of times,
    rotating and possibly translating after each step

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **cent** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – rotation center
        * **axis** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – rotation axis
        * **dvec** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – translation delta per step
        * **angle** (*float*) – total rotation angle (radians)
        * **space** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to define the space (typically object matrix)
        * **steps** (*int*) – number of steps
        * **use\_merge** (*bool*) – Merge first/last when the angle is a full revolution.
        * **use\_normal\_flip** (*bool*) – Create faces with reversed direction.
        * **use\_duplicate** (*bool*) – duplicate or extrude?

    Returns:
    :   * `geom_last`: result of last step

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.rotate\_uvs(*bm*, *faces=[]*, *use\_ccw=False*)[#](#bmesh.ops.rotate_uvs "Link to this definition")
:   UV Rotation.

    Cycle the loop UVs

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **use\_ccw** (*bool*) – rotate counter-clockwise if true, otherwise clockwise

bmesh.ops.reverse\_uvs(*bm*, *faces=[]*)[#](#bmesh.ops.reverse_uvs "Link to this definition")
:   UV Reverse.

    Reverse the UVs

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces

bmesh.ops.rotate\_colors(*bm*, *faces=[]*, *use\_ccw=False*, *color\_index=0*)[#](#bmesh.ops.rotate_colors "Link to this definition")
:   Color Rotation.

    Cycle the loop colors

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **use\_ccw** (*bool*) – rotate counter-clockwise if true, otherwise clockwise
        * **color\_index** (*int*) – index into color attribute list

bmesh.ops.reverse\_colors(*bm*, *faces=[]*, *color\_index=0*)[#](#bmesh.ops.reverse_colors "Link to this definition")
:   Color Reverse

    Reverse the loop colors.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **color\_index** (*int*) – index into color attribute list

bmesh.ops.split\_edges(*bm*, *edges=[]*, *verts=[]*, *use\_verts=False*)[#](#bmesh.ops.split_edges "Link to this definition")
:   Edge Split.

    Disconnects faces along input edges.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **verts** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))) – optional tag verts, use to have greater control of splits
        * **use\_verts** (*bool*) – use ‘verts’ for splitting, else just find verts to split from edges

    Returns:
    :   * `edges`: old output disconnected edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_grid(*bm*, *x\_segments=0*, *y\_segments=0*, *size=0*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_grid "Link to this definition")
:   Create Grid.

    Creates a grid with a variable number of subdivisions

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **x\_segments** (*int*) – number of x segments
        * **y\_segments** (*int*) – number of y segments
        * **size** (*float*) – size of the grid
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_uvsphere(*bm*, *u\_segments=0*, *v\_segments=0*, *radius=0*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_uvsphere "Link to this definition")
:   Create UV Sphere.

    Creates a grid with a variable number of subdivisions

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **u\_segments** (*int*) – number of u segments
        * **v\_segments** (*int*) – number of v segment
        * **radius** (*float*) – radius
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_icosphere(*bm*, *subdivisions=0*, *radius=0*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_icosphere "Link to this definition")
:   Create Ico-Sphere.

    Creates a grid with a variable number of subdivisions

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **subdivisions** (*int*) – how many times to recursively subdivide the sphere
        * **radius** (*float*) – radius
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_monkey(*bm*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_monkey "Link to this definition")
:   Create Suzanne.

    Creates a monkey (standard blender primitive).

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_cone(*bm*, *cap\_ends=False*, *cap\_tris=False*, *segments=0*, *radius1=0*, *radius2=0*, *depth=0*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_cone "Link to this definition")
:   Create Cone.

    Creates a cone with variable depth at both ends

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **cap\_ends** (*bool*) – whether or not to fill in the ends with faces
        * **cap\_tris** (*bool*) – fill ends with triangles instead of ngons
        * **segments** (*int*) – number of vertices in the base circle
        * **radius1** (*float*) – radius of one end
        * **radius2** (*float*) – radius of the opposite
        * **depth** (*float*) – distance between ends
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_circle(*bm*, *cap\_ends=False*, *cap\_tris=False*, *segments=0*, *radius=0*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_circle "Link to this definition")
:   Creates a Circle.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **cap\_ends** (*bool*) – whether or not to fill in the ends with faces
        * **cap\_tris** (*bool*) – fill ends with triangles instead of ngons
        * **segments** (*int*) – number of vertices in the circle
        * **radius** (*float*) – Radius of the circle.
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.create\_cube(*bm*, *size=0*, *matrix=mathutils.Matrix.Identity(4)*, *calc\_uvs=False*)[#](#bmesh.ops.create_cube "Link to this definition")
:   Create Cube

    Creates a cube.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **size** (*float*) – size of the cube
        * **matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – matrix to multiply the new geometry with
        * **calc\_uvs** (*bool*) – calculate default UVs

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.bevel(*bm*, *geom=[]*, *offset=0*, *offset\_type='OFFSET'*, *profile\_type='SUPERELLIPSE'*, *segments=0*, *profile=0*, *affect='VERTICES'*, *clamp\_overlap=False*, *material=0*, *loop\_slide=False*, *mark\_seam=False*, *mark\_sharp=False*, *harden\_normals=False*, *face\_strength\_mode='NONE'*, *miter\_outer='SHARP'*, *miter\_inner='SHARP'*, *spread=0*, *custom\_profile=None*, *vmesh\_method='ADJ'*)[#](#bmesh.ops.bevel "Link to this definition")
:   Bevel.

    Bevels edges and vertices

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input edges and vertices
        * **offset** (*float*) – amount to offset beveled edge
        * **offset\_type** (*enum in* *[**'OFFSET'**,* *'WIDTH'**,* *'DEPTH'**,* *'PERCENT'**,* *'ABSOLUTE'**]**,* *default 'OFFSET'*) – how to measure the offset
        * **profile\_type** (*enum in* *[**'SUPERELLIPSE'**,* *'CUSTOM'**]**,* *default 'SUPERELLIPSE'*) – The profile type to use for bevel.
        * **segments** (*int*) – number of segments in bevel
        * **profile** (*float*) – profile shape, 0->1 (.5=>round)
        * **affect** (*enum in* *[**'VERTICES'**,* *'EDGES'**]**,* *default 'VERTICES'*) – Whether to bevel vertices or edges.
        * **clamp\_overlap** (*bool*) – do not allow beveled edges/vertices to overlap each other
        * **material** (*int*) – material for bevel faces, -1 means get from adjacent faces
        * **loop\_slide** (*bool*) – prefer to slide along edges to having even widths
        * **mark\_seam** (*bool*) – extend edge data to allow seams to run across bevels
        * **mark\_sharp** (*bool*) – extend edge data to allow sharp edges to run across bevels
        * **harden\_normals** (*bool*) – harden normals
        * **face\_strength\_mode** (*enum in* *[**'NONE'**,* *'NEW'**,* *'AFFECTED'**,* *'ALL'**]**,* *default 'NONE'*) – whether to set face strength, and which faces to set if so
        * **miter\_outer** (*enum in* *[**'SHARP'**,* *'PATCH'**,* *'ARC'**]**,* *default 'SHARP'*) – outer miter kind
        * **miter\_inner** (*enum in* *[**'SHARP'**,* *'PATCH'**,* *'ARC'**]**,* *default 'SHARP'*) – outer miter kind
        * **spread** (*float*) – amount to offset beveled edge
        * **custom\_profile** ([`bpy.types.bpy_struct`](../../bpy/types/bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct")) – CurveProfile, if None ignored
        * **vmesh\_method** (*enum in* *[**'ADJ'**,* *'CUTOFF'**]**,* *default 'ADJ'*) – The method to use to create meshes at intersections.

    Returns:
    :   * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `edges`: output edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))
        * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))

    Return type:
    :   dict with string keys

bmesh.ops.beautify\_fill(*bm*, *faces=[]*, *edges=[]*, *use\_restrict\_tag=False*, *method='AREA'*)[#](#bmesh.ops.beautify_fill "Link to this definition")
:   Beautify Fill.

    Rotate edges to create more evenly spaced triangles.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – edges that can be flipped
        * **use\_restrict\_tag** (*bool*) – restrict edge rotation to mixed tagged vertices
        * **method** (*enum in* *[**'AREA'**,* *'ANGLE'**]**,* *default 'AREA'*) – method to define what is beautiful

    Returns:
    :   * `geom`: new flipped faces and edges

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.triangle\_fill(*bm*, *use\_beauty=False*, *use\_dissolve=False*, *edges=[]*, *normal=mathutils.Vector()*)[#](#bmesh.ops.triangle_fill "Link to this definition")
:   Triangle Fill.

    Fill edges with triangles

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **use\_beauty** (*bool*) – use best triangulation division
        * **use\_dissolve** (*bool*) – dissolve resulting faces
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **normal** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") or any sequence of 3 floats) – optionally pass the fill normal to use

    Returns:
    :   * `geom`: new faces and edges

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.solidify(*bm*, *geom=[]*, *thickness=0*)[#](#bmesh.ops.solidify "Link to this definition")
:   Solidify.

    Turns a mesh into a shell with thickness

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **geom** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **thickness** (*float*) – thickness

    Returns:
    :   * `geom`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.inset\_individual(*bm*, *faces=[]*, *thickness=0*, *depth=0*, *use\_even\_offset=False*, *use\_interpolate=False*, *use\_relative\_offset=False*)[#](#bmesh.ops.inset_individual "Link to this definition")
:   Face Inset (Individual).

    Insets individual faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **thickness** (*float*) – thickness
        * **depth** (*float*) – depth
        * **use\_even\_offset** (*bool*) – scale the offset to give more even thickness
        * **use\_interpolate** (*bool*) – blend face data across the inset
        * **use\_relative\_offset** (*bool*) – scale the offset by surrounding geometry

    Returns:
    :   * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.inset\_region(*bm*, *faces=[]*, *faces\_exclude=[]*, *use\_boundary=False*, *use\_even\_offset=False*, *use\_interpolate=False*, *use\_relative\_offset=False*, *use\_edge\_rail=False*, *thickness=0*, *depth=0*, *use\_outset=False*)[#](#bmesh.ops.inset_region "Link to this definition")
:   Face Inset (Regions).

    Inset or outset face regions.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **faces\_exclude** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces to explicitly exclude from inset
        * **use\_boundary** (*bool*) – inset face boundaries
        * **use\_even\_offset** (*bool*) – scale the offset to give more even thickness
        * **use\_interpolate** (*bool*) – blend face data across the inset
        * **use\_relative\_offset** (*bool*) – scale the offset by surrounding geometry
        * **use\_edge\_rail** (*bool*) – inset the region along existing edges
        * **thickness** (*float*) – thickness
        * **depth** (*float*) – depth
        * **use\_outset** (*bool*) – outset rather than inset

    Returns:
    :   * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.offset\_edgeloops(*bm*, *edges=[]*, *use\_cap\_endpoint=False*)[#](#bmesh.ops.offset_edgeloops "Link to this definition")
:   Edge-loop Offset.

    Creates edge loops based on simple edge-outset method.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **edges** (list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))) – input edges
        * **use\_cap\_endpoint** (*bool*) – extend loop around end-points

    Returns:
    :   * `edges`: output edges

          **type** list of ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"))

    Return type:
    :   dict with string keys

bmesh.ops.wireframe(*bm*, *faces=[]*, *thickness=0*, *offset=0*, *use\_replace=False*, *use\_boundary=False*, *use\_even\_offset=False*, *use\_crease=False*, *crease\_weight=0*, *use\_relative\_offset=False*, *material\_offset=0*)[#](#bmesh.ops.wireframe "Link to this definition")
:   Wire Frame.

    Makes a wire-frame copy of faces.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **thickness** (*float*) – thickness
        * **offset** (*float*) – offset the thickness from the center
        * **use\_replace** (*bool*) – remove original geometry
        * **use\_boundary** (*bool*) – inset face boundaries
        * **use\_even\_offset** (*bool*) – scale the offset to give more even thickness
        * **use\_crease** (*bool*) – crease hub edges for improved subdivision surface
        * **crease\_weight** (*float*) – the mean crease weight for resulting edges
        * **use\_relative\_offset** (*bool*) – scale the offset by surrounding geometry
        * **material\_offset** (*int*) – offset material index of generated faces

    Returns:
    :   * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.poke(*bm*, *faces=[]*, *offset=0*, *center\_mode='MEAN\_WEIGHTED'*, *use\_relative\_offset=False*)[#](#bmesh.ops.poke "Link to this definition")
:   Pokes a face.

    Splits a face into a triangle fan.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **faces** (list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input faces
        * **offset** (*float*) – center vertex offset along normal
        * **center\_mode** (*enum in* *[**'MEAN\_WEIGHTED'**,* *'MEAN'**,* *'BOUNDS'**]**,* *default 'MEAN\_WEIGHTED'*) – calculation mode for center vertex
        * **use\_relative\_offset** (*bool*) – apply offset

    Returns:
    :   * `verts`: output verts

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"))
        * `faces`: output faces

          **type** list of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.convex\_hull(*bm*, *input=[]*, *use\_existing\_faces=False*)[#](#bmesh.ops.convex_hull "Link to this definition")
:   Convex Hull

    Builds a convex hull from the vertices in ‘input’.

    If ‘use\_existing\_faces’ is true, the hull will not output triangles
    that are covered by a pre-existing face.

    All hull vertices, faces, and edges are added to ‘geom.out’. Any
    input elements that end up inside the hull (i.e. are not used by an
    output face) are added to the ‘interior\_geom’ slot. The
    ‘unused\_geom’ slot will contain all interior geometry that is
    completely unused. Lastly, ‘holes\_geom’ contains edges and faces
    that were in the input and are part of the hull.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **input** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **use\_existing\_faces** (*bool*) – skip hull triangles that are covered by a pre-existing face

    Returns:
    :   * `geom`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `geom_interior`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `geom_unused`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))
        * `geom_holes`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

bmesh.ops.symmetrize(*bm*, *input=[]*, *direction='-X'*, *dist=0*, *use\_shapekey=False*)[#](#bmesh.ops.symmetrize "Link to this definition")
:   Symmetrize.

    Makes the mesh elements in the “input” slot symmetrical. Unlike
    normal mirroring, it only copies in one direction, as specified by
    the “direction” slot. The edges and faces that cross the plane of
    symmetry are split as needed to enforce symmetry.

    All new vertices, edges, and faces are added to the “geom.out” slot.

    Parameters:
    :   * **bm** ([`bmesh.types.BMesh`](../types/index.md#bmesh.types.BMesh "bmesh.types.BMesh")) – The bmesh to operate on.
        * **input** (list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))) – input geometry
        * **direction** (*enum in* *[**'-X'**,* *'-Y'**,* *'-Z'**,* *'X'**,* *'Y'**,* *'Z'**]**,* *default '-X'*) – axis to use
        * **dist** (*float*) – minimum distance
        * **use\_shapekey** (*bool*) – Transform shape keys too.

    Returns:
    :   * `geom`:

          **type** list of ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert"), [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Return type:
    :   dict with string keys

[Next

BMesh Types (bmesh.types)](../types/index.md)
[Previous

BMesh Module (bmesh)](../../../meta/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bmesh.ops.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbmesh.ops.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* BMesh Operators (bmesh.ops)
  + [Operator Example](#operator-example)
    - [`smooth_vert()`](#bmesh.ops.smooth_vert)
    - [`smooth_laplacian_vert()`](#bmesh.ops.smooth_laplacian_vert)
    - [`recalc_face_normals()`](#bmesh.ops.recalc_face_normals)
    - [`planar_faces()`](#bmesh.ops.planar_faces)
    - [`region_extend()`](#bmesh.ops.region_extend)
    - [`rotate_edges()`](#bmesh.ops.rotate_edges)
    - [`reverse_faces()`](#bmesh.ops.reverse_faces)
    - [`flip_quad_tessellation()`](#bmesh.ops.flip_quad_tessellation)
    - [`bisect_edges()`](#bmesh.ops.bisect_edges)
    - [`mirror()`](#bmesh.ops.mirror)
    - [`find_doubles()`](#bmesh.ops.find_doubles)
    - [`remove_doubles()`](#bmesh.ops.remove_doubles)
    - [`collapse()`](#bmesh.ops.collapse)
    - [`pointmerge_facedata()`](#bmesh.ops.pointmerge_facedata)
    - [`average_vert_facedata()`](#bmesh.ops.average_vert_facedata)
    - [`pointmerge()`](#bmesh.ops.pointmerge)
    - [`collapse_uvs()`](#bmesh.ops.collapse_uvs)
    - [`weld_verts()`](#bmesh.ops.weld_verts)
    - [`create_vert()`](#bmesh.ops.create_vert)
    - [`join_triangles()`](#bmesh.ops.join_triangles)
    - [`contextual_create()`](#bmesh.ops.contextual_create)
    - [`bridge_loops()`](#bmesh.ops.bridge_loops)
    - [`grid_fill()`](#bmesh.ops.grid_fill)
    - [`holes_fill()`](#bmesh.ops.holes_fill)
    - [`face_attribute_fill()`](#bmesh.ops.face_attribute_fill)
    - [`edgeloop_fill()`](#bmesh.ops.edgeloop_fill)
    - [`edgenet_fill()`](#bmesh.ops.edgenet_fill)
    - [`edgenet_prepare()`](#bmesh.ops.edgenet_prepare)
    - [`rotate()`](#bmesh.ops.rotate)
    - [`translate()`](#bmesh.ops.translate)
    - [`scale()`](#bmesh.ops.scale)
    - [`transform()`](#bmesh.ops.transform)
    - [`object_load_bmesh()`](#bmesh.ops.object_load_bmesh)
    - [`bmesh_to_mesh()`](#bmesh.ops.bmesh_to_mesh)
    - [`mesh_to_bmesh()`](#bmesh.ops.mesh_to_bmesh)
    - [`extrude_discrete_faces()`](#bmesh.ops.extrude_discrete_faces)
    - [`extrude_edge_only()`](#bmesh.ops.extrude_edge_only)
    - [`extrude_vert_indiv()`](#bmesh.ops.extrude_vert_indiv)
    - [`connect_verts()`](#bmesh.ops.connect_verts)
    - [`connect_verts_concave()`](#bmesh.ops.connect_verts_concave)
    - [`connect_verts_nonplanar()`](#bmesh.ops.connect_verts_nonplanar)
    - [`connect_vert_pair()`](#bmesh.ops.connect_vert_pair)
    - [`extrude_face_region()`](#bmesh.ops.extrude_face_region)
    - [`dissolve_verts()`](#bmesh.ops.dissolve_verts)
    - [`dissolve_edges()`](#bmesh.ops.dissolve_edges)
    - [`dissolve_faces()`](#bmesh.ops.dissolve_faces)
    - [`dissolve_limit()`](#bmesh.ops.dissolve_limit)
    - [`dissolve_degenerate()`](#bmesh.ops.dissolve_degenerate)
    - [`triangulate()`](#bmesh.ops.triangulate)
    - [`unsubdivide()`](#bmesh.ops.unsubdivide)
    - [`subdivide_edges()`](#bmesh.ops.subdivide_edges)
    - [`subdivide_edgering()`](#bmesh.ops.subdivide_edgering)
    - [`bisect_plane()`](#bmesh.ops.bisect_plane)
    - [`delete()`](#bmesh.ops.delete)
    - [`duplicate()`](#bmesh.ops.duplicate)
    - [`split()`](#bmesh.ops.split)
    - [`spin()`](#bmesh.ops.spin)
    - [`rotate_uvs()`](#bmesh.ops.rotate_uvs)
    - [`reverse_uvs()`](#bmesh.ops.reverse_uvs)
    - [`rotate_colors()`](#bmesh.ops.rotate_colors)
    - [`reverse_colors()`](#bmesh.ops.reverse_colors)
    - [`split_edges()`](#bmesh.ops.split_edges)
    - [`create_grid()`](#bmesh.ops.create_grid)
    - [`create_uvsphere()`](#bmesh.ops.create_uvsphere)
    - [`create_icosphere()`](#bmesh.ops.create_icosphere)
    - [`create_monkey()`](#bmesh.ops.create_monkey)
    - [`create_cone()`](#bmesh.ops.create_cone)
    - [`create_circle()`](#bmesh.ops.create_circle)
    - [`create_cube()`](#bmesh.ops.create_cube)
    - [`bevel()`](#bmesh.ops.bevel)
    - [`beautify_fill()`](#bmesh.ops.beautify_fill)
    - [`triangle_fill()`](#bmesh.ops.triangle_fill)
    - [`solidify()`](#bmesh.ops.solidify)
    - [`inset_individual()`](#bmesh.ops.inset_individual)
    - [`inset_region()`](#bmesh.ops.inset_region)
    - [`offset_edgeloops()`](#bmesh.ops.offset_edgeloops)
    - [`wireframe()`](#bmesh.ops.wireframe)
    - [`poke()`](#bmesh.ops.poke)
    - [`convex_hull()`](#bmesh.ops.convex_hull)
    - [`symmetrize()`](#bmesh.ops.symmetrize)