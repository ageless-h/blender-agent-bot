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

  + [Geometry Utilities (mathutils.geometry)](../geometry/index.md)
  + BVHTree Utilities (mathutils.bvhtree)
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

# BVHTree Utilities (mathutils.bvhtree)[#](#module-mathutils.bvhtree "Link to this heading")

BVH tree structures for proximity searches and ray casts on geometry.

*class* mathutils.bvhtree.BVHTree[#](#mathutils.bvhtree.BVHTree "Link to this definition")
:   *classmethod* FromBMesh(*bmesh*, *epsilon=0.0*)[#](#mathutils.bvhtree.BVHTree.FromBMesh "Link to this definition")
    :   BVH tree based on `BMesh` data.

        Parameters:
        :   * **bmesh** (`BMesh`) – BMesh data.
            * **epsilon** (*float*) – Increase the threshold for detecting overlap and raycast hits.

    *classmethod* FromObject(*object*, *depsgraph*, *deform=True*, *render=False*, *cage=False*, *epsilon=0.0*)[#](#mathutils.bvhtree.BVHTree.FromObject "Link to this definition")
    :   BVH tree based on `Object` data.

        Parameters:
        :   * **object** (`Object`) – Object data.
            * **depsgraph** (`Depsgraph`) – Depsgraph to use for evaluating the mesh.
            * **deform** (*bool*) – Use mesh with deformations.
            * **cage** (*bool*) – Use modifiers cage.
            * **epsilon** (*float*) – Increase the threshold for detecting overlap and raycast hits.

    *classmethod* FromPolygons(*vertices*, *polygons*, *all\_triangles=False*, *epsilon=0.0*)[#](#mathutils.bvhtree.BVHTree.FromPolygons "Link to this definition")
    :   BVH tree constructed geometry passed in as arguments.

        Parameters:
        :   * **vertices** (*float triplet sequence*) – float triplets each representing `(x, y, z)`
            * **polygons** (*Sequence* *of* *sequences containing ints*) – Sequence of polyugons, each containing indices to the vertices argument.
            * **all\_triangles** (*bool*) – Use when all **polygons** are triangles for more efficient conversion.
            * **epsilon** (*float*) – Increase the threshold for detecting overlap and raycast hits.

    find\_nearest(*origin*, *distance=1.84467e+19*)[#](#mathutils.bvhtree.BVHTree.find_nearest "Link to this definition")
    :   Find the nearest element (typically face index) to a point.

        Parameters:
        :   * **co** (`Vector`) – Find nearest element to this point.
            * **distance** (*float*) – Maximum distance threshold.

        Returns:
        :   Returns a tuple
            (`Vector` location, `Vector` normal, int index, float distance),
            Values will all be None if no hit is found.

        Return type:
        :   `tuple`

    find\_nearest\_range(*origin*, *distance=1.84467e+19*)[#](#mathutils.bvhtree.BVHTree.find_nearest_range "Link to this definition")
    :   Find the nearest elements (typically face index) to a point in the distance range.

        Parameters:
        :   * **co** (`Vector`) – Find nearest elements to this point.
            * **distance** (*float*) – Maximum distance threshold.

        Returns:
        :   Returns a list of tuples
            (`Vector` location, `Vector` normal, int index, float distance),

        Return type:
        :   `list`

    overlap(*other\_tree*)[#](#mathutils.bvhtree.BVHTree.overlap "Link to this definition")
    :   Find overlapping indices between 2 trees.

        Parameters:
        :   **other\_tree** ([`BVHTree`](#mathutils.bvhtree.BVHTree "mathutils.bvhtree.BVHTree")) – Other tree to perform overlap test on.

        Returns:
        :   Returns a list of unique index pairs, the first index referencing this tree, the second referencing the **other\_tree**.

        Return type:
        :   `list`

    ray\_cast(*origin*, *direction*, *distance=sys.float\_info.max*)[#](#mathutils.bvhtree.BVHTree.ray_cast "Link to this definition")
    :   Cast a ray onto the mesh.

        Parameters:
        :   * **origin** (`Vector`) – Start location of the ray in object space.
            * **direction** (`Vector`) – Direction of the ray in object space.
            * **distance** (*float*) – Maximum distance threshold.

        Returns:
        :   Returns a tuple
            (`Vector` location, `Vector` normal, int index, float distance),
            Values will all be None if no hit is found.

        Return type:
        :   `tuple`

[Next

KDTree Utilities (mathutils.kdtree)](../kdtree/index.md)
[Previous

Geometry Utilities (mathutils.geometry)](../geometry/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60mathutils.bvhtree.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fmathutils.bvhtree.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* BVHTree Utilities (mathutils.bvhtree)
  + [`BVHTree`](#mathutils.bvhtree.BVHTree)
    - [`BVHTree.FromBMesh()`](#mathutils.bvhtree.BVHTree.FromBMesh)
    - [`BVHTree.FromObject()`](#mathutils.bvhtree.BVHTree.FromObject)
    - [`BVHTree.FromPolygons()`](#mathutils.bvhtree.BVHTree.FromPolygons)
    - [`BVHTree.find_nearest()`](#mathutils.bvhtree.BVHTree.find_nearest)
    - [`BVHTree.find_nearest_range()`](#mathutils.bvhtree.BVHTree.find_nearest_range)
    - [`BVHTree.overlap()`](#mathutils.bvhtree.BVHTree.overlap)
    - [`BVHTree.ray_cast()`](#mathutils.bvhtree.BVHTree.ray_cast)