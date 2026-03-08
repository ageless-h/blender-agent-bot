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
* [Math Types & Utilities (mathutils)](../../../meta/index.md)[x]

  Toggle navigation of Math Types & Utilities (mathutils)

  + Geometry Utilities (mathutils.geometry)
  + [BVHTree Utilities (mathutils.bvhtree)](../bvhtree/index.md)
  + [KDTree Utilities (mathutils.kdtree)](../kdtree/index.md)
  + [Interpolation Utilities (mathutils.interpolate)](../interpolate/index.md)
  + [Noise Utilities (mathutils.noise)](../noise/index.md)

* 4.2

  Versions

  + Loading...

Note

You are not using the most up to date version of the documentation.
 is the newest version.

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Geometry Utilities (mathutils.geometry)[#](#module-mathutils.geometry "Link to this heading")

The Blender geometry module

mathutils.geometry.area\_tri(*v1*, *v2*, *v3*)[#](#mathutils.geometry.area_tri "Link to this definition")
:   Returns the area size of the 2D or 3D triangle defined.

    Parameters:
    :   * **v1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point1
        * **v2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point2
        * **v3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point3

    Return type:
    :   float

mathutils.geometry.barycentric\_transform(*point*, *tri\_a1*, *tri\_a2*, *tri\_a3*, *tri\_b1*, *tri\_b2*, *tri\_b3*)[#](#mathutils.geometry.barycentric_transform "Link to this definition")
:   Return a transformed point, the transformation is defined by 2 triangles.

    Parameters:
    :   * **point** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The point to transform.
        * **tri\_a1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – source triangle vertex.
        * **tri\_a2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – source triangle vertex.
        * **tri\_a3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – source triangle vertex.
        * **tri\_b1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – target triangle vertex.
        * **tri\_b2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – target triangle vertex.
        * **tri\_b3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – target triangle vertex.

    Returns:
    :   The transformed point

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")’s

mathutils.geometry.box\_fit\_2d(*points*)[#](#mathutils.geometry.box_fit_2d "Link to this definition")
:   Returns an angle that best fits the points to an axis aligned rectangle

    Parameters:
    :   **points** (*list*) – list of 2d points.

    Returns:
    :   angle

    Return type:
    :   float

mathutils.geometry.box\_pack\_2d(*boxes*)[#](#mathutils.geometry.box_pack_2d "Link to this definition")
:   Returns a tuple with the width and height of the packed bounding box.

    Parameters:
    :   **boxes** (*list*) – list of boxes, each box is a list where the first 4 items are [x, y, width, height, …] other items are ignored.

    Returns:
    :   the width and height of the packed bounding box

    Return type:
    :   tuple, pair of floats

mathutils.geometry.closest\_point\_on\_tri(*pt*, *tri\_p1*, *tri\_p2*, *tri\_p3*)[#](#mathutils.geometry.closest_point_on_tri "Link to this definition")
:   Takes 4 vectors: one is the point and the next 3 define the triangle.

    Parameters:
    :   * **pt** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point
        * **tri\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the triangle
        * **tri\_p2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the triangle
        * **tri\_p3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Third point of the triangle

    Returns:
    :   The closest point of the triangle.

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.geometry.convex\_hull\_2d(*points*)[#](#mathutils.geometry.convex_hull_2d "Link to this definition")
:   Returns a list of indices into the list given

    Parameters:
    :   **points** (*list*) – list of 2d points.

    Returns:
    :   a list of indices

    Return type:
    :   list of ints

mathutils.geometry.delaunay\_2d\_cdt(*vert\_coords*, *edges*, *faces*, *output\_type*, *epsilon*, *need\_ids=True*)[#](#mathutils.geometry.delaunay_2d_cdt "Link to this definition")
:   Computes the Constrained Delaunay Triangulation of a set of vertices,
    with edges and faces that must appear in the triangulation.
    Some triangles may be eaten away, or combined with other triangles,
    according to output type.
    The returned verts may be in a different order from input verts, may be moved
    slightly, and may be merged with other nearby verts.
    The three returned orig lists give, for each of verts, edges, and faces, the list of
    input element indices corresponding to the positionally same output element.
    For edges, the orig indices start with the input edges and then continue
    with the edges implied by each of the faces (n of them for an n-gon).
    If the need\_ids argument is supplied, and False, then the code skips the preparation
    of the orig arrays, which may save some time.
    :arg vert\_coords: Vertex coordinates (2d)
    :type vert\_coords: list of [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")
    :arg edges: Edges, as pairs of indices in vert\_coords
    :type edges: list of (int, int)
    :arg faces: Faces, each sublist is a face, as indices in vert\_coords (CCW oriented)
    :type faces: list of list of int
    :arg output\_type: What output looks like. 0 => triangles with convex hull. 1 => triangles inside constraints. 2 => the input constraints, intersected. 3 => like 2 but detect holes and omit them from output. 4 => like 2 but with extra edges to make valid BMesh faces. 5 => like 4 but detect holes and omit them from output.
    :type output\_type: intn :arg epsilon: For nearness tests; should not be zero
    :type epsilon: float
    :arg need\_ids: are the orig output arrays needed?
    :type need\_args: bool
    :return: Output tuple, (vert\_coords, edges, faces, orig\_verts, orig\_edges, orig\_faces)
    :rtype: (list of mathutils.Vector, list of (int, int), list of list of int, list of list of int, list of list of int, list of list of int)

mathutils.geometry.distance\_point\_to\_plane(*pt*, *plane\_co*, *plane\_no*)[#](#mathutils.geometry.distance_point_to_plane "Link to this definition")
:   Returns the signed distance between a point and a plane (negative when below the normal).

    Parameters:
    :   * **pt** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point
        * **plane\_co** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – A point on the plane
        * **plane\_no** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The direction the plane is facing

    Return type:
    :   float

mathutils.geometry.interpolate\_bezier(*knot1*, *handle1*, *handle2*, *knot2*, *resolution*)[#](#mathutils.geometry.interpolate_bezier "Link to this definition")
:   Interpolate a bezier spline segment.

    Parameters:
    :   * **knot1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First bezier spline point.
        * **handle1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First bezier spline handle.
        * **handle2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second bezier spline handle.
        * **knot2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second bezier spline point.
        * **resolution** (*int*) – Number of points to return.

    Returns:
    :   The interpolated points

    Return type:
    :   list of [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")’s

mathutils.geometry.intersect\_line\_line(*v1*, *v2*, *v3*, *v4*)[#](#mathutils.geometry.intersect_line_line "Link to this definition")
:   Returns a tuple with the points on each line respectively closest to the other.

    Parameters:
    :   * **v1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the first line
        * **v2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the first line
        * **v3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the second line
        * **v4** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the second line

    Return type:
    :   tuple of [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")’s

mathutils.geometry.intersect\_line\_line\_2d(*lineA\_p1*, *lineA\_p2*, *lineB\_p1*, *lineB\_p2*)[#](#mathutils.geometry.intersect_line_line_2d "Link to this definition")
:   Takes 2 segments (defined by 4 vectors) and returns a vector for their point of intersection or None.

    Warning

    Despite its name, this function works on segments, and not on lines.

    Parameters:
    :   * **lineA\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the first line
        * **lineA\_p2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the first line
        * **lineB\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the second line
        * **lineB\_p2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the second line

    Returns:
    :   The point of intersection or None when not found

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None

mathutils.geometry.intersect\_line\_plane(*line\_a*, *line\_b*, *plane\_co*, *plane\_no*, *no\_flip=False*)[#](#mathutils.geometry.intersect_line_plane "Link to this definition")
:   Calculate the intersection between a line (as 2 vectors) and a plane.
    Returns a vector for the intersection or None.

    Parameters:
    :   * **line\_a** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the first line
        * **line\_b** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the first line
        * **plane\_co** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – A point on the plane
        * **plane\_no** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The direction the plane is facing

    Returns:
    :   The point of intersection or None when not found

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None

mathutils.geometry.intersect\_line\_sphere(*line\_a*, *line\_b*, *sphere\_co*, *sphere\_radius*, *clip=True*)[#](#mathutils.geometry.intersect_line_sphere "Link to this definition")
:   Takes a line (as 2 points) and a sphere (as a point and a radius) and
    returns the intersection

    Parameters:
    :   * **line\_a** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the line
        * **line\_b** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the line
        * **sphere\_co** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The center of the sphere
        * **sphere\_radius** (*sphere\_radius*) – Radius of the sphere

    Returns:
    :   The intersection points as a pair of vectors or None when there is no intersection

    Return type:
    :   A tuple pair containing [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None

mathutils.geometry.intersect\_line\_sphere\_2d(*line\_a*, *line\_b*, *sphere\_co*, *sphere\_radius*, *clip=True*)[#](#mathutils.geometry.intersect_line_sphere_2d "Link to this definition")
:   Takes a line (as 2 points) and a sphere (as a point and a radius) and
    returns the intersection

    Parameters:
    :   * **line\_a** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the line
        * **line\_b** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the line
        * **sphere\_co** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The center of the sphere
        * **sphere\_radius** (*sphere\_radius*) – Radius of the sphere

    Returns:
    :   The intersection points as a pair of vectors or None when there is no intersection

    Return type:
    :   A tuple pair containing [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None

mathutils.geometry.intersect\_plane\_plane(*plane\_a\_co*, *plane\_a\_no*, *plane\_b\_co*, *plane\_b\_no*)[#](#mathutils.geometry.intersect_plane_plane "Link to this definition")
:   Return the intersection between two planes

    Parameters:
    :   * **plane\_a\_co** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point on the first plane
        * **plane\_a\_no** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Normal of the first plane
        * **plane\_b\_co** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point on the second plane
        * **plane\_b\_no** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Normal of the second plane

    Returns:
    :   The line of the intersection represented as a point and a vector

    Return type:
    :   tuple pair of [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None if the intersection can’t be calculated

mathutils.geometry.intersect\_point\_line(*pt*, *line\_p1*, *line\_p2*)[#](#mathutils.geometry.intersect_point_line "Link to this definition")
:   Takes a point and a line and returns a tuple with the closest point on the line and its distance from the first point of the line as a percentage of the length of the line.

    Parameters:
    :   * **pt** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point
        * **line\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the line
        * **line\_p1** – Second point of the line

    Return type:
    :   ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector"), float)

mathutils.geometry.intersect\_point\_quad\_2d(*pt*, *quad\_p1*, *quad\_p2*, *quad\_p3*, *quad\_p4*)[#](#mathutils.geometry.intersect_point_quad_2d "Link to this definition")
:   Takes 5 vectors (using only the x and y coordinates): one is the point and the next 4 define the quad,
    only the x and y are used from the vectors. Returns 1 if the point is within the quad, otherwise 0.
    Works only with convex quads without singular edges.

    Parameters:
    :   * **pt** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point
        * **quad\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the quad
        * **quad\_p2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the quad
        * **quad\_p3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Third point of the quad
        * **quad\_p4** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Fourth point of the quad

    Return type:
    :   int

mathutils.geometry.intersect\_point\_tri(*pt*, *tri\_p1*, *tri\_p2*, *tri\_p3*)[#](#mathutils.geometry.intersect_point_tri "Link to this definition")
:   Takes 4 vectors: one is the point and the next 3 define the triangle. Projects the point onto the triangle plane and checks if it is within the triangle.

    Parameters:
    :   * **pt** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point
        * **tri\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the triangle
        * **tri\_p2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the triangle
        * **tri\_p3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Third point of the triangle

    Returns:
    :   Point on the triangles plane or None if its outside the triangle

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None

mathutils.geometry.intersect\_point\_tri\_2d(*pt*, *tri\_p1*, *tri\_p2*, *tri\_p3*)[#](#mathutils.geometry.intersect_point_tri_2d "Link to this definition")
:   Takes 4 vectors (using only the x and y coordinates): one is the point and the next 3 define the triangle. Returns 1 if the point is within the triangle, otherwise 0.

    Parameters:
    :   * **pt** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point
        * **tri\_p1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – First point of the triangle
        * **tri\_p2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Second point of the triangle
        * **tri\_p3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Third point of the triangle

    Return type:
    :   int

mathutils.geometry.intersect\_ray\_tri(*v1*, *v2*, *v3*, *ray*, *orig*, *clip=True*)[#](#mathutils.geometry.intersect_ray_tri "Link to this definition")
:   Returns the intersection between a ray and a triangle, if possible, returns None otherwise.

    Parameters:
    :   * **v1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point1
        * **v2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point2
        * **v3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point3
        * **ray** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Direction of the projection
        * **orig** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Origin
        * **clip** (*boolean*) – When False, don’t restrict the intersection to the area of the triangle, use the infinite plane defined by the triangle.

    Returns:
    :   The point of intersection or None if no intersection is found

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") or None

mathutils.geometry.intersect\_sphere\_sphere\_2d(*p\_a*, *radius\_a*, *p\_b*, *radius\_b*)[#](#mathutils.geometry.intersect_sphere_sphere_2d "Link to this definition")
:   Returns 2 points on between intersecting circles.

    Parameters:
    :   * **p\_a** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Center of the first circle
        * **radius\_a** (*float*) – Radius of the first circle
        * **p\_b** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Center of the second circle
        * **radius\_b** (*float*) – Radius of the second circle

    Return type:
    :   tuple of [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")’s or None when there is no intersection

mathutils.geometry.intersect\_tri\_tri\_2d(*tri\_a1*, *tri\_a2*, *tri\_a3*, *tri\_b1*, *tri\_b2*, *tri\_b3*)[#](#mathutils.geometry.intersect_tri_tri_2d "Link to this definition")
:   Check if two 2D triangles intersect.

    Return type:
    :   bool

mathutils.geometry.normal(*vectors*)[#](#mathutils.geometry.normal "Link to this definition")
:   Returns the normal of a 3D polygon.

    Parameters:
    :   **vectors** (*sequence* *of* *3* *or* *more 3d vector*) – Vectors to calculate normals with

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.geometry.points\_in\_planes(*planes*, *epsilon\_coplanar=1e-4*, *epsilon\_isect=1e-6*)[#](#mathutils.geometry.points_in_planes "Link to this definition")
:   Returns a list of points inside all planes given and a list of index values for the planes used.

    Parameters:
    :   * **planes** (list of [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – List of planes (4D vectors).
        * **epsilon\_coplanar** (*float*) – Epsilon value for interpreting plane pairs as co-plannar.
        * **epsilon\_isect** (*float*) – Epsilon value for intersection.

    Returns:
    :   two lists, once containing the vertices inside the planes, another containing the plane indices used

    Return type:
    :   pair of lists

mathutils.geometry.tessellate\_polygon(*veclist\_list*)[#](#mathutils.geometry.tessellate_polygon "Link to this definition")
:   Takes a list of polylines (each point a pair or triplet of numbers) and returns the point indices for a polyline filled with triangles. Does not handle degenerate geometry (such as zero-length lines due to consecutive identical points).

    Parameters:
    :   **veclist\_list** – list of polylines

    Return type:
    :   list

mathutils.geometry.volume\_tetrahedron(*v1*, *v2*, *v3*, *v4*)[#](#mathutils.geometry.volume_tetrahedron "Link to this definition")
:   Return the volume formed by a tetrahedron (points can be in any order).

    Parameters:
    :   * **v1** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point1
        * **v2** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point2
        * **v3** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point3
        * **v4** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – Point4

    Return type:
    :   float

[Next

BVHTree Utilities (mathutils.bvhtree)](../bvhtree/index.md)
[Previous

Math Types & Utilities (mathutils)](../../../meta/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60mathutils.geometry.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fmathutils.geometry.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Geometry Utilities (mathutils.geometry)
  + [`area_tri()`](#mathutils.geometry.area_tri)
  + [`barycentric_transform()`](#mathutils.geometry.barycentric_transform)
  + [`box_fit_2d()`](#mathutils.geometry.box_fit_2d)
  + [`box_pack_2d()`](#mathutils.geometry.box_pack_2d)
  + [`closest_point_on_tri()`](#mathutils.geometry.closest_point_on_tri)
  + [`convex_hull_2d()`](#mathutils.geometry.convex_hull_2d)
  + [`delaunay_2d_cdt()`](#mathutils.geometry.delaunay_2d_cdt)
  + [`distance_point_to_plane()`](#mathutils.geometry.distance_point_to_plane)
  + [`interpolate_bezier()`](#mathutils.geometry.interpolate_bezier)
  + [`intersect_line_line()`](#mathutils.geometry.intersect_line_line)
  + [`intersect_line_line_2d()`](#mathutils.geometry.intersect_line_line_2d)
  + [`intersect_line_plane()`](#mathutils.geometry.intersect_line_plane)
  + [`intersect_line_sphere()`](#mathutils.geometry.intersect_line_sphere)
  + [`intersect_line_sphere_2d()`](#mathutils.geometry.intersect_line_sphere_2d)
  + [`intersect_plane_plane()`](#mathutils.geometry.intersect_plane_plane)
  + [`intersect_point_line()`](#mathutils.geometry.intersect_point_line)
  + [`intersect_point_quad_2d()`](#mathutils.geometry.intersect_point_quad_2d)
  + [`intersect_point_tri()`](#mathutils.geometry.intersect_point_tri)
  + [`intersect_point_tri_2d()`](#mathutils.geometry.intersect_point_tri_2d)
  + [`intersect_ray_tri()`](#mathutils.geometry.intersect_ray_tri)
  + [`intersect_sphere_sphere_2d()`](#mathutils.geometry.intersect_sphere_sphere_2d)
  + [`intersect_tri_tri_2d()`](#mathutils.geometry.intersect_tri_tri_2d)
  + [`normal()`](#mathutils.geometry.normal)
  + [`points_in_planes()`](#mathutils.geometry.points_in_planes)
  + [`tessellate_polygon()`](#mathutils.geometry.tessellate_polygon)
  + [`volume_tetrahedron()`](#mathutils.geometry.volume_tetrahedron)