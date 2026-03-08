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

  + Freestyle Types (freestyle.types)
  + [Freestyle Predicates (freestyle.predicates)](../predicates/index.md)
  + [Freestyle Functions (freestyle.functions)](../functions/index.md)
  + [Freestyle Chaining Iterators (freestyle.chainingiterators)](../chainingiterators/index.md)
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

# Freestyle Types (freestyle.types)[#](#module-freestyle.types "Link to this heading")

This module contains core classes of the Freestyle Python API,
including data types of view map components (0D and 1D elements), base
classes for user-defined line stylization rules (predicates,
functions, chaining iterators, and stroke shaders), and operators.

Class hierarchy:

* [`BBox`](#freestyle.types.BBox "freestyle.types.BBox")
* [`BinaryPredicate0D`](#freestyle.types.BinaryPredicate0D "freestyle.types.BinaryPredicate0D")
* [`BinaryPredicate1D`](#freestyle.types.BinaryPredicate1D "freestyle.types.BinaryPredicate1D")
* [`Id`](#freestyle.types.Id "freestyle.types.Id")
* [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D")

  + [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")

    - [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")
  + [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")
  + [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")

    - [`NonTVertex`](#freestyle.types.NonTVertex "freestyle.types.NonTVertex")
    - [`TVertex`](#freestyle.types.TVertex "freestyle.types.TVertex")
* [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D")

  + [`Curve`](#freestyle.types.Curve "freestyle.types.Curve")

    - [`Chain`](#freestyle.types.Chain "freestyle.types.Chain")
  + [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    - [`FEdgeSharp`](#freestyle.types.FEdgeSharp "freestyle.types.FEdgeSharp")
    - [`FEdgeSmooth`](#freestyle.types.FEdgeSmooth "freestyle.types.FEdgeSmooth")
  + [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke")
  + [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")
* [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator")

  + [`AdjacencyIterator`](#freestyle.types.AdjacencyIterator "freestyle.types.AdjacencyIterator")
  + [`CurvePointIterator`](#freestyle.types.CurvePointIterator "freestyle.types.CurvePointIterator")
  + [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")
  + [`SVertexIterator`](#freestyle.types.SVertexIterator "freestyle.types.SVertexIterator")
  + [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")
  + [`ViewEdgeIterator`](#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator")

    - [`ChainingIterator`](#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator")
  + [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator")
* [`Material`](#freestyle.types.Material "freestyle.types.Material")
* [`Noise`](#freestyle.types.Noise "freestyle.types.Noise")
* [`Operators`](#freestyle.types.Operators "freestyle.types.Operators")
* [`SShape`](#freestyle.types.SShape "freestyle.types.SShape")
* [`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute")
* [`StrokeShader`](#freestyle.types.StrokeShader "freestyle.types.StrokeShader")
* [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D")

  + [`UnaryFunction0DDouble`](#freestyle.types.UnaryFunction0DDouble "freestyle.types.UnaryFunction0DDouble")
  + [`UnaryFunction0DEdgeNature`](#freestyle.types.UnaryFunction0DEdgeNature "freestyle.types.UnaryFunction0DEdgeNature")
  + [`UnaryFunction0DFloat`](#freestyle.types.UnaryFunction0DFloat "freestyle.types.UnaryFunction0DFloat")
  + [`UnaryFunction0DId`](#freestyle.types.UnaryFunction0DId "freestyle.types.UnaryFunction0DId")
  + [`UnaryFunction0DMaterial`](#freestyle.types.UnaryFunction0DMaterial "freestyle.types.UnaryFunction0DMaterial")
  + [`UnaryFunction0DUnsigned`](#freestyle.types.UnaryFunction0DUnsigned "freestyle.types.UnaryFunction0DUnsigned")
  + [`UnaryFunction0DVec2f`](#freestyle.types.UnaryFunction0DVec2f "freestyle.types.UnaryFunction0DVec2f")
  + [`UnaryFunction0DVec3f`](#freestyle.types.UnaryFunction0DVec3f "freestyle.types.UnaryFunction0DVec3f")
  + [`UnaryFunction0DVectorViewShape`](#freestyle.types.UnaryFunction0DVectorViewShape "freestyle.types.UnaryFunction0DVectorViewShape")
  + [`UnaryFunction0DViewShape`](#freestyle.types.UnaryFunction0DViewShape "freestyle.types.UnaryFunction0DViewShape")
* [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D")

  + [`UnaryFunction1DDouble`](#freestyle.types.UnaryFunction1DDouble "freestyle.types.UnaryFunction1DDouble")
  + [`UnaryFunction1DEdgeNature`](#freestyle.types.UnaryFunction1DEdgeNature "freestyle.types.UnaryFunction1DEdgeNature")
  + [`UnaryFunction1DFloat`](#freestyle.types.UnaryFunction1DFloat "freestyle.types.UnaryFunction1DFloat")
  + [`UnaryFunction1DUnsigned`](#freestyle.types.UnaryFunction1DUnsigned "freestyle.types.UnaryFunction1DUnsigned")
  + [`UnaryFunction1DVec2f`](#freestyle.types.UnaryFunction1DVec2f "freestyle.types.UnaryFunction1DVec2f")
  + [`UnaryFunction1DVec3f`](#freestyle.types.UnaryFunction1DVec3f "freestyle.types.UnaryFunction1DVec3f")
  + [`UnaryFunction1DVectorViewShape`](#freestyle.types.UnaryFunction1DVectorViewShape "freestyle.types.UnaryFunction1DVectorViewShape")
  + [`UnaryFunction1DVoid`](#freestyle.types.UnaryFunction1DVoid "freestyle.types.UnaryFunction1DVoid")
* [`UnaryPredicate0D`](#freestyle.types.UnaryPredicate0D "freestyle.types.UnaryPredicate0D")
* [`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")
* [`ViewMap`](#freestyle.types.ViewMap "freestyle.types.ViewMap")
* [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape")
* [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")
* [`MediumType`](#freestyle.types.MediumType "freestyle.types.MediumType")
* [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

*class* freestyle.types.AdjacencyIterator[#](#freestyle.types.AdjacencyIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`AdjacencyIterator`](#freestyle.types.AdjacencyIterator "freestyle.types.AdjacencyIterator")

    Class for representing adjacency iterators used in the chaining
    process. An AdjacencyIterator is created in the increment() and
    decrement() methods of a [`ChainingIterator`](#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator") and passed to the
    traverse() method of the ChainingIterator.

    \_\_init\_\_()[#](#freestyle.types.AdjacencyIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*vertex*, *restrict\_to\_selection=True*, *restrict\_to\_unvisited=True*)
    :   Builds an [`AdjacencyIterator`](#freestyle.types.AdjacencyIterator "freestyle.types.AdjacencyIterator") using the default constructor,
        copy constructor or the overloaded constructor.

        Parameters:
        :   * **brother** ([`AdjacencyIterator`](#freestyle.types.AdjacencyIterator "freestyle.types.AdjacencyIterator")) – An AdjacencyIterator object.
            * **vertex** ([`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")) – The vertex which is the next crossing.
            * **restrict\_to\_selection** (*bool*) – Indicates whether to force the chaining
              to stay within the set of selected ViewEdges or not.
            * **restrict\_to\_unvisited** (*bool*) – Indicates whether a ViewEdge that has
              already been chained must be ignored ot not.

    is\_incoming[#](#freestyle.types.AdjacencyIterator.is_incoming "Link to this definition")
    :   True if the current ViewEdge is coming towards the iteration vertex, and
        False otherwise.

        Type:
        :   bool

    object[#](#freestyle.types.AdjacencyIterator.object "Link to this definition")
    :   The ViewEdge object currently pointed to by this iterator.

        Type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

*class* freestyle.types.BBox[#](#freestyle.types.BBox "Link to this definition")
:   Class for representing a bounding box.

    \_\_init\_\_()[#](#freestyle.types.BBox.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.BinaryPredicate0D[#](#freestyle.types.BinaryPredicate0D "Link to this definition")
:   Base class for binary predicates working on [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D")
    objects. A BinaryPredicate0D is typically an ordering relation
    between two Interface0D objects. The predicate evaluates a relation
    between the two Interface0D instances and returns a boolean value (true
    or false). It is used by invoking the \_\_call\_\_() method.

    \_\_init\_\_()[#](#freestyle.types.BinaryPredicate0D.__init__ "Link to this definition")
    :   Default constructor.

    \_\_call\_\_(*inter1*, *inter2*)[#](#freestyle.types.BinaryPredicate0D.__call__ "Link to this definition")
    :   Must be overload by inherited classes. It evaluates a relation
        between two Interface0D objects.

        Parameters:
        :   * **inter1** ([`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D")) – The first Interface0D object.
            * **inter2** ([`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D")) – The second Interface0D object.

        Returns:
        :   True or false.

        Return type:
        :   bool

    name[#](#freestyle.types.BinaryPredicate0D.name "Link to this definition")
    :   The name of the binary 0D predicate.

        Type:
        :   str

*class* freestyle.types.BinaryPredicate1D[#](#freestyle.types.BinaryPredicate1D "Link to this definition")
:   Base class for binary predicates working on [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D")
    objects. A BinaryPredicate1D is typically an ordering relation
    between two Interface1D objects. The predicate evaluates a relation
    between the two Interface1D instances and returns a boolean value (true
    or false). It is used by invoking the \_\_call\_\_() method.

    \_\_init\_\_()[#](#freestyle.types.BinaryPredicate1D.__init__ "Link to this definition")
    :   Default constructor.

    \_\_call\_\_(*inter1*, *inter2*)[#](#freestyle.types.BinaryPredicate1D.__call__ "Link to this definition")
    :   Must be overload by inherited classes. It evaluates a relation
        between two Interface1D objects.

        Parameters:
        :   * **inter1** ([`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D")) – The first Interface1D object.
            * **inter2** ([`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D")) – The second Interface1D object.

        Returns:
        :   True or false.

        Return type:
        :   bool

    name[#](#freestyle.types.BinaryPredicate1D.name "Link to this definition")
    :   The name of the binary 1D predicate.

        Type:
        :   str

*class* freestyle.types.Chain[#](#freestyle.types.Chain "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`Curve`](#freestyle.types.Curve "freestyle.types.Curve") > [`Chain`](#freestyle.types.Chain "freestyle.types.Chain")

    Class to represent a 1D elements issued from the chaining process. A
    Chain is the last step before the [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke") and is used in the
    Splitting and Creation processes.

    \_\_init\_\_()[#](#freestyle.types.Chain.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*id*)
    :   Builds a [`Chain`](#freestyle.types.Chain "freestyle.types.Chain") using the default constructor,
        copy constructor or from an [`Id`](#freestyle.types.Id "freestyle.types.Id").

        Parameters:
        :   * **brother** ([`Chain`](#freestyle.types.Chain "freestyle.types.Chain")) – A Chain object.
            * **id** ([`Id`](#freestyle.types.Id "freestyle.types.Id")) – An Id object.

    push\_viewedge\_back(*viewedge*, *orientation*)[#](#freestyle.types.Chain.push_viewedge_back "Link to this definition")
    :   Adds a ViewEdge at the end of the Chain.

        Parameters:
        :   * **viewedge** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) – The ViewEdge that must be added.
            * **orientation** (*bool*) – The orientation with which the ViewEdge must be
              processed.

    push\_viewedge\_front(*viewedge*, *orientation*)[#](#freestyle.types.Chain.push_viewedge_front "Link to this definition")
    :   Adds a ViewEdge at the beginning of the Chain.

        Parameters:
        :   * **viewedge** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) – The ViewEdge that must be added.
            * **orientation** (*bool*) – The orientation with which the ViewEdge must be
              processed.

*class* freestyle.types.ChainingIterator[#](#freestyle.types.ChainingIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`ViewEdgeIterator`](#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator") > [`ChainingIterator`](#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator")

    Base class for chaining iterators. This class is designed to be
    overloaded in order to describe chaining rules. It makes the
    description of chaining rules easier. The two main methods that need
    to overloaded are traverse() and init(). traverse() tells which
    [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge") to follow, among the adjacent ones. If you specify
    restriction rules (such as “Chain only ViewEdges of the selection”),
    they will be included in the adjacency iterator (i.e, the adjacent
    iterator will only stop on “valid” edges).

    \_\_init\_\_(*restrict\_to\_selection=True*, *restrict\_to\_unvisited=True*, *begin=None*, *orientation=True*)[#](#freestyle.types.ChainingIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Builds a Chaining Iterator from the first ViewEdge used for
        iteration and its orientation or by using the copy constructor.

        Parameters:
        :   * **restrict\_to\_selection** (*bool*) – Indicates whether to force the chaining
              to stay within the set of selected ViewEdges or not.
            * **restrict\_to\_unvisited** (*bool*) – Indicates whether a ViewEdge that has
              already been chained must be ignored ot not.
            * **begin** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge") or None) – The ViewEdge from which to start the chain.
            * **orientation** (*bool*) – The direction to follow to explore the graph. If
              true, the direction indicated by the first ViewEdge is used.
            * **brother** ([*ChainingIterator*](#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator")) –

    init()[#](#freestyle.types.ChainingIterator.init "Link to this definition")
    :   Initializes the iterator context. This method is called each
        time a new chain is started. It can be used to reset some
        history information that you might want to keep.

    traverse(*it*)[#](#freestyle.types.ChainingIterator.traverse "Link to this definition")
    :   This method iterates over the potential next ViewEdges and returns
        the one that will be followed next. Returns the next ViewEdge to
        follow or None when the end of the chain is reached.

        Parameters:
        :   **it** ([`AdjacencyIterator`](#freestyle.types.AdjacencyIterator "freestyle.types.AdjacencyIterator")) – The iterator over the ViewEdges adjacent to the end vertex
            of the current ViewEdge. The adjacency iterator reflects the
            restriction rules by only iterating over the valid ViewEdges.

        Returns:
        :   Returns the next ViewEdge to follow, or None if chaining ends.

        Return type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge") or None

    is\_incrementing[#](#freestyle.types.ChainingIterator.is_incrementing "Link to this definition")
    :   True if the current iteration is an incrementation.

        Type:
        :   bool

    next\_vertex[#](#freestyle.types.ChainingIterator.next_vertex "Link to this definition")
    :   The ViewVertex that is the next crossing.

        Type:
        :   [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")

    object[#](#freestyle.types.ChainingIterator.object "Link to this definition")
    :   The ViewEdge object currently pointed by this iterator.

        Type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

*class* freestyle.types.Curve[#](#freestyle.types.Curve "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`Curve`](#freestyle.types.Curve "freestyle.types.Curve")

    Base class for curves made of CurvePoints. [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") is the
    type of the initial curve vertices. A [`Chain`](#freestyle.types.Chain "freestyle.types.Chain") is a
    specialization of a Curve.

    \_\_init\_\_()[#](#freestyle.types.Curve.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*id*)
    :   Builds a `FrsCurve` using a default constructor,
        copy constructor or from an [`Id`](#freestyle.types.Id "freestyle.types.Id").

        Parameters:
        :   * **brother** ([`Curve`](#freestyle.types.Curve "freestyle.types.Curve")) – A Curve object.
            * **id** ([`Id`](#freestyle.types.Id "freestyle.types.Id")) – An Id object.

    push\_vertex\_back(*vertex*)[#](#freestyle.types.Curve.push_vertex_back "Link to this definition")
    :   Adds a single vertex at the end of the Curve.

        Parameters:
        :   **vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") or [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")) – A vertex object.

    push\_vertex\_front(*vertex*)[#](#freestyle.types.Curve.push_vertex_front "Link to this definition")
    :   Adds a single vertex at the front of the Curve.

        Parameters:
        :   **vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") or [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")) – A vertex object.

    is\_empty[#](#freestyle.types.Curve.is_empty "Link to this definition")
    :   True if the Curve doesn’t have any Vertex yet.

        Type:
        :   bool

    segments\_size[#](#freestyle.types.Curve.segments_size "Link to this definition")
    :   The number of segments in the polyline constituting the Curve.

        Type:
        :   int

*class* freestyle.types.CurvePoint[#](#freestyle.types.CurvePoint "Link to this definition")
:   Class hierarchy: [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") > [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")

    Class to represent a point of a curve. A CurvePoint can be any point
    of a 1D curve (it doesn’t have to be a vertex of the curve). Any
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") is built upon ViewEdges, themselves built upon
    FEdges. Therefore, a curve is basically a polyline made of a list of
    [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") objects. Thus, a CurvePoint is built by linearly
    interpolating two [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") instances. CurvePoint can be used
    as virtual points while querying 0D information along a curve at a
    given resolution.

    \_\_init\_\_()[#](#freestyle.types.CurvePoint.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*first\_vertex*, *second\_vertex*, *t2d*)

    \_\_init\_\_(*first\_point*, *second\_point*, *t2d*)
    :   Builds a CurvePoint using the default constructor, copy constructor,
        or one of the overloaded constructors. The over loaded constructors
        can either take two [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") or two [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")
        objects and an interpolation parameter

        Parameters:
        :   * **brother** ([`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")) – A CurvePoint object.
            * **first\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The first SVertex.
            * **second\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The second SVertex.
            * **first\_point** ([`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")) – The first CurvePoint.
            * **second\_point** ([`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")) – The second CurvePoint.
            * **t2d** (*float*) – A 2D interpolation parameter used to linearly interpolate
              first\_vertex and second\_vertex or first\_point and second\_point.

    fedge[#](#freestyle.types.CurvePoint.fedge "Link to this definition")
    :   Gets the FEdge for the two SVertices that given CurvePoints consists out of.
        A shortcut for CurvePoint.first\_svertex.get\_fedge(CurvePoint.second\_svertex).

        Type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    first\_svertex[#](#freestyle.types.CurvePoint.first_svertex "Link to this definition")
    :   The first SVertex upon which the CurvePoint is built.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    second\_svertex[#](#freestyle.types.CurvePoint.second_svertex "Link to this definition")
    :   The second SVertex upon which the CurvePoint is built.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    t2d[#](#freestyle.types.CurvePoint.t2d "Link to this definition")
    :   The 2D interpolation parameter.

        Type:
        :   float

*class* freestyle.types.CurvePointIterator[#](#freestyle.types.CurvePointIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`CurvePointIterator`](#freestyle.types.CurvePointIterator "freestyle.types.CurvePointIterator")

    Class representing an iterator on a curve. Allows an iterating
    outside initial vertices. A CurvePoint is instantiated and returned
    through the .object attribute.

    \_\_init\_\_()[#](#freestyle.types.CurvePointIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*step=0.0*)
    :   Builds a CurvePointIterator object using either the default constructor,
        copy constructor, or the overloaded constructor.

        Parameters:
        :   * **brother** ([`CurvePointIterator`](#freestyle.types.CurvePointIterator "freestyle.types.CurvePointIterator")) – A CurvePointIterator object.
            * **step** (*float*) – A resampling resolution with which the curve is resampled.
              If zero, no resampling is done (i.e., the iterator iterates over
              initial vertices).

    object[#](#freestyle.types.CurvePointIterator.object "Link to this definition")
    :   The CurvePoint object currently pointed by this iterator.

        Type:
        :   [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")

    t[#](#freestyle.types.CurvePointIterator.t "Link to this definition")
    :   The curvilinear abscissa of the current point.

        Type:
        :   float

    u[#](#freestyle.types.CurvePointIterator.u "Link to this definition")
    :   The point parameter at the current point in the stroke (0 <= u <= 1).

        Type:
        :   float

*class* freestyle.types.FEdge[#](#freestyle.types.FEdge "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    Base Class for feature edges. This FEdge can represent a silhouette,
    a crease, a ridge/valley, a border or a suggestive contour. For
    silhouettes, the FEdge is oriented so that the visible face lies on
    the left of the edge. For borders, the FEdge is oriented so that the
    face lies on the left of the edge. An FEdge can represent an initial
    edge of the mesh or runs across a face of the initial mesh depending
    on the smoothness or sharpness of the mesh. This class is specialized
    into a smooth and a sharp version since their properties slightly vary
    from one to the other.

    FEdge()[#](#freestyle.types.FEdge.FEdge "Link to this definition")

    FEdge(*brother*)
    :   Builds an [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge") using the default constructor,
        copy constructor, or between two [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") objects.

        Parameters:
        :   * **brother** ([`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")) – An FEdge object.
            * **first\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The first SVertex.
            * **second\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The second SVertex.

    first\_svertex[#](#freestyle.types.FEdge.first_svertex "Link to this definition")
    :   The first SVertex constituting this FEdge.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    id[#](#freestyle.types.FEdge.id "Link to this definition")
    :   The Id of this FEdge.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    is\_smooth[#](#freestyle.types.FEdge.is_smooth "Link to this definition")
    :   True if this FEdge is a smooth FEdge.

        Type:
        :   bool

    nature[#](#freestyle.types.FEdge.nature "Link to this definition")
    :   The nature of this FEdge.

        Type:
        :   [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

    next\_fedge[#](#freestyle.types.FEdge.next_fedge "Link to this definition")
    :   The FEdge following this one in the ViewEdge. The value is None if
        this FEdge is the last of the ViewEdge.

        Type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    previous\_fedge[#](#freestyle.types.FEdge.previous_fedge "Link to this definition")
    :   The FEdge preceding this one in the ViewEdge. The value is None if
        this FEdge is the first one of the ViewEdge.

        Type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    second\_svertex[#](#freestyle.types.FEdge.second_svertex "Link to this definition")
    :   The second SVertex constituting this FEdge.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    viewedge[#](#freestyle.types.FEdge.viewedge "Link to this definition")
    :   The ViewEdge to which this FEdge belongs to.

        Type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

*class* freestyle.types.FEdgeSharp[#](#freestyle.types.FEdgeSharp "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge") > [`FEdgeSharp`](#freestyle.types.FEdgeSharp "freestyle.types.FEdgeSharp")

    Class defining a sharp FEdge. A Sharp FEdge corresponds to an initial
    edge of the input mesh. It can be a silhouette, a crease or a border.
    If it is a crease edge, then it is bordered by two faces of the mesh.
    Face a lies on its right whereas Face b lies on its left. If it is a
    border edge, then it doesn’t have any face on its right, and thus Face
    a is None.

    \_\_init\_\_()[#](#freestyle.types.FEdgeSharp.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*first\_vertex*, *second\_vertex*)
    :   Builds an [`FEdgeSharp`](#freestyle.types.FEdgeSharp "freestyle.types.FEdgeSharp") using the default constructor,
        copy constructor, or between two [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") objects.

        Parameters:
        :   * **brother** ([`FEdgeSharp`](#freestyle.types.FEdgeSharp "freestyle.types.FEdgeSharp")) – An FEdgeSharp object.
            * **first\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The first SVertex object.
            * **second\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The second SVertex object.

    face\_mark\_left[#](#freestyle.types.FEdgeSharp.face_mark_left "Link to this definition")
    :   The face mark of the face lying on the left of the FEdge.

        Type:
        :   bool

    face\_mark\_right[#](#freestyle.types.FEdgeSharp.face_mark_right "Link to this definition")
    :   The face mark of the face lying on the right of the FEdge. If this FEdge
        is a border, it has no face on the right and thus this property is set to
        false.

        Type:
        :   bool

    material\_index\_left[#](#freestyle.types.FEdgeSharp.material_index_left "Link to this definition")
    :   The index of the material of the face lying on the left of the FEdge.

        Type:
        :   int

    material\_index\_right[#](#freestyle.types.FEdgeSharp.material_index_right "Link to this definition")
    :   The index of the material of the face lying on the right of the FEdge.
        If this FEdge is a border, it has no Face on its right and therefore
        no material.

        Type:
        :   int

    material\_left[#](#freestyle.types.FEdgeSharp.material_left "Link to this definition")
    :   The material of the face lying on the left of the FEdge.

        Type:
        :   [`Material`](#freestyle.types.Material "freestyle.types.Material")

    material\_right[#](#freestyle.types.FEdgeSharp.material_right "Link to this definition")
    :   The material of the face lying on the right of the FEdge. If this FEdge
        is a border, it has no Face on its right and therefore no material.

        Type:
        :   [`Material`](#freestyle.types.Material "freestyle.types.Material")

    normal\_left[#](#freestyle.types.FEdgeSharp.normal_left "Link to this definition")
    :   The normal to the face lying on the left of the FEdge.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    normal\_right[#](#freestyle.types.FEdgeSharp.normal_right "Link to this definition")
    :   The normal to the face lying on the right of the FEdge. If this FEdge
        is a border, it has no Face on its right and therefore no normal.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

*class* freestyle.types.FEdgeSmooth[#](#freestyle.types.FEdgeSmooth "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge") > [`FEdgeSmooth`](#freestyle.types.FEdgeSmooth "freestyle.types.FEdgeSmooth")

    Class defining a smooth edge. This kind of edge typically runs across
    a face of the input mesh. It can be a silhouette, a ridge or valley,
    a suggestive contour.

    \_\_init\_\_()[#](#freestyle.types.FEdgeSmooth.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*first\_vertex*, *second\_vertex*)
    :   Builds an [`FEdgeSmooth`](#freestyle.types.FEdgeSmooth "freestyle.types.FEdgeSmooth") using the default constructor,
        copy constructor, or between two [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex").

        Parameters:
        :   * **brother** ([`FEdgeSmooth`](#freestyle.types.FEdgeSmooth "freestyle.types.FEdgeSmooth")) – An FEdgeSmooth object.
            * **first\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The first SVertex object.
            * **second\_vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The second SVertex object.

    face\_mark[#](#freestyle.types.FEdgeSmooth.face_mark "Link to this definition")
    :   The face mark of the face that this FEdge is running across.

        Type:
        :   bool

    material[#](#freestyle.types.FEdgeSmooth.material "Link to this definition")
    :   The material of the face that this FEdge is running across.

        Type:
        :   [`Material`](#freestyle.types.Material "freestyle.types.Material")

    material\_index[#](#freestyle.types.FEdgeSmooth.material_index "Link to this definition")
    :   The index of the material of the face that this FEdge is running across.

        Type:
        :   int

    normal[#](#freestyle.types.FEdgeSmooth.normal "Link to this definition")
    :   The normal of the face that this FEdge is running across.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

*class* freestyle.types.Id[#](#freestyle.types.Id "Link to this definition")
:   Class for representing an object Id.

    \_\_init\_\_(*brother*)[#](#freestyle.types.Id.__init__ "Link to this definition")

    \_\_init\_\_(*first=0*, *second=0*)
    :   Build the Id from two numbers or another [`Id`](#freestyle.types.Id "freestyle.types.Id") using the copy constructor.

        Parameters:
        :   * **brother** ([`Id`](#freestyle.types.Id "freestyle.types.Id") :arg first: The first number.) – An Id object.
            * **second** (*int*) – The second number.

    first[#](#freestyle.types.Id.first "Link to this definition")
    :   The first number constituting the Id.

        Type:
        :   int

    second[#](#freestyle.types.Id.second "Link to this definition")
    :   The second number constituting the Id.

        Type:
        :   int

*class* freestyle.types.IntegrationType[#](#freestyle.types.IntegrationType "Link to this definition")
:   Class hierarchy: int > [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

    Different integration methods that can be invoked to integrate into a
    single value the set of values obtained from each 0D element of an 1D
    element:

    * IntegrationType.MEAN: The value computed for the 1D element is the
      mean of the values obtained for the 0D elements.
    * IntegrationType.MIN: The value computed for the 1D element is the
      minimum of the values obtained for the 0D elements.
    * IntegrationType.MAX: The value computed for the 1D element is the
      maximum of the values obtained for the 0D elements.
    * IntegrationType.FIRST: The value computed for the 1D element is the
      first of the values obtained for the 0D elements.
    * IntegrationType.LAST: The value computed for the 1D element is the
      last of the values obtained for the 0D elements.

*class* freestyle.types.Interface0D[#](#freestyle.types.Interface0D "Link to this definition")
:   Base class for any 0D element.

    \_\_init\_\_()[#](#freestyle.types.Interface0D.__init__ "Link to this definition")
    :   Default constructor.

    get\_fedge(*inter*)[#](#freestyle.types.Interface0D.get_fedge "Link to this definition")
    :   Returns the FEdge that lies between this 0D element and the 0D
        element given as the argument.

        Parameters:
        :   **inter** ([`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D")) – A 0D element.

        Returns:
        :   The FEdge lying between the two 0D elements.

        Return type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    id[#](#freestyle.types.Interface0D.id "Link to this definition")
    :   The Id of this 0D element.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    name[#](#freestyle.types.Interface0D.name "Link to this definition")
    :   The string of the name of this 0D element.

        Type:
        :   str

    nature[#](#freestyle.types.Interface0D.nature "Link to this definition")
    :   The nature of this 0D element.

        Type:
        :   [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

    point\_2d[#](#freestyle.types.Interface0D.point_2d "Link to this definition")
    :   The 2D point of this 0D element.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    point\_3d[#](#freestyle.types.Interface0D.point_3d "Link to this definition")
    :   The 3D point of this 0D element.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    projected\_x[#](#freestyle.types.Interface0D.projected_x "Link to this definition")
    :   The X coordinate of the projected 3D point of this 0D element.

        Type:
        :   float

    projected\_y[#](#freestyle.types.Interface0D.projected_y "Link to this definition")
    :   The Y coordinate of the projected 3D point of this 0D element.

        Type:
        :   float

    projected\_z[#](#freestyle.types.Interface0D.projected_z "Link to this definition")
    :   The Z coordinate of the projected 3D point of this 0D element.

        Type:
        :   float

*class* freestyle.types.Interface0DIterator[#](#freestyle.types.Interface0DIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")

    Class defining an iterator over Interface0D elements. An instance of
    this iterator is always obtained from a 1D element.

    \_\_init\_\_(*brother*)[#](#freestyle.types.Interface0DIterator.__init__ "Link to this definition")

    \_\_init\_\_(*it*)
    :   Construct a nested Interface0DIterator using either the copy constructor
        or the constructor that takes an he argument of a Function0D.

        Parameters:
        :   * **brother** ([`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")) – An Interface0DIterator object.
            * **it** ([`SVertexIterator`](#freestyle.types.SVertexIterator "freestyle.types.SVertexIterator"), [`CurvePointIterator`](#freestyle.types.CurvePointIterator "freestyle.types.CurvePointIterator"), or
              [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")) – An iterator object to be nested.

    at\_last[#](#freestyle.types.Interface0DIterator.at_last "Link to this definition")
    :   True if the iterator points to the last valid element.
        For its counterpart (pointing to the first valid element), use it.is\_begin.

        Type:
        :   bool

    object[#](#freestyle.types.Interface0DIterator.object "Link to this definition")
    :   The 0D object currently pointed to by this iterator. Note that the object
        may be an instance of an Interface0D subclass. For example if the iterator
        has been created from the vertices\_begin() method of the [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke")
        class, the .object property refers to a [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex") object.

        Type:
        :   [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") or one of its subclasses.

    t[#](#freestyle.types.Interface0DIterator.t "Link to this definition")
    :   The curvilinear abscissa of the current point.

        Type:
        :   float

    u[#](#freestyle.types.Interface0DIterator.u "Link to this definition")
    :   The point parameter at the current point in the 1D element (0 <= u <= 1).

        Type:
        :   float

*class* freestyle.types.Interface1D[#](#freestyle.types.Interface1D "Link to this definition")
:   Base class for any 1D element.

    \_\_init\_\_()[#](#freestyle.types.Interface1D.__init__ "Link to this definition")
    :   Default constructor.

    points\_begin(*t=0.0*)[#](#freestyle.types.Interface1D.points_begin "Link to this definition")
    :   Returns an iterator over the Interface1D points, pointing to the
        first point. The difference with vertices\_begin() is that here we can
        iterate over points of the 1D element at a any given sampling.
        Indeed, for each iteration, a virtual point is created.

        Parameters:
        :   **t** (*float*) – A sampling with which we want to iterate over points of
            this 1D element.

        Returns:
        :   An Interface0DIterator pointing to the first point.

        Return type:
        :   [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")

    points\_end(*t=0.0*)[#](#freestyle.types.Interface1D.points_end "Link to this definition")
    :   Returns an iterator over the Interface1D points, pointing after the
        last point. The difference with vertices\_end() is that here we can
        iterate over points of the 1D element at a given sampling. Indeed,
        for each iteration, a virtual point is created.

        Parameters:
        :   **t** (*float*) – A sampling with which we want to iterate over points of
            this 1D element.

        Returns:
        :   An Interface0DIterator pointing after the last point.

        Return type:
        :   [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")

    vertices\_begin()[#](#freestyle.types.Interface1D.vertices_begin "Link to this definition")
    :   Returns an iterator over the Interface1D vertices, pointing to the
        first vertex.

        Returns:
        :   An Interface0DIterator pointing to the first vertex.

        Return type:
        :   [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")

    vertices\_end()[#](#freestyle.types.Interface1D.vertices_end "Link to this definition")
    :   Returns an iterator over the Interface1D vertices, pointing after
        the last vertex.

        Returns:
        :   An Interface0DIterator pointing after the last vertex.

        Return type:
        :   [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")

    id[#](#freestyle.types.Interface1D.id "Link to this definition")
    :   The Id of this Interface1D.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    length\_2d[#](#freestyle.types.Interface1D.length_2d "Link to this definition")
    :   The 2D length of this Interface1D.

        Type:
        :   float

    name[#](#freestyle.types.Interface1D.name "Link to this definition")
    :   The string of the name of the 1D element.

        Type:
        :   str

    nature[#](#freestyle.types.Interface1D.nature "Link to this definition")
    :   The nature of this Interface1D.

        Type:
        :   [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

    time\_stamp[#](#freestyle.types.Interface1D.time_stamp "Link to this definition")
    :   The time stamp of the 1D element, mainly used for selection.

        Type:
        :   int

*class* freestyle.types.Iterator[#](#freestyle.types.Iterator "Link to this definition")
:   Base class to define iterators.

    \_\_init\_\_()[#](#freestyle.types.Iterator.__init__ "Link to this definition")
    :   Default constructor.

    decrement()[#](#freestyle.types.Iterator.decrement "Link to this definition")
    :   Makes the iterator point the previous element.

    increment()[#](#freestyle.types.Iterator.increment "Link to this definition")
    :   Makes the iterator point the next element.

    is\_begin[#](#freestyle.types.Iterator.is_begin "Link to this definition")
    :   True if the iterator points to the first element.

        Type:
        :   bool

    is\_end[#](#freestyle.types.Iterator.is_end "Link to this definition")
    :   True if the iterator points to the last element.

        Type:
        :   bool

    name[#](#freestyle.types.Iterator.name "Link to this definition")
    :   The string of the name of this iterator.

        Type:
        :   str

*class* freestyle.types.Material[#](#freestyle.types.Material "Link to this definition")
:   Class defining a material.

    \_\_init\_\_()[#](#freestyle.types.Material.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*line*, *diffuse*, *ambient*, *specular*, *emission*, *shininess*, *priority*)
    :   Creates a `FrsMaterial` using either default constructor,
        copy constructor, or an overloaded constructor

        Parameters:
        :   * **brother** ([`Material`](#freestyle.types.Material "freestyle.types.Material")) – A Material object to be used as a copy constructor.
            * **line** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 4 float values) – The line color.
            * **diffuse** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 4 float values) – The diffuse color.
            * **ambient** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 4 float values) – The ambient color.
            * **specular** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 4 float values) – The specular color.
            * **emission** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 4 float values) – The emissive color.
            * **shininess** (*float*) – The shininess coefficient.
            * **priority** (*int*) – The line color priority.

    ambient[#](#freestyle.types.Material.ambient "Link to this definition")
    :   RGBA components of the ambient color of the material.

        Type:
        :   [`mathutils.Color`](../../mathutils/index.md#mathutils.Color "mathutils.Color")

    diffuse[#](#freestyle.types.Material.diffuse "Link to this definition")
    :   RGBA components of the diffuse color of the material.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    emission[#](#freestyle.types.Material.emission "Link to this definition")
    :   RGBA components of the emissive color of the material.

        Type:
        :   [`mathutils.Color`](../../mathutils/index.md#mathutils.Color "mathutils.Color")

    line[#](#freestyle.types.Material.line "Link to this definition")
    :   RGBA components of the line color of the material.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    priority[#](#freestyle.types.Material.priority "Link to this definition")
    :   Line color priority of the material.

        Type:
        :   int

    shininess[#](#freestyle.types.Material.shininess "Link to this definition")
    :   Shininess coefficient of the material.

        Type:
        :   float

    specular[#](#freestyle.types.Material.specular "Link to this definition")
    :   RGBA components of the specular color of the material.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

*class* freestyle.types.MediumType[#](#freestyle.types.MediumType "Link to this definition")
:   Class hierarchy: int > [`MediumType`](#freestyle.types.MediumType "freestyle.types.MediumType")

    The different blending modes available to simulate the interaction
    media-medium:

    * Stroke.DRY\_MEDIUM: To simulate a dry medium such as Pencil or Charcoal.
    * Stroke.HUMID\_MEDIUM: To simulate ink painting (color subtraction blending).
    * Stroke.OPAQUE\_MEDIUM: To simulate an opaque medium (oil, spray…).

*class* freestyle.types.Nature[#](#freestyle.types.Nature "Link to this definition")
:   Class hierarchy: int > [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

    Different possible natures of 0D and 1D elements of the ViewMap.

    Vertex natures:

    * Nature.POINT: True for any 0D element.
    * Nature.S\_VERTEX: True for SVertex.
    * Nature.VIEW\_VERTEX: True for ViewVertex.
    * Nature.NON\_T\_VERTEX: True for NonTVertex.
    * Nature.T\_VERTEX: True for TVertex.
    * Nature.CUSP: True for CUSP.

    Edge natures:

    * Nature.NO\_FEATURE: True for non feature edges (always false for 1D
      elements of the ViewMap).
    * Nature.SILHOUETTE: True for silhouettes.
    * Nature.BORDER: True for borders.
    * Nature.CREASE: True for creases.
    * Nature.RIDGE: True for ridges.
    * Nature.VALLEY: True for valleys.
    * Nature.SUGGESTIVE\_CONTOUR: True for suggestive contours.
    * Nature.MATERIAL\_BOUNDARY: True for edges at material boundaries.
    * Nature.EDGE\_MARK: True for edges having user-defined edge marks.

*class* freestyle.types.Noise[#](#freestyle.types.Noise "Link to this definition")
:   Class to provide Perlin noise functionalities.

    \_\_init\_\_(*seed=-1*)[#](#freestyle.types.Noise.__init__ "Link to this definition")
    :   Builds a Noise object. Seed is an optional argument. The seed value is used
        as a seed for random number generation if it is equal to or greater than zero;
        otherwise, time is used as a seed.

        Parameters:
        :   **seed** (*int*) – Seed for random number generation.

    Undocumented, consider [contributing](https://developer.blender.org/).

    smoothNoise1(*v*)[#](#freestyle.types.Noise.smoothNoise1 "Link to this definition")
    :   Returns a smooth noise value for a 1D element.

        Parameters:
        :   **v** (*float*) – One-dimensional sample point.

        Returns:
        :   A smooth noise value.

        Return type:
        :   float

    smoothNoise2(*v*)[#](#freestyle.types.Noise.smoothNoise2 "Link to this definition")
    :   Returns a smooth noise value for a 2D element.

        Parameters:
        :   **v** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 2 real numbers) – Two-dimensional sample point.

        Returns:
        :   A smooth noise value.

        Return type:
        :   float

    smoothNoise3(*v*)[#](#freestyle.types.Noise.smoothNoise3 "Link to this definition")
    :   Returns a smooth noise value for a 3D element.

        Parameters:
        :   **v** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 3 real numbers) – Three-dimensional sample point.

        Returns:
        :   A smooth noise value.

        Return type:
        :   float

    turbulence1(*v*, *freq*, *amp*, *oct=4*)[#](#freestyle.types.Noise.turbulence1 "Link to this definition")
    :   Returns a noise value for a 1D element.

        Parameters:
        :   * **v** (*float*) – One-dimensional sample point.
            * **freq** (*float*) – Noise frequency.
            * **amp** (*float*) – Amplitude.
            * **oct** (*int*) – Number of octaves.

        Returns:
        :   A noise value.

        Return type:
        :   float

    turbulence2(*v*, *freq*, *amp*, *oct=4*)[#](#freestyle.types.Noise.turbulence2 "Link to this definition")
    :   Returns a noise value for a 2D element.

        Parameters:
        :   * **v** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 2 real numbers) – Two-dimensional sample point.
            * **freq** (*float*) – Noise frequency.
            * **amp** (*float*) – Amplitude.
            * **oct** (*int*) – Number of octaves.

        Returns:
        :   A noise value.

        Return type:
        :   float

    turbulence3(*v*, *freq*, *amp*, *oct=4*)[#](#freestyle.types.Noise.turbulence3 "Link to this definition")
    :   Returns a noise value for a 3D element.

        Parameters:
        :   * **v** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 3 real numbers) – Three-dimensional sample point.
            * **freq** (*float*) – Noise frequency.
            * **amp** (*float*) – Amplitude.
            * **oct** (*int*) – Number of octaves.

        Returns:
        :   A noise value.

        Return type:
        :   float

    Undocumented, consider [contributing](https://developer.blender.org/).

*class* freestyle.types.NonTVertex[#](#freestyle.types.NonTVertex "Link to this definition")
:   Class hierarchy: [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") > [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex") > [`NonTVertex`](#freestyle.types.NonTVertex "freestyle.types.NonTVertex")

    View vertex for corners, cusps, etc. associated to a single SVertex.
    Can be associated to 2 or more view edges.

    \_\_init\_\_()[#](#freestyle.types.NonTVertex.__init__ "Link to this definition")

    \_\_init\_\_(*svertex*)
    :   Builds a [`NonTVertex`](#freestyle.types.NonTVertex "freestyle.types.NonTVertex") using the default constructor or a [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex").

        Parameters:
        :   **svertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – An SVertex object.

    svertex[#](#freestyle.types.NonTVertex.svertex "Link to this definition")
    :   The SVertex on top of which this NonTVertex is built.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

*class* freestyle.types.Operators[#](#freestyle.types.Operators "Link to this definition")
:   Class defining the operators used in a style module. There are five
    types of operators: Selection, chaining, splitting, sorting and
    creation. All these operators are user controlled through functors,
    predicates and shaders that are taken as arguments.

    *static* bidirectional\_chain(*it*, *pred*)[#](#freestyle.types.Operators.bidirectional_chain "Link to this definition")

    *static* bidirectional\_chain(*it*)
    :   Builds a set of chains from the current set of ViewEdges. Each
        ViewEdge of the current list potentially starts a new chain. The
        chaining operator then iterates over the ViewEdges of the ViewMap
        using the user specified iterator. This operator iterates both using
        the increment and decrement operators and is therefore bidirectional.
        This operator works with a ChainingIterator which contains the
        chaining rules. It is this last one which can be told to chain only
        edges that belong to the selection or not to process twice a ViewEdge
        during the chaining. Each time a ViewEdge is added to a chain, its
        chaining time stamp is incremented. This allows you to keep track of
        the number of chains to which a ViewEdge belongs to.

        Parameters:
        :   * **it** ([`ChainingIterator`](#freestyle.types.ChainingIterator "freestyle.types.ChainingIterator")) – The ChainingIterator on the ViewEdges of the ViewMap. It
              contains the chaining rule.
            * **pred** ([`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")) – The predicate on the ViewEdge that expresses the stopping condition.
              This parameter is optional, you make not want to pass a stopping criterion
              when the stopping criterion is already contained in the iterator definition.

    *static* chain(*it*, *pred*, *modifier*)[#](#freestyle.types.Operators.chain "Link to this definition")

    *static* chain(*it*, *pred*)
    :   Builds a set of chains from the current set of ViewEdges. Each
        ViewEdge of the current list starts a new chain. The chaining
        operator then iterates over the ViewEdges of the ViewMap using the
        user specified iterator. This operator only iterates using the
        increment operator and is therefore unidirectional.

        Parameters:
        :   * **it** ([`ViewEdgeIterator`](#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator")) – The iterator on the ViewEdges of the ViewMap. It contains
              the chaining rule.
            * **pred** ([`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")) – The predicate on the ViewEdge that expresses the
              stopping condition.
            * **modifier** ([`UnaryFunction1DVoid`](#freestyle.types.UnaryFunction1DVoid "freestyle.types.UnaryFunction1DVoid")) – A function that takes a ViewEdge as argument and
              that is used to modify the processed ViewEdge state (the
              timestamp incrementation is a typical illustration of such a modifier).
              If this argument is not given, the time stamp is automatically managed.

    *static* create(*pred*, *shaders*)[#](#freestyle.types.Operators.create "Link to this definition")
    :   Creates and shades the strokes from the current set of chains. A
        predicate can be specified to make a selection pass on the chains.

        Parameters:
        :   * **pred** ([`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")) – The predicate that a chain must verify in order to be
              transform as a stroke.
            * **shaders** (list of [`StrokeShader`](#freestyle.types.StrokeShader "freestyle.types.StrokeShader") objects) – The list of shaders used to shade the strokes.

    *static* get\_chain\_from\_index(*i*)[#](#freestyle.types.Operators.get_chain_from_index "Link to this definition")
    :   Returns the Chain at the index in the current set of Chains.

        Parameters:
        :   **i** (*int*) – index (0 <= i < Operators.get\_chains\_size()).

        Returns:
        :   The Chain object.

        Return type:
        :   [`Chain`](#freestyle.types.Chain "freestyle.types.Chain")

    *static* get\_chains\_size()[#](#freestyle.types.Operators.get_chains_size "Link to this definition")
    :   Returns the number of Chains.

        Returns:
        :   The number of Chains.

        Return type:
        :   int

    *static* get\_stroke\_from\_index(*i*)[#](#freestyle.types.Operators.get_stroke_from_index "Link to this definition")
    :   Returns the Stroke at the index in the current set of Strokes.

        Parameters:
        :   **i** (*int*) – index (0 <= i < Operators.get\_strokes\_size()).

        Returns:
        :   The Stroke object.

        Return type:
        :   [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke")

    *static* get\_strokes\_size()[#](#freestyle.types.Operators.get_strokes_size "Link to this definition")
    :   Returns the number of Strokes.

        Returns:
        :   The number of Strokes.

        Return type:
        :   int

    *static* get\_view\_edges\_size()[#](#freestyle.types.Operators.get_view_edges_size "Link to this definition")
    :   Returns the number of ViewEdges.

        Returns:
        :   The number of ViewEdges.

        Return type:
        :   int

    *static* get\_viewedge\_from\_index(*i*)[#](#freestyle.types.Operators.get_viewedge_from_index "Link to this definition")
    :   Returns the ViewEdge at the index in the current set of ViewEdges.

        Parameters:
        :   **i** (*int*) – index (0 <= i < Operators.get\_view\_edges\_size()).

        Returns:
        :   The ViewEdge object.

        Return type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    *static* recursive\_split(*func*, *pred\_1d*, *sampling=0.0*)[#](#freestyle.types.Operators.recursive_split "Link to this definition")

    *static* recursive\_split(*func*, *pred\_0d*, *pred\_1d*, *sampling=0.0*)
    :   Splits the current set of chains in a recursive way. We process the
        points of each chain (with a specified sampling) to find the point
        minimizing a specified function. The chain is split in two at this
        point and the two new chains are processed in the same way. The
        recursivity level is controlled through a predicate 1D that expresses
        a stopping condition on the chain that is about to be processed.

        The user can also specify a 0D predicate to make a first selection on the points
        that can potentially be split. A point that doesn’t verify the 0D
        predicate won’t be candidate in realizing the min.

        Parameters:
        :   * **func** ([`UnaryFunction0DDouble`](#freestyle.types.UnaryFunction0DDouble "freestyle.types.UnaryFunction0DDouble")) – The Unary Function evaluated at each point of the chain.
              The splitting point is the point minimizing this function.
            * **pred\_0d** ([`UnaryPredicate0D`](#freestyle.types.UnaryPredicate0D "freestyle.types.UnaryPredicate0D")) – The Unary Predicate 0D used to select the candidate
              points where the split can occur. For example, it is very likely
              that would rather have your chain splitting around its middle
              point than around one of its extremities. A 0D predicate working
              on the curvilinear abscissa allows to add this kind of constraints.
            * **pred\_1d** ([`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")) – The Unary Predicate expressing the recursivity stopping
              condition. This predicate is evaluated for each curve before it
              actually gets split. If pred\_1d(chain) is true, the curve won’t be
              split anymore.
            * **sampling** (*float*) – The resolution used to sample the chain for the
              predicates evaluation. (The chain is not actually resampled; a
              virtual point only progresses along the curve using this
              resolution.)

    *static* reset(*delete\_strokes=True*)[#](#freestyle.types.Operators.reset "Link to this definition")
    :   Resets the line stylization process to the initial state. The results of
        stroke creation are accumulated if **delete\_strokes** is set to False.

        Parameters:
        :   **delete\_strokes** (*bool*) – Delete the strokes that are currently stored.

    *static* select(*pred*)[#](#freestyle.types.Operators.select "Link to this definition")
    :   Selects the ViewEdges of the ViewMap verifying a specified
        condition.

        Parameters:
        :   **pred** ([`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D "freestyle.types.UnaryPredicate1D")) – The predicate expressing this condition.

    *static* sequential\_split(*starting\_pred*, *stopping\_pred*, *sampling=0.0*)[#](#freestyle.types.Operators.sequential_split "Link to this definition")

    *static* sequential\_split(*pred*, *sampling=0.0*)
    :   Splits each chain of the current set of chains in a sequential way.
        The points of each chain are processed (with a specified sampling)
        sequentially. The first point of the initial chain is the
        first point of one of the resulting chains. The splitting ends when
        no more chain can start.

        Tip

        By specifying a starting and stopping predicate allows
        the chains to overlap rather than chains partitioning.

        Parameters:
        :   * **starting\_pred** ([`UnaryPredicate0D`](#freestyle.types.UnaryPredicate0D "freestyle.types.UnaryPredicate0D")) – The predicate on a point that expresses the
              starting condition. Each time this condition is verified, a new chain begins
            * **stopping\_pred** ([`UnaryPredicate0D`](#freestyle.types.UnaryPredicate0D "freestyle.types.UnaryPredicate0D")) – The predicate on a point that expresses the
              stopping condition. The chain ends as soon as this predicate is verified.
            * **pred** ([`UnaryPredicate0D`](#freestyle.types.UnaryPredicate0D "freestyle.types.UnaryPredicate0D")) – The predicate on a point that expresses the splitting condition.
              Each time the condition is verified, the chain is split into two chains.
              The resulting set of chains is a partition of the initial chain
            * **sampling** (*float*) – The resolution used to sample the chain for the
              predicates evaluation. (The chain is not actually resampled;
              a virtual point only progresses along the curve using this
              resolution.)

    *static* sort(*pred*)[#](#freestyle.types.Operators.sort "Link to this definition")
    :   Sorts the current set of chains (or viewedges) according to the
        comparison predicate given as argument.

        Parameters:
        :   **pred** ([`BinaryPredicate1D`](#freestyle.types.BinaryPredicate1D "freestyle.types.BinaryPredicate1D")) – The binary predicate used for the comparison.

*class* freestyle.types.SShape[#](#freestyle.types.SShape "Link to this definition")
:   Class to define a feature shape. It is the gathering of feature
    elements from an identified input shape.

    \_\_init\_\_()[#](#freestyle.types.SShape.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Creates a [`SShape`](#freestyle.types.SShape "freestyle.types.SShape") class using either a default constructor or copy constructor.

        Parameters:
        :   **brother** ([`SShape`](#freestyle.types.SShape "freestyle.types.SShape")) – An SShape object.

    add\_edge(*edge*)[#](#freestyle.types.SShape.add_edge "Link to this definition")
    :   Adds an FEdge to the list of FEdges.

        Parameters:
        :   **edge** ([`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")) – An FEdge object.

    add\_vertex(*vertex*)[#](#freestyle.types.SShape.add_vertex "Link to this definition")
    :   Adds an SVertex to the list of SVertex of this Shape. The SShape
        attribute of the SVertex is also set to this SShape.

        Parameters:
        :   **vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – An SVertex object.

    compute\_bbox()[#](#freestyle.types.SShape.compute_bbox "Link to this definition")
    :   Compute the bbox of the SShape.

    bbox[#](#freestyle.types.SShape.bbox "Link to this definition")
    :   The bounding box of the SShape.

        Type:
        :   [`BBox`](#freestyle.types.BBox "freestyle.types.BBox")

    edges[#](#freestyle.types.SShape.edges "Link to this definition")
    :   The list of edges constituting this SShape.

        Type:
        :   List of [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge") objects

    id[#](#freestyle.types.SShape.id "Link to this definition")
    :   The Id of this SShape.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    name[#](#freestyle.types.SShape.name "Link to this definition")
    :   The name of the SShape.

        Type:
        :   str

    vertices[#](#freestyle.types.SShape.vertices "Link to this definition")
    :   The list of vertices constituting this SShape.

        Type:
        :   List of [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") objects

*class* freestyle.types.SVertex[#](#freestyle.types.SVertex "Link to this definition")
:   Class hierarchy: [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") > [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    Class to define a vertex of the embedding.

    \_\_init\_\_()[#](#freestyle.types.SVertex.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*point\_3d*, *id*)
    :   Builds a [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") using the default constructor,
        copy constructor or the overloaded constructor which builds a [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") from 3D coordinates and an Id.

        Parameters:
        :   * **brother** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – A SVertex object.
            * **point\_3d** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")) – A three-dimensional vector.
            * **id** ([`Id`](#freestyle.types.Id "freestyle.types.Id")) – An Id object.

    add\_fedge(*fedge*)[#](#freestyle.types.SVertex.add_fedge "Link to this definition")
    :   Add an FEdge to the list of edges emanating from this SVertex.

        Parameters:
        :   **fedge** ([`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")) – An FEdge.

    add\_normal(*normal*)[#](#freestyle.types.SVertex.add_normal "Link to this definition")
    :   Adds a normal to the SVertex’s set of normals. If the same normal
        is already in the set, nothing changes.

        Parameters:
        :   **normal** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 3 real numbers) – A three-dimensional vector.

    curvatures[#](#freestyle.types.SVertex.curvatures "Link to this definition")
    :   Curvature information expressed in the form of a seven-element tuple
        (K1, e1, K2, e2, Kr, er, dKr), where K1 and K2 are scalar values
        representing the first (maximum) and second (minimum) principal
        curvatures at this SVertex, respectively; e1 and e2 are
        three-dimensional vectors representing the first and second principal
        directions, i.e. the directions of the normal plane where the
        curvature takes its maximum and minimum values, respectively; and Kr,
        er and dKr are the radial curvature, radial direction, and the
        derivative of the radial curvature at this SVertex, respectively.

        Type:
        :   tuple

    id[#](#freestyle.types.SVertex.id "Link to this definition")
    :   The Id of this SVertex.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    normals[#](#freestyle.types.SVertex.normals "Link to this definition")
    :   The normals for this Vertex as a list. In a sharp surface, an SVertex
        has exactly one normal. In a smooth surface, an SVertex can have any
        number of normals.

        Type:
        :   list of [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") objects

    normals\_size[#](#freestyle.types.SVertex.normals_size "Link to this definition")
    :   The number of different normals for this SVertex.

        Type:
        :   int

    point\_2d[#](#freestyle.types.SVertex.point_2d "Link to this definition")
    :   The projected 3D coordinates of the SVertex.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    point\_3d[#](#freestyle.types.SVertex.point_3d "Link to this definition")
    :   The 3D coordinates of the SVertex.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    viewvertex[#](#freestyle.types.SVertex.viewvertex "Link to this definition")
    :   If this SVertex is also a ViewVertex, this property refers to the
        ViewVertex, and None otherwise.

        Type:
        :   [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")

*class* freestyle.types.SVertexIterator[#](#freestyle.types.SVertexIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`SVertexIterator`](#freestyle.types.SVertexIterator "freestyle.types.SVertexIterator")

    Class representing an iterator over [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") of a
    [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge"). An instance of an SVertexIterator can be obtained
    from a ViewEdge by calling verticesBegin() or verticesEnd().

    \_\_init\_\_()[#](#freestyle.types.SVertexIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*vertex*, *begin*, *previous\_edge*, *next\_edge*, *t*)

    Build an SVertexIterator using either the default constructor, copy constructor,

    or the overloaded constructor that starts iteration from an SVertex object vertex.
    :   Parameters:
        :   * **brother** ([`SVertexIterator`](#freestyle.types.SVertexIterator "freestyle.types.SVertexIterator")) – An SVertexIterator object.
            * **vertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The SVertex from which the iterator starts iteration.
            * **begin** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – The first SVertex of a ViewEdge.
            * **previous\_edge** ([`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")) – The previous FEdge coming to vertex.
            * **next\_edge** ([`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")) – The next FEdge going out from vertex.
            * **t** (*float*) – The curvilinear abscissa at vertex.

    object[#](#freestyle.types.SVertexIterator.object "Link to this definition")
    :   The SVertex object currently pointed by this iterator.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    t[#](#freestyle.types.SVertexIterator.t "Link to this definition")
    :   The curvilinear abscissa of the current point.

        Type:
        :   float

    u[#](#freestyle.types.SVertexIterator.u "Link to this definition")
    :   The point parameter at the current point in the 1D element (0 <= u <= 1).

        Type:
        :   float

*class* freestyle.types.Stroke[#](#freestyle.types.Stroke "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke")

    Class to define a stroke. A stroke is made of a set of 2D vertices
    ([`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")), regularly spaced out. This set of vertices
    defines the stroke’s backbone geometry. Each of these stroke vertices
    defines the stroke’s shape and appearance at this vertex position.

    Stroke()[#](#freestyle.types.Stroke.Stroke "Link to this definition")

    Stroke(*brother*)
    :   Creates a [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke") using the default constructor or copy constructor

    compute\_sampling(*n*)[#](#freestyle.types.Stroke.compute_sampling "Link to this definition")
    :   Compute the sampling needed to get N vertices. If the
        specified number of vertices is less than the actual number of
        vertices, the actual sampling value is returned. (To remove Vertices,
        use the RemoveVertex() method of this class.)

        Parameters:
        :   **n** (*int*) – The number of stroke vertices we eventually want
            in our Stroke.

        Returns:
        :   The sampling that must be used in the Resample(float)
            method.

        Return type:
        :   float

    insert\_vertex(*vertex*, *next*)[#](#freestyle.types.Stroke.insert_vertex "Link to this definition")
    :   Inserts the StrokeVertex given as argument into the Stroke before the
        point specified by next. The length and curvilinear abscissa are
        updated consequently.

        Parameters:
        :   * **vertex** ([`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")) – The StrokeVertex to insert in the Stroke.
            * **next** ([`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")) – A StrokeVertexIterator pointing to the StrokeVertex
              before which vertex must be inserted.

    remove\_all\_vertices()[#](#freestyle.types.Stroke.remove_all_vertices "Link to this definition")
    :   Removes all vertices from the Stroke.

    remove\_vertex(*vertex*)[#](#freestyle.types.Stroke.remove_vertex "Link to this definition")
    :   Removes the StrokeVertex given as argument from the Stroke. The length
        and curvilinear abscissa are updated consequently.

        Parameters:
        :   **vertex** ([`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")) – the StrokeVertex to remove from the Stroke.

    resample(*n*)[#](#freestyle.types.Stroke.resample "Link to this definition")

    resample(*sampling*)
    :   Resamples the stroke so using one of two methods with the goal
        of creating a stroke with fewer points and the same shape.

        Parameters:
        :   * **n** (*int*) – Resamples the stroke so that it eventually has N points. That means
              it is going to add N-vertices\_size, where vertices\_size is the
              number of points we already have. If vertices\_size >= N, no
              resampling is done.
            * **sampling** (*float*) – Resamples the stroke with a given sampling value. If the
              sampling is smaller than the actual sampling value, no resampling is done.

    stroke\_vertices\_begin(*t=0.0*)[#](#freestyle.types.Stroke.stroke_vertices_begin "Link to this definition")
    :   Returns a StrokeVertexIterator pointing on the first StrokeVertex of
        the Stroke. One can specify a sampling value to re-sample the Stroke
        on the fly if needed.

        Parameters:
        :   **t** (*float*) – The resampling value with which we want our Stroke to be
            resampled. If 0 is specified, no resampling is done.

        Returns:
        :   A StrokeVertexIterator pointing on the first StrokeVertex.

        Return type:
        :   [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")

    stroke\_vertices\_end()[#](#freestyle.types.Stroke.stroke_vertices_end "Link to this definition")
    :   Returns a StrokeVertexIterator pointing after the last StrokeVertex
        of the Stroke.

        Returns:
        :   A StrokeVertexIterator pointing after the last StrokeVertex.

        Return type:
        :   [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")

    stroke\_vertices\_size()[#](#freestyle.types.Stroke.stroke_vertices_size "Link to this definition")
    :   Returns the number of StrokeVertex constituting the Stroke.

        Returns:
        :   The number of stroke vertices.

        Return type:
        :   int

    update\_length()[#](#freestyle.types.Stroke.update_length "Link to this definition")
    :   Updates the 2D length of the Stroke.

    id[#](#freestyle.types.Stroke.id "Link to this definition")
    :   The Id of this Stroke.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    length\_2d[#](#freestyle.types.Stroke.length_2d "Link to this definition")
    :   The 2D length of the Stroke.

        Type:
        :   float

    medium\_type[#](#freestyle.types.Stroke.medium_type "Link to this definition")
    :   The MediumType used for this Stroke.

        Type:
        :   [`MediumType`](#freestyle.types.MediumType "freestyle.types.MediumType")

    texture\_id[#](#freestyle.types.Stroke.texture_id "Link to this definition")
    :   The ID of the texture used to simulate th marks system for this Stroke.

        Type:
        :   int

    tips[#](#freestyle.types.Stroke.tips "Link to this definition")
    :   True if this Stroke uses a texture with tips, and false otherwise.

        Type:
        :   bool

*class* freestyle.types.StrokeAttribute[#](#freestyle.types.StrokeAttribute "Link to this definition")
:   Class to define a set of attributes associated with a [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex").
    The attribute set stores the color, alpha and thickness values for a Stroke
    Vertex.

    \_\_init\_\_()[#](#freestyle.types.StrokeAttribute.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*red*, *green*, *blue*, *alpha*, *thickness\_right*, *thickness\_left*)

    \_\_init\_\_(*attribute1*, *attribute2*, *t*)
    :   Creates a [`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute") object using either a default constructor,
        copy constructor, overloaded constructor, or and interpolation constructor
        to interpolate between two [`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute") objects.

        Parameters:
        :   * **brother** ([`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute")) – A StrokeAttribute object to be used as a copy constructor.
            * **red** (*float*) – Red component of a stroke color.
            * **green** (*float*) – Green component of a stroke color.
            * **blue** (*float*) – Blue component of a stroke color.
            * **alpha** (*float*) – Alpha component of a stroke color.
            * **thickness\_right** (*float*) – Stroke thickness on the right.
            * **thickness\_left** (*float*) – Stroke thickness on the left.
            * **attribute1** ([`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute")) – The first StrokeAttribute object.
            * **attribute2** ([`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute")) – The second StrokeAttribute object.
            * **t** (*float*) – The interpolation parameter (0 <= t <= 1).

    get\_attribute\_real(*name*)[#](#freestyle.types.StrokeAttribute.get_attribute_real "Link to this definition")
    :   Returns an attribute of float type.

        Parameters:
        :   **name** (*str*) – The name of the attribute.

        Returns:
        :   The attribute value.

        Return type:
        :   float

    get\_attribute\_vec2(*name*)[#](#freestyle.types.StrokeAttribute.get_attribute_vec2 "Link to this definition")
    :   Returns an attribute of two-dimensional vector type.

        Parameters:
        :   **name** (*str*) – The name of the attribute.

        Returns:
        :   The attribute value.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    get\_attribute\_vec3(*name*)[#](#freestyle.types.StrokeAttribute.get_attribute_vec3 "Link to this definition")
    :   Returns an attribute of three-dimensional vector type.

        Parameters:
        :   **name** (*str*) – The name of the attribute.

        Returns:
        :   The attribute value.

        Return type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    has\_attribute\_real(*name*)[#](#freestyle.types.StrokeAttribute.has_attribute_real "Link to this definition")
    :   Checks whether the attribute name of float type is available.

        Parameters:
        :   **name** (*str*) – The name of the attribute.

        Returns:
        :   True if the attribute is available.

        Return type:
        :   bool

    has\_attribute\_vec2(*name*)[#](#freestyle.types.StrokeAttribute.has_attribute_vec2 "Link to this definition")
    :   Checks whether the attribute name of two-dimensional vector type
        is available.

        Parameters:
        :   **name** (*str*) – The name of the attribute.

        Returns:
        :   True if the attribute is available.

        Return type:
        :   bool

    has\_attribute\_vec3(*name*)[#](#freestyle.types.StrokeAttribute.has_attribute_vec3 "Link to this definition")
    :   Checks whether the attribute name of three-dimensional vector
        type is available.

        Parameters:
        :   **name** (*str*) – The name of the attribute.

        Returns:
        :   True if the attribute is available.

        Return type:
        :   bool

    set\_attribute\_real(*name*, *value*)[#](#freestyle.types.StrokeAttribute.set_attribute_real "Link to this definition")
    :   Adds a user-defined attribute of float type. If there is no
        attribute of the given name, it is added. Otherwise, the new value
        replaces the old one.

        Parameters:
        :   * **name** (*str*) – The name of the attribute.
            * **value** (*float*) – The attribute value.

    set\_attribute\_vec2(*name*, *value*)[#](#freestyle.types.StrokeAttribute.set_attribute_vec2 "Link to this definition")
    :   Adds a user-defined attribute of two-dimensional vector type. If
        there is no attribute of the given name, it is added. Otherwise,
        the new value replaces the old one.

        Parameters:
        :   * **name** (*str*) – The name of the attribute.
            * **value** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 2 real numbers) – The attribute value.

    set\_attribute\_vec3(*name*, *value*)[#](#freestyle.types.StrokeAttribute.set_attribute_vec3 "Link to this definition")
    :   Adds a user-defined attribute of three-dimensional vector type.
        If there is no attribute of the given name, it is added.
        Otherwise, the new value replaces the old one.

        Parameters:
        :   * **name** (*str*) – The name of the attribute.
            * **value** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector"), list or tuple of 3 real numbers) – The attribute value.

    alpha[#](#freestyle.types.StrokeAttribute.alpha "Link to this definition")
    :   Alpha component of the stroke color.

        Type:
        :   float

    color[#](#freestyle.types.StrokeAttribute.color "Link to this definition")
    :   RGB components of the stroke color.

        Type:
        :   [`mathutils.Color`](../../mathutils/index.md#mathutils.Color "mathutils.Color")

    thickness[#](#freestyle.types.StrokeAttribute.thickness "Link to this definition")
    :   Right and left components of the stroke thickness.
        The right (left) component is the thickness on the right (left) of the vertex
        when following the stroke.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    visible[#](#freestyle.types.StrokeAttribute.visible "Link to this definition")
    :   The visibility flag. True if the StrokeVertex is visible.

        Type:
        :   bool

*class* freestyle.types.StrokeShader[#](#freestyle.types.StrokeShader "Link to this definition")
:   Base class for stroke shaders. Any stroke shader must inherit from
    this class and overload the shade() method. A StrokeShader is
    designed to modify stroke attributes such as thickness, color,
    geometry, texture, blending mode, and so on. The basic way for this
    operation is to iterate over the stroke vertices of the [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke")
    and to modify the [`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute") of each vertex. Here is a
    code example of such an iteration:

    ```
    it = ioStroke.strokeVerticesBegin()
    while not it.is_end:
        att = it.object.attribute
        ## perform here any attribute modification
        it.increment()
    ```

    \_\_init\_\_()[#](#freestyle.types.StrokeShader.__init__ "Link to this definition")
    :   Default constructor.

    shade(*stroke*)[#](#freestyle.types.StrokeShader.shade "Link to this definition")
    :   The shading method. Must be overloaded by inherited classes.

        Parameters:
        :   **stroke** ([`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke")) – A Stroke object.

    name[#](#freestyle.types.StrokeShader.name "Link to this definition")
    :   The name of the stroke shader.

        Type:
        :   str

*class* freestyle.types.StrokeVertex[#](#freestyle.types.StrokeVertex "Link to this definition")
:   Class hierarchy: [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") > [`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint") > [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")

    Class to define a stroke vertex.

    \_\_init\_\_()[#](#freestyle.types.StrokeVertex.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*first\_vertex*, *second\_vertex*, *t3d*)

    \_\_init\_\_(*point*)

    \_\_init\_\_(*svertex*)

    \_\_init\_\_(*svertex*, *attribute*)
    :   Builds a [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex") using the default constructor,
        copy constructor, from 2 [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex") and an interpolation parameter,
        from a CurvePoint, from a SVertex, or a [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex") and a [`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute") object.

        Parameters:
        :   * **brother** ([`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")) – A StrokeVertex object.
            * **first\_vertex** ([`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")) – The first StrokeVertex.
            * **second\_vertex** ([`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")) – The second StrokeVertex.
            * **t3d** (*float*) – An interpolation parameter.
            * **point** ([`CurvePoint`](#freestyle.types.CurvePoint "freestyle.types.CurvePoint")) – A CurvePoint object.
            * **svertex** ([`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")) – An SVertex object.
            * **svertex** – An SVertex object.
            * **attribute** ([`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute")) – A StrokeAttribute object.

    attribute[#](#freestyle.types.StrokeVertex.attribute "Link to this definition")
    :   StrokeAttribute for this StrokeVertex.

        Type:
        :   [`StrokeAttribute`](#freestyle.types.StrokeAttribute "freestyle.types.StrokeAttribute")

    curvilinear\_abscissa[#](#freestyle.types.StrokeVertex.curvilinear_abscissa "Link to this definition")
    :   Curvilinear abscissa of this StrokeVertex in the Stroke.

        Type:
        :   float

    point[#](#freestyle.types.StrokeVertex.point "Link to this definition")
    :   2D point coordinates.

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector")

    stroke\_length[#](#freestyle.types.StrokeVertex.stroke_length "Link to this definition")
    :   Stroke length (it is only a value retained by the StrokeVertex,
        and it won’t change the real stroke length).

        Type:
        :   float

    u[#](#freestyle.types.StrokeVertex.u "Link to this definition")
    :   Curvilinear abscissa of this StrokeVertex in the Stroke.

        Type:
        :   float

*class* freestyle.types.StrokeVertexIterator[#](#freestyle.types.StrokeVertexIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")

    Class defining an iterator designed to iterate over the
    [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex") of a [`Stroke`](#freestyle.types.Stroke "freestyle.types.Stroke"). An instance of a
    StrokeVertexIterator can be obtained from a Stroke by calling
    iter(), stroke\_vertices\_begin() or stroke\_vertices\_begin(). It is iterating
    over the same vertices as an [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator"). The difference
    resides in the object access: an Interface0DIterator only allows
    access to an Interface0D while one might need to access the
    specialized StrokeVertex type. In this case, one should use a
    StrokeVertexIterator. To call functions of the UnaryFuntion0D type,
    a StrokeVertexIterator can be converted to an Interface0DIterator by
    by calling Interface0DIterator(it).

    \_\_init\_\_()[#](#freestyle.types.StrokeVertexIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Creates a [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator") using either the
        default constructor or the copy constructor.

        Parameters:
        :   **brother** ([`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")) – A StrokeVertexIterator object.

    decremented()[#](#freestyle.types.StrokeVertexIterator.decremented "Link to this definition")
    :   Returns a copy of a decremented StrokeVertexIterator.

        Returns:
        :   A StrokeVertexIterator pointing the previous StrokeVertex.

        Return type:
        :   [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")

    incremented()[#](#freestyle.types.StrokeVertexIterator.incremented "Link to this definition")
    :   Returns a copy of an incremented StrokeVertexIterator.

        Returns:
        :   A StrokeVertexIterator pointing the next StrokeVertex.

        Return type:
        :   [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")

    reversed()[#](#freestyle.types.StrokeVertexIterator.reversed "Link to this definition")
    :   Returns a StrokeVertexIterator that traverses stroke vertices in the
        reversed order.

        Returns:
        :   A StrokeVertexIterator traversing stroke vertices backward.

        Return type:
        :   [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator "freestyle.types.StrokeVertexIterator")

    at\_last[#](#freestyle.types.StrokeVertexIterator.at_last "Link to this definition")
    :   True if the iterator points to the last valid element.
        For its counterpart (pointing to the first valid element), use it.is\_begin.

        Type:
        :   bool

    object[#](#freestyle.types.StrokeVertexIterator.object "Link to this definition")
    :   The StrokeVertex object currently pointed to by this iterator.

        Type:
        :   [`StrokeVertex`](#freestyle.types.StrokeVertex "freestyle.types.StrokeVertex")

    t[#](#freestyle.types.StrokeVertexIterator.t "Link to this definition")
    :   The curvilinear abscissa of the current point.

        Type:
        :   float

    u[#](#freestyle.types.StrokeVertexIterator.u "Link to this definition")
    :   The point parameter at the current point in the stroke (0 <= u <= 1).

        Type:
        :   float

*class* freestyle.types.TVertex[#](#freestyle.types.TVertex "Link to this definition")
:   Class hierarchy: [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") > [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex") > [`TVertex`](#freestyle.types.TVertex "freestyle.types.TVertex")

    Class to define a T vertex, i.e. an intersection between two edges.
    It points towards two SVertex and four ViewEdges. Among the
    ViewEdges, two are front and the other two are back. Basically a
    front edge hides part of a back edge. So, among the back edges, one
    is of invisibility N and the other of invisibility N+1.

    \_\_init\_\_()[#](#freestyle.types.TVertex.__init__ "Link to this definition")
    :   Default constructor.

    get\_mate(*viewedge*)[#](#freestyle.types.TVertex.get_mate "Link to this definition")
    :   Returns the mate edge of the ViewEdge given as argument. If the
        ViewEdge is frontEdgeA, frontEdgeB is returned. If the ViewEdge is
        frontEdgeB, frontEdgeA is returned. Same for back edges.

        Parameters:
        :   **viewedge** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) – A ViewEdge object.

        Returns:
        :   The mate edge of the given ViewEdge.

        Return type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    get\_svertex(*fedge*)[#](#freestyle.types.TVertex.get_svertex "Link to this definition")
    :   Returns the SVertex (among the 2) belonging to the given FEdge.

        Parameters:
        :   **fedge** ([`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")) – An FEdge object.

        Returns:
        :   The SVertex belonging to the given FEdge.

        Return type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    back\_svertex[#](#freestyle.types.TVertex.back_svertex "Link to this definition")
    :   The SVertex that is further away from the viewpoint.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    front\_svertex[#](#freestyle.types.TVertex.front_svertex "Link to this definition")
    :   The SVertex that is closer to the viewpoint.

        Type:
        :   [`SVertex`](#freestyle.types.SVertex "freestyle.types.SVertex")

    id[#](#freestyle.types.TVertex.id "Link to this definition")
    :   The Id of this TVertex.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

*class* freestyle.types.UnaryFunction0D[#](#freestyle.types.UnaryFunction0D "Link to this definition")
:   Base class for Unary Functions (functors) working on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator"). A unary function will be used by
    invoking \_\_call\_\_() on an Interface0DIterator. In Python, several
    different subclasses of UnaryFunction0D are used depending on the
    types of functors’ return values. For example, you would inherit from
    a [`UnaryFunction0DDouble`](#freestyle.types.UnaryFunction0DDouble "freestyle.types.UnaryFunction0DDouble") if you wish to define a function that
    returns a double value. Available UnaryFunction0D subclasses are:

    * [`UnaryFunction0DDouble`](#freestyle.types.UnaryFunction0DDouble "freestyle.types.UnaryFunction0DDouble")
    * [`UnaryFunction0DEdgeNature`](#freestyle.types.UnaryFunction0DEdgeNature "freestyle.types.UnaryFunction0DEdgeNature")
    * [`UnaryFunction0DFloat`](#freestyle.types.UnaryFunction0DFloat "freestyle.types.UnaryFunction0DFloat")
    * [`UnaryFunction0DId`](#freestyle.types.UnaryFunction0DId "freestyle.types.UnaryFunction0DId")
    * [`UnaryFunction0DMaterial`](#freestyle.types.UnaryFunction0DMaterial "freestyle.types.UnaryFunction0DMaterial")
    * [`UnaryFunction0DUnsigned`](#freestyle.types.UnaryFunction0DUnsigned "freestyle.types.UnaryFunction0DUnsigned")
    * [`UnaryFunction0DVec2f`](#freestyle.types.UnaryFunction0DVec2f "freestyle.types.UnaryFunction0DVec2f")
    * [`UnaryFunction0DVec3f`](#freestyle.types.UnaryFunction0DVec3f "freestyle.types.UnaryFunction0DVec3f")
    * [`UnaryFunction0DVectorViewShape`](#freestyle.types.UnaryFunction0DVectorViewShape "freestyle.types.UnaryFunction0DVectorViewShape")
    * [`UnaryFunction0DViewShape`](#freestyle.types.UnaryFunction0DViewShape "freestyle.types.UnaryFunction0DViewShape")

    name[#](#freestyle.types.UnaryFunction0D.name "Link to this definition")
    :   The name of the unary 0D function.

        Type:
        :   str

*class* freestyle.types.UnaryFunction0DDouble[#](#freestyle.types.UnaryFunction0DDouble "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DDouble`](#freestyle.types.UnaryFunction0DDouble "freestyle.types.UnaryFunction0DDouble")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a float value.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DDouble.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DEdgeNature[#](#freestyle.types.UnaryFunction0DEdgeNature "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DEdgeNature`](#freestyle.types.UnaryFunction0DEdgeNature "freestyle.types.UnaryFunction0DEdgeNature")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a [`Nature`](#freestyle.types.Nature "freestyle.types.Nature") object.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DEdgeNature.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DFloat[#](#freestyle.types.UnaryFunction0DFloat "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DFloat`](#freestyle.types.UnaryFunction0DFloat "freestyle.types.UnaryFunction0DFloat")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a float value.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DFloat.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DId[#](#freestyle.types.UnaryFunction0DId "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DId`](#freestyle.types.UnaryFunction0DId "freestyle.types.UnaryFunction0DId")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return an [`Id`](#freestyle.types.Id "freestyle.types.Id") object.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DId.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DMaterial[#](#freestyle.types.UnaryFunction0DMaterial "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DMaterial`](#freestyle.types.UnaryFunction0DMaterial "freestyle.types.UnaryFunction0DMaterial")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a [`Material`](#freestyle.types.Material "freestyle.types.Material") object.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DMaterial.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DUnsigned[#](#freestyle.types.UnaryFunction0DUnsigned "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DUnsigned`](#freestyle.types.UnaryFunction0DUnsigned "freestyle.types.UnaryFunction0DUnsigned")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return an int value.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DUnsigned.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DVec2f[#](#freestyle.types.UnaryFunction0DVec2f "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DVec2f`](#freestyle.types.UnaryFunction0DVec2f "freestyle.types.UnaryFunction0DVec2f")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a 2D vector.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DVec2f.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DVec3f[#](#freestyle.types.UnaryFunction0DVec3f "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DVec3f`](#freestyle.types.UnaryFunction0DVec3f "freestyle.types.UnaryFunction0DVec3f")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a 3D vector.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DVec3f.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DVectorViewShape[#](#freestyle.types.UnaryFunction0DVectorViewShape "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DVectorViewShape`](#freestyle.types.UnaryFunction0DVectorViewShape "freestyle.types.UnaryFunction0DVectorViewShape")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a list of [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape")
    objects.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DVectorViewShape.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction0DViewShape[#](#freestyle.types.UnaryFunction0DViewShape "Link to this definition")
:   Class hierarchy: [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D "freestyle.types.UnaryFunction0D") > [`UnaryFunction0DViewShape`](#freestyle.types.UnaryFunction0DViewShape "freestyle.types.UnaryFunction0DViewShape")

    Base class for unary functions (functors) that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator") and return a [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape") object.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction0DViewShape.__init__ "Link to this definition")
    :   Default constructor.

*class* freestyle.types.UnaryFunction1D[#](#freestyle.types.UnaryFunction1D "Link to this definition")
:   Base class for Unary Functions (functors) working on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D"). A unary function will be used by invoking
    \_\_call\_\_() on an Interface1D. In Python, several different subclasses
    of UnaryFunction1D are used depending on the types of functors’ return
    values. For example, you would inherit from a
    [`UnaryFunction1DDouble`](#freestyle.types.UnaryFunction1DDouble "freestyle.types.UnaryFunction1DDouble") if you wish to define a function that
    returns a double value. Available UnaryFunction1D subclasses are:

    * [`UnaryFunction1DDouble`](#freestyle.types.UnaryFunction1DDouble "freestyle.types.UnaryFunction1DDouble")
    * [`UnaryFunction1DEdgeNature`](#freestyle.types.UnaryFunction1DEdgeNature "freestyle.types.UnaryFunction1DEdgeNature")
    * [`UnaryFunction1DFloat`](#freestyle.types.UnaryFunction1DFloat "freestyle.types.UnaryFunction1DFloat")
    * [`UnaryFunction1DUnsigned`](#freestyle.types.UnaryFunction1DUnsigned "freestyle.types.UnaryFunction1DUnsigned")
    * [`UnaryFunction1DVec2f`](#freestyle.types.UnaryFunction1DVec2f "freestyle.types.UnaryFunction1DVec2f")
    * [`UnaryFunction1DVec3f`](#freestyle.types.UnaryFunction1DVec3f "freestyle.types.UnaryFunction1DVec3f")
    * [`UnaryFunction1DVectorViewShape`](#freestyle.types.UnaryFunction1DVectorViewShape "freestyle.types.UnaryFunction1DVectorViewShape")
    * [`UnaryFunction1DVoid`](#freestyle.types.UnaryFunction1DVoid "freestyle.types.UnaryFunction1DVoid")

    name[#](#freestyle.types.UnaryFunction1D.name "Link to this definition")
    :   The name of the unary 1D function.

        Type:
        :   str

*class* freestyle.types.UnaryFunction1DDouble[#](#freestyle.types.UnaryFunction1DDouble "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DDouble`](#freestyle.types.UnaryFunction1DDouble "freestyle.types.UnaryFunction1DDouble")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return a float value.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DDouble.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DDouble.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DEdgeNature[#](#freestyle.types.UnaryFunction1DEdgeNature "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DEdgeNature`](#freestyle.types.UnaryFunction1DEdgeNature "freestyle.types.UnaryFunction1DEdgeNature")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return a [`Nature`](#freestyle.types.Nature "freestyle.types.Nature") object.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DEdgeNature.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DEdgeNature.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DFloat[#](#freestyle.types.UnaryFunction1DFloat "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DFloat`](#freestyle.types.UnaryFunction1DFloat "freestyle.types.UnaryFunction1DFloat")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return a float value.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DFloat.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DFloat.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DUnsigned[#](#freestyle.types.UnaryFunction1DUnsigned "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DUnsigned`](#freestyle.types.UnaryFunction1DUnsigned "freestyle.types.UnaryFunction1DUnsigned")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return an int value.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DUnsigned.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DUnsigned.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DVec2f[#](#freestyle.types.UnaryFunction1DVec2f "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DVec2f`](#freestyle.types.UnaryFunction1DVec2f "freestyle.types.UnaryFunction1DVec2f")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return a 2D vector.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DVec2f.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DVec2f.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DVec3f[#](#freestyle.types.UnaryFunction1DVec3f "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DVec3f`](#freestyle.types.UnaryFunction1DVec3f "freestyle.types.UnaryFunction1DVec3f")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return a 3D vector.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DVec3f.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DVec3f.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DVectorViewShape[#](#freestyle.types.UnaryFunction1DVectorViewShape "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DVectorViewShape`](#freestyle.types.UnaryFunction1DVectorViewShape "freestyle.types.UnaryFunction1DVectorViewShape")

    Base class for unary functions (functors) that work on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") and return a list of [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape")
    objects.

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DVectorViewShape.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using the default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DVectorViewShape.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryFunction1DVoid[#](#freestyle.types.UnaryFunction1DVoid "Link to this definition")
:   Class hierarchy: [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D "freestyle.types.UnaryFunction1D") > [`UnaryFunction1DVoid`](#freestyle.types.UnaryFunction1DVoid "freestyle.types.UnaryFunction1DVoid")

    Base class for unary functions (functors) working on
    [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D").

    \_\_init\_\_()[#](#freestyle.types.UnaryFunction1DVoid.__init__ "Link to this definition")

    \_\_init\_\_(*integration\_type*)
    :   Builds a unary 1D function using either a default constructor
        or the integration method given as an argument.

        Parameters:
        :   **integration\_type** ([`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")) – An integration method.

    integration\_type[#](#freestyle.types.UnaryFunction1DVoid.integration_type "Link to this definition")
    :   The integration method.

        Type:
        :   [`IntegrationType`](#freestyle.types.IntegrationType "freestyle.types.IntegrationType")

*class* freestyle.types.UnaryPredicate0D[#](#freestyle.types.UnaryPredicate0D "Link to this definition")
:   Base class for unary predicates that work on
    [`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator"). A UnaryPredicate0D is a functor that
    evaluates a condition on an Interface0DIterator and returns true or
    false depending on whether this condition is satisfied or not. The
    UnaryPredicate0D is used by invoking its \_\_call\_\_() method. Any
    inherited class must overload the \_\_call\_\_() method.

    \_\_init\_\_()[#](#freestyle.types.UnaryPredicate0D.__init__ "Link to this definition")
    :   Default constructor.

    \_\_call\_\_(*it*)[#](#freestyle.types.UnaryPredicate0D.__call__ "Link to this definition")
    :   Must be overload by inherited classes.

        Parameters:
        :   **it** ([`Interface0DIterator`](#freestyle.types.Interface0DIterator "freestyle.types.Interface0DIterator")) – The Interface0DIterator pointing onto the Interface0D at
            which we wish to evaluate the predicate.

        Returns:
        :   True if the condition is satisfied, false otherwise.

        Return type:
        :   bool

    name[#](#freestyle.types.UnaryPredicate0D.name "Link to this definition")
    :   The name of the unary 0D predicate.

        Type:
        :   str

*class* freestyle.types.UnaryPredicate1D[#](#freestyle.types.UnaryPredicate1D "Link to this definition")
:   Base class for unary predicates that work on [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D"). A
    UnaryPredicate1D is a functor that evaluates a condition on a
    Interface1D and returns true or false depending on whether this
    condition is satisfied or not. The UnaryPredicate1D is used by
    invoking its \_\_call\_\_() method. Any inherited class must overload the
    \_\_call\_\_() method.

    \_\_init\_\_()[#](#freestyle.types.UnaryPredicate1D.__init__ "Link to this definition")
    :   Default constructor.

    \_\_call\_\_(*inter*)[#](#freestyle.types.UnaryPredicate1D.__call__ "Link to this definition")
    :   Must be overload by inherited classes.

        Parameters:
        :   **inter** ([`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D")) – The Interface1D on which we wish to evaluate the predicate.

        Returns:
        :   True if the condition is satisfied, false otherwise.

        Return type:
        :   bool

    name[#](#freestyle.types.UnaryPredicate1D.name "Link to this definition")
    :   The name of the unary 1D predicate.

        Type:
        :   str

*class* freestyle.types.ViewEdge[#](#freestyle.types.ViewEdge "Link to this definition")
:   Class hierarchy: [`Interface1D`](#freestyle.types.Interface1D "freestyle.types.Interface1D") > [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    Class defining a ViewEdge. A ViewEdge in an edge of the image graph.
    it connects two [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex") objects. It is made by connecting
    a set of FEdges.

    \_\_init\_\_()[#](#freestyle.types.ViewEdge.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Builds a [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge") using the default constructor or the copy constructor.

        Parameters:
        :   **brother** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) – A ViewEdge object.

    update\_fedges()[#](#freestyle.types.ViewEdge.update_fedges "Link to this definition")
    :   Sets Viewedge to this for all embedded fedges.

    chaining\_time\_stamp[#](#freestyle.types.ViewEdge.chaining_time_stamp "Link to this definition")
    :   The time stamp of this ViewEdge.

        Type:
        :   int

    first\_fedge[#](#freestyle.types.ViewEdge.first_fedge "Link to this definition")
    :   The first FEdge that constitutes this ViewEdge.

        Type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    first\_viewvertex[#](#freestyle.types.ViewEdge.first_viewvertex "Link to this definition")
    :   The first ViewVertex.

        Type:
        :   [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")

    id[#](#freestyle.types.ViewEdge.id "Link to this definition")
    :   The Id of this ViewEdge.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    is\_closed[#](#freestyle.types.ViewEdge.is_closed "Link to this definition")
    :   True if this ViewEdge forms a closed loop.

        Type:
        :   bool

    last\_fedge[#](#freestyle.types.ViewEdge.last_fedge "Link to this definition")
    :   The last FEdge that constitutes this ViewEdge.

        Type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    last\_viewvertex[#](#freestyle.types.ViewEdge.last_viewvertex "Link to this definition")
    :   The second ViewVertex.

        Type:
        :   [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")

    nature[#](#freestyle.types.ViewEdge.nature "Link to this definition")
    :   The nature of this ViewEdge.

        Type:
        :   [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

    occludee[#](#freestyle.types.ViewEdge.occludee "Link to this definition")
    :   The shape that is occluded by the ViewShape to which this ViewEdge
        belongs to. If no object is occluded, this property is set to None.

        Type:
        :   [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape")

    qi[#](#freestyle.types.ViewEdge.qi "Link to this definition")
    :   The quantitative invisibility.

        Type:
        :   int

    viewshape[#](#freestyle.types.ViewEdge.viewshape "Link to this definition")
    :   The ViewShape to which this ViewEdge belongs to.

        Type:
        :   [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape")

*class* freestyle.types.ViewEdgeIterator[#](#freestyle.types.ViewEdgeIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`ViewEdgeIterator`](#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator")

    Base class for iterators over ViewEdges of the [`ViewMap`](#freestyle.types.ViewMap "freestyle.types.ViewMap") Graph.
    Basically the increment() operator of this class should be able to
    take the decision of “where” (on which ViewEdge) to go when pointing
    on a given ViewEdge.

    \_\_init\_\_(*begin=None*, *orientation=True*)[#](#freestyle.types.ViewEdgeIterator.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)
    :   Builds a ViewEdgeIterator from a starting ViewEdge and its
        orientation or the copy constructor.

        Parameters:
        :   * **begin** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge") or None) – The ViewEdge from where to start the iteration.
            * **orientation** (*bool*) – If true, we’ll look for the next ViewEdge among
              the ViewEdges that surround the ending ViewVertex of begin. If
              false, we’ll search over the ViewEdges surrounding the ending
              ViewVertex of begin.
            * **brother** ([`ViewEdgeIterator`](#freestyle.types.ViewEdgeIterator "freestyle.types.ViewEdgeIterator")) – A ViewEdgeIterator object.

    change\_orientation()[#](#freestyle.types.ViewEdgeIterator.change_orientation "Link to this definition")
    :   Changes the current orientation.

    begin[#](#freestyle.types.ViewEdgeIterator.begin "Link to this definition")
    :   The first ViewEdge used for the iteration.

        Type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    current\_edge[#](#freestyle.types.ViewEdgeIterator.current_edge "Link to this definition")
    :   The ViewEdge object currently pointed by this iterator.

        Type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    object[#](#freestyle.types.ViewEdgeIterator.object "Link to this definition")
    :   The ViewEdge object currently pointed by this iterator.

        Type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    orientation[#](#freestyle.types.ViewEdgeIterator.orientation "Link to this definition")
    :   The orientation of the pointed ViewEdge in the iteration.
        If true, the iterator looks for the next ViewEdge among those ViewEdges
        that surround the ending ViewVertex of the “begin” ViewEdge. If false,
        the iterator searches over the ViewEdges surrounding the ending ViewVertex
        of the “begin” ViewEdge.

        Type:
        :   bool

*class* freestyle.types.ViewMap[#](#freestyle.types.ViewMap "Link to this definition")
:   Class defining the ViewMap.

    \_\_init\_\_()[#](#freestyle.types.ViewMap.__init__ "Link to this definition")
    :   Default constructor.

    get\_closest\_fedge(*x*, *y*)[#](#freestyle.types.ViewMap.get_closest_fedge "Link to this definition")
    :   Gets the FEdge nearest to the 2D point specified as arguments.

        Parameters:
        :   * **x** (*float*) – X coordinate of a 2D point.
            * **y** (*float*) – Y coordinate of a 2D point.

        Returns:
        :   The FEdge nearest to the specified 2D point.

        Return type:
        :   [`FEdge`](#freestyle.types.FEdge "freestyle.types.FEdge")

    get\_closest\_viewedge(*x*, *y*)[#](#freestyle.types.ViewMap.get_closest_viewedge "Link to this definition")
    :   Gets the ViewEdge nearest to the 2D point specified as arguments.

        Parameters:
        :   * **x** (*float*) – X coordinate of a 2D point.
            * **y** (*float*) – Y coordinate of a 2D point.

        Returns:
        :   The ViewEdge nearest to the specified 2D point.

        Return type:
        :   [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")

    scene\_bbox[#](#freestyle.types.ViewMap.scene_bbox "Link to this definition")
    :   The 3D bounding box of the scene.

        Type:
        :   [`BBox`](#freestyle.types.BBox "freestyle.types.BBox")

*class* freestyle.types.ViewShape[#](#freestyle.types.ViewShape "Link to this definition")
:   Class gathering the elements of the ViewMap (i.e., [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")
    and [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) that are issued from the same input shape.

    \_\_init\_\_()[#](#freestyle.types.ViewShape.__init__ "Link to this definition")

    \_\_init\_\_(*brother*)

    \_\_init\_\_(*sshape*)
    :   Builds a [`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape") using the default constructor,
        copy constructor, or from a [`SShape`](#freestyle.types.SShape "freestyle.types.SShape").

        Parameters:
        :   * **brother** ([`ViewShape`](#freestyle.types.ViewShape "freestyle.types.ViewShape")) – A ViewShape object.
            * **sshape** ([`SShape`](#freestyle.types.SShape "freestyle.types.SShape")) – An SShape object.

    add\_edge(*edge*)[#](#freestyle.types.ViewShape.add_edge "Link to this definition")
    :   Adds a ViewEdge to the list of ViewEdge objects.

        Parameters:
        :   **edge** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) – A ViewEdge object.

    add\_vertex(*vertex*)[#](#freestyle.types.ViewShape.add_vertex "Link to this definition")
    :   Adds a ViewVertex to the list of the ViewVertex objects.

        Parameters:
        :   **vertex** ([`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")) – A ViewVertex object.

    edges[#](#freestyle.types.ViewShape.edges "Link to this definition")
    :   The list of ViewEdge objects contained in this ViewShape.

        Type:
        :   List of [`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge") objects

    id[#](#freestyle.types.ViewShape.id "Link to this definition")
    :   The Id of this ViewShape.

        Type:
        :   [`Id`](#freestyle.types.Id "freestyle.types.Id")

    library\_path[#](#freestyle.types.ViewShape.library_path "Link to this definition")
    :   The library path of the ViewShape.

        Type:
        :   str, or None if the ViewShape is not part of a library

    name[#](#freestyle.types.ViewShape.name "Link to this definition")
    :   The name of the ViewShape.

        Type:
        :   str

    sshape[#](#freestyle.types.ViewShape.sshape "Link to this definition")
    :   The SShape on top of which this ViewShape is built.

        Type:
        :   [`SShape`](#freestyle.types.SShape "freestyle.types.SShape")

    vertices[#](#freestyle.types.ViewShape.vertices "Link to this definition")
    :   The list of ViewVertex objects contained in this ViewShape.

        Type:
        :   List of [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex") objects

*class* freestyle.types.ViewVertex[#](#freestyle.types.ViewVertex "Link to this definition")
:   Class hierarchy: [`Interface0D`](#freestyle.types.Interface0D "freestyle.types.Interface0D") > [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex")

    Class to define a view vertex. A view vertex is a feature vertex
    corresponding to a point of the image graph, where the characteristics
    of an edge (e.g., nature and visibility) might change. A
    [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex") can be of two kinds: A [`TVertex`](#freestyle.types.TVertex "freestyle.types.TVertex") when it
    corresponds to the intersection between two ViewEdges or a
    [`NonTVertex`](#freestyle.types.NonTVertex "freestyle.types.NonTVertex") when it corresponds to a vertex of the initial
    input mesh (it is the case for vertices such as corners for example).
    Thus, this class can be specialized into two classes, the
    [`TVertex`](#freestyle.types.TVertex "freestyle.types.TVertex") class and the [`NonTVertex`](#freestyle.types.NonTVertex "freestyle.types.NonTVertex") class.

    edges\_begin()[#](#freestyle.types.ViewVertex.edges_begin "Link to this definition")
    :   Returns an iterator over the ViewEdges that goes to or comes from
        this ViewVertex pointing to the first ViewEdge of the list. The
        orientedViewEdgeIterator allows to iterate in CCW order over these
        ViewEdges and to get the orientation for each ViewEdge
        (incoming/outgoing).

        Returns:
        :   An orientedViewEdgeIterator pointing to the first ViewEdge.

        Return type:
        :   [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator")

    edges\_end()[#](#freestyle.types.ViewVertex.edges_end "Link to this definition")
    :   Returns an orientedViewEdgeIterator over the ViewEdges around this
        ViewVertex, pointing after the last ViewEdge.

        Returns:
        :   An orientedViewEdgeIterator pointing after the last ViewEdge.

        Return type:
        :   [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator")

    edges\_iterator(*edge*)[#](#freestyle.types.ViewVertex.edges_iterator "Link to this definition")
    :   Returns an orientedViewEdgeIterator pointing to the ViewEdge given
        as argument.

        Parameters:
        :   **edge** ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge")) – A ViewEdge object.

        Returns:
        :   An orientedViewEdgeIterator pointing to the given ViewEdge.

        Return type:
        :   [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator")

    nature[#](#freestyle.types.ViewVertex.nature "Link to this definition")
    :   The nature of this ViewVertex.

        Type:
        :   [`Nature`](#freestyle.types.Nature "freestyle.types.Nature")

*class* freestyle.types.orientedViewEdgeIterator[#](#freestyle.types.orientedViewEdgeIterator "Link to this definition")
:   Class hierarchy: [`Iterator`](#freestyle.types.Iterator "freestyle.types.Iterator") > [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator")

    Class representing an iterator over oriented ViewEdges around a
    [`ViewVertex`](#freestyle.types.ViewVertex "freestyle.types.ViewVertex"). This iterator allows a CCW iteration (in the image
    plane). An instance of an orientedViewEdgeIterator can only be
    obtained from a ViewVertex by calling edges\_begin() or edges\_end().

    \_\_init\_\_()[#](#freestyle.types.orientedViewEdgeIterator.__init__ "Link to this definition")

    \_\_init\_\_(*iBrother*)
    :   Creates an [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator") using either the
        default constructor or the copy constructor.

        Parameters:
        :   **iBrother** ([`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator "freestyle.types.orientedViewEdgeIterator")) – An orientedViewEdgeIterator object.

    object[#](#freestyle.types.orientedViewEdgeIterator.object "Link to this definition")
    :   The oriented ViewEdge (i.e., a tuple of the pointed ViewEdge and a boolean
        value) currently pointed to by this iterator. If the boolean value is true,
        the ViewEdge is incoming.

        Type:
        :   ([`ViewEdge`](#freestyle.types.ViewEdge "freestyle.types.ViewEdge"), bool)

[Next

Freestyle Predicates (freestyle.predicates)](../predicates/index.md)
[Previous

Freestyle Module (freestyle)](../../../meta/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60freestyle.types.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Ffreestyle.types.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Freestyle Types (freestyle.types)
  + [`AdjacencyIterator`](#freestyle.types.AdjacencyIterator)
    - [`AdjacencyIterator.__init__()`](#freestyle.types.AdjacencyIterator.__init__)
    - [`AdjacencyIterator.is_incoming`](#freestyle.types.AdjacencyIterator.is_incoming)
    - [`AdjacencyIterator.object`](#freestyle.types.AdjacencyIterator.object)
  + [`BBox`](#freestyle.types.BBox)
    - [`BBox.__init__()`](#freestyle.types.BBox.__init__)
  + [`BinaryPredicate0D`](#freestyle.types.BinaryPredicate0D)
    - [`BinaryPredicate0D.__init__()`](#freestyle.types.BinaryPredicate0D.__init__)
    - [`BinaryPredicate0D.__call__()`](#freestyle.types.BinaryPredicate0D.__call__)
    - [`BinaryPredicate0D.name`](#freestyle.types.BinaryPredicate0D.name)
  + [`BinaryPredicate1D`](#freestyle.types.BinaryPredicate1D)
    - [`BinaryPredicate1D.__init__()`](#freestyle.types.BinaryPredicate1D.__init__)
    - [`BinaryPredicate1D.__call__()`](#freestyle.types.BinaryPredicate1D.__call__)
    - [`BinaryPredicate1D.name`](#freestyle.types.BinaryPredicate1D.name)
  + [`Chain`](#freestyle.types.Chain)
    - [`Chain.__init__()`](#freestyle.types.Chain.__init__)
    - [`Chain.push_viewedge_back()`](#freestyle.types.Chain.push_viewedge_back)
    - [`Chain.push_viewedge_front()`](#freestyle.types.Chain.push_viewedge_front)
  + [`ChainingIterator`](#freestyle.types.ChainingIterator)
    - [`ChainingIterator.__init__()`](#freestyle.types.ChainingIterator.__init__)
    - [`ChainingIterator.init()`](#freestyle.types.ChainingIterator.init)
    - [`ChainingIterator.traverse()`](#freestyle.types.ChainingIterator.traverse)
    - [`ChainingIterator.is_incrementing`](#freestyle.types.ChainingIterator.is_incrementing)
    - [`ChainingIterator.next_vertex`](#freestyle.types.ChainingIterator.next_vertex)
    - [`ChainingIterator.object`](#freestyle.types.ChainingIterator.object)
  + [`Curve`](#freestyle.types.Curve)
    - [`Curve.__init__()`](#freestyle.types.Curve.__init__)
    - [`Curve.push_vertex_back()`](#freestyle.types.Curve.push_vertex_back)
    - [`Curve.push_vertex_front()`](#freestyle.types.Curve.push_vertex_front)
    - [`Curve.is_empty`](#freestyle.types.Curve.is_empty)
    - [`Curve.segments_size`](#freestyle.types.Curve.segments_size)
  + [`CurvePoint`](#freestyle.types.CurvePoint)
    - [`CurvePoint.__init__()`](#freestyle.types.CurvePoint.__init__)
    - [`CurvePoint.fedge`](#freestyle.types.CurvePoint.fedge)
    - [`CurvePoint.first_svertex`](#freestyle.types.CurvePoint.first_svertex)
    - [`CurvePoint.second_svertex`](#freestyle.types.CurvePoint.second_svertex)
    - [`CurvePoint.t2d`](#freestyle.types.CurvePoint.t2d)
  + [`CurvePointIterator`](#freestyle.types.CurvePointIterator)
    - [`CurvePointIterator.__init__()`](#freestyle.types.CurvePointIterator.__init__)
    - [`CurvePointIterator.object`](#freestyle.types.CurvePointIterator.object)
    - [`CurvePointIterator.t`](#freestyle.types.CurvePointIterator.t)
    - [`CurvePointIterator.u`](#freestyle.types.CurvePointIterator.u)
  + [`FEdge`](#freestyle.types.FEdge)
    - [`FEdge.FEdge()`](#freestyle.types.FEdge.FEdge)
    - [`FEdge.first_svertex`](#freestyle.types.FEdge.first_svertex)
    - [`FEdge.id`](#freestyle.types.FEdge.id)
    - [`FEdge.is_smooth`](#freestyle.types.FEdge.is_smooth)
    - [`FEdge.nature`](#freestyle.types.FEdge.nature)
    - [`FEdge.next_fedge`](#freestyle.types.FEdge.next_fedge)
    - [`FEdge.previous_fedge`](#freestyle.types.FEdge.previous_fedge)
    - [`FEdge.second_svertex`](#freestyle.types.FEdge.second_svertex)
    - [`FEdge.viewedge`](#freestyle.types.FEdge.viewedge)
  + [`FEdgeSharp`](#freestyle.types.FEdgeSharp)
    - [`FEdgeSharp.__init__()`](#freestyle.types.FEdgeSharp.__init__)
    - [`FEdgeSharp.face_mark_left`](#freestyle.types.FEdgeSharp.face_mark_left)
    - [`FEdgeSharp.face_mark_right`](#freestyle.types.FEdgeSharp.face_mark_right)
    - [`FEdgeSharp.material_index_left`](#freestyle.types.FEdgeSharp.material_index_left)
    - [`FEdgeSharp.material_index_right`](#freestyle.types.FEdgeSharp.material_index_right)
    - [`FEdgeSharp.material_left`](#freestyle.types.FEdgeSharp.material_left)
    - [`FEdgeSharp.material_right`](#freestyle.types.FEdgeSharp.material_right)
    - [`FEdgeSharp.normal_left`](#freestyle.types.FEdgeSharp.normal_left)
    - [`FEdgeSharp.normal_right`](#freestyle.types.FEdgeSharp.normal_right)
  + [`FEdgeSmooth`](#freestyle.types.FEdgeSmooth)
    - [`FEdgeSmooth.__init__()`](#freestyle.types.FEdgeSmooth.__init__)
    - [`FEdgeSmooth.face_mark`](#freestyle.types.FEdgeSmooth.face_mark)
    - [`FEdgeSmooth.material`](#freestyle.types.FEdgeSmooth.material)
    - [`FEdgeSmooth.material_index`](#freestyle.types.FEdgeSmooth.material_index)
    - [`FEdgeSmooth.normal`](#freestyle.types.FEdgeSmooth.normal)
  + [`Id`](#freestyle.types.Id)
    - [`Id.__init__()`](#freestyle.types.Id.__init__)
    - [`Id.first`](#freestyle.types.Id.first)
    - [`Id.second`](#freestyle.types.Id.second)
  + [`IntegrationType`](#freestyle.types.IntegrationType)
  + [`Interface0D`](#freestyle.types.Interface0D)
    - [`Interface0D.__init__()`](#freestyle.types.Interface0D.__init__)
    - [`Interface0D.get_fedge()`](#freestyle.types.Interface0D.get_fedge)
    - [`Interface0D.id`](#freestyle.types.Interface0D.id)
    - [`Interface0D.name`](#freestyle.types.Interface0D.name)
    - [`Interface0D.nature`](#freestyle.types.Interface0D.nature)
    - [`Interface0D.point_2d`](#freestyle.types.Interface0D.point_2d)
    - [`Interface0D.point_3d`](#freestyle.types.Interface0D.point_3d)
    - [`Interface0D.projected_x`](#freestyle.types.Interface0D.projected_x)
    - [`Interface0D.projected_y`](#freestyle.types.Interface0D.projected_y)
    - [`Interface0D.projected_z`](#freestyle.types.Interface0D.projected_z)
  + [`Interface0DIterator`](#freestyle.types.Interface0DIterator)
    - [`Interface0DIterator.__init__()`](#freestyle.types.Interface0DIterator.__init__)
    - [`Interface0DIterator.at_last`](#freestyle.types.Interface0DIterator.at_last)
    - [`Interface0DIterator.object`](#freestyle.types.Interface0DIterator.object)
    - [`Interface0DIterator.t`](#freestyle.types.Interface0DIterator.t)
    - [`Interface0DIterator.u`](#freestyle.types.Interface0DIterator.u)
  + [`Interface1D`](#freestyle.types.Interface1D)
    - [`Interface1D.__init__()`](#freestyle.types.Interface1D.__init__)
    - [`Interface1D.points_begin()`](#freestyle.types.Interface1D.points_begin)
    - [`Interface1D.points_end()`](#freestyle.types.Interface1D.points_end)
    - [`Interface1D.vertices_begin()`](#freestyle.types.Interface1D.vertices_begin)
    - [`Interface1D.vertices_end()`](#freestyle.types.Interface1D.vertices_end)
    - [`Interface1D.id`](#freestyle.types.Interface1D.id)
    - [`Interface1D.length_2d`](#freestyle.types.Interface1D.length_2d)
    - [`Interface1D.name`](#freestyle.types.Interface1D.name)
    - [`Interface1D.nature`](#freestyle.types.Interface1D.nature)
    - [`Interface1D.time_stamp`](#freestyle.types.Interface1D.time_stamp)
  + [`Iterator`](#freestyle.types.Iterator)
    - [`Iterator.__init__()`](#freestyle.types.Iterator.__init__)
    - [`Iterator.decrement()`](#freestyle.types.Iterator.decrement)
    - [`Iterator.increment()`](#freestyle.types.Iterator.increment)
    - [`Iterator.is_begin`](#freestyle.types.Iterator.is_begin)
    - [`Iterator.is_end`](#freestyle.types.Iterator.is_end)
    - [`Iterator.name`](#freestyle.types.Iterator.name)
  + [`Material`](#freestyle.types.Material)
    - [`Material.__init__()`](#freestyle.types.Material.__init__)
    - [`Material.ambient`](#freestyle.types.Material.ambient)
    - [`Material.diffuse`](#freestyle.types.Material.diffuse)
    - [`Material.emission`](#freestyle.types.Material.emission)
    - [`Material.line`](#freestyle.types.Material.line)
    - [`Material.priority`](#freestyle.types.Material.priority)
    - [`Material.shininess`](#freestyle.types.Material.shininess)
    - [`Material.specular`](#freestyle.types.Material.specular)
  + [`MediumType`](#freestyle.types.MediumType)
  + [`Nature`](#freestyle.types.Nature)
  + [`Noise`](#freestyle.types.Noise)
    - [`Noise.__init__()`](#freestyle.types.Noise.__init__)
    - [`Noise.smoothNoise1()`](#freestyle.types.Noise.smoothNoise1)
    - [`Noise.smoothNoise2()`](#freestyle.types.Noise.smoothNoise2)
    - [`Noise.smoothNoise3()`](#freestyle.types.Noise.smoothNoise3)
    - [`Noise.turbulence1()`](#freestyle.types.Noise.turbulence1)
    - [`Noise.turbulence2()`](#freestyle.types.Noise.turbulence2)
    - [`Noise.turbulence3()`](#freestyle.types.Noise.turbulence3)
  + [`NonTVertex`](#freestyle.types.NonTVertex)
    - [`NonTVertex.__init__()`](#freestyle.types.NonTVertex.__init__)
    - [`NonTVertex.svertex`](#freestyle.types.NonTVertex.svertex)
  + [`Operators`](#freestyle.types.Operators)
    - [`Operators.bidirectional_chain()`](#freestyle.types.Operators.bidirectional_chain)
    - [`Operators.chain()`](#freestyle.types.Operators.chain)
    - [`Operators.create()`](#freestyle.types.Operators.create)
    - [`Operators.get_chain_from_index()`](#freestyle.types.Operators.get_chain_from_index)
    - [`Operators.get_chains_size()`](#freestyle.types.Operators.get_chains_size)
    - [`Operators.get_stroke_from_index()`](#freestyle.types.Operators.get_stroke_from_index)
    - [`Operators.get_strokes_size()`](#freestyle.types.Operators.get_strokes_size)
    - [`Operators.get_view_edges_size()`](#freestyle.types.Operators.get_view_edges_size)
    - [`Operators.get_viewedge_from_index()`](#freestyle.types.Operators.get_viewedge_from_index)
    - [`Operators.recursive_split()`](#freestyle.types.Operators.recursive_split)
    - [`Operators.reset()`](#freestyle.types.Operators.reset)
    - [`Operators.select()`](#freestyle.types.Operators.select)
    - [`Operators.sequential_split()`](#freestyle.types.Operators.sequential_split)
    - [`Operators.sort()`](#freestyle.types.Operators.sort)
  + [`SShape`](#freestyle.types.SShape)
    - [`SShape.__init__()`](#freestyle.types.SShape.__init__)
    - [`SShape.add_edge()`](#freestyle.types.SShape.add_edge)
    - [`SShape.add_vertex()`](#freestyle.types.SShape.add_vertex)
    - [`SShape.compute_bbox()`](#freestyle.types.SShape.compute_bbox)
    - [`SShape.bbox`](#freestyle.types.SShape.bbox)
    - [`SShape.edges`](#freestyle.types.SShape.edges)
    - [`SShape.id`](#freestyle.types.SShape.id)
    - [`SShape.name`](#freestyle.types.SShape.name)
    - [`SShape.vertices`](#freestyle.types.SShape.vertices)
  + [`SVertex`](#freestyle.types.SVertex)
    - [`SVertex.__init__()`](#freestyle.types.SVertex.__init__)
    - [`SVertex.add_fedge()`](#freestyle.types.SVertex.add_fedge)
    - [`SVertex.add_normal()`](#freestyle.types.SVertex.add_normal)
    - [`SVertex.curvatures`](#freestyle.types.SVertex.curvatures)
    - [`SVertex.id`](#freestyle.types.SVertex.id)
    - [`SVertex.normals`](#freestyle.types.SVertex.normals)
    - [`SVertex.normals_size`](#freestyle.types.SVertex.normals_size)
    - [`SVertex.point_2d`](#freestyle.types.SVertex.point_2d)
    - [`SVertex.point_3d`](#freestyle.types.SVertex.point_3d)
    - [`SVertex.viewvertex`](#freestyle.types.SVertex.viewvertex)
  + [`SVertexIterator`](#freestyle.types.SVertexIterator)
    - [`SVertexIterator.__init__()`](#freestyle.types.SVertexIterator.__init__)
    - [`SVertexIterator.object`](#freestyle.types.SVertexIterator.object)
    - [`SVertexIterator.t`](#freestyle.types.SVertexIterator.t)
    - [`SVertexIterator.u`](#freestyle.types.SVertexIterator.u)
  + [`Stroke`](#freestyle.types.Stroke)
    - [`Stroke.Stroke()`](#freestyle.types.Stroke.Stroke)
    - [`Stroke.compute_sampling()`](#freestyle.types.Stroke.compute_sampling)
    - [`Stroke.insert_vertex()`](#freestyle.types.Stroke.insert_vertex)
    - [`Stroke.remove_all_vertices()`](#freestyle.types.Stroke.remove_all_vertices)
    - [`Stroke.remove_vertex()`](#freestyle.types.Stroke.remove_vertex)
    - [`Stroke.resample()`](#freestyle.types.Stroke.resample)
    - [`Stroke.stroke_vertices_begin()`](#freestyle.types.Stroke.stroke_vertices_begin)
    - [`Stroke.stroke_vertices_end()`](#freestyle.types.Stroke.stroke_vertices_end)
    - [`Stroke.stroke_vertices_size()`](#freestyle.types.Stroke.stroke_vertices_size)
    - [`Stroke.update_length()`](#freestyle.types.Stroke.update_length)
    - [`Stroke.id`](#freestyle.types.Stroke.id)
    - [`Stroke.length_2d`](#freestyle.types.Stroke.length_2d)
    - [`Stroke.medium_type`](#freestyle.types.Stroke.medium_type)
    - [`Stroke.texture_id`](#freestyle.types.Stroke.texture_id)
    - [`Stroke.tips`](#freestyle.types.Stroke.tips)
  + [`StrokeAttribute`](#freestyle.types.StrokeAttribute)
    - [`StrokeAttribute.__init__()`](#freestyle.types.StrokeAttribute.__init__)
    - [`StrokeAttribute.get_attribute_real()`](#freestyle.types.StrokeAttribute.get_attribute_real)
    - [`StrokeAttribute.get_attribute_vec2()`](#freestyle.types.StrokeAttribute.get_attribute_vec2)
    - [`StrokeAttribute.get_attribute_vec3()`](#freestyle.types.StrokeAttribute.get_attribute_vec3)
    - [`StrokeAttribute.has_attribute_real()`](#freestyle.types.StrokeAttribute.has_attribute_real)
    - [`StrokeAttribute.has_attribute_vec2()`](#freestyle.types.StrokeAttribute.has_attribute_vec2)
    - [`StrokeAttribute.has_attribute_vec3()`](#freestyle.types.StrokeAttribute.has_attribute_vec3)
    - [`StrokeAttribute.set_attribute_real()`](#freestyle.types.StrokeAttribute.set_attribute_real)
    - [`StrokeAttribute.set_attribute_vec2()`](#freestyle.types.StrokeAttribute.set_attribute_vec2)
    - [`StrokeAttribute.set_attribute_vec3()`](#freestyle.types.StrokeAttribute.set_attribute_vec3)
    - [`StrokeAttribute.alpha`](#freestyle.types.StrokeAttribute.alpha)
    - [`StrokeAttribute.color`](#freestyle.types.StrokeAttribute.color)
    - [`StrokeAttribute.thickness`](#freestyle.types.StrokeAttribute.thickness)
    - [`StrokeAttribute.visible`](#freestyle.types.StrokeAttribute.visible)
  + [`StrokeShader`](#freestyle.types.StrokeShader)
    - [`StrokeShader.__init__()`](#freestyle.types.StrokeShader.__init__)
    - [`StrokeShader.shade()`](#freestyle.types.StrokeShader.shade)
    - [`StrokeShader.name`](#freestyle.types.StrokeShader.name)
  + [`StrokeVertex`](#freestyle.types.StrokeVertex)
    - [`StrokeVertex.__init__()`](#freestyle.types.StrokeVertex.__init__)
    - [`StrokeVertex.attribute`](#freestyle.types.StrokeVertex.attribute)
    - [`StrokeVertex.curvilinear_abscissa`](#freestyle.types.StrokeVertex.curvilinear_abscissa)
    - [`StrokeVertex.point`](#freestyle.types.StrokeVertex.point)
    - [`StrokeVertex.stroke_length`](#freestyle.types.StrokeVertex.stroke_length)
    - [`StrokeVertex.u`](#freestyle.types.StrokeVertex.u)
  + [`StrokeVertexIterator`](#freestyle.types.StrokeVertexIterator)
    - [`StrokeVertexIterator.__init__()`](#freestyle.types.StrokeVertexIterator.__init__)
    - [`StrokeVertexIterator.decremented()`](#freestyle.types.StrokeVertexIterator.decremented)
    - [`StrokeVertexIterator.incremented()`](#freestyle.types.StrokeVertexIterator.incremented)
    - [`StrokeVertexIterator.reversed()`](#freestyle.types.StrokeVertexIterator.reversed)
    - [`StrokeVertexIterator.at_last`](#freestyle.types.StrokeVertexIterator.at_last)
    - [`StrokeVertexIterator.object`](#freestyle.types.StrokeVertexIterator.object)
    - [`StrokeVertexIterator.t`](#freestyle.types.StrokeVertexIterator.t)
    - [`StrokeVertexIterator.u`](#freestyle.types.StrokeVertexIterator.u)
  + [`TVertex`](#freestyle.types.TVertex)
    - [`TVertex.__init__()`](#freestyle.types.TVertex.__init__)
    - [`TVertex.get_mate()`](#freestyle.types.TVertex.get_mate)
    - [`TVertex.get_svertex()`](#freestyle.types.TVertex.get_svertex)
    - [`TVertex.back_svertex`](#freestyle.types.TVertex.back_svertex)
    - [`TVertex.front_svertex`](#freestyle.types.TVertex.front_svertex)
    - [`TVertex.id`](#freestyle.types.TVertex.id)
  + [`UnaryFunction0D`](#freestyle.types.UnaryFunction0D)
    - [`UnaryFunction0D.name`](#freestyle.types.UnaryFunction0D.name)
  + [`UnaryFunction0DDouble`](#freestyle.types.UnaryFunction0DDouble)
    - [`UnaryFunction0DDouble.__init__()`](#freestyle.types.UnaryFunction0DDouble.__init__)
  + [`UnaryFunction0DEdgeNature`](#freestyle.types.UnaryFunction0DEdgeNature)
    - [`UnaryFunction0DEdgeNature.__init__()`](#freestyle.types.UnaryFunction0DEdgeNature.__init__)
  + [`UnaryFunction0DFloat`](#freestyle.types.UnaryFunction0DFloat)
    - [`UnaryFunction0DFloat.__init__()`](#freestyle.types.UnaryFunction0DFloat.__init__)
  + [`UnaryFunction0DId`](#freestyle.types.UnaryFunction0DId)
    - [`UnaryFunction0DId.__init__()`](#freestyle.types.UnaryFunction0DId.__init__)
  + [`UnaryFunction0DMaterial`](#freestyle.types.UnaryFunction0DMaterial)
    - [`UnaryFunction0DMaterial.__init__()`](#freestyle.types.UnaryFunction0DMaterial.__init__)
  + [`UnaryFunction0DUnsigned`](#freestyle.types.UnaryFunction0DUnsigned)
    - [`UnaryFunction0DUnsigned.__init__()`](#freestyle.types.UnaryFunction0DUnsigned.__init__)
  + [`UnaryFunction0DVec2f`](#freestyle.types.UnaryFunction0DVec2f)
    - [`UnaryFunction0DVec2f.__init__()`](#freestyle.types.UnaryFunction0DVec2f.__init__)
  + [`UnaryFunction0DVec3f`](#freestyle.types.UnaryFunction0DVec3f)
    - [`UnaryFunction0DVec3f.__init__()`](#freestyle.types.UnaryFunction0DVec3f.__init__)
  + [`UnaryFunction0DVectorViewShape`](#freestyle.types.UnaryFunction0DVectorViewShape)
    - [`UnaryFunction0DVectorViewShape.__init__()`](#freestyle.types.UnaryFunction0DVectorViewShape.__init__)
  + [`UnaryFunction0DViewShape`](#freestyle.types.UnaryFunction0DViewShape)
    - [`UnaryFunction0DViewShape.__init__()`](#freestyle.types.UnaryFunction0DViewShape.__init__)
  + [`UnaryFunction1D`](#freestyle.types.UnaryFunction1D)
    - [`UnaryFunction1D.name`](#freestyle.types.UnaryFunction1D.name)
  + [`UnaryFunction1DDouble`](#freestyle.types.UnaryFunction1DDouble)
    - [`UnaryFunction1DDouble.__init__()`](#freestyle.types.UnaryFunction1DDouble.__init__)
    - [`UnaryFunction1DDouble.integration_type`](#freestyle.types.UnaryFunction1DDouble.integration_type)
  + [`UnaryFunction1DEdgeNature`](#freestyle.types.UnaryFunction1DEdgeNature)
    - [`UnaryFunction1DEdgeNature.__init__()`](#freestyle.types.UnaryFunction1DEdgeNature.__init__)
    - [`UnaryFunction1DEdgeNature.integration_type`](#freestyle.types.UnaryFunction1DEdgeNature.integration_type)
  + [`UnaryFunction1DFloat`](#freestyle.types.UnaryFunction1DFloat)
    - [`UnaryFunction1DFloat.__init__()`](#freestyle.types.UnaryFunction1DFloat.__init__)
    - [`UnaryFunction1DFloat.integration_type`](#freestyle.types.UnaryFunction1DFloat.integration_type)
  + [`UnaryFunction1DUnsigned`](#freestyle.types.UnaryFunction1DUnsigned)
    - [`UnaryFunction1DUnsigned.__init__()`](#freestyle.types.UnaryFunction1DUnsigned.__init__)
    - [`UnaryFunction1DUnsigned.integration_type`](#freestyle.types.UnaryFunction1DUnsigned.integration_type)
  + [`UnaryFunction1DVec2f`](#freestyle.types.UnaryFunction1DVec2f)
    - [`UnaryFunction1DVec2f.__init__()`](#freestyle.types.UnaryFunction1DVec2f.__init__)
    - [`UnaryFunction1DVec2f.integration_type`](#freestyle.types.UnaryFunction1DVec2f.integration_type)
  + [`UnaryFunction1DVec3f`](#freestyle.types.UnaryFunction1DVec3f)
    - [`UnaryFunction1DVec3f.__init__()`](#freestyle.types.UnaryFunction1DVec3f.__init__)
    - [`UnaryFunction1DVec3f.integration_type`](#freestyle.types.UnaryFunction1DVec3f.integration_type)
  + [`UnaryFunction1DVectorViewShape`](#freestyle.types.UnaryFunction1DVectorViewShape)
    - [`UnaryFunction1DVectorViewShape.__init__()`](#freestyle.types.UnaryFunction1DVectorViewShape.__init__)
    - [`UnaryFunction1DVectorViewShape.integration_type`](#freestyle.types.UnaryFunction1DVectorViewShape.integration_type)
  + [`UnaryFunction1DVoid`](#freestyle.types.UnaryFunction1DVoid)
    - [`UnaryFunction1DVoid.__init__()`](#freestyle.types.UnaryFunction1DVoid.__init__)
    - [`UnaryFunction1DVoid.integration_type`](#freestyle.types.UnaryFunction1DVoid.integration_type)
  + [`UnaryPredicate0D`](#freestyle.types.UnaryPredicate0D)
    - [`UnaryPredicate0D.__init__()`](#freestyle.types.UnaryPredicate0D.__init__)
    - [`UnaryPredicate0D.__call__()`](#freestyle.types.UnaryPredicate0D.__call__)
    - [`UnaryPredicate0D.name`](#freestyle.types.UnaryPredicate0D.name)
  + [`UnaryPredicate1D`](#freestyle.types.UnaryPredicate1D)
    - [`UnaryPredicate1D.__init__()`](#freestyle.types.UnaryPredicate1D.__init__)
    - [`UnaryPredicate1D.__call__()`](#freestyle.types.UnaryPredicate1D.__call__)
    - [`UnaryPredicate1D.name`](#freestyle.types.UnaryPredicate1D.name)
  + [`ViewEdge`](#freestyle.types.ViewEdge)
    - [`ViewEdge.__init__()`](#freestyle.types.ViewEdge.__init__)
    - [`ViewEdge.update_fedges()`](#freestyle.types.ViewEdge.update_fedges)
    - [`ViewEdge.chaining_time_stamp`](#freestyle.types.ViewEdge.chaining_time_stamp)
    - [`ViewEdge.first_fedge`](#freestyle.types.ViewEdge.first_fedge)
    - [`ViewEdge.first_viewvertex`](#freestyle.types.ViewEdge.first_viewvertex)
    - [`ViewEdge.id`](#freestyle.types.ViewEdge.id)
    - [`ViewEdge.is_closed`](#freestyle.types.ViewEdge.is_closed)
    - [`ViewEdge.last_fedge`](#freestyle.types.ViewEdge.last_fedge)
    - [`ViewEdge.last_viewvertex`](#freestyle.types.ViewEdge.last_viewvertex)
    - [`ViewEdge.nature`](#freestyle.types.ViewEdge.nature)
    - [`ViewEdge.occludee`](#freestyle.types.ViewEdge.occludee)
    - [`ViewEdge.qi`](#freestyle.types.ViewEdge.qi)
    - [`ViewEdge.viewshape`](#freestyle.types.ViewEdge.viewshape)
  + [`ViewEdgeIterator`](#freestyle.types.ViewEdgeIterator)
    - [`ViewEdgeIterator.__init__()`](#freestyle.types.ViewEdgeIterator.__init__)
    - [`ViewEdgeIterator.change_orientation()`](#freestyle.types.ViewEdgeIterator.change_orientation)
    - [`ViewEdgeIterator.begin`](#freestyle.types.ViewEdgeIterator.begin)
    - [`ViewEdgeIterator.current_edge`](#freestyle.types.ViewEdgeIterator.current_edge)
    - [`ViewEdgeIterator.object`](#freestyle.types.ViewEdgeIterator.object)
    - [`ViewEdgeIterator.orientation`](#freestyle.types.ViewEdgeIterator.orientation)
  + [`ViewMap`](#freestyle.types.ViewMap)
    - [`ViewMap.__init__()`](#freestyle.types.ViewMap.__init__)
    - [`ViewMap.get_closest_fedge()`](#freestyle.types.ViewMap.get_closest_fedge)
    - [`ViewMap.get_closest_viewedge()`](#freestyle.types.ViewMap.get_closest_viewedge)
    - [`ViewMap.scene_bbox`](#freestyle.types.ViewMap.scene_bbox)
  + [`ViewShape`](#freestyle.types.ViewShape)
    - [`ViewShape.__init__()`](#freestyle.types.ViewShape.__init__)
    - [`ViewShape.add_edge()`](#freestyle.types.ViewShape.add_edge)
    - [`ViewShape.add_vertex()`](#freestyle.types.ViewShape.add_vertex)
    - [`ViewShape.edges`](#freestyle.types.ViewShape.edges)
    - [`ViewShape.id`](#freestyle.types.ViewShape.id)
    - [`ViewShape.library_path`](#freestyle.types.ViewShape.library_path)
    - [`ViewShape.name`](#freestyle.types.ViewShape.name)
    - [`ViewShape.sshape`](#freestyle.types.ViewShape.sshape)
    - [`ViewShape.vertices`](#freestyle.types.ViewShape.vertices)
  + [`ViewVertex`](#freestyle.types.ViewVertex)
    - [`ViewVertex.edges_begin()`](#freestyle.types.ViewVertex.edges_begin)
    - [`ViewVertex.edges_end()`](#freestyle.types.ViewVertex.edges_end)
    - [`ViewVertex.edges_iterator()`](#freestyle.types.ViewVertex.edges_iterator)
    - [`ViewVertex.nature`](#freestyle.types.ViewVertex.nature)
  + [`orientedViewEdgeIterator`](#freestyle.types.orientedViewEdgeIterator)
    - [`orientedViewEdgeIterator.__init__()`](#freestyle.types.orientedViewEdgeIterator.__init__)
    - [`orientedViewEdgeIterator.object`](#freestyle.types.orientedViewEdgeIterator.object)