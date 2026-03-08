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

# Menu(bpy\_struct)[#](#menu-bpy-struct "Link to this heading")

## Basic Menu Example[#](#basic-menu-example "Link to this heading")

Here is an example of a simple menu. Menus differ from panels in that they must
reference from a header, panel or another menu.

Notice the ‘CATEGORY\_MT\_name’ in [`Menu.bl_idname`](#bpy.types.Menu.bl_idname "bpy.types.Menu.bl_idname"), this is a naming
convention for menus.

Note

Menu subclasses must be registered before referencing them from blender.

Note

Menus have their `Layout.operator_context` initialized as
‘EXEC\_REGION\_WIN’ rather than ‘INVOKE\_DEFAULT’ (see [Execution Context](../ops/index.md#operator-execution-context)).
If the operator context needs to initialize inputs from the
[`Operator.invoke`](Operator.md#bpy.types.Operator.invoke "bpy.types.Operator.invoke") function, then this needs to be explicitly set.

```
import bpy

class BasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_test"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")

bpy.utils.register_class(BasicMenu)

# test call to display immediately.
bpy.ops.wm.call_menu(name="OBJECT_MT_select_test")
```

## Submenus[#](#submenus "Link to this heading")

This menu demonstrates some different functions.

```
import bpy

class SubMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_submenu"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")

        # access this operator as a submenu
        layout.operator_menu_enum("object.select_by_type", "type", text="Select All by Type...")

        layout.separator()

        # expand each operator option into this menu
        layout.operator_enum("object.light_add", "type")

        layout.separator()

        # use existing memu
        layout.menu("VIEW3D_MT_transform")

bpy.utils.register_class(SubMenu)

# test call to display immediately.
bpy.ops.wm.call_menu(name="OBJECT_MT_select_submenu")
```

## Extending Menus[#](#extending-menus "Link to this heading")

When creating menus for add-ons you can’t reference menus
in Blender’s default scripts.
Instead, the add-on can add menu items to existing menus.

The function menu\_draw acts like [`Menu.draw`](#bpy.types.Menu.draw "bpy.types.Menu.draw").

```
import bpy

def menu_draw(self, context):
    self.layout.operator("wm.save_homefile")

bpy.types.TOPBAR_MT_file.append(menu_draw)
```

## Preset Menus[#](#preset-menus "Link to this heading")

Preset menus are simply a convention that uses a menu sub-class
to perform the common task of managing presets.

This example shows how you can add a preset menu.

This example uses the object display options,
however you can use properties defined by your own scripts too.

```
import bpy
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

class OBJECT_MT_display_presets(Menu):
    bl_label = "Object Display Presets"
    preset_subdir = "object/display"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset

class AddPresetObjectDisplay(AddPresetBase, Operator):
    '''Add a Object Display Preset'''
    bl_idname = "camera.object_display_preset_add"
    bl_label = "Add Object Display Preset"
    preset_menu = "OBJECT_MT_display_presets"

    # variable used for all preset values
    preset_defines = [
        "obj = bpy.context.object"
    ]

    # properties to store in the preset
    preset_values = [
        "obj.display_type",
        "obj.show_bounds",
        "obj.display_bounds_type",
        "obj.show_name",
        "obj.show_axis",
        "obj.show_wire",
    ]

    # where to store the preset
    preset_subdir = "object/display"

# Display into an existing panel
def panel_func(self, context):
    layout = self.layout

    row = layout.row(align=True)
    row.menu(OBJECT_MT_display_presets.__name__, text=OBJECT_MT_display_presets.bl_label)
    row.operator(AddPresetObjectDisplay.bl_idname, text="", icon='ZOOM_IN')
    row.operator(AddPresetObjectDisplay.bl_idname, text="", icon='ZOOM_OUT').remove_active = True

classes = (
    OBJECT_MT_display_presets,
    AddPresetObjectDisplay,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.OBJECT_PT_display.prepend(panel_func)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.OBJECT_PT_display.remove(panel_func)

if __name__ == "__main__":
    register()
```

## Extending the Button Context Menu[#](#extending-the-button-context-menu "Link to this heading")

This example enables you to insert your own menu entry into the common
right click menu that you get while hovering over a UI button (e.g. operator,
value field, color, string, etc.)

To make the example work, you have to first select an object
then right click on an user interface element (maybe a color in the
material properties) and choose *Execute Custom Action*.

Executing the operator will then print all values.

```
import bpy

def dump(obj, text):
    for attr in dir(obj):
        print("{!r}.{:s} = {:s}".format(obj, attr, getattr(obj, attr)))

class WM_OT_button_context_test(bpy.types.Operator):
    """Right click entry test"""
    bl_idname = "wm.button_context_test"
    bl_label = "Run Context Test"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        value = getattr(context, "button_pointer", None)
        if value is not None:
            dump(value, "button_pointer")

        value = getattr(context, "button_prop", None)
        if value is not None:
            dump(value, "button_prop")

        value = getattr(context, "button_operator", None)
        if value is not None:
            dump(value, "button_operator")

        return {'FINISHED'}

def draw_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(WM_OT_button_context_test.bl_idname)

def register():
    bpy.utils.register_class(WM_OT_button_context_test)
    bpy.types.UI_MT_button_context_menu.append(draw_menu)

def unregister():
    bpy.types.UI_MT_button_context_menu.remove(draw_menu)
    bpy.utils.unregister_class(WM_OT_button_context_test)

if __name__ == "__main__":
    register()
```

base class — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct")

*class* bpy.types.Menu(*bpy\_struct*)[#](#bpy.types.Menu "Link to this definition")
:   Editor menu containing buttons

    bl\_description[#](#bpy.types.Menu.bl_description "Link to this definition")
    :   Type:
        :   string, default “”

    bl\_idname[#](#bpy.types.Menu.bl_idname "Link to this definition")
    :   If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is “OBJECT\_MT\_hello”, and bl\_idname is not set by the script, then bl\_idname = “OBJECT\_MT\_hello”)

        Type:
        :   string, default “”, (never None)

    bl\_label[#](#bpy.types.Menu.bl_label "Link to this definition")
    :   The menu label

        Type:
        :   string, default “”, (never None)

    bl\_options[#](#bpy.types.Menu.bl_options "Link to this definition")
    :   Options for this menu type

        * `SEARCH_ON_KEY_PRESS`
          Search on Key Press – Open a menu search when a key pressed while the menu is open.

        Type:
        :   enum set in {‘SEARCH\_ON\_KEY\_PRESS’}, default {‘SEARCH\_ON\_KEY\_PRESS’}

    bl\_owner\_id[#](#bpy.types.Menu.bl_owner_id "Link to this definition")
    :   Type:
        :   string, default “”, (never None)

    bl\_translation\_context[#](#bpy.types.Menu.bl_translation_context "Link to this definition")
    :   Type:
        :   string, default “\*”, (never None)

    layout[#](#bpy.types.Menu.layout "Link to this definition")
    :   Defines the structure of the menu in the UI

        Type:
        :   [`UILayout`](UILayout.md#bpy.types.UILayout "bpy.types.UILayout"), (readonly)

    *classmethod* poll(*context*)[#](#bpy.types.Menu.poll "Link to this definition")
    :   If this method returns a non-null output, then the menu can be drawn

        Return type:
        :   boolean

    draw(*context*)[#](#bpy.types.Menu.draw "Link to this definition")
    :   Draw UI elements into the menu UI layout

    *classmethod* append(*draw\_func*)[#](#bpy.types.Menu.append "Link to this definition")
    :   Append a draw function to this menu,
        takes the same arguments as the menus draw function

    *classmethod* draw\_collapsible(*context*, *layout*)[#](#bpy.types.Menu.draw_collapsible "Link to this definition")

    draw\_preset(*\_context*)[#](#bpy.types.Menu.draw_preset "Link to this definition")
    :   Define these on the subclass:
        - preset\_operator (string)
        - preset\_subdir (string)

        Optionally:
        - preset\_add\_operator (string)
        - preset\_extensions (set of strings)
        - preset\_operator\_defaults (dict of keyword args)

    *classmethod* is\_extended()[#](#bpy.types.Menu.is_extended "Link to this definition")

    path\_menu(*searchpaths*, *operator*, *\**, *props\_default=None*, *prop\_filepath='filepath'*, *filter\_ext=None*, *filter\_path=None*, *display\_name=None*, *add\_operator=None*, *add\_operator\_props=None*)[#](#bpy.types.Menu.path_menu "Link to this definition")
    :   Populate a menu from a list of paths.

        Parameters:
        :   * **searchpaths** (*sequence* *of* *strings.*) – Paths to scan.
            * **operator** (*string*) – The operator id to use with each file.
            * **prop\_filepath** (*string*) – Optional operator filepath property (defaults to “filepath”).
            * **props\_default** (*dict*) – Properties to assign to each operator.
            * **filter\_ext** (*Callable that takes a string and returns a bool.*) –

              Optional callback that takes the file extensions.

              Returning false excludes the file from the list.
            * **display\_name** (*Callable that takes a string and returns a string.*) – Optional callback that takes the full path, returns the name to display.

    *classmethod* prepend(*draw\_func*)[#](#bpy.types.Menu.prepend "Link to this definition")
    :   Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

    *classmethod* remove(*draw\_func*)[#](#bpy.types.Menu.remove "Link to this definition")
    :   Remove a draw function that has been added to this menu

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.Menu.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.Menu.bl_rna_get_subclass_py "Link to this definition")
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

Mesh(ID)](Mesh.md)
[Previous

MaterialSlot(bpy\_struct)](MaterialSlot.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.Menu.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.Menu.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Menu(bpy\_struct)
  + [Basic Menu Example](#basic-menu-example)
  + [Submenus](#submenus)
  + [Extending Menus](#extending-menus)
  + [Preset Menus](#preset-menus)
  + [Extending the Button Context Menu](#extending-the-button-context-menu)
    - [`Menu`](#bpy.types.Menu)
      * [`Menu.bl_description`](#bpy.types.Menu.bl_description)
      * [`Menu.bl_idname`](#bpy.types.Menu.bl_idname)
      * [`Menu.bl_label`](#bpy.types.Menu.bl_label)
      * [`Menu.bl_options`](#bpy.types.Menu.bl_options)
      * [`Menu.bl_owner_id`](#bpy.types.Menu.bl_owner_id)
      * [`Menu.bl_translation_context`](#bpy.types.Menu.bl_translation_context)
      * [`Menu.layout`](#bpy.types.Menu.layout)
      * [`Menu.poll()`](#bpy.types.Menu.poll)
      * [`Menu.draw()`](#bpy.types.Menu.draw)
      * [`Menu.append()`](#bpy.types.Menu.append)
      * [`Menu.draw_collapsible()`](#bpy.types.Menu.draw_collapsible)
      * [`Menu.draw_preset()`](#bpy.types.Menu.draw_preset)
      * [`Menu.is_extended()`](#bpy.types.Menu.is_extended)
      * [`Menu.path_menu()`](#bpy.types.Menu.path_menu)
      * [`Menu.prepend()`](#bpy.types.Menu.prepend)
      * [`Menu.remove()`](#bpy.types.Menu.remove)
      * [`Menu.bl_rna_get_subclass()`](#bpy.types.Menu.bl_rna_get_subclass)
      * [`Menu.bl_rna_get_subclass_py()`](#bpy.types.Menu.bl_rna_get_subclass_py)
    - [Inherited Properties](#inherited-properties)
    - [Inherited Functions](#inherited-functions)