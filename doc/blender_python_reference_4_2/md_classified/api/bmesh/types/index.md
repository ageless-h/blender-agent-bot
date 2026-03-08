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
  + BMesh Types (bmesh.types)
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

# BMesh Types (bmesh.types)[#](#module-bmesh.types "Link to this heading")

## Base Mesh Type[#](#base-mesh-type "Link to this heading")

*class* bmesh.types.BMesh[#](#bmesh.types.BMesh "Link to this definition")
:   The BMesh data structure

    calc\_loop\_triangles()[#](#bmesh.types.BMesh.calc_loop_triangles "Link to this definition")
    :   Calculate triangle tessellation from quads/ngons.

        Returns:
        :   The triangulated faces.

        Return type:
        :   list of [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop") tuples

    calc\_volume(*signed=False*)[#](#bmesh.types.BMesh.calc_volume "Link to this definition")
    :   Calculate mesh volume based on face normals.

        Parameters:
        :   **signed** (*bool*) – when signed is true, negative values may be returned.

        Returns:
        :   The volume of the mesh.

        Return type:
        :   float

    clear()[#](#bmesh.types.BMesh.clear "Link to this definition")
    :   Clear all mesh data.

    copy()[#](#bmesh.types.BMesh.copy "Link to this definition")
    :   Returns:
        :   A copy of this BMesh.

        Return type:
        :   [`BMesh`](#bmesh.types.BMesh "bmesh.types.BMesh")

    free()[#](#bmesh.types.BMesh.free "Link to this definition")
    :   Explicitly free the BMesh data from memory, causing exceptions on further access.

        Note

        The BMesh is freed automatically, typically when the script finishes executing.
        However in some cases its hard to predict when this will be and its useful to
        explicitly free the data.

    from\_mesh(*mesh*, *face\_normals=True*, *vertex\_normals=True*, *use\_shape\_key=False*, *shape\_key\_index=0*)[#](#bmesh.types.BMesh.from_mesh "Link to this definition")
    :   Initialize this bmesh from existing mesh datablock.

        Parameters:
        :   * **mesh** (`Mesh`) – The mesh data to load.
            * **use\_shape\_key** (*boolean*) – Use the locations from a shape key.
            * **shape\_key\_index** (*int*) – The shape key index to use.

        Note

        Multiple calls can be used to join multiple meshes.

        Custom-data layers are only copied from `mesh` on initialization.
        Further calls will copy custom-data to matching layers, layers missing on the target mesh won’t be added.

    from\_object(*object*, *depsgraph*, *cage=False*, *face\_normals=True*, *vertex\_normals=True*)[#](#bmesh.types.BMesh.from_object "Link to this definition")
    :   Initialize this bmesh from existing object data-block (only meshes are currently supported).

        Parameters:
        :   * **object** (`Object`) – The object data to load.
            * **cage** (*boolean*) – Get the mesh as a deformed cage.
            * **face\_normals** (*boolean*) – Calculate face normals.
            * **vertex\_normals** (*boolean*) – Calculate vertex normals.

    normal\_update()[#](#bmesh.types.BMesh.normal_update "Link to this definition")
    :   Update normals of mesh faces and verts.

        Note

        The normal of any vertex where `is_wire` is True will be a zero vector.

    select\_flush(*select*)[#](#bmesh.types.BMesh.select_flush "Link to this definition")
    :   Flush selection, independent of the current selection mode.

        Parameters:
        :   **select** (*boolean*) – flush selection or de-selected elements.

    select\_flush\_mode()[#](#bmesh.types.BMesh.select_flush_mode "Link to this definition")
    :   flush selection based on the current mode current [`BMesh.select_mode`](#bmesh.types.BMesh.select_mode "bmesh.types.BMesh.select_mode").

    to\_mesh(*mesh*)[#](#bmesh.types.BMesh.to_mesh "Link to this definition")
    :   Writes this BMesh data into an existing Mesh datablock.

        Parameters:
        :   **mesh** (`Mesh`) – The mesh data to write into.

    transform(*matrix*, *filter=None*)[#](#bmesh.types.BMesh.transform "Link to this definition")
    :   Transform the mesh (optionally filtering flagged data only).

        Parameters:
        :   * **matrix** (4x4 [`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – transform matrix.
            * **filter** (*set*) – set of values in (‘SELECT’, ‘HIDE’, ‘SEAM’, ‘SMOOTH’, ‘TAG’).

    edges[#](#bmesh.types.BMesh.edges "Link to this definition")
    :   This meshes edge sequence (read-only).

        Type:
        :   [`BMEdgeSeq`](#bmesh.types.BMEdgeSeq "bmesh.types.BMEdgeSeq")

    faces[#](#bmesh.types.BMesh.faces "Link to this definition")
    :   This meshes face sequence (read-only).

        Type:
        :   [`BMFaceSeq`](#bmesh.types.BMFaceSeq "bmesh.types.BMFaceSeq")

    is\_valid[#](#bmesh.types.BMesh.is_valid "Link to this definition")
    :   True when this element is valid (hasn’t been removed).

        Type:
        :   boolean

    is\_wrapped[#](#bmesh.types.BMesh.is_wrapped "Link to this definition")
    :   True when this mesh is owned by blender (typically the editmode BMesh).

        Type:
        :   boolean

    loops[#](#bmesh.types.BMesh.loops "Link to this definition")
    :   This meshes loops (read-only).

        Type:
        :   [`BMLoopSeq`](#bmesh.types.BMLoopSeq "bmesh.types.BMLoopSeq")

        Note

        Loops must be accessed via faces, this is only exposed for layer access.

    select\_history[#](#bmesh.types.BMesh.select_history "Link to this definition")
    :   Sequence of selected items (the last is displayed as active).

        Type:
        :   [`BMEditSelSeq`](#bmesh.types.BMEditSelSeq "bmesh.types.BMEditSelSeq")

    select\_mode[#](#bmesh.types.BMesh.select_mode "Link to this definition")
    :   The selection mode, values can be {‘VERT’, ‘EDGE’, ‘FACE’}, can’t be assigned an empty set.

        Type:
        :   set

    verts[#](#bmesh.types.BMesh.verts "Link to this definition")
    :   This meshes vert sequence (read-only).

        Type:
        :   [`BMVertSeq`](#bmesh.types.BMVertSeq "bmesh.types.BMVertSeq")

## Mesh Elements[#](#mesh-elements "Link to this heading")

*class* bmesh.types.BMVert[#](#bmesh.types.BMVert "Link to this definition")
:   The BMesh vertex type

    calc\_edge\_angle(*fallback=None*)[#](#bmesh.types.BMVert.calc_edge_angle "Link to this definition")
    :   Return the angle between this vert’s two connected edges.

        Parameters:
        :   **fallback** (*any*) – return this when the vert doesn’t have 2 edges
            (instead of raising a `ValueError`).

        Returns:
        :   Angle between edges in radians.

        Return type:
        :   float

    calc\_shell\_factor()[#](#bmesh.types.BMVert.calc_shell_factor "Link to this definition")
    :   Return a multiplier calculated based on the sharpness of the vertex.
        Where a flat surface gives 1.0, and higher values sharper edges.
        This is used to maintain shell thickness when offsetting verts along their normals.

        Returns:
        :   offset multiplier

        Return type:
        :   float

    copy\_from(*other*)[#](#bmesh.types.BMVert.copy_from "Link to this definition")
    :   Copy values from another element of matching type.

    copy\_from\_face\_interp(*face*)[#](#bmesh.types.BMVert.copy_from_face_interp "Link to this definition")
    :   Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        Parameters:
        :   **face** ([`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")) – The face to interpolate data from.

    copy\_from\_vert\_interp(*vert\_pair*, *fac*)[#](#bmesh.types.BMVert.copy_from_vert_interp "Link to this definition")
    :   Interpolate the customdata from a vert between 2 other verts.

        Parameters:
        :   **vert\_pair** (pair of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – The verts between which to interpolate data from.

    hide\_set(*hide*)[#](#bmesh.types.BMVert.hide_set "Link to this definition")
    :   Set the hide state.
        This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.

        Parameters:
        :   **hide** (*boolean*) – Hidden or visible.

    normal\_update()[#](#bmesh.types.BMVert.normal_update "Link to this definition")
    :   Update vertex normal.
        This does not update the normals of adjoining faces.

        Note

        The vertex normal will be a zero vector if vertex [`is_wire`](#bmesh.types.BMVert.is_wire "bmesh.types.BMVert.is_wire") is True.

    select\_set(*select*)[#](#bmesh.types.BMVert.select_set "Link to this definition")
    :   Set the selection.
        This is different from the *select* attribute because it updates the selection state of associated geometry.

        Parameters:
        :   **select** (*boolean*) – Select or de-select.

        Note

        Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex won’t de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.

    co[#](#bmesh.types.BMVert.co "Link to this definition")
    :   The coordinates for this vertex as a 3D, wrapped vector.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    hide[#](#bmesh.types.BMVert.hide "Link to this definition")
    :   Hidden state of this element.

        Type:
        :   boolean

    index[#](#bmesh.types.BMVert.index "Link to this definition")
    :   Index of this element.

        Type:
        :   int

        Note

        This value is not necessarily valid, while editing the mesh it can become *dirty*.

        It’s also possible to assign any number to this attribute for a scripts internal logic.

        To ensure the value is up to date - see [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update").

    is\_boundary[#](#bmesh.types.BMVert.is_boundary "Link to this definition")
    :   True when this vertex is connected to boundary edges (read-only).

        Type:
        :   boolean

    is\_manifold[#](#bmesh.types.BMVert.is_manifold "Link to this definition")
    :   True when this vertex is manifold (read-only).

        Type:
        :   boolean

    is\_valid[#](#bmesh.types.BMVert.is_valid "Link to this definition")
    :   True when this element is valid (hasn’t been removed).

        Type:
        :   boolean

    is\_wire[#](#bmesh.types.BMVert.is_wire "Link to this definition")
    :   True when this vertex is not connected to any faces (read-only).

        Type:
        :   boolean

    link\_edges[#](#bmesh.types.BMVert.link_edges "Link to this definition")
    :   Edges connected to this vertex (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge")

    link\_faces[#](#bmesh.types.BMVert.link_faces "Link to this definition")
    :   Faces connected to this vertex (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

    link\_loops[#](#bmesh.types.BMVert.link_loops "Link to this definition")
    :   Loops that use this vertex (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    normal[#](#bmesh.types.BMVert.normal "Link to this definition")
    :   The normal for this vertex as a 3D, wrapped vector.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    select[#](#bmesh.types.BMVert.select "Link to this definition")
    :   Selected state of this element.

        Type:
        :   boolean

    tag[#](#bmesh.types.BMVert.tag "Link to this definition")
    :   Generic attribute scripts can use for own logic

        Type:
        :   boolean

*class* bmesh.types.BMEdge[#](#bmesh.types.BMEdge "Link to this definition")
:   The BMesh edge connecting 2 verts

    calc\_face\_angle(*fallback=None*)[#](#bmesh.types.BMEdge.calc_face_angle "Link to this definition")
    :   Parameters:
        :   **fallback** (*any*) – return this when the edge doesn’t have 2 faces
            (instead of raising a `ValueError`).

        Returns:
        :   The angle between 2 connected faces in radians.

        Return type:
        :   float

    calc\_face\_angle\_signed(*fallback=None*)[#](#bmesh.types.BMEdge.calc_face_angle_signed "Link to this definition")
    :   Parameters:
        :   **fallback** (*any*) – return this when the edge doesn’t have 2 faces
            (instead of raising a `ValueError`).

        Returns:
        :   The angle between 2 connected faces in radians (negative for concave join).

        Return type:
        :   float

    calc\_length()[#](#bmesh.types.BMEdge.calc_length "Link to this definition")
    :   Returns:
        :   The length between both verts.

        Return type:
        :   float

    calc\_tangent(*loop*)[#](#bmesh.types.BMEdge.calc_tangent "Link to this definition")
    :   Return the tangent at this edge relative to a face (pointing inward into the face).
        This uses the face normal for calculation.

        Parameters:
        :   **loop** ([`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")) – The loop used for tangent calculation.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    copy\_from(*other*)[#](#bmesh.types.BMEdge.copy_from "Link to this definition")
    :   Copy values from another element of matching type.

    hide\_set(*hide*)[#](#bmesh.types.BMEdge.hide_set "Link to this definition")
    :   Set the hide state.
        This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.

        Parameters:
        :   **hide** (*boolean*) – Hidden or visible.

    normal\_update()[#](#bmesh.types.BMEdge.normal_update "Link to this definition")
    :   Update normals of all connected faces and the edge verts.

        Note

        The normal of edge vertex will be a zero vector if vertex [`is_wire`](#bmesh.types.BMEdge.is_wire "bmesh.types.BMEdge.is_wire") is True.

    other\_vert(*vert*)[#](#bmesh.types.BMEdge.other_vert "Link to this definition")
    :   Return the other vertex on this edge or None if the vertex is not used by this edge.

        Parameters:
        :   **vert** ([`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – a vert in this edge.

        Returns:
        :   The edges other vert.

        Return type:
        :   [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert") or None

    select\_set(*select*)[#](#bmesh.types.BMEdge.select_set "Link to this definition")
    :   Set the selection.
        This is different from the *select* attribute because it updates the selection state of associated geometry.

        Parameters:
        :   **select** (*boolean*) – Select or de-select.

        Note

        Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex won’t de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.

    hide[#](#bmesh.types.BMEdge.hide "Link to this definition")
    :   Hidden state of this element.

        Type:
        :   boolean

    index[#](#bmesh.types.BMEdge.index "Link to this definition")
    :   Index of this element.

        Type:
        :   int

        Note

        This value is not necessarily valid, while editing the mesh it can become *dirty*.

        It’s also possible to assign any number to this attribute for a scripts internal logic.

        To ensure the value is up to date - see [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update").

    is\_boundary[#](#bmesh.types.BMEdge.is_boundary "Link to this definition")
    :   True when this edge is at the boundary of a face (read-only).

        Type:
        :   boolean

    is\_contiguous[#](#bmesh.types.BMEdge.is_contiguous "Link to this definition")
    :   True when this edge is manifold, between two faces with the same winding (read-only).

        Type:
        :   boolean

    is\_convex[#](#bmesh.types.BMEdge.is_convex "Link to this definition")
    :   True when this edge joins two convex faces, depends on a valid face normal (read-only).

        Type:
        :   boolean

    is\_manifold[#](#bmesh.types.BMEdge.is_manifold "Link to this definition")
    :   True when this edge is manifold (read-only).

        Type:
        :   boolean

    is\_valid[#](#bmesh.types.BMEdge.is_valid "Link to this definition")
    :   True when this element is valid (hasn’t been removed).

        Type:
        :   boolean

    is\_wire[#](#bmesh.types.BMEdge.is_wire "Link to this definition")
    :   True when this edge is not connected to any faces (read-only).

        Type:
        :   boolean

    link\_faces[#](#bmesh.types.BMEdge.link_faces "Link to this definition")
    :   Faces connected to this edge, (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

    link\_loops[#](#bmesh.types.BMEdge.link_loops "Link to this definition")
    :   Loops connected to this edge, (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    seam[#](#bmesh.types.BMEdge.seam "Link to this definition")
    :   Seam for UV unwrapping.

        Type:
        :   boolean

    select[#](#bmesh.types.BMEdge.select "Link to this definition")
    :   Selected state of this element.

        Type:
        :   boolean

    smooth[#](#bmesh.types.BMEdge.smooth "Link to this definition")
    :   Smooth state of this element.

        Type:
        :   boolean

    tag[#](#bmesh.types.BMEdge.tag "Link to this definition")
    :   Generic attribute scripts can use for own logic

        Type:
        :   boolean

    verts[#](#bmesh.types.BMEdge.verts "Link to this definition")
    :   Verts this edge uses (always 2), (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")

*class* bmesh.types.BMFace[#](#bmesh.types.BMFace "Link to this definition")
:   The BMesh face with 3 or more sides

    calc\_area()[#](#bmesh.types.BMFace.calc_area "Link to this definition")
    :   Return the area of the face.

        Returns:
        :   Return the area of the face.

        Return type:
        :   float

    calc\_center\_bounds()[#](#bmesh.types.BMFace.calc_center_bounds "Link to this definition")
    :   Return bounds center of the face.

        Returns:
        :   a 3D vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_center\_median()[#](#bmesh.types.BMFace.calc_center_median "Link to this definition")
    :   Return median center of the face.

        Returns:
        :   a 3D vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_center\_median\_weighted()[#](#bmesh.types.BMFace.calc_center_median_weighted "Link to this definition")
    :   Return median center of the face weighted by edge lengths.

        Returns:
        :   a 3D vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_perimeter()[#](#bmesh.types.BMFace.calc_perimeter "Link to this definition")
    :   Return the perimeter of the face.

        Returns:
        :   Return the perimeter of the face.

        Return type:
        :   float

    calc\_tangent\_edge()[#](#bmesh.types.BMFace.calc_tangent_edge "Link to this definition")
    :   Return face tangent based on longest edge.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_tangent\_edge\_diagonal()[#](#bmesh.types.BMFace.calc_tangent_edge_diagonal "Link to this definition")
    :   Return face tangent based on the edge farthest from any vertex.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_tangent\_edge\_pair()[#](#bmesh.types.BMFace.calc_tangent_edge_pair "Link to this definition")
    :   Return face tangent based on the two longest disconnected edges.

        * Tris: Use the edge pair with the most similar lengths.
        * Quads: Use the longest edge pair.
        * NGons: Use the two longest disconnected edges.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_tangent\_vert\_diagonal()[#](#bmesh.types.BMFace.calc_tangent_vert_diagonal "Link to this definition")
    :   Return face tangent based on the two most distant vertices.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    copy(*verts=True*, *edges=True*)[#](#bmesh.types.BMFace.copy "Link to this definition")
    :   Make a copy of this face.

        Parameters:
        :   * **verts** (*boolean*) – When set, the faces verts will be duplicated too.
            * **edges** (*boolean*) – When set, the faces edges will be duplicated too.

        Returns:
        :   The newly created face.

        Return type:
        :   [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

    copy\_from(*other*)[#](#bmesh.types.BMFace.copy_from "Link to this definition")
    :   Copy values from another element of matching type.

    copy\_from\_face\_interp(*face*, *vert=True*)[#](#bmesh.types.BMFace.copy_from_face_interp "Link to this definition")
    :   Interpolate the customdata from another face onto this one (faces should overlap).

        Parameters:
        :   * **face** ([`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")) – The face to interpolate data from.
            * **vert** (*boolean*) – When True, also copy vertex data.

    hide\_set(*hide*)[#](#bmesh.types.BMFace.hide_set "Link to this definition")
    :   Set the hide state.
        This is different from the *hide* attribute because it updates the selection and hide state of associated geometry.

        Parameters:
        :   **hide** (*boolean*) – Hidden or visible.

    normal\_flip()[#](#bmesh.types.BMFace.normal_flip "Link to this definition")
    :   Reverses winding of a face, which flips its normal.

    normal\_update()[#](#bmesh.types.BMFace.normal_update "Link to this definition")
    :   Update face normal based on the positions of the face verts.
        This does not update the normals of face verts.

    select\_set(*select*)[#](#bmesh.types.BMFace.select_set "Link to this definition")
    :   Set the selection.
        This is different from the *select* attribute because it updates the selection state of associated geometry.

        Parameters:
        :   **select** (*boolean*) – Select or de-select.

        Note

        Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex won’t de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.

    edges[#](#bmesh.types.BMFace.edges "Link to this definition")
    :   Edges of this face, (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge")

    hide[#](#bmesh.types.BMFace.hide "Link to this definition")
    :   Hidden state of this element.

        Type:
        :   boolean

    index[#](#bmesh.types.BMFace.index "Link to this definition")
    :   Index of this element.

        Type:
        :   int

        Note

        This value is not necessarily valid, while editing the mesh it can become *dirty*.

        It’s also possible to assign any number to this attribute for a scripts internal logic.

        To ensure the value is up to date - see [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update").

    is\_valid[#](#bmesh.types.BMFace.is_valid "Link to this definition")
    :   True when this element is valid (hasn’t been removed).

        Type:
        :   boolean

    loops[#](#bmesh.types.BMFace.loops "Link to this definition")
    :   Loops of this face, (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    material\_index[#](#bmesh.types.BMFace.material_index "Link to this definition")
    :   The face’s material index.

        Type:
        :   int

    normal[#](#bmesh.types.BMFace.normal "Link to this definition")
    :   The normal for this face as a 3D, wrapped vector.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    select[#](#bmesh.types.BMFace.select "Link to this definition")
    :   Selected state of this element.

        Type:
        :   boolean

    smooth[#](#bmesh.types.BMFace.smooth "Link to this definition")
    :   Smooth state of this element.

        Type:
        :   boolean

    tag[#](#bmesh.types.BMFace.tag "Link to this definition")
    :   Generic attribute scripts can use for own logic

        Type:
        :   boolean

    verts[#](#bmesh.types.BMFace.verts "Link to this definition")
    :   Verts of this face, (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")

*class* bmesh.types.BMLoop[#](#bmesh.types.BMLoop "Link to this definition")
:   This is normally accessed from [`BMFace.loops`](#bmesh.types.BMFace.loops "bmesh.types.BMFace.loops") where each face loop represents a corner of the face.

    calc\_angle()[#](#bmesh.types.BMLoop.calc_angle "Link to this definition")
    :   Return the angle at this loops corner of the face.
        This is calculated so sharper corners give lower angles.

        Returns:
        :   The angle in radians.

        Return type:
        :   float

    calc\_normal()[#](#bmesh.types.BMLoop.calc_normal "Link to this definition")
    :   Return normal at this loops corner of the face.
        Falls back to the face normal for straight lines.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    calc\_tangent()[#](#bmesh.types.BMLoop.calc_tangent "Link to this definition")
    :   Return the tangent at this loops corner of the face (pointing inward into the face).
        Falls back to the face normal for straight lines.

        Returns:
        :   a normalized vector.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    copy\_from(*other*)[#](#bmesh.types.BMLoop.copy_from "Link to this definition")
    :   Copy values from another element of matching type.

    copy\_from\_face\_interp(*face*, *vert=True*, *multires=True*)[#](#bmesh.types.BMLoop.copy_from_face_interp "Link to this definition")
    :   Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).

        Parameters:
        :   * **face** ([`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")) – The face to interpolate data from.
            * **vert** (*boolean*) – When enabled, interpolate the loops vertex data (optional).
            * **multires** (*boolean*) – When enabled, interpolate the loops multires data (optional).

    edge[#](#bmesh.types.BMLoop.edge "Link to this definition")
    :   The loop’s edge (between this loop and the next), (read-only).

        Type:
        :   [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge")

    face[#](#bmesh.types.BMLoop.face "Link to this definition")
    :   The face this loop makes (read-only).

        Type:
        :   [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

    index[#](#bmesh.types.BMLoop.index "Link to this definition")
    :   Index of this element.

        Type:
        :   int

        Note

        This value is not necessarily valid, while editing the mesh it can become *dirty*.

        It’s also possible to assign any number to this attribute for a scripts internal logic.

        To ensure the value is up to date - see [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update").

    is\_convex[#](#bmesh.types.BMLoop.is_convex "Link to this definition")
    :   True when this loop is at the convex corner of a face, depends on a valid face normal (read-only).

        Type:
        :   boolean

    is\_valid[#](#bmesh.types.BMLoop.is_valid "Link to this definition")
    :   True when this element is valid (hasn’t been removed).

        Type:
        :   boolean

    link\_loop\_next[#](#bmesh.types.BMLoop.link_loop_next "Link to this definition")
    :   The next face corner (read-only).

        Type:
        :   [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    link\_loop\_prev[#](#bmesh.types.BMLoop.link_loop_prev "Link to this definition")
    :   The previous face corner (read-only).

        Type:
        :   [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    link\_loop\_radial\_next[#](#bmesh.types.BMLoop.link_loop_radial_next "Link to this definition")
    :   The next loop around the edge (read-only).

        Type:
        :   [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    link\_loop\_radial\_prev[#](#bmesh.types.BMLoop.link_loop_radial_prev "Link to this definition")
    :   The previous loop around the edge (read-only).

        Type:
        :   [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    link\_loops[#](#bmesh.types.BMLoop.link_loops "Link to this definition")
    :   Loops connected to this loop, (read-only).

        Type:
        :   [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") of [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop")

    tag[#](#bmesh.types.BMLoop.tag "Link to this definition")
    :   Generic attribute scripts can use for own logic

        Type:
        :   boolean

    vert[#](#bmesh.types.BMLoop.vert "Link to this definition")
    :   The loop’s vertex (read-only).

        Type:
        :   [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")

## Sequence Accessors[#](#sequence-accessors "Link to this heading")

*class* bmesh.types.BMElemSeq[#](#bmesh.types.BMElemSeq "Link to this definition")
:   General sequence type used for accessing any sequence of
    [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert"), [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge"), [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace"), [`BMLoop`](#bmesh.types.BMLoop "bmesh.types.BMLoop").

    When accessed via [`BMesh.verts`](#bmesh.types.BMesh.verts "bmesh.types.BMesh.verts"), [`BMesh.edges`](#bmesh.types.BMesh.edges "bmesh.types.BMesh.edges"), [`BMesh.faces`](#bmesh.types.BMesh.faces "bmesh.types.BMesh.faces")
    there are also functions to create/remove items.

    index\_update()[#](#bmesh.types.BMElemSeq.index_update "Link to this definition")
    :   Initialize the index values of this sequence.

        This is the equivalent of looping over all elements and assigning the index values.

        ```
        for index, ele in enumerate(sequence):
            ele.index = index
        ```

        Note

        Running this on sequences besides [`BMesh.verts`](#bmesh.types.BMesh.verts "bmesh.types.BMesh.verts"), [`BMesh.edges`](#bmesh.types.BMesh.edges "bmesh.types.BMesh.edges"), [`BMesh.faces`](#bmesh.types.BMesh.faces "bmesh.types.BMesh.faces")
        works but won’t result in each element having a valid index, instead its order in the sequence will be set.

*class* bmesh.types.BMVertSeq[#](#bmesh.types.BMVertSeq "Link to this definition")
:   ensure\_lookup\_table()[#](#bmesh.types.BMVertSeq.ensure_lookup_table "Link to this definition")
    :   Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg `bm.verts[index]`.

        This needs to be called again after adding/removing data in this sequence.

    index\_update()[#](#bmesh.types.BMVertSeq.index_update "Link to this definition")
    :   Initialize the index values of this sequence.

        This is the equivalent of looping over all elements and assigning the index values.

        ```
        for index, ele in enumerate(sequence):
            ele.index = index
        ```

        Note

        Running this on sequences besides [`BMesh.verts`](#bmesh.types.BMesh.verts "bmesh.types.BMesh.verts"), [`BMesh.edges`](#bmesh.types.BMesh.edges "bmesh.types.BMesh.edges"), [`BMesh.faces`](#bmesh.types.BMesh.faces "bmesh.types.BMesh.faces")
        works but won’t result in each element having a valid index, instead its order in the sequence will be set.

    new(*co=(0.0, 0.0, 0.0)*, *example=None*)[#](#bmesh.types.BMVertSeq.new "Link to this definition")
    :   Create a new vertex.

        Parameters:
        :   * **co** (*float triplet*) – The initial location of the vertex (optional argument).
            * **example** ([`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – Existing vert to initialize settings.

        Returns:
        :   The newly created vertex.

        Return type:
        :   [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")

    remove(*vert*)[#](#bmesh.types.BMVertSeq.remove "Link to this definition")
    :   Remove a vert.

    sort(*key=None*, *reverse=False*)[#](#bmesh.types.BMVertSeq.sort "Link to this definition")
    :   Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update") can be used for that.

        Parameters:
        :   * **key** – The key that sets the ordering of the elements.
            * **reverse** – Reverse the order of the elements

        Note

        When the ‘key’ argument is not provided, the elements are reordered following their current index value.
        In particular this can be used by setting indices manually before calling this method.

        Warning

        Existing references to the N’th element, will continue to point the data at that index.

    layers[#](#bmesh.types.BMVertSeq.layers "Link to this definition")
    :   custom-data layers (read-only).

        Type:
        :   [`BMLayerAccessVert`](#bmesh.types.BMLayerAccessVert "bmesh.types.BMLayerAccessVert")

*class* bmesh.types.BMEdgeSeq[#](#bmesh.types.BMEdgeSeq "Link to this definition")
:   ensure\_lookup\_table()[#](#bmesh.types.BMEdgeSeq.ensure_lookup_table "Link to this definition")
    :   Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg `bm.verts[index]`.

        This needs to be called again after adding/removing data in this sequence.

    get(*verts*, *fallback=None*)[#](#bmesh.types.BMEdgeSeq.get "Link to this definition")
    :   Return an edge which uses the **verts** passed.

        Parameters:
        :   * **verts** (sequence of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – Sequence of verts.
            * **fallback** – Return this value if nothing is found.

        Returns:
        :   The edge found or None

        Return type:
        :   [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge")

    index\_update()[#](#bmesh.types.BMEdgeSeq.index_update "Link to this definition")
    :   Initialize the index values of this sequence.

        This is the equivalent of looping over all elements and assigning the index values.

        ```
        for index, ele in enumerate(sequence):
            ele.index = index
        ```

        Note

        Running this on sequences besides [`BMesh.verts`](#bmesh.types.BMesh.verts "bmesh.types.BMesh.verts"), [`BMesh.edges`](#bmesh.types.BMesh.edges "bmesh.types.BMesh.edges"), [`BMesh.faces`](#bmesh.types.BMesh.faces "bmesh.types.BMesh.faces")
        works but won’t result in each element having a valid index, instead its order in the sequence will be set.

    new(*verts*, *example=None*)[#](#bmesh.types.BMEdgeSeq.new "Link to this definition")
    :   Create a new edge from a given pair of verts.

        Parameters:
        :   * **verts** (pair of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – Vertex pair.
            * **example** ([`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge")) – Existing edge to initialize settings (optional argument).

        Returns:
        :   The newly created edge.

        Return type:
        :   [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge")

    remove(*edge*)[#](#bmesh.types.BMEdgeSeq.remove "Link to this definition")
    :   Remove an edge.

    sort(*key=None*, *reverse=False*)[#](#bmesh.types.BMEdgeSeq.sort "Link to this definition")
    :   Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update") can be used for that.

        Parameters:
        :   * **key** – The key that sets the ordering of the elements.
            * **reverse** – Reverse the order of the elements

        Note

        When the ‘key’ argument is not provided, the elements are reordered following their current index value.
        In particular this can be used by setting indices manually before calling this method.

        Warning

        Existing references to the N’th element, will continue to point the data at that index.

    layers[#](#bmesh.types.BMEdgeSeq.layers "Link to this definition")
    :   custom-data layers (read-only).

        Type:
        :   [`BMLayerAccessEdge`](#bmesh.types.BMLayerAccessEdge "bmesh.types.BMLayerAccessEdge")

*class* bmesh.types.BMFaceSeq[#](#bmesh.types.BMFaceSeq "Link to this definition")
:   ensure\_lookup\_table()[#](#bmesh.types.BMFaceSeq.ensure_lookup_table "Link to this definition")
    :   Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg `bm.verts[index]`.

        This needs to be called again after adding/removing data in this sequence.

    get(*verts*, *fallback=None*)[#](#bmesh.types.BMFaceSeq.get "Link to this definition")
    :   Return a face which uses the **verts** passed.

        Parameters:
        :   * **verts** (sequence of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – Sequence of verts.
            * **fallback** – Return this value if nothing is found.

        Returns:
        :   The face found or None

        Return type:
        :   [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

    index\_update()[#](#bmesh.types.BMFaceSeq.index_update "Link to this definition")
    :   Initialize the index values of this sequence.

        This is the equivalent of looping over all elements and assigning the index values.

        ```
        for index, ele in enumerate(sequence):
            ele.index = index
        ```

        Note

        Running this on sequences besides [`BMesh.verts`](#bmesh.types.BMesh.verts "bmesh.types.BMesh.verts"), [`BMesh.edges`](#bmesh.types.BMesh.edges "bmesh.types.BMesh.edges"), [`BMesh.faces`](#bmesh.types.BMesh.faces "bmesh.types.BMesh.faces")
        works but won’t result in each element having a valid index, instead its order in the sequence will be set.

    new(*verts*, *example=None*)[#](#bmesh.types.BMFaceSeq.new "Link to this definition")
    :   Create a new face from a given set of verts.

        Parameters:
        :   * **verts** (sequence of [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert")) – Sequence of 3 or more verts.
            * **example** ([`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")) – Existing face to initialize settings (optional argument).

        Returns:
        :   The newly created face.

        Return type:
        :   [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

    remove(*face*)[#](#bmesh.types.BMFaceSeq.remove "Link to this definition")
    :   Remove a face.

    sort(*key=None*, *reverse=False*)[#](#bmesh.types.BMFaceSeq.sort "Link to this definition")
    :   Sort the elements of this sequence, using an optional custom sort key.
        Indices of elements are not changed, [`BMElemSeq.index_update`](#bmesh.types.BMElemSeq.index_update "bmesh.types.BMElemSeq.index_update") can be used for that.

        Parameters:
        :   * **key** – The key that sets the ordering of the elements.
            * **reverse** – Reverse the order of the elements

        Note

        When the ‘key’ argument is not provided, the elements are reordered following their current index value.
        In particular this can be used by setting indices manually before calling this method.

        Warning

        Existing references to the N’th element, will continue to point the data at that index.

    active[#](#bmesh.types.BMFaceSeq.active "Link to this definition")
    :   active face.

        Type:
        :   [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace") or None

    layers[#](#bmesh.types.BMFaceSeq.layers "Link to this definition")
    :   custom-data layers (read-only).

        Type:
        :   [`BMLayerAccessFace`](#bmesh.types.BMLayerAccessFace "bmesh.types.BMLayerAccessFace")

*class* bmesh.types.BMLoopSeq[#](#bmesh.types.BMLoopSeq "Link to this definition")
:   layers[#](#bmesh.types.BMLoopSeq.layers "Link to this definition")
    :   custom-data layers (read-only).

        Type:
        :   [`BMLayerAccessLoop`](#bmesh.types.BMLayerAccessLoop "bmesh.types.BMLayerAccessLoop")

*class* bmesh.types.BMIter[#](#bmesh.types.BMIter "Link to this definition")
:   Internal BMesh type for looping over verts/faces/edges,
    used for iterating over [`BMElemSeq`](#bmesh.types.BMElemSeq "bmesh.types.BMElemSeq") types.

## Selection History[#](#selection-history "Link to this heading")

*class* bmesh.types.BMEditSelSeq[#](#bmesh.types.BMEditSelSeq "Link to this definition")
:   add(*element*)[#](#bmesh.types.BMEditSelSeq.add "Link to this definition")
    :   Add an element to the selection history (no action taken if its already added).

    clear()[#](#bmesh.types.BMEditSelSeq.clear "Link to this definition")
    :   Empties the selection history.

    discard(*element*)[#](#bmesh.types.BMEditSelSeq.discard "Link to this definition")
    :   Discard an element from the selection history.

        Like remove but doesn’t raise an error when the elements not in the selection list.

    remove(*element*)[#](#bmesh.types.BMEditSelSeq.remove "Link to this definition")
    :   Remove an element from the selection history.

    validate()[#](#bmesh.types.BMEditSelSeq.validate "Link to this definition")
    :   Ensures all elements in the selection history are selected.

    active[#](#bmesh.types.BMEditSelSeq.active "Link to this definition")
    :   The last selected element or None (read-only).

        Type:
        :   [`BMVert`](#bmesh.types.BMVert "bmesh.types.BMVert"), [`BMEdge`](#bmesh.types.BMEdge "bmesh.types.BMEdge") or [`BMFace`](#bmesh.types.BMFace "bmesh.types.BMFace")

*class* bmesh.types.BMEditSelIter[#](#bmesh.types.BMEditSelIter "Link to this definition")

## Custom-Data Layer Access[#](#custom-data-layer-access "Link to this heading")

*class* bmesh.types.BMLayerAccessVert[#](#bmesh.types.BMLayerAccessVert "Link to this definition")
:   Exposes custom-data layer attributes.

    color[#](#bmesh.types.BMLayerAccessVert.color "Link to this definition")
    :   Generic RGBA color with 8-bit precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    deform[#](#bmesh.types.BMLayerAccessVert.deform "Link to this definition")
    :   Vertex deform weight [`BMDeformVert`](#bmesh.types.BMDeformVert "bmesh.types.BMDeformVert") (TODO).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float[#](#bmesh.types.BMLayerAccessVert.float "Link to this definition")
    :   Generic float custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_color[#](#bmesh.types.BMLayerAccessVert.float_color "Link to this definition")
    :   Generic RGBA color with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_vector[#](#bmesh.types.BMLayerAccessVert.float_vector "Link to this definition")
    :   Generic 3D vector with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    int[#](#bmesh.types.BMLayerAccessVert.int "Link to this definition")
    :   Generic int custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    shape[#](#bmesh.types.BMLayerAccessVert.shape "Link to this definition")
    :   Vertex shapekey absolute location (as a 3D Vector).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    skin[#](#bmesh.types.BMLayerAccessVert.skin "Link to this definition")
    :   Accessor for skin layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    string[#](#bmesh.types.BMLayerAccessVert.string "Link to this definition")
    :   Generic string custom-data layer (exposed as bytes, 255 max length).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

*class* bmesh.types.BMLayerAccessEdge[#](#bmesh.types.BMLayerAccessEdge "Link to this definition")
:   Exposes custom-data layer attributes.

    color[#](#bmesh.types.BMLayerAccessEdge.color "Link to this definition")
    :   Generic RGBA color with 8-bit precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float[#](#bmesh.types.BMLayerAccessEdge.float "Link to this definition")
    :   Generic float custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_color[#](#bmesh.types.BMLayerAccessEdge.float_color "Link to this definition")
    :   Generic RGBA color with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_vector[#](#bmesh.types.BMLayerAccessEdge.float_vector "Link to this definition")
    :   Generic 3D vector with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    freestyle[#](#bmesh.types.BMLayerAccessEdge.freestyle "Link to this definition")
    :   Accessor for Freestyle edge layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    int[#](#bmesh.types.BMLayerAccessEdge.int "Link to this definition")
    :   Generic int custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    string[#](#bmesh.types.BMLayerAccessEdge.string "Link to this definition")
    :   Generic string custom-data layer (exposed as bytes, 255 max length).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

*class* bmesh.types.BMLayerAccessFace[#](#bmesh.types.BMLayerAccessFace "Link to this definition")
:   Exposes custom-data layer attributes.

    color[#](#bmesh.types.BMLayerAccessFace.color "Link to this definition")
    :   Generic RGBA color with 8-bit precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float[#](#bmesh.types.BMLayerAccessFace.float "Link to this definition")
    :   Generic float custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_color[#](#bmesh.types.BMLayerAccessFace.float_color "Link to this definition")
    :   Generic RGBA color with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_vector[#](#bmesh.types.BMLayerAccessFace.float_vector "Link to this definition")
    :   Generic 3D vector with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    freestyle[#](#bmesh.types.BMLayerAccessFace.freestyle "Link to this definition")
    :   Accessor for Freestyle face layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    int[#](#bmesh.types.BMLayerAccessFace.int "Link to this definition")
    :   Generic int custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    string[#](#bmesh.types.BMLayerAccessFace.string "Link to this definition")
    :   Generic string custom-data layer (exposed as bytes, 255 max length).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

*class* bmesh.types.BMLayerAccessLoop[#](#bmesh.types.BMLayerAccessLoop "Link to this definition")
:   Exposes custom-data layer attributes.

    color[#](#bmesh.types.BMLayerAccessLoop.color "Link to this definition")
    :   Generic RGBA color with 8-bit precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float[#](#bmesh.types.BMLayerAccessLoop.float "Link to this definition")
    :   Generic float custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_color[#](#bmesh.types.BMLayerAccessLoop.float_color "Link to this definition")
    :   Generic RGBA color with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    float\_vector[#](#bmesh.types.BMLayerAccessLoop.float_vector "Link to this definition")
    :   Generic 3D vector with float precision custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    int[#](#bmesh.types.BMLayerAccessLoop.int "Link to this definition")
    :   Generic int custom-data layer.

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    string[#](#bmesh.types.BMLayerAccessLoop.string "Link to this definition")
    :   Generic string custom-data layer (exposed as bytes, 255 max length).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

    uv[#](#bmesh.types.BMLayerAccessLoop.uv "Link to this definition")
    :   Accessor for [`BMLoopUV`](#bmesh.types.BMLoopUV "bmesh.types.BMLoopUV") UV (as a 2D Vector).

        Type:
        :   [`BMLayerCollection`](#bmesh.types.BMLayerCollection "bmesh.types.BMLayerCollection")

*class* bmesh.types.BMLayerCollection[#](#bmesh.types.BMLayerCollection "Link to this definition")
:   Gives access to a collection of custom-data layers of the same type and behaves like Python dictionaries, except for the ability to do list like index access.

    get(*key*, *default=None*)[#](#bmesh.types.BMLayerCollection.get "Link to this definition")
    :   Returns the value of the layer matching the key or default
        when not found (matches Python’s dictionary function of the same name).

        Parameters:
        :   * **key** (*string*) – The key associated with the layer.
            * **default** (*Undefined*) – Optional argument for the value to return if
              *key* is not found.

    items()[#](#bmesh.types.BMLayerCollection.items "Link to this definition")
    :   Return the identifiers of collection members
        (matching Python’s dict.items() functionality).

        Returns:
        :   (key, value) pairs for each member of this collection.

        Return type:
        :   list of tuples

    keys()[#](#bmesh.types.BMLayerCollection.keys "Link to this definition")
    :   Return the identifiers of collection members
        (matching Python’s dict.keys() functionality).

        Returns:
        :   the identifiers for each member of this collection.

        Return type:
        :   list of strings

    new(*name*)[#](#bmesh.types.BMLayerCollection.new "Link to this definition")
    :   Create a new layer

        Parameters:
        :   **name** (*string*) – Optional name argument (will be made unique).

        Returns:
        :   The newly created layer.

        Return type:
        :   [`BMLayerItem`](#bmesh.types.BMLayerItem "bmesh.types.BMLayerItem")

    remove(*layer*)[#](#bmesh.types.BMLayerCollection.remove "Link to this definition")
    :   Remove a layer

        Parameters:
        :   **layer** ([`BMLayerItem`](#bmesh.types.BMLayerItem "bmesh.types.BMLayerItem")) – The layer to remove.

    values()[#](#bmesh.types.BMLayerCollection.values "Link to this definition")
    :   Return the values of collection
        (matching Python’s dict.values() functionality).

        Returns:
        :   the members of this collection.

        Return type:
        :   list

    verify()[#](#bmesh.types.BMLayerCollection.verify "Link to this definition")
    :   Create a new layer or return an existing active layer

        Returns:
        :   The newly verified layer.

        Return type:
        :   [`BMLayerItem`](#bmesh.types.BMLayerItem "bmesh.types.BMLayerItem")

    active[#](#bmesh.types.BMLayerCollection.active "Link to this definition")
    :   The active layer of this type (read-only).

        Type:
        :   [`BMLayerItem`](#bmesh.types.BMLayerItem "bmesh.types.BMLayerItem")

    is\_singleton[#](#bmesh.types.BMLayerCollection.is_singleton "Link to this definition")
    :   True if there can exists only one layer of this type (read-only).

        Type:
        :   boolean

*class* bmesh.types.BMLayerItem[#](#bmesh.types.BMLayerItem "Link to this definition")
:   Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data.

    copy\_from(*other*)[#](#bmesh.types.BMLayerItem.copy_from "Link to this definition")
    :   Return a copy of the layer

        Parameters:
        :   **other** ([`BMLayerItem`](#bmesh.types.BMLayerItem "bmesh.types.BMLayerItem")) – Another layer to copy from.

    name[#](#bmesh.types.BMLayerItem.name "Link to this definition")
    :   The layers unique name (read-only).

        Type:
        :   string

## Custom-Data Layer Types[#](#custom-data-layer-types "Link to this heading")

*class* bmesh.types.BMLoopUV[#](#bmesh.types.BMLoopUV "Link to this definition")
:   pin\_uv[#](#bmesh.types.BMLoopUV.pin_uv "Link to this definition")
    :   UV pin state.

        Type:
        :   boolean

    select[#](#bmesh.types.BMLoopUV.select "Link to this definition")
    :   UV select state.

        Type:
        :   boolean

    select\_edge[#](#bmesh.types.BMLoopUV.select_edge "Link to this definition")
    :   UV edge select state.

        Type:
        :   boolean

    uv[#](#bmesh.types.BMLoopUV.uv "Link to this definition")
    :   Loops UV (as a 2D Vector).

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

*class* bmesh.types.BMDeformVert[#](#bmesh.types.BMDeformVert "Link to this definition")
:   clear()[#](#bmesh.types.BMDeformVert.clear "Link to this definition")
    :   Clears all weights.

    get(*key*, *default=None*)[#](#bmesh.types.BMDeformVert.get "Link to this definition")
    :   Returns the deform weight matching the key or default
        when not found (matches Python’s dictionary function of the same name).

        Parameters:
        :   * **key** (*int*) – The key associated with deform weight.
            * **default** (*Undefined*) – Optional argument for the value to return if
              *key* is not found.

    items()[#](#bmesh.types.BMDeformVert.items "Link to this definition")
    :   Return (group, weight) pairs for this vertex
        (matching Python’s dict.items() functionality).

        Returns:
        :   (key, value) pairs for each deform weight of this vertex.

        Return type:
        :   list of tuples

    keys()[#](#bmesh.types.BMDeformVert.keys "Link to this definition")
    :   Return the group indices used by this vertex
        (matching Python’s dict.keys() functionality).

        Returns:
        :   the deform group this vertex uses

        Return type:
        :   list of ints

    values()[#](#bmesh.types.BMDeformVert.values "Link to this definition")
    :   Return the weights of the deform vertex
        (matching Python’s dict.values() functionality).

        Returns:
        :   The weights that influence this vertex

        Return type:
        :   list of floats

[Next

BMesh Utilities (bmesh.utils)](../utils/index.md)
[Previous

BMesh Operators (bmesh.ops)](../ops/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bmesh.types.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbmesh.types.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* BMesh Types (bmesh.types)
  + [Base Mesh Type](#base-mesh-type)
    - [`BMesh`](#bmesh.types.BMesh)
      * [`BMesh.calc_loop_triangles()`](#bmesh.types.BMesh.calc_loop_triangles)
      * [`BMesh.calc_volume()`](#bmesh.types.BMesh.calc_volume)
      * [`BMesh.clear()`](#bmesh.types.BMesh.clear)
      * [`BMesh.copy()`](#bmesh.types.BMesh.copy)
      * [`BMesh.free()`](#bmesh.types.BMesh.free)
      * [`BMesh.from_mesh()`](#bmesh.types.BMesh.from_mesh)
      * [`BMesh.from_object()`](#bmesh.types.BMesh.from_object)
      * [`BMesh.normal_update()`](#bmesh.types.BMesh.normal_update)
      * [`BMesh.select_flush()`](#bmesh.types.BMesh.select_flush)
      * [`BMesh.select_flush_mode()`](#bmesh.types.BMesh.select_flush_mode)
      * [`BMesh.to_mesh()`](#bmesh.types.BMesh.to_mesh)
      * [`BMesh.transform()`](#bmesh.types.BMesh.transform)
      * [`BMesh.edges`](#bmesh.types.BMesh.edges)
      * [`BMesh.faces`](#bmesh.types.BMesh.faces)
      * [`BMesh.is_valid`](#bmesh.types.BMesh.is_valid)
      * [`BMesh.is_wrapped`](#bmesh.types.BMesh.is_wrapped)
      * [`BMesh.loops`](#bmesh.types.BMesh.loops)
      * [`BMesh.select_history`](#bmesh.types.BMesh.select_history)
      * [`BMesh.select_mode`](#bmesh.types.BMesh.select_mode)
      * [`BMesh.verts`](#bmesh.types.BMesh.verts)
  + [Mesh Elements](#mesh-elements)
    - [`BMVert`](#bmesh.types.BMVert)
      * [`BMVert.calc_edge_angle()`](#bmesh.types.BMVert.calc_edge_angle)
      * [`BMVert.calc_shell_factor()`](#bmesh.types.BMVert.calc_shell_factor)
      * [`BMVert.copy_from()`](#bmesh.types.BMVert.copy_from)
      * [`BMVert.copy_from_face_interp()`](#bmesh.types.BMVert.copy_from_face_interp)
      * [`BMVert.copy_from_vert_interp()`](#bmesh.types.BMVert.copy_from_vert_interp)
      * [`BMVert.hide_set()`](#bmesh.types.BMVert.hide_set)
      * [`BMVert.normal_update()`](#bmesh.types.BMVert.normal_update)
      * [`BMVert.select_set()`](#bmesh.types.BMVert.select_set)
      * [`BMVert.co`](#bmesh.types.BMVert.co)
      * [`BMVert.hide`](#bmesh.types.BMVert.hide)
      * [`BMVert.index`](#bmesh.types.BMVert.index)
      * [`BMVert.is_boundary`](#bmesh.types.BMVert.is_boundary)
      * [`BMVert.is_manifold`](#bmesh.types.BMVert.is_manifold)
      * [`BMVert.is_valid`](#bmesh.types.BMVert.is_valid)
      * [`BMVert.is_wire`](#bmesh.types.BMVert.is_wire)
      * [`BMVert.link_edges`](#bmesh.types.BMVert.link_edges)
      * [`BMVert.link_faces`](#bmesh.types.BMVert.link_faces)
      * [`BMVert.link_loops`](#bmesh.types.BMVert.link_loops)
      * [`BMVert.normal`](#bmesh.types.BMVert.normal)
      * [`BMVert.select`](#bmesh.types.BMVert.select)
      * [`BMVert.tag`](#bmesh.types.BMVert.tag)
    - [`BMEdge`](#bmesh.types.BMEdge)
      * [`BMEdge.calc_face_angle()`](#bmesh.types.BMEdge.calc_face_angle)
      * [`BMEdge.calc_face_angle_signed()`](#bmesh.types.BMEdge.calc_face_angle_signed)
      * [`BMEdge.calc_length()`](#bmesh.types.BMEdge.calc_length)
      * [`BMEdge.calc_tangent()`](#bmesh.types.BMEdge.calc_tangent)
      * [`BMEdge.copy_from()`](#bmesh.types.BMEdge.copy_from)
      * [`BMEdge.hide_set()`](#bmesh.types.BMEdge.hide_set)
      * [`BMEdge.normal_update()`](#bmesh.types.BMEdge.normal_update)
      * [`BMEdge.other_vert()`](#bmesh.types.BMEdge.other_vert)
      * [`BMEdge.select_set()`](#bmesh.types.BMEdge.select_set)
      * [`BMEdge.hide`](#bmesh.types.BMEdge.hide)
      * [`BMEdge.index`](#bmesh.types.BMEdge.index)
      * [`BMEdge.is_boundary`](#bmesh.types.BMEdge.is_boundary)
      * [`BMEdge.is_contiguous`](#bmesh.types.BMEdge.is_contiguous)
      * [`BMEdge.is_convex`](#bmesh.types.BMEdge.is_convex)
      * [`BMEdge.is_manifold`](#bmesh.types.BMEdge.is_manifold)
      * [`BMEdge.is_valid`](#bmesh.types.BMEdge.is_valid)
      * [`BMEdge.is_wire`](#bmesh.types.BMEdge.is_wire)
      * [`BMEdge.link_faces`](#bmesh.types.BMEdge.link_faces)
      * [`BMEdge.link_loops`](#bmesh.types.BMEdge.link_loops)
      * [`BMEdge.seam`](#bmesh.types.BMEdge.seam)
      * [`BMEdge.select`](#bmesh.types.BMEdge.select)
      * [`BMEdge.smooth`](#bmesh.types.BMEdge.smooth)
      * [`BMEdge.tag`](#bmesh.types.BMEdge.tag)
      * [`BMEdge.verts`](#bmesh.types.BMEdge.verts)
    - [`BMFace`](#bmesh.types.BMFace)
      * [`BMFace.calc_area()`](#bmesh.types.BMFace.calc_area)
      * [`BMFace.calc_center_bounds()`](#bmesh.types.BMFace.calc_center_bounds)
      * [`BMFace.calc_center_median()`](#bmesh.types.BMFace.calc_center_median)
      * [`BMFace.calc_center_median_weighted()`](#bmesh.types.BMFace.calc_center_median_weighted)
      * [`BMFace.calc_perimeter()`](#bmesh.types.BMFace.calc_perimeter)
      * [`BMFace.calc_tangent_edge()`](#bmesh.types.BMFace.calc_tangent_edge)
      * [`BMFace.calc_tangent_edge_diagonal()`](#bmesh.types.BMFace.calc_tangent_edge_diagonal)
      * [`BMFace.calc_tangent_edge_pair()`](#bmesh.types.BMFace.calc_tangent_edge_pair)
      * [`BMFace.calc_tangent_vert_diagonal()`](#bmesh.types.BMFace.calc_tangent_vert_diagonal)
      * [`BMFace.copy()`](#bmesh.types.BMFace.copy)
      * [`BMFace.copy_from()`](#bmesh.types.BMFace.copy_from)
      * [`BMFace.copy_from_face_interp()`](#bmesh.types.BMFace.copy_from_face_interp)
      * [`BMFace.hide_set()`](#bmesh.types.BMFace.hide_set)
      * [`BMFace.normal_flip()`](#bmesh.types.BMFace.normal_flip)
      * [`BMFace.normal_update()`](#bmesh.types.BMFace.normal_update)
      * [`BMFace.select_set()`](#bmesh.types.BMFace.select_set)
      * [`BMFace.edges`](#bmesh.types.BMFace.edges)
      * [`BMFace.hide`](#bmesh.types.BMFace.hide)
      * [`BMFace.index`](#bmesh.types.BMFace.index)
      * [`BMFace.is_valid`](#bmesh.types.BMFace.is_valid)
      * [`BMFace.loops`](#bmesh.types.BMFace.loops)
      * [`BMFace.material_index`](#bmesh.types.BMFace.material_index)
      * [`BMFace.normal`](#bmesh.types.BMFace.normal)
      * [`BMFace.select`](#bmesh.types.BMFace.select)
      * [`BMFace.smooth`](#bmesh.types.BMFace.smooth)
      * [`BMFace.tag`](#bmesh.types.BMFace.tag)
      * [`BMFace.verts`](#bmesh.types.BMFace.verts)
    - [`BMLoop`](#bmesh.types.BMLoop)
      * [`BMLoop.calc_angle()`](#bmesh.types.BMLoop.calc_angle)
      * [`BMLoop.calc_normal()`](#bmesh.types.BMLoop.calc_normal)
      * [`BMLoop.calc_tangent()`](#bmesh.types.BMLoop.calc_tangent)
      * [`BMLoop.copy_from()`](#bmesh.types.BMLoop.copy_from)
      * [`BMLoop.copy_from_face_interp()`](#bmesh.types.BMLoop.copy_from_face_interp)
      * [`BMLoop.edge`](#bmesh.types.BMLoop.edge)
      * [`BMLoop.face`](#bmesh.types.BMLoop.face)
      * [`BMLoop.index`](#bmesh.types.BMLoop.index)
      * [`BMLoop.is_convex`](#bmesh.types.BMLoop.is_convex)
      * [`BMLoop.is_valid`](#bmesh.types.BMLoop.is_valid)
      * [`BMLoop.link_loop_next`](#bmesh.types.BMLoop.link_loop_next)
      * [`BMLoop.link_loop_prev`](#bmesh.types.BMLoop.link_loop_prev)
      * [`BMLoop.link_loop_radial_next`](#bmesh.types.BMLoop.link_loop_radial_next)
      * [`BMLoop.link_loop_radial_prev`](#bmesh.types.BMLoop.link_loop_radial_prev)
      * [`BMLoop.link_loops`](#bmesh.types.BMLoop.link_loops)
      * [`BMLoop.tag`](#bmesh.types.BMLoop.tag)
      * [`BMLoop.vert`](#bmesh.types.BMLoop.vert)
  + [Sequence Accessors](#sequence-accessors)
    - [`BMElemSeq`](#bmesh.types.BMElemSeq)
      * [`BMElemSeq.index_update()`](#bmesh.types.BMElemSeq.index_update)
    - [`BMVertSeq`](#bmesh.types.BMVertSeq)
      * [`BMVertSeq.ensure_lookup_table()`](#bmesh.types.BMVertSeq.ensure_lookup_table)
      * [`BMVertSeq.index_update()`](#bmesh.types.BMVertSeq.index_update)
      * [`BMVertSeq.new()`](#bmesh.types.BMVertSeq.new)
      * [`BMVertSeq.remove()`](#bmesh.types.BMVertSeq.remove)
      * [`BMVertSeq.sort()`](#bmesh.types.BMVertSeq.sort)
      * [`BMVertSeq.layers`](#bmesh.types.BMVertSeq.layers)
    - [`BMEdgeSeq`](#bmesh.types.BMEdgeSeq)
      * [`BMEdgeSeq.ensure_lookup_table()`](#bmesh.types.BMEdgeSeq.ensure_lookup_table)
      * [`BMEdgeSeq.get()`](#bmesh.types.BMEdgeSeq.get)
      * [`BMEdgeSeq.index_update()`](#bmesh.types.BMEdgeSeq.index_update)
      * [`BMEdgeSeq.new()`](#bmesh.types.BMEdgeSeq.new)
      * [`BMEdgeSeq.remove()`](#bmesh.types.BMEdgeSeq.remove)
      * [`BMEdgeSeq.sort()`](#bmesh.types.BMEdgeSeq.sort)
      * [`BMEdgeSeq.layers`](#bmesh.types.BMEdgeSeq.layers)
    - [`BMFaceSeq`](#bmesh.types.BMFaceSeq)
      * [`BMFaceSeq.ensure_lookup_table()`](#bmesh.types.BMFaceSeq.ensure_lookup_table)
      * [`BMFaceSeq.get()`](#bmesh.types.BMFaceSeq.get)
      * [`BMFaceSeq.index_update()`](#bmesh.types.BMFaceSeq.index_update)
      * [`BMFaceSeq.new()`](#bmesh.types.BMFaceSeq.new)
      * [`BMFaceSeq.remove()`](#bmesh.types.BMFaceSeq.remove)
      * [`BMFaceSeq.sort()`](#bmesh.types.BMFaceSeq.sort)
      * [`BMFaceSeq.active`](#bmesh.types.BMFaceSeq.active)
      * [`BMFaceSeq.layers`](#bmesh.types.BMFaceSeq.layers)
    - [`BMLoopSeq`](#bmesh.types.BMLoopSeq)
      * [`BMLoopSeq.layers`](#bmesh.types.BMLoopSeq.layers)
    - [`BMIter`](#bmesh.types.BMIter)
  + [Selection History](#selection-history)
    - [`BMEditSelSeq`](#bmesh.types.BMEditSelSeq)
      * [`BMEditSelSeq.add()`](#bmesh.types.BMEditSelSeq.add)
      * [`BMEditSelSeq.clear()`](#bmesh.types.BMEditSelSeq.clear)
      * [`BMEditSelSeq.discard()`](#bmesh.types.BMEditSelSeq.discard)
      * [`BMEditSelSeq.remove()`](#bmesh.types.BMEditSelSeq.remove)
      * [`BMEditSelSeq.validate()`](#bmesh.types.BMEditSelSeq.validate)
      * [`BMEditSelSeq.active`](#bmesh.types.BMEditSelSeq.active)
    - [`BMEditSelIter`](#bmesh.types.BMEditSelIter)
  + [Custom-Data Layer Access](#custom-data-layer-access)
    - [`BMLayerAccessVert`](#bmesh.types.BMLayerAccessVert)
      * [`BMLayerAccessVert.color`](#bmesh.types.BMLayerAccessVert.color)
      * [`BMLayerAccessVert.deform`](#bmesh.types.BMLayerAccessVert.deform)
      * [`BMLayerAccessVert.float`](#bmesh.types.BMLayerAccessVert.float)
      * [`BMLayerAccessVert.float_color`](#bmesh.types.BMLayerAccessVert.float_color)
      * [`BMLayerAccessVert.float_vector`](#bmesh.types.BMLayerAccessVert.float_vector)
      * [`BMLayerAccessVert.int`](#bmesh.types.BMLayerAccessVert.int)
      * [`BMLayerAccessVert.shape`](#bmesh.types.BMLayerAccessVert.shape)
      * [`BMLayerAccessVert.skin`](#bmesh.types.BMLayerAccessVert.skin)
      * [`BMLayerAccessVert.string`](#bmesh.types.BMLayerAccessVert.string)
    - [`BMLayerAccessEdge`](#bmesh.types.BMLayerAccessEdge)
      * [`BMLayerAccessEdge.color`](#bmesh.types.BMLayerAccessEdge.color)
      * [`BMLayerAccessEdge.float`](#bmesh.types.BMLayerAccessEdge.float)
      * [`BMLayerAccessEdge.float_color`](#bmesh.types.BMLayerAccessEdge.float_color)
      * [`BMLayerAccessEdge.float_vector`](#bmesh.types.BMLayerAccessEdge.float_vector)
      * [`BMLayerAccessEdge.freestyle`](#bmesh.types.BMLayerAccessEdge.freestyle)
      * [`BMLayerAccessEdge.int`](#bmesh.types.BMLayerAccessEdge.int)
      * [`BMLayerAccessEdge.string`](#bmesh.types.BMLayerAccessEdge.string)
    - [`BMLayerAccessFace`](#bmesh.types.BMLayerAccessFace)
      * [`BMLayerAccessFace.color`](#bmesh.types.BMLayerAccessFace.color)
      * [`BMLayerAccessFace.float`](#bmesh.types.BMLayerAccessFace.float)
      * [`BMLayerAccessFace.float_color`](#bmesh.types.BMLayerAccessFace.float_color)
      * [`BMLayerAccessFace.float_vector`](#bmesh.types.BMLayerAccessFace.float_vector)
      * [`BMLayerAccessFace.freestyle`](#bmesh.types.BMLayerAccessFace.freestyle)
      * [`BMLayerAccessFace.int`](#bmesh.types.BMLayerAccessFace.int)
      * [`BMLayerAccessFace.string`](#bmesh.types.BMLayerAccessFace.string)
    - [`BMLayerAccessLoop`](#bmesh.types.BMLayerAccessLoop)
      * [`BMLayerAccessLoop.color`](#bmesh.types.BMLayerAccessLoop.color)
      * [`BMLayerAccessLoop.float`](#bmesh.types.BMLayerAccessLoop.float)
      * [`BMLayerAccessLoop.float_color`](#bmesh.types.BMLayerAccessLoop.float_color)
      * [`BMLayerAccessLoop.float_vector`](#bmesh.types.BMLayerAccessLoop.float_vector)
      * [`BMLayerAccessLoop.int`](#bmesh.types.BMLayerAccessLoop.int)
      * [`BMLayerAccessLoop.string`](#bmesh.types.BMLayerAccessLoop.string)
      * [`BMLayerAccessLoop.uv`](#bmesh.types.BMLayerAccessLoop.uv)
    - [`BMLayerCollection`](#bmesh.types.BMLayerCollection)
      * [`BMLayerCollection.get()`](#bmesh.types.BMLayerCollection.get)
      * [`BMLayerCollection.items()`](#bmesh.types.BMLayerCollection.items)
      * [`BMLayerCollection.keys()`](#bmesh.types.BMLayerCollection.keys)
      * [`BMLayerCollection.new()`](#bmesh.types.BMLayerCollection.new)
      * [`BMLayerCollection.remove()`](#bmesh.types.BMLayerCollection.remove)
      * [`BMLayerCollection.values()`](#bmesh.types.BMLayerCollection.values)
      * [`BMLayerCollection.verify()`](#bmesh.types.BMLayerCollection.verify)
      * [`BMLayerCollection.active`](#bmesh.types.BMLayerCollection.active)
      * [`BMLayerCollection.is_singleton`](#bmesh.types.BMLayerCollection.is_singleton)
    - [`BMLayerItem`](#bmesh.types.BMLayerItem)
      * [`BMLayerItem.copy_from()`](#bmesh.types.BMLayerItem.copy_from)
      * [`BMLayerItem.name`](#bmesh.types.BMLayerItem.name)
  + [Custom-Data Layer Types](#custom-data-layer-types)
    - [`BMLoopUV`](#bmesh.types.BMLoopUV)
      * [`BMLoopUV.pin_uv`](#bmesh.types.BMLoopUV.pin_uv)
      * [`BMLoopUV.select`](#bmesh.types.BMLoopUV.select)
      * [`BMLoopUV.select_edge`](#bmesh.types.BMLoopUV.select_edge)
      * [`BMLoopUV.uv`](#bmesh.types.BMLoopUV.uv)
    - [`BMDeformVert`](#bmesh.types.BMDeformVert)
      * [`BMDeformVert.clear()`](#bmesh.types.BMDeformVert.clear)
      * [`BMDeformVert.get()`](#bmesh.types.BMDeformVert.get)
      * [`BMDeformVert.items()`](#bmesh.types.BMDeformVert.items)
      * [`BMDeformVert.keys()`](#bmesh.types.BMDeformVert.keys)
      * [`BMDeformVert.values()`](#bmesh.types.BMDeformVert.values)