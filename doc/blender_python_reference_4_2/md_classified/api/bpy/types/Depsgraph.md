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

# Depsgraph(bpy\_struct)[#](#depsgraph-bpy-struct "Link to this heading")

## Dependency graph: Evaluated ID example[#](#dependency-graph-evaluated-id-example "Link to this heading")

This example demonstrates access to the evaluated ID (such as object, material, etc.) state from
an original ID.
This is needed every time one needs to access state with animation, constraints, and modifiers
taken into account.

```
import bpy

class OBJECT_OT_evaluated_example(bpy.types.Operator):
    """Access evaluated object state and do something with it"""
    bl_label = "DEG Access Evaluated Object"
    bl_idname = "object.evaluated_example"

    def execute(self, context):
        # This is an original object. Its data does not have any modifiers applied.
        obj = context.object
        if obj is None or obj.type != 'MESH':
            self.report({'INFO'}, "No active mesh object to get info from")
            return {'CANCELLED'}
        # Evaluated object exists within a specific dependency graph.
        # We will request evaluated object from the dependency graph which corresponds to the
        # current scene and view layer.
        #
        # NOTE: This call ensure the dependency graph is fully evaluated. This might be expensive
        # if changes were made made to the scene, but is needed to ensure no dangling or incorrect
        # pointers are exposed.
        depsgraph = context.evaluated_depsgraph_get()
        # Actually request evaluated object.
        #
        # This object has animation and drivers applied on it, together with constraints and
        # modifiers.
        #
        # For mesh objects the object.data will be a mesh with all modifiers applied.
        # This means that in access to vertices or faces after modifier stack happens via fields of
        # object_eval.object.
        #
        # For other types of objects the object_eval.data does not have modifiers applied on it,
        # but has animation applied.
        #
        # NOTE: All ID types have `evaluated_get()`, including materials, node trees, worlds.
        object_eval = obj.evaluated_get(depsgraph)
        mesh_eval = object_eval.data
        self.report({'INFO'}, f"Number of evaluated vertices: {len(mesh_eval.vertices)}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_evaluated_example)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_evaluated_example)

if __name__ == "__main__":
    register()
```

## Dependency graph: Original object example[#](#dependency-graph-original-object-example "Link to this heading")

This example demonstrates access to the original ID.
Such access is needed to check whether object is selected, or to compare pointers.

```
import bpy

class OBJECT_OT_original_example(bpy.types.Operator):
    """Access original object and do something with it"""
    bl_label = "DEG Access Original Object"
    bl_idname = "object.original_example"

    def check_object_selected(self, object_eval):
        # Selection depends on a context and is only valid for original objects. This means we need
        # to request the original object from the known evaluated one.
        #
        # NOTE: All ID types have an `original` field.
        obj = object_eval.original
        return obj.select_get()

    def execute(self, context):
        # NOTE: It seems redundant to iterate over original objects to request evaluated ones
        # just to get original back. But we want to keep example as short as possible, but in real
        # world there are cases when evaluated object is coming from a more meaningful source.
        depsgraph = context.evaluated_depsgraph_get()
        for obj in context.editable_objects:
            object_eval = obj.evaluated_get(depsgraph)
            if self.check_object_selected(object_eval):
                self.report({'INFO'}, f"Object is selected: {object_eval.name}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_original_example)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_original_example)

if __name__ == "__main__":
    register()
```

## Dependency graph: Iterate over all object instances[#](#dependency-graph-iterate-over-all-object-instances "Link to this heading")

Sometimes it is needed to know all the instances with their matrices (for example, when writing an
exporter or a custom render engine).
This example shows how to access all objects and instances in the scene.

```
import bpy

class OBJECT_OT_object_instances(bpy.types.Operator):
    """Access original object and do something with it"""
    bl_label = "DEG Iterate Object Instances"
    bl_idname = "object.object_instances"

    def execute(self, context):
        depsgraph = context.evaluated_depsgraph_get()
        for object_instance in depsgraph.object_instances:
            # This is an object which is being instanced.
            obj = object_instance.object
            # `is_instance` denotes whether the object is coming from instances (as an opposite of
            # being an emitting object. )
            if not object_instance.is_instance:
                print(f"Object {obj.name} at {object_instance.matrix_world}")
            else:
                # Instanced will additionally have fields like uv, random_id and others which are
                # specific for instances. See Python API for DepsgraphObjectInstance for details,
                print(f"Instance of {obj.name} at {object_instance.matrix_world}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_object_instances)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_object_instances)

if __name__ == "__main__":
    register()
```

