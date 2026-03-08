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
  + Freestyle Chaining Iterators (freestyle.chainingiterators)
  + [Freestyle Shaders (freestyle.shaders)](../shaders/index.md)
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

# Freestyle Chaining Iterators (freestyle.chainingiterators)[#](#module-freestyle.chainingiterators "Link to this heading")

This module contains chaining iterators used for the chaining
operation to construct long strokes by concatenating feature edges
according to selected chaining rules. The module is also intended to
be a collection of examples for defining chaining iterators in Python.

*class* freestyle.chainingiterators.ChainPredicateIterator[#](#freestyle.chainingiterators.ChainPredicateIterator "Link to this definition")
:   Class hierarchy: [`freestyle.types.Iterator`](../types/index.md#freestyle.types.Iterator "freestyle.types.Iterator") >
    [`freestyle.types.ViewEdgeIterator`](../types/index.md#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator") >
    [`freestyle.types.ChainingIterator`](../types/index.md#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator") >
    [`ChainPredicateIterator`](#freestyle.chainingiterators.ChainPredicateIterator "freestyle.chainingiterators.ChainPredicateIterator")

    A “generic” user-controlled ViewEdge iterator. This iterator is in
    particular built from a unary predicate and a binary predicate.
    First, the unary predicate is evaluated for all potential next
    ViewEdges in order to only keep the ones respecting a certain
    constraint. Then, the binary predicate is evaluated on the current
    ViewEdge together with each ViewEdge of the previous selection. The
    first ViewEdge respecting both the unary predicate and the binary
    predicate is kept as the next one. If none of the potential next
    ViewEdge respects these two predicates, None is returned.

    \_\_init\_\_(*upred*, *bpred*, *restrict\_to\_selection=True*, *restrict\_to\_unvisited=True*, *begin=None*, *orientation=True*)[#](#freestyle.chainingiterators.ChainPredicateIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Builds a ChainPredicateIterator from a unary predicate, a binary
        predicate, a starting ViewEdge and its orientation or using the copy constructor.

        Parameters:
        :   * **upred** ([`freestyle.types.UnaryPredicate1D`](../types/index.md#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")) – The unary predicate that the next ViewEdge must satisfy.
            * **bpred** ([`freestyle.types.BinaryPredicate1D`](../types/index.md#freestyle.types.BinaryPredicate1D "freestyle.types.BinaryPredicate1D")) – The binary predicate that the next ViewEdge must
              satisfy together with the actual pointed ViewEdge.
            * **restrict\_to\_selection** (*bool*) – Indicates whether to force the chaining
              to stay within the set of selected ViewEdges or not.
            * **restrict\_to\_unvisited** (*bool*) – Indicates whether a ViewEdge that has
              already been chained must be ignored ot not.
            * **begin** ([`freestyle.types.ViewEdge`](../types/index.md#freestyle.types.ViewEdge "freestyle.types.ViewEdge") or None) – The ViewEdge from where to start the iteration.
            * **orientation** (*bool*) – If true, we’ll look for the next ViewEdge among
              the ViewEdges that surround the ending ViewVertex of begin. If
              false, we’ll search over the ViewEdges surrounding the ending
              ViewVertex of begin.
            * **brother** ([`ChainPredicateIterator`](#freestyle.chainingiterators.ChainPredicateIterator "freestyle.chainingiterators.ChainPredicateIterator")) – A ChainPredicateIterator object.

*class* freestyle.chainingiterators.ChainSilhouetteIterator[#](#freestyle.chainingiterators.ChainSilhouetteIterator "Link to this definition")
:   Class hierarchy: [`freestyle.types.Iterator`](../types/index.md#freestyle.types.Iterator "freestyle.types.Iterator") >
    [`freestyle.types.ViewEdgeIterator`](../types/index.md#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator") >
    [`freestyle.types.ChainingIterator`](../types/index.md#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator") >
    [`ChainSilhouetteIterator`](#freestyle.chainingiterators.ChainSilhouetteIterator "freestyle.chainingiterators.ChainSilhouetteIterator")

    A ViewEdge Iterator used to follow ViewEdges the most naturally. For
    example, it will follow visible ViewEdges of same nature. As soon, as
    the nature or the visibility changes, the iteration stops (by setting
    the pointed ViewEdge to 0). In the case of an iteration over a set of
    ViewEdge that are both Silhouette and Crease, there will be a
    precedence of the silhouette over the crease criterion.

    \_\_init\_\_(*restrict\_to\_selection=True*, *begin=None*, *orientation=True*)[#](#freestyle.chainingiterators.ChainSilhouetteIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Builds a ChainSilhouetteIterator from the first ViewEdge used for
        iteration and its orientation or the copy constructor.

        Parameters:
        :   * **restrict\_to\_selection** (*bool*) – Indicates whether to force the chaining
              to stay within the set of selected ViewEdges or not.
            * **begin** ([`freestyle.types.ViewEdge`](../types/index.md#freestyle.types.ViewEdge "freestyle.types.ViewEdge") or None) – The ViewEdge from where to start the iteration.
            * **orientation** (*bool*) – If true, we’ll look for the next ViewEdge among
              the ViewEdges that surround the ending ViewVertex of begin. If
              false, we’ll search over the ViewEdges surrounding the ending
              ViewVertex of begin.
            * **brother** ([`ChainSilhouetteIterator`](#freestyle.chainingiterators.ChainSilhouetteIterator "freestyle.chainingiterators.ChainSilhouetteIterator")) – A ChainSilhouetteIterator object.

*class* freestyle.chainingiterators.pyChainSilhouetteIterator[#](#freestyle.chainingiterators.pyChainSilhouetteIterator "Link to this definition")
:   Natural chaining iterator that follows the edges of the same nature
    following the topology of objects, with decreasing priority for
    silhouettes, then borders, then suggestive contours, then all other edge
    types. A ViewEdge is only chained once.

    init()[#](#freestyle.chainingiterators.pyChainSilhouetteIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyChainSilhouetteIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyChainSilhouetteGenericIterator[#](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator "Link to this definition")
:   Natural chaining iterator that follows the edges of the same nature
    following the topology of objects, with decreasing priority for
    silhouettes, then borders, then suggestive contours, then all other
    edge types.

    \_\_init\_\_(*self*, *stayInSelection=True*, *stayInUnvisited=True*)[#](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator.__init__ "Link to this definition")
    :   Builds a pyChainSilhouetteGenericIterator object.

        Parameters:
        :   * **stayInSelection** (*bool*) – True if it is allowed to go out of the selection
            * **stayInUnvisited** (*bool*) – May the same ViewEdge be chained twice

    init()[#](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyExternalContourChainingIterator[#](#freestyle.chainingiterators.pyExternalContourChainingIterator "Link to this definition")
:   Chains by external contour

    checkViewEdge(*ve*, *orientation*)[#](#freestyle.chainingiterators.pyExternalContourChainingIterator.checkViewEdge "Link to this definition")

    init()[#](#freestyle.chainingiterators.pyExternalContourChainingIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyExternalContourChainingIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pySketchyChainSilhouetteIterator[#](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator "Link to this definition")
:   Natural chaining iterator with a sketchy multiple touch. It chains the
    same ViewEdge multiple times to achieve a sketchy effect.

    \_\_init\_\_(*self*, *nRounds=3*, *stayInSelection=True*)[#](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.__init__ "Link to this definition")
    :   Builds a pySketchyChainSilhouetteIterator object.

        Parameters:
        :   * **nRounds** (*int*) – Number of times every Viewedge is chained.
            * **stayInSelection** (*bool*) – if False, edges outside of the selection can be chained.

    init()[#](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.init "Link to this definition")

    make\_sketchy(*ve*)[#](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.make_sketchy "Link to this definition")
    :   Creates the sketchy effect by causing the chain to run from
        the start again. (loop over itself again)

    traverse(*iter*)[#](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pySketchyChainingIterator[#](#freestyle.chainingiterators.pySketchyChainingIterator "Link to this definition")
:   Chaining iterator designed for sketchy style. It chains the same
    ViewEdge several times in order to produce multiple strokes per
    ViewEdge.

    init()[#](#freestyle.chainingiterators.pySketchyChainingIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pySketchyChainingIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator[#](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator "Link to this definition")
:   Chaining iterator that fills small occlusions

    \_\_init\_\_(*self*, *percent*)[#](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator.__init__ "Link to this definition")
    :   Builds a pyFillOcclusionsRelativeChainingIterator object.

        Parameters:
        :   **percent** (*float*) – The maximal length of the occluded part, expressed
            in a percentage of the total chain length.

    init()[#](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator "Link to this definition")
:   Chaining iterator that fills small occlusions

    \_\_init\_\_(*self*, *length*)[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator.__init__ "Link to this definition")
    :   Builds a pyFillOcclusionsAbsoluteChainingIterator object.

        Parameters:
        :   **length** (*int*) – The maximum length of the occluded part in pixels.

    init()[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator "Link to this definition")
:   Chaining iterator that fills small occlusions regardless of the
    selection.

    \_\_init\_\_(*self*, *percent*, *l*)[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator.__init__ "Link to this definition")
    :   Builds a pyFillOcclusionsAbsoluteAndRelativeChainingIterator object.

        Parameters:
        :   * **percent** (*float*) – The maximal length of the occluded part as a
              percentage of the total chain length.
            * **l** (*float*) – Absolute length.

    init()[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator[#](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator "Link to this definition")
:   Chaining iterator that fills small occlusions regardless of the
    selection.

    \_\_init\_\_(*self*, *percent*, *l*)[#](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator.__init__ "Link to this definition")
    :   Builds a pyFillQi0AbsoluteAndRelativeChainingIterator object.

        Parameters:
        :   * **percent** (*float*) – The maximal length of the occluded part as a
              percentage of the total chain length.
            * **l** (*float*) – Absolute length.

    init()[#](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator.traverse "Link to this definition")

*class* freestyle.chainingiterators.pyNoIdChainSilhouetteIterator[#](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator "Link to this definition")
:   Natural chaining iterator that follows the edges of the same nature
    following the topology of objects, with decreasing priority for
    silhouettes, then borders, then suggestive contours, then all other edge
    types. It won’t chain the same ViewEdge twice.

    \_\_init\_\_(*self*, *stayInSelection=True*)[#](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator.__init__ "Link to this definition")
    :   Builds a pyNoIdChainSilhouetteIterator object.

        Parameters:
        :   **stayInSelection** (*bool*) – True if it is allowed to go out of the selection

    init()[#](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator.init "Link to this definition")

    traverse(*iter*)[#](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator.traverse "Link to this definition")

[Next

Freestyle Shaders (freestyle.shaders)](../shaders/index.md)
[Previous

Freestyle Functions (freestyle.functions)](../functions/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60freestyle.chainingiterators.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Ffreestyle.chainingiterators.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Freestyle Chaining Iterators (freestyle.chainingiterators)
  + [`ChainPredicateIterator`](#freestyle.chainingiterators.ChainPredicateIterator)
    - [`ChainPredicateIterator.__init__()`](#freestyle.chainingiterators.ChainPredicateIterator.__init__)
  + [`ChainSilhouetteIterator`](#freestyle.chainingiterators.ChainSilhouetteIterator)
    - [`ChainSilhouetteIterator.__init__()`](#freestyle.chainingiterators.ChainSilhouetteIterator.__init__)
  + [`pyChainSilhouetteIterator`](#freestyle.chainingiterators.pyChainSilhouetteIterator)
    - [`pyChainSilhouetteIterator.init()`](#freestyle.chainingiterators.pyChainSilhouetteIterator.init)
    - [`pyChainSilhouetteIterator.traverse()`](#freestyle.chainingiterators.pyChainSilhouetteIterator.traverse)
  + [`pyChainSilhouetteGenericIterator`](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator)
    - [`pyChainSilhouetteGenericIterator.__init__()`](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator.__init__)
    - [`pyChainSilhouetteGenericIterator.init()`](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator.init)
    - [`pyChainSilhouetteGenericIterator.traverse()`](#freestyle.chainingiterators.pyChainSilhouetteGenericIterator.traverse)
  + [`pyExternalContourChainingIterator`](#freestyle.chainingiterators.pyExternalContourChainingIterator)
    - [`pyExternalContourChainingIterator.checkViewEdge()`](#freestyle.chainingiterators.pyExternalContourChainingIterator.checkViewEdge)
    - [`pyExternalContourChainingIterator.init()`](#freestyle.chainingiterators.pyExternalContourChainingIterator.init)
    - [`pyExternalContourChainingIterator.traverse()`](#freestyle.chainingiterators.pyExternalContourChainingIterator.traverse)
  + [`pySketchyChainSilhouetteIterator`](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator)
    - [`pySketchyChainSilhouetteIterator.__init__()`](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.__init__)
    - [`pySketchyChainSilhouetteIterator.init()`](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.init)
    - [`pySketchyChainSilhouetteIterator.make_sketchy()`](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.make_sketchy)
    - [`pySketchyChainSilhouetteIterator.traverse()`](#freestyle.chainingiterators.pySketchyChainSilhouetteIterator.traverse)
  + [`pySketchyChainingIterator`](#freestyle.chainingiterators.pySketchyChainingIterator)
    - [`pySketchyChainingIterator.init()`](#freestyle.chainingiterators.pySketchyChainingIterator.init)
    - [`pySketchyChainingIterator.traverse()`](#freestyle.chainingiterators.pySketchyChainingIterator.traverse)
  + [`pyFillOcclusionsRelativeChainingIterator`](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator)
    - [`pyFillOcclusionsRelativeChainingIterator.__init__()`](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator.__init__)
    - [`pyFillOcclusionsRelativeChainingIterator.init()`](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator.init)
    - [`pyFillOcclusionsRelativeChainingIterator.traverse()`](#freestyle.chainingiterators.pyFillOcclusionsRelativeChainingIterator.traverse)
  + [`pyFillOcclusionsAbsoluteChainingIterator`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator)
    - [`pyFillOcclusionsAbsoluteChainingIterator.__init__()`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator.__init__)
    - [`pyFillOcclusionsAbsoluteChainingIterator.init()`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator.init)
    - [`pyFillOcclusionsAbsoluteChainingIterator.traverse()`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteChainingIterator.traverse)
  + [`pyFillOcclusionsAbsoluteAndRelativeChainingIterator`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator)
    - [`pyFillOcclusionsAbsoluteAndRelativeChainingIterator.__init__()`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator.__init__)
    - [`pyFillOcclusionsAbsoluteAndRelativeChainingIterator.init()`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator.init)
    - [`pyFillOcclusionsAbsoluteAndRelativeChainingIterator.traverse()`](#freestyle.chainingiterators.pyFillOcclusionsAbsoluteAndRelativeChainingIterator.traverse)
  + [`pyFillQi0AbsoluteAndRelativeChainingIterator`](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator)
    - [`pyFillQi0AbsoluteAndRelativeChainingIterator.__init__()`](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator.__init__)
    - [`pyFillQi0AbsoluteAndRelativeChainingIterator.init()`](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator.init)
    - [`pyFillQi0AbsoluteAndRelativeChainingIterator.traverse()`](#freestyle.chainingiterators.pyFillQi0AbsoluteAndRelativeChainingIterator.traverse)
  + [`pyNoIdChainSilhouetteIterator`](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator)
    - [`pyNoIdChainSilhouetteIterator.__init__()`](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator.__init__)
    - [`pyNoIdChainSilhouetteIterator.init()`](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator.init)
    - [`pyNoIdChainSilhouetteIterator.traverse()`](#freestyle.chainingiterators.pyNoIdChainSilhouetteIterator.traverse)