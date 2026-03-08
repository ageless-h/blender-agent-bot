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

  + [BMesh Operators (bmesh.ops)](../ops/index.md)
  + [BMesh Types (bmesh.types)](../types/index.md)
  + BMesh Utilities (bmesh.utils)
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

# BMesh Utilities (bmesh.utils)[#](#module-bmesh.utils "Link to this heading")

This module provides access to blenders bmesh data structures.

bmesh.utils.edge\_rotate(*edge*, *ccw=False*)[#](#bmesh.utils.edge_rotate "Link to this definition")
:   Rotate the edge and return the newly created edge.
    If rotating the edge fails, None will be returned.

    Parameters:
    :   * **edge** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – The edge to rotate.
        * **ccw** (*boolean*) – When True the edge will be rotated counter clockwise.

    Returns:
    :   The newly rotated edge.

    Return type:
    :   [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")

bmesh.utils.edge\_split(*edge*, *vert*, *fac*)[#](#bmesh.utils.edge_split "Link to this definition")
:   Split an edge, return the newly created data.

    Parameters:
    :   * **edge** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – The edge to split.
        * **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – One of the verts on the edge, defines the split direction.
        * **fac** (*float*) – The point on the edge where the new vert will be created [0 - 1].

    Returns:
    :   The newly created (edge, vert) pair.

    Return type:
    :   tuple

bmesh.utils.face\_flip(*faces*)[#](#bmesh.utils.face_flip "Link to this definition")
:   Flip the faces direction.

    Parameters:
    :   **face** ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")) – Face to flip.

bmesh.utils.face\_join(*faces*, *remove=True*)[#](#bmesh.utils.face_join "Link to this definition")
:   Joins a sequence of faces.

    Parameters:
    :   * **faces** ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")) – Sequence of faces.
        * **remove** (*boolean*) – Remove the edges and vertices between the faces.

    Returns:
    :   The newly created face or None on failure.

    Return type:
    :   [`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")

bmesh.utils.face\_split(*face*, *vert\_a*, *vert\_b*, *coords=()*, *use\_exist=True*, *example=None*)[#](#bmesh.utils.face_split "Link to this definition")
:   Face split with optional intermediate points.

    Parameters:
    :   * **face** ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")) – The face to cut.
        * **vert\_a** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – First vertex to cut in the face (face must contain the vert).
        * **vert\_b** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – Second vertex to cut in the face (face must contain the vert).
        * **coords** (*sequence* *of* *float triplets*) – Optional argument to define points in between *vert\_a* and *vert\_b*.
        * **use\_exist** (*boolean*) – .Use an existing edge if it exists (Only used when *coords* argument is empty or omitted)
        * **example** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – Newly created edge will copy settings from this one.

    Returns:
    :   The newly created face or None on failure.

    Return type:
    :   ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"), [`bmesh.types.BMLoop`](../types/index.md#bmesh.types.BMLoop "bmesh.types.BMLoop")) pair

bmesh.utils.face\_split\_edgenet(*face*, *edgenet*)[#](#bmesh.utils.face_split_edgenet "Link to this definition")
:   Splits a face into any number of regions defined by an edgenet.

    Parameters:
    :   * **face** ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")) – The face to split.
        * **face** – The face to split.
        * **edgenet** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – Sequence of edges.

    Returns:
    :   The newly created faces.

    Return type:
    :   tuple of ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace"))

    Note

    Regions defined by edges need to connect to the face, otherwise they’re ignored as loose edges.

bmesh.utils.face\_vert\_separate(*face*, *vert*)[#](#bmesh.utils.face_vert_separate "Link to this definition")
:   Rip a vertex in a face away and add a new vertex.

    Parameters:
    :   * **face** ([`bmesh.types.BMFace`](../types/index.md#bmesh.types.BMFace "bmesh.types.BMFace")) – The face to separate.
        * **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – A vertex in the face to separate.

    Return vert:
    :   The newly created vertex or None on failure.

    Rtype vert:
    :   [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")

    Note

    This is the same as loop\_separate, and has only been added for convenience.

bmesh.utils.loop\_separate(*loop*)[#](#bmesh.utils.loop_separate "Link to this definition")
:   Rip a vertex in a face away and add a new vertex.

    Parameters:
    :   **loop** ([`bmesh.types.BMLoop`](../types/index.md#bmesh.types.BMLoop "bmesh.types.BMLoop")) – The loop to separate.

    Return vert:
    :   The newly created vertex or None on failure.

    Rtype vert:
    :   [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")

bmesh.utils.vert\_collapse\_edge(*vert*, *edge*)[#](#bmesh.utils.vert_collapse_edge "Link to this definition")
:   Collapse a vertex into an edge.

    Parameters:
    :   * **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – The vert that will be collapsed.
        * **edge** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – The edge to collapse into.

    Returns:
    :   The resulting edge from the collapse operation.

    Return type:
    :   [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")

bmesh.utils.vert\_collapse\_faces(*vert*, *edge*, *fac*, *join\_faces*)[#](#bmesh.utils.vert_collapse_faces "Link to this definition")
:   Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.

    Parameters:
    :   * **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – The vert that will be collapsed.
        * **edge** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – The edge to collapse into.
        * **fac** (*float*) – The factor to use when merging customdata [0 - 1].
        * **join\_faces** (*bool*) – When true the faces around the vertex will be joined otherwise collapse the vertex by merging the 2 edges this vertex connects to into one.

    Returns:
    :   The resulting edge from the collapse operation.

    Return type:
    :   [`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")

bmesh.utils.vert\_dissolve(*vert*)[#](#bmesh.utils.vert_dissolve "Link to this definition")
:   Dissolve this vertex (will be removed).

    Parameters:
    :   **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – The vert to be dissolved.

    Returns:
    :   True when the vertex dissolve is successful.

    Return type:
    :   boolean

bmesh.utils.vert\_separate(*vert*, *edges*)[#](#bmesh.utils.vert_separate "Link to this definition")
:   Separate this vertex at every edge.

    Parameters:
    :   * **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – The vert to be separated.
        * **edges** ([`bmesh.types.BMEdge`](../types/index.md#bmesh.types.BMEdge "bmesh.types.BMEdge")) – The edges to separated.

    Returns:
    :   The newly separated verts (including the vertex passed).

    Return type:
    :   tuple of [`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")

bmesh.utils.vert\_splice(*vert*, *vert\_target*)[#](#bmesh.utils.vert_splice "Link to this definition")
:   Splice vert into vert\_target.

    Parameters:
    :   * **vert** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – The vertex to be removed.
        * **vert\_target** ([`bmesh.types.BMVert`](../types/index.md#bmesh.types.BMVert "bmesh.types.BMVert")) – The vertex to use.

    Note

    The verts mustn’t share an edge or face.

[Next

BMesh Geometry Utilities (bmesh.geometry)](../geometry/index.md)
[Previous

BMesh Types (bmesh.types)](../types/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bmesh.utils.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbmesh.utils.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* BMesh Utilities (bmesh.utils)
  + [`edge_rotate()`](#bmesh.utils.edge_rotate)
  + [`edge_split()`](#bmesh.utils.edge_split)
  + [`face_flip()`](#bmesh.utils.face_flip)
  + [`face_join()`](#bmesh.utils.face_join)
  + [`face_split()`](#bmesh.utils.face_split)
  + [`face_split_edgenet()`](#bmesh.utils.face_split_edgenet)
  + [`face_vert_separate()`](#bmesh.utils.face_vert_separate)
  + [`loop_separate()`](#bmesh.utils.loop_separate)
  + [`vert_collapse_edge()`](#bmesh.utils.vert_collapse_edge)
  + [`vert_collapse_faces()`](#bmesh.utils.vert_collapse_faces)
  + [`vert_dissolve()`](#bmesh.utils.vert_dissolve)
  + [`vert_separate()`](#bmesh.utils.vert_separate)
  + [`vert_splice()`](#bmesh.utils.vert_splice)