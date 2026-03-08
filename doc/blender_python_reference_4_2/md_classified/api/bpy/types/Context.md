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

# Context(bpy\_struct)[#](#context-bpy-struct "Link to this heading")

base class — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct")

*class* bpy.types.Context(*bpy\_struct*)[#](#bpy.types.Context "Link to this definition")
:   Current windowmanager and data context

    area[#](#bpy.types.Context.area "Link to this definition")
    :   Type:
        :   [`Area`](Area.md#bpy.types.Area "bpy.types.Area"), (readonly)

    asset[#](#bpy.types.Context.asset "Link to this definition")
    :   Type:
        :   [`AssetRepresentation`](AssetRepresentation.md#bpy.types.AssetRepresentation "bpy.types.AssetRepresentation"), (readonly)

    blend\_data[#](#bpy.types.Context.blend_data "Link to this definition")
    :   Type:
        :   [`BlendData`](BlendData.md#bpy.types.BlendData "bpy.types.BlendData"), (readonly)

    collection[#](#bpy.types.Context.collection "Link to this definition")
    :   Type:
        :   [`Collection`](Collection.md#bpy.types.Collection "bpy.types.Collection"), (readonly)

    engine[#](#bpy.types.Context.engine "Link to this definition")
    :   Type:
        :   string, default “”, (readonly, never None)

    gizmo\_group[#](#bpy.types.Context.gizmo_group "Link to this definition")
    :   Type:
        :   [`GizmoGroup`](GizmoGroup.md#bpy.types.GizmoGroup "bpy.types.GizmoGroup"), (readonly)

    layer\_collection[#](#bpy.types.Context.layer_collection "Link to this definition")
    :   Type:
        :   [`LayerCollection`](LayerCollection.md#bpy.types.LayerCollection "bpy.types.LayerCollection"), (readonly)

    mode[#](#bpy.types.Context.mode "Link to this definition")
    :   Type:
        :   enum in [Context Mode Items](../../../appendix/bpy_types_enum_items/context_mode_items.md#rna-enum-context-mode-items), default ‘EDIT\_MESH’, (readonly)

    preferences[#](#bpy.types.Context.preferences "Link to this definition")
    :   Type:
        :   [`Preferences`](Preferences.md#bpy.types.Preferences "bpy.types.Preferences"), (readonly)

    region[#](#bpy.types.Context.region "Link to this definition")
    :   Type:
        :   [`Region`](Region.md#bpy.types.Region "bpy.types.Region"), (readonly)

    region\_data[#](#bpy.types.Context.region_data "Link to this definition")
    :   Type:
        :   [`RegionView3D`](RegionView3D.md#bpy.types.RegionView3D "bpy.types.RegionView3D"), (readonly)

    region\_popup[#](#bpy.types.Context.region_popup "Link to this definition")
    :   The temporary region for pop-ups (including menus and pop-overs)

        Type:
        :   [`Region`](Region.md#bpy.types.Region "bpy.types.Region"), (readonly)

    scene[#](#bpy.types.Context.scene "Link to this definition")
    :   Type:
        :   [`Scene`](Scene.md#bpy.types.Scene "bpy.types.Scene"), (readonly)

    screen[#](#bpy.types.Context.screen "Link to this definition")
    :   Type:
        :   [`Screen`](Screen.md#bpy.types.Screen "bpy.types.Screen"), (readonly)

    space\_data[#](#bpy.types.Context.space_data "Link to this definition")
    :   The current space, may be None in background-mode, when the cursor is outside the window or when using menu-search

        Type:
        :   [`Space`](Space.md#bpy.types.Space "bpy.types.Space"), (readonly)

    tool\_settings[#](#bpy.types.Context.tool_settings "Link to this definition")
    :   Type:
        :   [`ToolSettings`](ToolSettings.md#bpy.types.ToolSettings "bpy.types.ToolSettings"), (readonly)

    view\_layer[#](#bpy.types.Context.view_layer "Link to this definition")
    :   Type:
        :   [`ViewLayer`](ViewLayer.md#bpy.types.ViewLayer "bpy.types.ViewLayer"), (readonly)

    window[#](#bpy.types.Context.window "Link to this definition")
    :   Type:
        :   [`Window`](Window.md#bpy.types.Window "bpy.types.Window"), (readonly)

    window\_manager[#](#bpy.types.Context.window_manager "Link to this definition")
    :   Type:
        :   [`WindowManager`](WindowManager.md#bpy.types.WindowManager "bpy.types.WindowManager"), (readonly)

    workspace[#](#bpy.types.Context.workspace "Link to this definition")
    :   Type:
        :   [`WorkSpace`](WorkSpace.md#bpy.types.WorkSpace "bpy.types.WorkSpace"), (readonly)

    evaluated\_depsgraph\_get()[#](#bpy.types.Context.evaluated_depsgraph_get "Link to this definition")
    :   Get the dependency graph for the current scene and view layer, to access to data-blocks with animation and modifiers applied. If any data-blocks have been edited, the dependency graph will be updated. This invalidates all references to evaluated data-blocks from the dependency graph.

        Returns:
        :   Evaluated dependency graph

        Return type:
        :   [`Depsgraph`](Depsgraph.md#bpy.types.Depsgraph "bpy.types.Depsgraph")

    copy()[#](#bpy.types.Context.copy "Link to this definition")

    path\_resolve(*path*, *coerce=True*)[#](#bpy.types.Context.path_resolve "Link to this definition")
    :   Returns the property from the path, raise an exception when not found.

        Parameters:
        :   * **path** (*string*) – patch which this property resolves.
            * **coerce** (*boolean*) – optional argument, when True, the property will be converted into its Python representation.

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.Context.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.Context.bl_rna_get_subclass_py "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The class or default when not found.

        Return type:
        :   type

    temp\_override(*window=None*, *area=None*, *region=None*, *\*\*keywords*)[#](#bpy.types.Context.temp_override "Link to this definition")
    :   Context manager to temporarily override members in the context.

        Parameters:
        :   * **window** ([`bpy.types.Window`](Window.md#bpy.types.Window "bpy.types.Window")) – Window override or None.
            * **screen** ([`bpy.types.Screen`](Screen.md#bpy.types.Screen "bpy.types.Screen")) –

              Screen override or None.

              Note

              Switching to or away from full-screen areas & temporary screens isn’t supported. Passing in these screens will raise an exception, actions that leave the context such screens won’t restore the prior screen.

              Note

              Changing the screen has wider implications than other arguments as it will also change the works-space and potentially the scene (when pinned).
            * **area** ([`bpy.types.Area`](Area.md#bpy.types.Area "bpy.types.Area")) – Area override or None.
            * **region** ([`bpy.types.Region`](Region.md#bpy.types.Region "bpy.types.Region")) – Region override or None.
            * **keywords** – Additional keywords override context members.

        Returns:
        :   The context manager .

        Return type:
        :   context manager

        Overriding the context can be used to temporarily activate another `window` / `area` & `region`,
        as well as other members such as the `active_object` or `bone`.

        Notes:

        * When overriding window, area and regions: the arguments must be consistent,
          so any region argument that’s passed in must be contained by the current area or the area passed in.
          The same goes for the area needing to be contained in the current window.
        * Temporary context overrides may be nested, when this is done, members will be added to the existing overrides.
        * Context members are restored outside the scope of the context-manager.
          The only exception to this is when the data is no longer available.

          In the event windowing data was removed (for example), the state of the context is left as-is.
          While this isn’t likely to happen, explicit window operation such as closing windows or loading a new file
          remove the windowing data that was set before the temporary context was created.

        Overriding the context can be useful to set the context after loading files
        (which would otherwise by None). For example:

        ```
        import bpy
        from bpy import context

        # Reload the current file and select all.
        bpy.ops.wm.open_mainfile(filepath=bpy.data.filepath)
        window = context.window_manager.windows[0]
        with context.temp_override(window=window):
            bpy.ops.mesh.primitive_uv_sphere_add()
            # The context override is needed so it's possible to set edit-mode.
            bpy.ops.object.mode_set(mode='EDIT')
        ```

        This example shows how it’s possible to add an object to the scene in another window.

        ```
        import bpy
        from bpy import context

        win_active = context.window
        win_other = None
        for win_iter in context.window_manager.windows:
            if win_iter != win_active:
                win_other = win_iter
                break

        # Add cube in the other window.
        with context.temp_override(window=win_other):
            bpy.ops.mesh.primitive_cube_add()
        ```

## Inherited Properties[#](#inherited-properties "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.id_data`](bpy_struct.md#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data") |  |

## Inherited Functions[#](#inherited-functions "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.as_pointer`](bpy_struct.md#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer") * [`bpy_struct.driver_add`](bpy_struct.md#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add") * [`bpy_struct.driver_remove`](bpy_struct.md#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove") * [`bpy_struct.get`](bpy_struct.md#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get") * [`bpy_struct.id_properties_clear`](bpy_struct.md#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear") * [`bpy_struct.id_properties_ensure`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure") * [`bpy_struct.id_properties_ui`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui") * [`bpy_struct.is_property_hidden`](bpy_struct.md#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden") * [`bpy_struct.is_property_overridable_library`](bpy_struct.md#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library") * [`bpy_struct.is_property_readonly`](bpy_struct.md#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly") * [`bpy_struct.is_property_set`](bpy_struct.md#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set") | * [`bpy_struct.items`](bpy_struct.md#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items") * [`bpy_struct.keyframe_delete`](bpy_struct.md#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete") * [`bpy_struct.keyframe_insert`](bpy_struct.md#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert") * [`bpy_struct.keys`](bpy_struct.md#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys") * [`bpy_struct.path_from_id`](bpy_struct.md#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id") * [`bpy_struct.path_resolve`](bpy_struct.md#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve") * [`bpy_struct.pop`](bpy_struct.md#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop") * [`bpy_struct.property_overridable_library_set`](bpy_struct.md#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set") * [`bpy_struct.property_unset`](bpy_struct.md#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset") * [`bpy_struct.type_recast`](bpy_struct.md#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast") * [`bpy_struct.values`](bpy_struct.md#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values") |

## References[#](#references "Link to this heading")

|  |  |
| --- | --- |
| * [`AssetShelf.draw_context_menu`](AssetShelf.md#bpy.types.AssetShelf.draw_context_menu "bpy.types.AssetShelf.draw_context_menu") * [`AssetShelf.poll`](AssetShelf.md#bpy.types.AssetShelf.poll "bpy.types.AssetShelf.poll") * [`FileHandler.poll_drop`](FileHandler.md#bpy.types.FileHandler.poll_drop "bpy.types.FileHandler.poll_drop") * [`Gizmo.draw`](Gizmo.md#bpy.types.Gizmo.draw "bpy.types.Gizmo.draw") * [`Gizmo.draw_select`](Gizmo.md#bpy.types.Gizmo.draw_select "bpy.types.Gizmo.draw_select") * [`Gizmo.exit`](Gizmo.md#bpy.types.Gizmo.exit "bpy.types.Gizmo.exit") * [`Gizmo.invoke`](Gizmo.md#bpy.types.Gizmo.invoke "bpy.types.Gizmo.invoke") * [`Gizmo.modal`](Gizmo.md#bpy.types.Gizmo.modal "bpy.types.Gizmo.modal") * [`Gizmo.test_select`](Gizmo.md#bpy.types.Gizmo.test_select "bpy.types.Gizmo.test_select") * [`GizmoGroup.draw_prepare`](GizmoGroup.md#bpy.types.GizmoGroup.draw_prepare "bpy.types.GizmoGroup.draw_prepare") * [`GizmoGroup.invoke_prepare`](GizmoGroup.md#bpy.types.GizmoGroup.invoke_prepare "bpy.types.GizmoGroup.invoke_prepare") * [`GizmoGroup.poll`](GizmoGroup.md#bpy.types.GizmoGroup.poll "bpy.types.GizmoGroup.poll") * [`GizmoGroup.refresh`](GizmoGroup.md#bpy.types.GizmoGroup.refresh "bpy.types.GizmoGroup.refresh") * [`GizmoGroup.setup`](GizmoGroup.md#bpy.types.GizmoGroup.setup "bpy.types.GizmoGroup.setup") * [`Header.draw`](Header.md#bpy.types.Header.draw "bpy.types.Header.draw") * [`KeyingSetInfo.generate`](KeyingSetInfo.md#bpy.types.KeyingSetInfo.generate "bpy.types.KeyingSetInfo.generate") * [`KeyingSetInfo.iterator`](KeyingSetInfo.md#bpy.types.KeyingSetInfo.iterator "bpy.types.KeyingSetInfo.iterator") * [`KeyingSetInfo.poll`](KeyingSetInfo.md#bpy.types.KeyingSetInfo.poll "bpy.types.KeyingSetInfo.poll") * [`Macro.draw`](Macro.md#bpy.types.Macro.draw "bpy.types.Macro.draw") * [`Macro.poll`](Macro.md#bpy.types.Macro.poll "bpy.types.Macro.poll") * [`Menu.draw`](Menu.md#bpy.types.Menu.draw "bpy.types.Menu.draw") * [`Menu.poll`](Menu.md#bpy.types.Menu.poll "bpy.types.Menu.poll") * [`Node.draw_buttons`](Node.md#bpy.types.Node.draw_buttons "bpy.types.Node.draw_buttons") * [`Node.draw_buttons_ext`](Node.md#bpy.types.Node.draw_buttons_ext "bpy.types.Node.draw_buttons_ext") * [`Node.init`](Node.md#bpy.types.Node.init "bpy.types.Node.init") * [`Node.socket_value_update`](Node.md#bpy.types.Node.socket_value_update "bpy.types.Node.socket_value_update") * [`NodeInternal.draw_buttons`](NodeInternal.md#bpy.types.NodeInternal.draw_buttons "bpy.types.NodeInternal.draw_buttons") * [`NodeInternal.draw_buttons_ext`](NodeInternal.md#bpy.types.NodeInternal.draw_buttons_ext "bpy.types.NodeInternal.draw_buttons_ext") * [`NodeSocket.draw`](NodeSocket.md#bpy.types.NodeSocket.draw "bpy.types.NodeSocket.draw") * [`NodeSocket.draw_color`](NodeSocket.md#bpy.types.NodeSocket.draw_color "bpy.types.NodeSocket.draw_color") * [`NodeSocketStandard.draw`](NodeSocketStandard.md#bpy.types.NodeSocketStandard.draw "bpy.types.NodeSocketStandard.draw") * [`NodeSocketStandard.draw_color`](NodeSocketStandard.md#bpy.types.NodeSocketStandard.draw_color "bpy.types.NodeSocketStandard.draw_color") * [`NodeTree.get_from_context`](NodeTree.md#bpy.types.NodeTree.get_from_context "bpy.types.NodeTree.get_from_context") * [`NodeTree.interface_update`](NodeTree.md#bpy.types.NodeTree.interface_update "bpy.types.NodeTree.interface_update") * [`NodeTree.poll`](NodeTree.md#bpy.types.NodeTree.poll "bpy.types.NodeTree.poll") * [`NodeTreeInterfaceSocket.draw`](NodeTreeInterfaceSocket.md#bpy.types.NodeTreeInterfaceSocket.draw "bpy.types.NodeTreeInterfaceSocket.draw") * [`NodeTreeInterfaceSocketBool.draw`](NodeTreeInterfaceSocketBool.md#bpy.types.NodeTreeInterfaceSocketBool.draw "bpy.types.NodeTreeInterfaceSocketBool.draw") * [`NodeTreeInterfaceSocketCollection.draw`](NodeTreeInterfaceSocketCollection.md#bpy.types.NodeTreeInterfaceSocketCollection.draw "bpy.types.NodeTreeInterfaceSocketCollection.draw") * [`NodeTreeInterfaceSocketColor.draw`](NodeTreeInterfaceSocketColor.md#bpy.types.NodeTreeInterfaceSocketColor.draw "bpy.types.NodeTreeInterfaceSocketColor.draw") * [`NodeTreeInterfaceSocketFloat.draw`](NodeTreeInterfaceSocketFloat.md#bpy.types.NodeTreeInterfaceSocketFloat.draw "bpy.types.NodeTreeInterfaceSocketFloat.draw") * [`NodeTreeInterfaceSocketFloatAngle.draw`](NodeTreeInterfaceSocketFloatAngle.md#bpy.types.NodeTreeInterfaceSocketFloatAngle.draw "bpy.types.NodeTreeInterfaceSocketFloatAngle.draw") * [`NodeTreeInterfaceSocketFloatDistance.draw`](NodeTreeInterfaceSocketFloatDistance.md#bpy.types.NodeTreeInterfaceSocketFloatDistance.draw "bpy.types.NodeTreeInterfaceSocketFloatDistance.draw") * [`NodeTreeInterfaceSocketFloatFactor.draw`](NodeTreeInterfaceSocketFloatFactor.md#bpy.types.NodeTreeInterfaceSocketFloatFactor.draw "bpy.types.NodeTreeInterfaceSocketFloatFactor.draw") * [`NodeTreeInterfaceSocketFloatPercentage.draw`](NodeTreeInterfaceSocketFloatPercentage.md#bpy.types.NodeTreeInterfaceSocketFloatPercentage.draw "bpy.types.NodeTreeInterfaceSocketFloatPercentage.draw") * [`NodeTreeInterfaceSocketFloatTime.draw`](NodeTreeInterfaceSocketFloatTime.md#bpy.types.NodeTreeInterfaceSocketFloatTime.draw "bpy.types.NodeTreeInterfaceSocketFloatTime.draw") * [`NodeTreeInterfaceSocketFloatTimeAbsolute.draw`](NodeTreeInterfaceSocketFloatTimeAbsolute.md#bpy.types.NodeTreeInterfaceSocketFloatTimeAbsolute.draw "bpy.types.NodeTreeInterfaceSocketFloatTimeAbsolute.draw") * [`NodeTreeInterfaceSocketFloatUnsigned.draw`](NodeTreeInterfaceSocketFloatUnsigned.md#bpy.types.NodeTreeInterfaceSocketFloatUnsigned.draw "bpy.types.NodeTreeInterfaceSocketFloatUnsigned.draw") * [`NodeTreeInterfaceSocketFloatWavelength.draw`](NodeTreeInterfaceSocketFloatWavelength.md#bpy.types.NodeTreeInterfaceSocketFloatWavelength.draw "bpy.types.NodeTreeInterfaceSocketFloatWavelength.draw") * [`NodeTreeInterfaceSocketGeometry.draw`](NodeTreeInterfaceSocketGeometry.md#bpy.types.NodeTreeInterfaceSocketGeometry.draw "bpy.types.NodeTreeInterfaceSocketGeometry.draw") * [`NodeTreeInterfaceSocketImage.draw`](NodeTreeInterfaceSocketImage.md#bpy.types.NodeTreeInterfaceSocketImage.draw "bpy.types.NodeTreeInterfaceSocketImage.draw") * [`NodeTreeInterfaceSocketInt.draw`](NodeTreeInterfaceSocketInt.md#bpy.types.NodeTreeInterfaceSocketInt.draw "bpy.types.NodeTreeInterfaceSocketInt.draw") | * [`NodeTreeInterfaceSocketIntFactor.draw`](NodeTreeInterfaceSocketIntFactor.md#bpy.types.NodeTreeInterfaceSocketIntFactor.draw "bpy.types.NodeTreeInterfaceSocketIntFactor.draw") * [`NodeTreeInterfaceSocketIntPercentage.draw`](NodeTreeInterfaceSocketIntPercentage.md#bpy.types.NodeTreeInterfaceSocketIntPercentage.draw "bpy.types.NodeTreeInterfaceSocketIntPercentage.draw") * [`NodeTreeInterfaceSocketIntUnsigned.draw`](NodeTreeInterfaceSocketIntUnsigned.md#bpy.types.NodeTreeInterfaceSocketIntUnsigned.draw "bpy.types.NodeTreeInterfaceSocketIntUnsigned.draw") * [`NodeTreeInterfaceSocketMaterial.draw`](NodeTreeInterfaceSocketMaterial.md#bpy.types.NodeTreeInterfaceSocketMaterial.draw "bpy.types.NodeTreeInterfaceSocketMaterial.draw") * [`NodeTreeInterfaceSocketMatrix.draw`](NodeTreeInterfaceSocketMatrix.md#bpy.types.NodeTreeInterfaceSocketMatrix.draw "bpy.types.NodeTreeInterfaceSocketMatrix.draw") * [`NodeTreeInterfaceSocketMenu.draw`](NodeTreeInterfaceSocketMenu.md#bpy.types.NodeTreeInterfaceSocketMenu.draw "bpy.types.NodeTreeInterfaceSocketMenu.draw") * [`NodeTreeInterfaceSocketObject.draw`](NodeTreeInterfaceSocketObject.md#bpy.types.NodeTreeInterfaceSocketObject.draw "bpy.types.NodeTreeInterfaceSocketObject.draw") * [`NodeTreeInterfaceSocketRotation.draw`](NodeTreeInterfaceSocketRotation.md#bpy.types.NodeTreeInterfaceSocketRotation.draw "bpy.types.NodeTreeInterfaceSocketRotation.draw") * [`NodeTreeInterfaceSocketShader.draw`](NodeTreeInterfaceSocketShader.md#bpy.types.NodeTreeInterfaceSocketShader.draw "bpy.types.NodeTreeInterfaceSocketShader.draw") * [`NodeTreeInterfaceSocketString.draw`](NodeTreeInterfaceSocketString.md#bpy.types.NodeTreeInterfaceSocketString.draw "bpy.types.NodeTreeInterfaceSocketString.draw") * [`NodeTreeInterfaceSocketTexture.draw`](NodeTreeInterfaceSocketTexture.md#bpy.types.NodeTreeInterfaceSocketTexture.draw "bpy.types.NodeTreeInterfaceSocketTexture.draw") * [`NodeTreeInterfaceSocketVector.draw`](NodeTreeInterfaceSocketVector.md#bpy.types.NodeTreeInterfaceSocketVector.draw "bpy.types.NodeTreeInterfaceSocketVector.draw") * [`NodeTreeInterfaceSocketVectorAcceleration.draw`](NodeTreeInterfaceSocketVectorAcceleration.md#bpy.types.NodeTreeInterfaceSocketVectorAcceleration.draw "bpy.types.NodeTreeInterfaceSocketVectorAcceleration.draw") * [`NodeTreeInterfaceSocketVectorDirection.draw`](NodeTreeInterfaceSocketVectorDirection.md#bpy.types.NodeTreeInterfaceSocketVectorDirection.draw "bpy.types.NodeTreeInterfaceSocketVectorDirection.draw") * [`NodeTreeInterfaceSocketVectorEuler.draw`](NodeTreeInterfaceSocketVectorEuler.md#bpy.types.NodeTreeInterfaceSocketVectorEuler.draw "bpy.types.NodeTreeInterfaceSocketVectorEuler.draw") * [`NodeTreeInterfaceSocketVectorTranslation.draw`](NodeTreeInterfaceSocketVectorTranslation.md#bpy.types.NodeTreeInterfaceSocketVectorTranslation.draw "bpy.types.NodeTreeInterfaceSocketVectorTranslation.draw") * [`NodeTreeInterfaceSocketVectorVelocity.draw`](NodeTreeInterfaceSocketVectorVelocity.md#bpy.types.NodeTreeInterfaceSocketVectorVelocity.draw "bpy.types.NodeTreeInterfaceSocketVectorVelocity.draw") * [`NodeTreeInterfaceSocketVectorXYZ.draw`](NodeTreeInterfaceSocketVectorXYZ.md#bpy.types.NodeTreeInterfaceSocketVectorXYZ.draw "bpy.types.NodeTreeInterfaceSocketVectorXYZ.draw") * [`Operator.cancel`](Operator.md#bpy.types.Operator.cancel "bpy.types.Operator.cancel") * [`Operator.check`](Operator.md#bpy.types.Operator.check "bpy.types.Operator.check") * [`Operator.description`](Operator.md#bpy.types.Operator.description "bpy.types.Operator.description") * [`Operator.draw`](Operator.md#bpy.types.Operator.draw "bpy.types.Operator.draw") * [`Operator.execute`](Operator.md#bpy.types.Operator.execute "bpy.types.Operator.execute") * [`Operator.invoke`](Operator.md#bpy.types.Operator.invoke "bpy.types.Operator.invoke") * [`Operator.modal`](Operator.md#bpy.types.Operator.modal "bpy.types.Operator.modal") * [`Operator.poll`](Operator.md#bpy.types.Operator.poll "bpy.types.Operator.poll") * [`Panel.draw`](Panel.md#bpy.types.Panel.draw "bpy.types.Panel.draw") * [`Panel.draw_header`](Panel.md#bpy.types.Panel.draw_header "bpy.types.Panel.draw_header") * [`Panel.draw_header_preset`](Panel.md#bpy.types.Panel.draw_header_preset "bpy.types.Panel.draw_header_preset") * [`Panel.poll`](Panel.md#bpy.types.Panel.poll "bpy.types.Panel.poll") * [`RenderEngine.draw`](RenderEngine.md#bpy.types.RenderEngine.draw "bpy.types.RenderEngine.draw") * [`RenderEngine.view_draw`](RenderEngine.md#bpy.types.RenderEngine.view_draw "bpy.types.RenderEngine.view_draw") * [`RenderEngine.view_update`](RenderEngine.md#bpy.types.RenderEngine.view_update "bpy.types.RenderEngine.view_update") * [`UIList.draw_filter`](UIList.md#bpy.types.UIList.draw_filter "bpy.types.UIList.draw_filter") * [`UIList.draw_item`](UIList.md#bpy.types.UIList.draw_item "bpy.types.UIList.draw_item") * [`UIList.filter_items`](UIList.md#bpy.types.UIList.filter_items "bpy.types.UIList.filter_items") * [`XrSessionState.action_binding_create`](XrSessionState.md#bpy.types.XrSessionState.action_binding_create "bpy.types.XrSessionState.action_binding_create") * [`XrSessionState.action_create`](XrSessionState.md#bpy.types.XrSessionState.action_create "bpy.types.XrSessionState.action_create") * [`XrSessionState.action_set_create`](XrSessionState.md#bpy.types.XrSessionState.action_set_create "bpy.types.XrSessionState.action_set_create") * [`XrSessionState.action_state_get`](XrSessionState.md#bpy.types.XrSessionState.action_state_get "bpy.types.XrSessionState.action_state_get") * [`XrSessionState.active_action_set_set`](XrSessionState.md#bpy.types.XrSessionState.active_action_set_set "bpy.types.XrSessionState.active_action_set_set") * [`XrSessionState.controller_aim_location_get`](XrSessionState.md#bpy.types.XrSessionState.controller_aim_location_get "bpy.types.XrSessionState.controller_aim_location_get") * [`XrSessionState.controller_aim_rotation_get`](XrSessionState.md#bpy.types.XrSessionState.controller_aim_rotation_get "bpy.types.XrSessionState.controller_aim_rotation_get") * [`XrSessionState.controller_grip_location_get`](XrSessionState.md#bpy.types.XrSessionState.controller_grip_location_get "bpy.types.XrSessionState.controller_grip_location_get") * [`XrSessionState.controller_grip_rotation_get`](XrSessionState.md#bpy.types.XrSessionState.controller_grip_rotation_get "bpy.types.XrSessionState.controller_grip_rotation_get") * [`XrSessionState.controller_pose_actions_set`](XrSessionState.md#bpy.types.XrSessionState.controller_pose_actions_set "bpy.types.XrSessionState.controller_pose_actions_set") * [`XrSessionState.haptic_action_apply`](XrSessionState.md#bpy.types.XrSessionState.haptic_action_apply "bpy.types.XrSessionState.haptic_action_apply") * [`XrSessionState.haptic_action_stop`](XrSessionState.md#bpy.types.XrSessionState.haptic_action_stop "bpy.types.XrSessionState.haptic_action_stop") * [`XrSessionState.is_running`](XrSessionState.md#bpy.types.XrSessionState.is_running "bpy.types.XrSessionState.is_running") * [`XrSessionState.reset_to_base_pose`](XrSessionState.md#bpy.types.XrSessionState.reset_to_base_pose "bpy.types.XrSessionState.reset_to_base_pose") |

[Next

CopyLocationConstraint(Constraint)](CopyLocationConstraint.md)
[Previous

ConstraintTargetBone(bpy\_struct)](ConstraintTargetBone.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.Context.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.Context.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Context(bpy\_struct)
  + [`Context`](#bpy.types.Context)
    - [`Context.area`](#bpy.types.Context.area)
    - [`Context.asset`](#bpy.types.Context.asset)
    - [`Context.blend_data`](#bpy.types.Context.blend_data)
    - [`Context.collection`](#bpy.types.Context.collection)
    - [`Context.engine`](#bpy.types.Context.engine)
    - [`Context.gizmo_group`](#bpy.types.Context.gizmo_group)
    - [`Context.layer_collection`](#bpy.types.Context.layer_collection)
    - [`Context.mode`](#bpy.types.Context.mode)
    - [`Context.preferences`](#bpy.types.Context.preferences)
    - [`Context.region`](#bpy.types.Context.region)
    - [`Context.region_data`](#bpy.types.Context.region_data)
    - [`Context.region_popup`](#bpy.types.Context.region_popup)
    - [`Context.scene`](#bpy.types.Context.scene)
    - [`Context.screen`](#bpy.types.Context.screen)
    - [`Context.space_data`](#bpy.types.Context.space_data)
    - [`Context.tool_settings`](#bpy.types.Context.tool_settings)
    - [`Context.view_layer`](#bpy.types.Context.view_layer)
    - [`Context.window`](#bpy.types.Context.window)
    - [`Context.window_manager`](#bpy.types.Context.window_manager)
    - [`Context.workspace`](#bpy.types.Context.workspace)
    - [`Context.evaluated_depsgraph_get()`](#bpy.types.Context.evaluated_depsgraph_get)
    - [`Context.copy()`](#bpy.types.Context.copy)
    - [`Context.path_resolve()`](#bpy.types.Context.path_resolve)
    - [`Context.bl_rna_get_subclass()`](#bpy.types.Context.bl_rna_get_subclass)
    - [`Context.bl_rna_get_subclass_py()`](#bpy.types.Context.bl_rna_get_subclass_py)
    - [`Context.temp_override()`](#bpy.types.Context.temp_override)
  + [Inherited Properties](#inherited-properties)
  + [Inherited Functions](#inherited-functions)
  + [References](#references)