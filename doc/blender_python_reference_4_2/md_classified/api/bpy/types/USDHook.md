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

# USDHook(bpy\_struct)[#](#usdhook-bpy-struct "Link to this heading")

## USD Hook Example[#](#usd-hook-example "Link to this heading")

This example shows an implementation of `USDHook` to extend USD
export and import functionalty.

One may optionally define any or all of the following callback functions
in the `USDHook` subclass.

Hook function `on_export()` is called before the USD export finalizes,
allowing modifications to the USD stage immediately before it is
saved. This function takes as an argument an instance of an
internally defined class `USDSceneExportContext` which provides the
following accessors to the scene data:

* `get_stage()` returns the USD stage to be saved.
* `get_depsgraph()` returns the Blender scene dependency graph.

Hook function `on_material_export()` is called for each material that is exported,
allowing modifications to the USD material, such as shader generation.
It is called with three arguments:

-`export_context`: An instance of the internally defined type `USDMaterialExportContext`.
-`bl_material`: The source Blender material.
-`usd_material`: The target USD material to be exported.

`USDMaterialExportContext` implements a `get_stage()` function which returns the
USD stage to be saved.

Note that the target USD material might already have connected shaders created by the USD exporter or
by other material export hooks.

Hook function `on_import()` is called after the USD import finalizes. This function takes
as an argument an instance of an internally defined class `USDSceneImportContext` which provides the
following accessors to the scene data:

* `get_stage()` returns the USD stage which was imported.

The hook functions should return `True` on success or `False` if the operation was bypassed or
otherwise failed to complete. Exceptions raised by these functions will be reported in Blender, with
the exception details printed to the console.

The `USDHookExample` class in this example impements the fllowing functions:

* `on_export()` function to add custom data to the stage’s root layer.
* `on_material_export()` function to create a simple `MaterialX` shader on the givne USD material.
* `on_import()` function to create a text object to display the stage’s custom layer data.

```
import bpy
import bpy.types
import pxr.Gf as Gf
import pxr.Sdf as Sdf
import pxr.Usd as Usd
import pxr.UsdShade as UsdShade
import textwrap

class USDHookExample(bpy.types.USDHook):
    """Example implementation of USD IO hooks"""
    bl_idname = "usd_hook_example"
    bl_label = "Example"

    @staticmethod
    def on_export(export_context):
        """ Include the Blender filepath in the root layer custom data.
        """

        stage = export_context.get_stage()

        if stage is None:
            return False
        data = bpy.data
        if data is None:
            return False

        # Set the custom data.
        rootLayer = stage.GetRootLayer()
        customData = rootLayer.customLayerData
        customData["blenderFilepath"] = data.filepath
        rootLayer.customLayerData = customData

        return True

    @staticmethod
    def on_material_export(export_context, bl_material, usd_material):
        """ Create a simple MaterialX shader on the exported material.
        """

        stage = export_context.get_stage()

        # Create a MaterialX standard surface shader
        mtl_path = usd_material.GetPrim().GetPath()
        shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("mtlxstandard_surface"))
        shader.CreateIdAttr("ND_standard_surface_surfaceshader")

        # Connect the shader.  MaterialX materials use "mtlx" renderContext
        usd_material.CreateSurfaceOutput("mtlx").ConnectToSource(shader.ConnectableAPI(), "out")

        # Set the color to the Blender material's viewport display color.
        col = bl_material.diffuse_color
        shader.CreateInput("base_color", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(col[0], col[1], col[2]))

        return True

    @staticmethod
    def on_import(import_context):
        """ Create a text object to display the stage's custom data.
        """
        stage = import_context.get_stage()

        if stage is None:
            return False

        # Get the custom data.
        rootLayer = stage.GetRootLayer()
        customData = rootLayer.customLayerData

        # Create a text object to display the stage path
        # and custom data dictionary entries.

        bpy.ops.object.text_add()
        ob = bpy.context.view_layer.objects.active

        if (ob is None) or (ob.data is None):
            return False

        ob.name = "layer_data"
        ob.data.name = "layer_data"

        # The stage root path is the first line.
        text = rootLayer.realPath

        # Append key/value strings, enforcing text wrapping.
        for item in customData.items():
            print(item)
            text += '\n'
            line = str(item[0]) + ': ' + str(item[1])
            text += textwrap.fill(line, width=80)

        ob.data.body = text

        return True

def register():
    bpy.utils.register_class(USDHookExample)

def unregister():
    bpy.utils.unregister_class(USDHookExample)

if __name__ == "__main__":
    register()
```

base class — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct")

*class* bpy.types.USDHook(*bpy\_struct*)[#](#bpy.types.USDHook "Link to this definition")
:   Defines callback functions to extend USD IO

    bl\_description[#](#bpy.types.USDHook.bl_description "Link to this definition")
    :   A short description of the USD hook

        Type:
        :   string, default “”, (never None)

    bl\_idname[#](#bpy.types.USDHook.bl_idname "Link to this definition")
    :   Type:
        :   string, default “”, (never None)

    bl\_label[#](#bpy.types.USDHook.bl_label "Link to this definition")
    :   Type:
        :   string, default “”, (never None)

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.USDHook.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.USDHook.bl_rna_get_subclass_py "Link to this definition")
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

[Next

USERPREF\_UL\_asset\_libraries(UIList)](USERPREF_UL_asset_libraries.md)
[Previous

UI\_UL\_list(UIList)](UI_UL_list.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.USDHook.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.USDHook.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* USDHook(bpy\_struct)
  + [USD Hook Example](#usd-hook-example)
    - [`USDHook`](#bpy.types.USDHook)
      * [`USDHook.bl_description`](#bpy.types.USDHook.bl_description)
      * [`USDHook.bl_idname`](#bpy.types.USDHook.bl_idname)
      * [`USDHook.bl_label`](#bpy.types.USDHook.bl_label)
      * [`USDHook.bl_rna_get_subclass()`](#bpy.types.USDHook.bl_rna_get_subclass)
      * [`USDHook.bl_rna_get_subclass_py()`](#bpy.types.USDHook.bl_rna_get_subclass_py)
    - [Inherited Properties](#inherited-properties)
    - [Inherited Functions](#inherited-functions)