## Dependency graph: Object.to\_mesh()[#](#dependency-graph-object-to-mesh "Link to this heading")

Function to get a mesh from any object with geometry. It is typically used by exporters, render
engines and tools that need to access the evaluated mesh as displayed in the viewport.

Object.to\_mesh() is closely interacting with dependency graph: its behavior depends on whether it
is used on original or evaluated object.

When is used on original object, the result mesh is calculated from the object without taking
animation or modifiers into account:

* For meshes this is similar to duplicating the source mesh.
* For curves this disables own modifiers, and modifiers of objects used as bevel and taper.
* For metaballs this produces an empty mesh since polygonization is done as a modifier evaluation.

When is used on evaluated object all modifiers are taken into account.

Note

The result mesh is owned by the object. It can be freed by calling [`to_mesh_clear()`](Object.md#bpy.types.Object.to_mesh_clear "bpy.types.Object.to_mesh_clear").

Note

The result mesh must be treated as temporary, and cannot be referenced from objects in the main
database. If the mesh intended to be used in a persistent manner use [`new_from_object()`](BlendDataMeshes.md#bpy.types.BlendDataMeshes.new_from_object "bpy.types.BlendDataMeshes.new_from_object")
instead.

Note

If object does not have geometry (i.e. camera) the functions returns None.

```
import bpy

class OBJECT_OT_object_to_mesh(bpy.types.Operator):
    """Convert selected object to mesh and show number of vertices"""
    bl_label = "DEG Object to Mesh"
    bl_idname = "object.object_to_mesh"

    def execute(self, context):
        # Access input original object.
        obj = context.object
        if obj is None:
            self.report({'INFO'}, "No active mesh object to convert to mesh")
            return {'CANCELLED'}
        # Avoid annoying None checks later on.
        if obj.type not in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}:
            self.report({'INFO'}, "Object cannot be converted to mesh")
            return {'CANCELLED'}
        depsgraph = context.evaluated_depsgraph_get()
        # Invoke to_mesh() for original object.
        mesh_from_orig = obj.to_mesh()
        self.report({'INFO'}, f"{len(mesh_from_orig.vertices)} in new mesh without modifiers.")
        # Remove temporary mesh.
        obj.to_mesh_clear()
        # Invoke to_mesh() for evaluated object.
        object_eval = obj.evaluated_get(depsgraph)
        mesh_from_eval = object_eval.to_mesh()
        self.report({'INFO'}, f"{len(mesh_from_eval.vertices)} in new mesh with modifiers.")
        # Remove temporary mesh.
        object_eval.to_mesh_clear()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_object_to_mesh)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_object_to_mesh)

if __name__ == "__main__":
    register()
```

## Dependency graph: bpy.data.meshes.new\_from\_object()[#](#dependency-graph-bpy-data-meshes-new-from-object "Link to this heading")

Function to copy a new mesh from any object with geometry. The mesh is added to the main
database and can be referenced by objects. Typically used by tools that create new objects
or apply modifiers.

When is used on original object, the result mesh is calculated from the object without taking
animation or modifiers into account:

* For meshes this is similar to duplicating the source mesh.
* For curves this disables own modifiers, and modifiers of objects used as bevel and taper.
* For metaballs this produces an empty mesh since polygonization is done as a modifier evaluation.

When is used on evaluated object all modifiers are taken into account.

All the references (such as materials) are re-mapped to original. This ensures validity and
consistency of the main database.

Note

If object does not have geometry (i.e. camera) the functions returns None.

```
import bpy

class OBJECT_OT_mesh_from_object(bpy.types.Operator):
    """Convert selected object to mesh and show number of vertices"""
    bl_label = "DEG Mesh From Object"
    bl_idname = "object.mesh_from_object"

    def execute(self, context):
        # Access input original object.
        obj = context.object
        if obj is None:
            self.report({'INFO'}, "No active mesh object to convert to mesh")
            return {'CANCELLED'}
        # Avoid annoying None checks later on.
        if obj.type not in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}:
            self.report({'INFO'}, "Object cannot be converted to mesh")
            return {'CANCELLED'}
        depsgraph = context.evaluated_depsgraph_get()
        object_eval = obj.evaluated_get(depsgraph)
        mesh_from_eval = bpy.data.meshes.new_from_object(object_eval)
        self.report({'INFO'}, f"{len(mesh_from_eval.vertices)} in new mesh, and is ready for use!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_mesh_from_object)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_mesh_from_object)

if __name__ == "__main__":
    register()
```

## Dependency graph: Simple exporter[#](#dependency-graph-simple-exporter "Link to this heading")

This example is a combination of all previous ones, and shows how to write a simple exporter
script.

```
import bpy

class OBJECT_OT_simple_exporter(bpy.types.Operator):
    """Simple (fake) exporter of selected objects"""
    bl_label = "DEG Export Selected"
    bl_idname = "object.simple_exporter"

    apply_modifiers: bpy.props.BoolProperty(name="Apply Modifiers")

    def execute(self, context):
        depsgraph = context.evaluated_depsgraph_get()
        for object_instance in depsgraph.object_instances:
            if not self.is_object_instance_from_selected(object_instance):
                # We only export selected objects
                continue
            # NOTE: This will create a mesh for every instance, which is not ideal at all. In
            # reality destination format will support some sort of instancing mechanism, so the
            # code here will simply say "instance this object at object_instance.matrix_world".
            mesh = self.create_mesh_for_object_instance(object_instance)
            if mesh is None:
                # Happens for non-geometry objects.
                continue
            print(f"Exporting mesh with {len(mesh.vertices)} vertices "
                  f"at {object_instance.matrix_world}")
            object_instace.to_mesh_clear()

        return {'FINISHED'}

    def is_object_instance_from_selected(self, object_instance):
        # For instanced objects we check selection of their instancer (more accurately: check
        # selection status of the original object corresponding to the instancer).
        if object_instance.parent:
            return object_instance.parent.original.select_get()
        # For non-instanced objects we check selection state of the original object.
        return object_instance.object.original.select_get()

    def create_mesh_for_object_instance(self, object_instance):
        if self.apply_modifiers:
            return object_instance.object.to_mesh()
        else:
            return object_instance.object.original.to_mesh()

def register():
    bpy.utils.register_class(OBJECT_OT_simple_exporter)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_simple_exporter)

if __name__ == "__main__":
    register()
```

## Dependency graph: Object.to\_curve()[#](#dependency-graph-object-to-curve "Link to this heading")

Function to get a curve from text and curve objects. It is typically used by exporters, render
engines, and tools that need to access the curve representing the object.

The function takes the evaluated dependency graph as a required parameter and optionally a boolean
apply\_modifiers which defaults to false. If apply\_modifiers is true and the object is a curve object,
the spline deform modifiers are applied on the control points. Note that constructive modifiers and
modifiers that are not spline-enabled will not be applied. So modifiers like Array will not be applied
and deform modifiers that have Apply On Spline disabled will not be applied.

If the object is a text object. The text will be converted into a 3D curve and returned. Modifiers are
never applied on text objects and apply\_modifiers will be ignored. If the object is neither a curve nor
a text object, an error will be reported.

Note

The resulting curve is owned by the object. It can be freed by calling [`to_curve_clear()`](Object.md#bpy.types.Object.to_curve_clear "bpy.types.Object.to_curve_clear").

Note

The resulting curve must be treated as temporary, and cannot be referenced from objects in the main
database.

```
import bpy

class OBJECT_OT_object_to_curve(bpy.types.Operator):
    """Convert selected object to curve and show number of splines"""
    bl_label = "DEG Object to Curve"
    bl_idname = "object.object_to_curve"

    def execute(self, context):
        # Access input original object.
        obj = context.object
        if obj is None:
            self.report({'INFO'}, "No active object to convert to curve")
            return {'CANCELLED'}
        if obj.type not in {'CURVE', 'FONT'}:
            self.report({'INFO'}, "Object cannot be converted to curve")
            return {'CANCELLED'}
        depsgraph = context.evaluated_depsgraph_get()
        # Invoke to_curve() without applying modifiers.
        curve_without_modifiers = obj.to_curve(depsgraph)
        self.report({'INFO'}, f"{len(curve_without_modifiers.splines)} splines in a new curve without modifiers.")
        # Remove temporary curve.
        obj.to_curve_clear()
        # Invoke to_curve() with applying modifiers.
        curve_with_modifiers = obj.to_curve(depsgraph, apply_modifiers=True)
        self.report({'INFO'}, f"{len(curve_with_modifiers.splines)} splines in new curve with modifiers.")
        # Remove temporary curve.
        obj.to_curve_clear()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_object_to_curve)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_object_to_curve)

if __name__ == "__main__":
    register()
```

base class — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct")

*class* bpy.types.Depsgraph(*bpy\_struct*)[#](#bpy.types.Depsgraph "Link to this definition")
:   ids[#](#bpy.types.Depsgraph.ids "Link to this definition")
    :   All evaluated data-blocks

        Type:
        :   [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`ID`](ID.md#bpy.types.ID "bpy.types.ID"), (readonly)

    mode[#](#bpy.types.Depsgraph.mode "Link to this definition")
    :   Evaluation mode

        * `VIEWPORT`
          Viewport – Viewport non-rendered mode.
        * `RENDER`
          Render – Render.

        Type:
        :   enum in [‘VIEWPORT’, ‘RENDER’], default ‘VIEWPORT’, (readonly)

    object\_instances[#](#bpy.types.Depsgraph.object_instances "Link to this definition")
    :   All object instances to display or render (Warning: Only use this as an iterator, never as a sequence, and do not keep any references to its items)

        Type:
        :   [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`DepsgraphObjectInstance`](DepsgraphObjectInstance.md#bpy.types.DepsgraphObjectInstance "bpy.types.DepsgraphObjectInstance"), (readonly)

    objects[#](#bpy.types.Depsgraph.objects "Link to this definition")
    :   Evaluated objects in the dependency graph

        Type:
        :   [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`Object`](Object.md#bpy.types.Object "bpy.types.Object"), (readonly)

    scene[#](#bpy.types.Depsgraph.scene "Link to this definition")
    :   Original scene dependency graph is built for

        Type:
        :   [`Scene`](Scene.md#bpy.types.Scene "bpy.types.Scene"), (readonly)

    scene\_eval[#](#bpy.types.Depsgraph.scene_eval "Link to this definition")
    :   Scene at its evaluated state

        Type:
        :   [`Scene`](Scene.md#bpy.types.Scene "bpy.types.Scene"), (readonly)

    updates[#](#bpy.types.Depsgraph.updates "Link to this definition")
    :   Updates to data-blocks

        Type:
        :   [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`DepsgraphUpdate`](DepsgraphUpdate.md#bpy.types.DepsgraphUpdate "bpy.types.DepsgraphUpdate"), (readonly)

    view\_layer[#](#bpy.types.Depsgraph.view_layer "Link to this definition")
    :   Original view layer dependency graph is built for

        Type:
        :   [`ViewLayer`](ViewLayer.md#bpy.types.ViewLayer "bpy.types.ViewLayer"), (readonly)

    view\_layer\_eval[#](#bpy.types.Depsgraph.view_layer_eval "Link to this definition")
    :   View layer at its evaluated state

        Type:
        :   [`ViewLayer`](ViewLayer.md#bpy.types.ViewLayer "bpy.types.ViewLayer"), (readonly)

    debug\_relations\_graphviz(*filepath*)[#](#bpy.types.Depsgraph.debug_relations_graphviz "Link to this definition")
    :   debug\_relations\_graphviz

        Parameters:
        :   **filepath** (*string**,* *(**never None**)*) – File Name, Output path for the graphviz debug file

    debug\_stats\_gnuplot(*filepath*, *output\_filepath*)[#](#bpy.types.Depsgraph.debug_stats_gnuplot "Link to this definition")
    :   debug\_stats\_gnuplot

        Parameters:
        :   * **filepath** (*string**,* *(**never None**)*) – File Name, Output path for the gnuplot debug file
            * **output\_filepath** (*string**,* *(**never None**)*) – Output File Name, File name where gnuplot script will save the result

    debug\_tag\_update()[#](#bpy.types.Depsgraph.debug_tag_update "Link to this definition")
    :   debug\_tag\_update

    debug\_stats()[#](#bpy.types.Depsgraph.debug_stats "Link to this definition")
    :   Report the number of elements in the Dependency Graph

        Returns:
        :   result

        Return type:
        :   string, (never None)

    update()[#](#bpy.types.Depsgraph.update "Link to this definition")
    :   Re-evaluate any modified data-blocks, for example for animation or modifiers. This invalidates all references to evaluated data-blocks from this dependency graph.

    id\_eval\_get(*id*)[#](#bpy.types.Depsgraph.id_eval_get "Link to this definition")
    :   id\_eval\_get

        Parameters:
        :   **id** ([`ID`](ID.md#bpy.types.ID "bpy.types.ID")) – Original ID to get evaluated complementary part for

        Returns:
        :   Evaluated ID for the given original one

        Return type:
        :   [`ID`](ID.md#bpy.types.ID "bpy.types.ID")

    id\_type\_updated(*id\_type*)[#](#bpy.types.Depsgraph.id_type_updated "Link to this definition")
    :   id\_type\_updated

        Parameters:
        :   **id\_type** (enum in [Id Type Items](../../../appendix/bpy_types_enum_items/id_type_items.md#rna-enum-id-type-items)) – ID Type

        Returns:
        :   Updated, True if any datablock with this type was added, updated or removed

        Return type:
        :   boolean

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.Depsgraph.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.Depsgraph.bl_rna_get_subclass_py "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The class or default when not found.

        Return type:
        :   type

### Inherited Properties[#](#inherited-properties "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.id_data`](bpy_struct.md#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data") |  |

### Inherited Functions[#](#inherited-functions "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.as_pointer`](bpy_struct.md#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer") * [`bpy_struct.driver_add`](bpy_struct.md#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add") * [`bpy_struct.driver_remove`](bpy_struct.md#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove") * [`bpy_struct.get`](bpy_struct.md#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get") * [`bpy_struct.id_properties_clear`](bpy_struct.md#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear") * [`bpy_struct.id_properties_ensure`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure") * [`bpy_struct.id_properties_ui`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui") * [`bpy_struct.is_property_hidden`](bpy_struct.md#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden") * [`bpy_struct.is_property_overridable_library`](bpy_struct.md#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library") * [`bpy_struct.is_property_readonly`](bpy_struct.md#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly") * [`bpy_struct.is_property_set`](bpy_struct.md#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set") | * [`bpy_struct.items`](bpy_struct.md#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items") * [`bpy_struct.keyframe_delete`](bpy_struct.md#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete") * [`bpy_struct.keyframe_insert`](bpy_struct.md#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert") * [`bpy_struct.keys`](bpy_struct.md#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys") * [`bpy_struct.path_from_id`](bpy_struct.md#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id") * [`bpy_struct.path_resolve`](bpy_struct.md#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve") * [`bpy_struct.pop`](bpy_struct.md#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop") * [`bpy_struct.property_overridable_library_set`](bpy_struct.md#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set") * [`bpy_struct.property_unset`](bpy_struct.md#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset") * [`bpy_struct.type_recast`](bpy_struct.md#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast") * [`bpy_struct.values`](bpy_struct.md#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values") |

### References[#](#references "Link to this heading")

|  |  |
| --- | --- |
| * [`BlendDataMeshes.new_from_object`](BlendDataMeshes.md#bpy.types.BlendDataMeshes.new_from_object "bpy.types.BlendDataMeshes.new_from_object") * [`Context.evaluated_depsgraph_get`](Context.md#bpy.types.Context.evaluated_depsgraph_get "bpy.types.Context.evaluated_depsgraph_get") * [`ID.evaluated_get`](ID.md#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get") * [`Object.calc_matrix_camera`](Object.md#bpy.types.Object.calc_matrix_camera "bpy.types.Object.calc_matrix_camera") * [`Object.camera_fit_coords`](Object.md#bpy.types.Object.camera_fit_coords "bpy.types.Object.camera_fit_coords") * [`Object.closest_point_on_mesh`](Object.md#bpy.types.Object.closest_point_on_mesh "bpy.types.Object.closest_point_on_mesh") * [`Object.crazyspace_eval`](Object.md#bpy.types.Object.crazyspace_eval "bpy.types.Object.crazyspace_eval") * [`Object.ray_cast`](Object.md#bpy.types.Object.ray_cast "bpy.types.Object.ray_cast") * [`Object.to_curve`](Object.md#bpy.types.Object.to_curve "bpy.types.Object.to_curve") * [`Object.to_mesh`](Object.md#bpy.types.Object.to_mesh "bpy.types.Object.to_mesh") * [`RenderEngine.bake`](RenderEngine.md#bpy.types.RenderEngine.bake "bpy.types.RenderEngine.bake") | * [`RenderEngine.draw`](RenderEngine.md#bpy.types.RenderEngine.draw "bpy.types.RenderEngine.draw") * [`RenderEngine.render`](RenderEngine.md#bpy.types.RenderEngine.render "bpy.types.RenderEngine.render") * [`RenderEngine.update`](RenderEngine.md#bpy.types.RenderEngine.update "bpy.types.RenderEngine.update") * [`RenderEngine.view_draw`](RenderEngine.md#bpy.types.RenderEngine.view_draw "bpy.types.RenderEngine.view_draw") * [`RenderEngine.view_update`](RenderEngine.md#bpy.types.RenderEngine.view_update "bpy.types.RenderEngine.view_update") * [`Scene.ray_cast`](Scene.md#bpy.types.Scene.ray_cast "bpy.types.Scene.ray_cast") * [`ShaderNodeTexPointDensity.cache_point_density`](ShaderNodeTexPointDensity.md#bpy.types.ShaderNodeTexPointDensity.cache_point_density "bpy.types.ShaderNodeTexPointDensity.cache_point_density") * [`ShaderNodeTexPointDensity.calc_point_density`](ShaderNodeTexPointDensity.md#bpy.types.ShaderNodeTexPointDensity.calc_point_density "bpy.types.ShaderNodeTexPointDensity.calc_point_density") * [`ShaderNodeTexPointDensity.calc_point_density_minmax`](ShaderNodeTexPointDensity.md#bpy.types.ShaderNodeTexPointDensity.calc_point_density_minmax "bpy.types.ShaderNodeTexPointDensity.calc_point_density_minmax") * [`ViewLayer.depsgraph`](ViewLayer.md#bpy.types.ViewLayer.depsgraph "bpy.types.ViewLayer.depsgraph") |

[Next

DepsgraphObjectInstance(bpy\_struct)](DepsgraphObjectInstance.md)
[Previous

DecimateModifier(Modifier)](DecimateModifier.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.Depsgraph.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.Depsgraph.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Depsgraph(bpy\_struct)
  + [Dependency graph: Evaluated ID example](#dependency-graph-evaluated-id-example)
  + [Dependency graph: Original object example](#dependency-graph-original-object-example)
  + [Dependency graph: Iterate over all object instances](#dependency-graph-iterate-over-all-object-instances)
  + [Dependency graph: Object.to\_mesh()](#dependency-graph-object-to-mesh)
  + [Dependency graph: bpy.data.meshes.new\_from\_object()](#dependency-graph-bpy-data-meshes-new-from-object)
  + [Dependency graph: Simple exporter](#dependency-graph-simple-exporter)
  + [Dependency graph: Object.to\_curve()](#dependency-graph-object-to-curve)
    - [`Depsgraph`](#bpy.types.Depsgraph)
      * [`Depsgraph.ids`](#bpy.types.Depsgraph.ids)
      * [`Depsgraph.mode`](#bpy.types.Depsgraph.mode)
      * [`Depsgraph.object_instances`](#bpy.types.Depsgraph.object_instances)
      * [`Depsgraph.objects`](#bpy.types.Depsgraph.objects)
      * [`Depsgraph.scene`](#bpy.types.Depsgraph.scene)
      * [`Depsgraph.scene_eval`](#bpy.types.Depsgraph.scene_eval)
      * [`Depsgraph.updates`](#bpy.types.Depsgraph.updates)
      * [`Depsgraph.view_layer`](#bpy.types.Depsgraph.view_layer)
      * [`Depsgraph.view_layer_eval`](#bpy.types.Depsgraph.view_layer_eval)
      * [`Depsgraph.debug_relations_graphviz()`](#bpy.types.Depsgraph.debug_relations_graphviz)
      * [`Depsgraph.debug_stats_gnuplot()`](#bpy.types.Depsgraph.debug_stats_gnuplot)
      * [`Depsgraph.debug_tag_update()`](#bpy.types.Depsgraph.debug_tag_update)
      * [`Depsgraph.debug_stats()`](#bpy.types.Depsgraph.debug_stats)
      * [`Depsgraph.update()`](#bpy.types.Depsgraph.update)
      * [`Depsgraph.id_eval_get()`](#bpy.types.Depsgraph.id_eval_get)
      * [`Depsgraph.id_type_updated()`](#bpy.types.Depsgraph.id_type_updated)
      * [`Depsgraph.bl_rna_get_subclass()`](#bpy.types.Depsgraph.bl_rna_get_subclass)
      * [`Depsgraph.bl_rna_get_subclass_py()`](#bpy.types.Depsgraph.bl_rna_get_subclass_py)
    - [Inherited Properties](#inherited-properties)
    - [Inherited Functions](#inherited-functions)
    - [References](#references)