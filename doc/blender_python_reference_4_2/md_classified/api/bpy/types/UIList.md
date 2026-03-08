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

# UIList(bpy\_struct)[#](#uilist-bpy-struct "Link to this heading")

## Basic UIList Example[#](#basic-uilist-example "Link to this heading")

This script is the UIList subclass used to show material slots, with a bunch of additional commentaries.

Notice the name of the class, this naming convention is similar as the one for panels or menus.

Note

UIList subclasses must be registered for blender to use them.

```
import bpy

class MATERIAL_UL_matslots_example(bpy.types.UIList):
    # The draw_item function is called for each item of the collection that is visible in the list.
    #   data is the RNA object containing the collection,
    #   item is the current drawn item of the collection,
    #   icon is the "computed" icon for the item (as an integer, because some objects like materials or textures
    #   have custom icons ID, which are not available as enum items).
    #   active_data is the RNA object containing the active property for the collection (i.e. integer pointing to the
    #   active item of the collection).
    #   active_propname is the name of the active property (use 'getattr(active_data, active_propname)').
    #   index is index of the current item in the collection.
    #   flt_flag is the result of the filtering process for this item.
    #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
    #         need them.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        ob = data
        slot = item
        ma = slot.material
        # draw_item must handle the three layout types... Usually 'DEFAULT' and 'COMPACT' can share the same code.
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            # You should always start your row layout by a label (icon + text), or a non-embossed text field,
            # this will also make the row easily selectable in the list! The later also enables ctrl-click rename.
            # We use icon_value of label, as our given icon is an integer value, not an enum ID.
            # Note "data" names should never be translated!
            if ma:
                layout.prop(ma, "name", text="", emboss=False, icon_value=icon)
            else:
                layout.label(text="", translate=False, icon_value=icon)
        # 'GRID' layout type should be as compact as possible (typically a single icon!).
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

# And now we can use this list everywhere in Blender. Here is a small example panel.
class UIListPanelExample1(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "UIList Example 1 Panel"
    bl_idname = "OBJECT_PT_ui_list_example_1"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        # template_list now takes two new args.
        # The first one is the identifier of the registered UIList to use (if you want only the default list,
        # with no custom draw code, use "UI_UL_list").
        layout.template_list("MATERIAL_UL_matslots_example", "", obj, "material_slots", obj, "active_material_index")

        # The second one can usually be left as an empty string.
        # It's an additional ID used to distinguish lists in case you use the same list several times in a given area.
        layout.template_list("MATERIAL_UL_matslots_example", "compact", obj, "material_slots",
                             obj, "active_material_index", type='COMPACT')

def register():
    bpy.utils.register_class(MATERIAL_UL_matslots_example)
    bpy.utils.register_class(UIListPanelExample1)

def unregister():
    bpy.utils.unregister_class(UIListPanelExample1)
    bpy.utils.unregister_class(MATERIAL_UL_matslots_example)

if __name__ == "__main__":
    register()
```

## Advanced UIList Example - Filtering and Reordering[#](#advanced-uilist-example-filtering-and-reordering "Link to this heading")

This script is an extended version of the `UIList` subclass used to show vertex groups. It is not used ‘as is’,
because iterating over all vertices in a ‘draw’ function is a very bad idea for UI performances! However, it’s a good
example of how to create/use filtering/reordering callbacks.

```
import bpy

class MESH_UL_vgroups_slow(bpy.types.UIList):
    # Constants (flags)
    # Be careful not to shadow FILTER_ITEM!
    VGROUP_EMPTY = 1 << 0

    # Custom properties, saved with .blend file.
    use_filter_empty: bpy.props.BoolProperty(
        name="Filter Empty",
        default=False,
        options=set(),
        description="Whether to filter empty vertex groups",
    )
    use_filter_empty_reverse: bpy.props.BoolProperty(
        name="Reverse Empty",
        default=False,
        options=set(),
        description="Reverse empty filtering",
    )
    use_filter_name_reverse: bpy.props.BoolProperty(
        name="Reverse Name",
        default=False,
        options=set(),
        description="Reverse name filtering",
    )

    # This allows us to have mutually exclusive options, which are also all disable-able!
    def _gen_order_update(name1, name2):
        def _u(self, ctxt):
            if (getattr(self, name1)):
                setattr(self, name2, False)
        return _u
    use_order_name: bpy.props.BoolProperty(
        name="Name", default=False, options=set(),
        description="Sort groups by their name (case-insensitive)",
        update=_gen_order_update("use_order_name", "use_order_importance"),
    )
    use_order_importance: bpy.props.BoolProperty(
        name="Importance",
        default=False,
        options=set(),
        description="Sort groups by their average weight in the mesh",
        update=_gen_order_update("use_order_importance", "use_order_name"),
    )

    # Usual draw item function.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
        # Just in case, we do not use it here!
        self.use_filter_invert = False

        # assert(isinstance(item, bpy.types.VertexGroup)
        vgroup = item
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            # Here we use one feature of new filtering feature: it can pass data to draw_item, through flt_flag
            # parameter, which contains exactly what filter_items set in its filter list for this item!
            # In this case, we show empty groups grayed out.
            if flt_flag & self.VGROUP_EMPTY:
                col = layout.column()
                col.enabled = False
                col.alignment = 'LEFT'
                col.prop(vgroup, "name", text="", emboss=False, icon_value=icon)
            else:
                layout.prop(vgroup, "name", text="", emboss=False, icon_value=icon)
            icon = 'LOCKED' if vgroup.lock_weight else 'UNLOCKED'
            layout.prop(vgroup, "lock_weight", text="", icon=icon, emboss=False)
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            if flt_flag & self.VGROUP_EMPTY:
                layout.enabled = False
            layout.label(text="", icon_value=icon)

    def draw_filter(self, context, layout):
        # Nothing much to say here, it's usual UI code...
        row = layout.row()

        subrow = row.row(align=True)
        subrow.prop(self, "filter_name", text="")
        icon = 'ZOOM_OUT' if self.use_filter_name_reverse else 'ZOOM_IN'
        subrow.prop(self, "use_filter_name_reverse", text="", icon=icon)

        subrow = row.row(align=True)
        subrow.prop(self, "use_filter_empty", toggle=True)
        icon = 'ZOOM_OUT' if self.use_filter_empty_reverse else 'ZOOM_IN'
        subrow.prop(self, "use_filter_empty_reverse", text="", icon=icon)

        row = layout.row(align=True)
        row.label(text="Order by:")
        row.prop(self, "use_order_name", toggle=True)
        row.prop(self, "use_order_importance", toggle=True)
        icon = 'TRIA_UP' if self.use_filter_orderby_invert else 'TRIA_DOWN'
        row.prop(self, "use_filter_orderby_invert", text="", icon=icon)

    def filter_items_empty_vgroups(self, context, vgroups):
        # This helper function checks vgroups to find out whether they are empty, and what's their average weights.
        # TODO: This should be RNA helper actually (a vgroup prop like "raw_data: ((vidx, vweight), etc.)").
        #       Too slow for python!
        obj_data = context.active_object.data
        ret = {vg.index: [True, 0.0] for vg in vgroups}
        if hasattr(obj_data, "vertices"):  # Mesh data
            if obj_data.is_editmode:
                import bmesh
                bm = bmesh.from_edit_mesh(obj_data)
                # only ever one deform weight layer
                dvert_lay = bm.verts.layers.deform.active
                fact = 1 / len(bm.verts)
                if dvert_lay:
                    for v in bm.verts:
                        for vg_idx, vg_weight in v[dvert_lay].items():
                            ret[vg_idx][0] = False
                            ret[vg_idx][1] += vg_weight * fact
            else:
                fact = 1 / len(obj_data.vertices)
                for v in obj_data.vertices:
                    for vg in v.groups:
                        ret[vg.group][0] = False
                        ret[vg.group][1] += vg.weight * fact
        elif hasattr(obj_data, "points"):  # Lattice data
            # XXX no access to lattice editdata?
            fact = 1 / len(obj_data.points)
            for v in obj_data.points:
                for vg in v.groups:
                    ret[vg.group][0] = False
                    ret[vg.group][1] += vg.weight * fact
        return ret

    def filter_items(self, context, data, propname):
        # This function gets the collection property (as the usual tuple (data, propname)), and must return two lists:
        # * The first one is for filtering, it must contain 32bit integers were self.bitflag_filter_item marks the
        #   matching item as filtered (i.e. to be shown). The upper 16 bits (including self.bitflag_filter_item) are
        #   reserved for internal use, the lower 16 bits are free for custom use. Here we use the first bit to mark
        #   VGROUP_EMPTY.
        # * The second one is for reordering, it must return a list containing the new indices of the items (which
        #   gives us a mapping org_idx -> new_idx).
        # Please note that the default UI_UL_list defines helper functions for common tasks (see its doc for more info).
        # If you do not make filtering and/or ordering, return empty list(s) (this will be more efficient than
        # returning full lists doing nothing!).
        vgroups = getattr(data, propname)
        helper_funcs = bpy.types.UI_UL_list

        # Default return values.
        flt_flags = []
        flt_neworder = []

        # Pre-compute of vgroups data, CPU-intensive. :/
        vgroups_empty = self.filter_items_empty_vgroups(context, vgroups)

        # Filtering by name
        if self.filter_name:
            flt_flags = helper_funcs.filter_items_by_name(self.filter_name, self.bitflag_filter_item, vgroups, "name",
                                                          reverse=self.use_filter_name_reverse)
        if not flt_flags:
            flt_flags = [self.bitflag_filter_item] * len(vgroups)

        # Filter by emptiness.
        for idx, vg in enumerate(vgroups):
            if vgroups_empty[vg.index][0]:
                flt_flags[idx] |= self.VGROUP_EMPTY
                if self.use_filter_empty and self.use_filter_empty_reverse:
                    flt_flags[idx] &= ~self.bitflag_filter_item
            elif self.use_filter_empty and not self.use_filter_empty_reverse:
                flt_flags[idx] &= ~self.bitflag_filter_item

        # Reorder by name or average weight.
        if self.use_order_name:
            flt_neworder = helper_funcs.sort_items_by_name(vgroups, "name")
        elif self.use_order_importance:
            _sort = [(idx, vgroups_empty[vg.index][1]) for idx, vg in enumerate(vgroups)]
            flt_neworder = helper_funcs.sort_items_helper(_sort, lambda e: e[1], True)

        return flt_flags, flt_neworder

# Minimal code to use above UIList...
class UIListPanelExample2(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "UIList Example 2 Panel"
    bl_idname = "OBJECT_PT_ui_list_example_2"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # template_list now takes two new args.
        # The first one is the identifier of the registered UIList to use (if you want only the default list,
        # with no custom draw code, use "UI_UL_list").
        layout.template_list("MESH_UL_vgroups_slow", "", obj, "vertex_groups", obj.vertex_groups, "active_index")

def register():
    bpy.utils.register_class(MESH_UL_vgroups_slow)
    bpy.utils.register_class(UIListPanelExample2)

def unregister():
    bpy.utils.unregister_class(UIListPanelExample2)
    bpy.utils.unregister_class(MESH_UL_vgroups_slow)

if __name__ == "__main__":
    register()
```

base class — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct")

subclasses —
[`ASSETBROWSER_UL_metadata_tags`](ASSETBROWSER_UL_metadata_tags.md#bpy.types.ASSETBROWSER_UL_metadata_tags "bpy.types.ASSETBROWSER_UL_metadata_tags"), [`CLIP_UL_tracking_objects`](CLIP_UL_tracking_objects.md#bpy.types.CLIP_UL_tracking_objects "bpy.types.CLIP_UL_tracking_objects"), [`CURVES_UL_attributes`](CURVES_UL_attributes.md#bpy.types.CURVES_UL_attributes "bpy.types.CURVES_UL_attributes"), [`DATA_UL_bone_collections`](DATA_UL_bone_collections.md#bpy.types.DATA_UL_bone_collections "bpy.types.DATA_UL_bone_collections"), [`FILEBROWSER_UL_dir`](FILEBROWSER_UL_dir.md#bpy.types.FILEBROWSER_UL_dir "bpy.types.FILEBROWSER_UL_dir"), [`GPENCIL_UL_annotation_layer`](GPENCIL_UL_annotation_layer.md#bpy.types.GPENCIL_UL_annotation_layer "bpy.types.GPENCIL_UL_annotation_layer"), [`GPENCIL_UL_layer`](GPENCIL_UL_layer.md#bpy.types.GPENCIL_UL_layer "bpy.types.GPENCIL_UL_layer"), [`GPENCIL_UL_masks`](GPENCIL_UL_masks.md#bpy.types.GPENCIL_UL_masks "bpy.types.GPENCIL_UL_masks"), [`GPENCIL_UL_matslots`](GPENCIL_UL_matslots.md#bpy.types.GPENCIL_UL_matslots "bpy.types.GPENCIL_UL_matslots"), [`GPENCIL_UL_vgroups`](GPENCIL_UL_vgroups.md#bpy.types.GPENCIL_UL_vgroups "bpy.types.GPENCIL_UL_vgroups"), [`GREASE_PENCIL_UL_masks`](GREASE_PENCIL_UL_masks.md#bpy.types.GREASE_PENCIL_UL_masks "bpy.types.GREASE_PENCIL_UL_masks"), [`IMAGE_UL_render_slots`](IMAGE_UL_render_slots.md#bpy.types.IMAGE_UL_render_slots "bpy.types.IMAGE_UL_render_slots"), [`IMAGE_UL_udim_tiles`](IMAGE_UL_udim_tiles.md#bpy.types.IMAGE_UL_udim_tiles "bpy.types.IMAGE_UL_udim_tiles"), [`MASK_UL_layers`](MASK_UL_layers.md#bpy.types.MASK_UL_layers "bpy.types.MASK_UL_layers"), [`MATERIAL_UL_matslots`](MATERIAL_UL_matslots.md#bpy.types.MATERIAL_UL_matslots "bpy.types.MATERIAL_UL_matslots"), [`MESH_UL_attributes`](MESH_UL_attributes.md#bpy.types.MESH_UL_attributes "bpy.types.MESH_UL_attributes"), [`MESH_UL_color_attributes`](MESH_UL_color_attributes.md#bpy.types.MESH_UL_color_attributes "bpy.types.MESH_UL_color_attributes"), [`MESH_UL_color_attributes_selector`](MESH_UL_color_attributes_selector.md#bpy.types.MESH_UL_color_attributes_selector "bpy.types.MESH_UL_color_attributes_selector"), [`MESH_UL_shape_keys`](MESH_UL_shape_keys.md#bpy.types.MESH_UL_shape_keys "bpy.types.MESH_UL_shape_keys"), [`MESH_UL_uvmaps`](MESH_UL_uvmaps.md#bpy.types.MESH_UL_uvmaps "bpy.types.MESH_UL_uvmaps"), [`MESH_UL_vgroups`](MESH_UL_vgroups.md#bpy.types.MESH_UL_vgroups "bpy.types.MESH_UL_vgroups"), [`PARTICLE_UL_particle_systems`](PARTICLE_UL_particle_systems.md#bpy.types.PARTICLE_UL_particle_systems "bpy.types.PARTICLE_UL_particle_systems"), [`PHYSICS_UL_dynapaint_surfaces`](PHYSICS_UL_dynapaint_surfaces.md#bpy.types.PHYSICS_UL_dynapaint_surfaces "bpy.types.PHYSICS_UL_dynapaint_surfaces"), [`POINTCLOUD_UL_attributes`](POINTCLOUD_UL_attributes.md#bpy.types.POINTCLOUD_UL_attributes "bpy.types.POINTCLOUD_UL_attributes"), [`POSE_UL_selection_set`](POSE_UL_selection_set.md#bpy.types.POSE_UL_selection_set "bpy.types.POSE_UL_selection_set"), [`RENDER_UL_renderviews`](RENDER_UL_renderviews.md#bpy.types.RENDER_UL_renderviews "bpy.types.RENDER_UL_renderviews"), [`SCENE_UL_gltf2_filter_action`](SCENE_UL_gltf2_filter_action.md#bpy.types.SCENE_UL_gltf2_filter_action "bpy.types.SCENE_UL_gltf2_filter_action"), [`SCENE_UL_keying_set_paths`](SCENE_UL_keying_set_paths.md#bpy.types.SCENE_UL_keying_set_paths "bpy.types.SCENE_UL_keying_set_paths"), [`TEXTURE_UL_texpaintslots`](TEXTURE_UL_texpaintslots.md#bpy.types.TEXTURE_UL_texpaintslots "bpy.types.TEXTURE_UL_texpaintslots"), [`TEXTURE_UL_texslots`](TEXTURE_UL_texslots.md#bpy.types.TEXTURE_UL_texslots "bpy.types.TEXTURE_UL_texslots"), [`UI_UL_list`](UI_UL_list.md#bpy.types.UI_UL_list "bpy.types.UI_UL_list"), [`USERPREF_UL_asset_libraries`](USERPREF_UL_asset_libraries.md#bpy.types.USERPREF_UL_asset_libraries "bpy.types.USERPREF_UL_asset_libraries"), [`USERPREF_UL_extension_repos`](USERPREF_UL_extension_repos.md#bpy.types.USERPREF_UL_extension_repos "bpy.types.USERPREF_UL_extension_repos"), [`VIEWLAYER_UL_aov`](VIEWLAYER_UL_aov.md#bpy.types.VIEWLAYER_UL_aov "bpy.types.VIEWLAYER_UL_aov"), [`VIEWLAYER_UL_linesets`](VIEWLAYER_UL_linesets.md#bpy.types.VIEWLAYER_UL_linesets "bpy.types.VIEWLAYER_UL_linesets"), [`VOLUME_UL_grids`](VOLUME_UL_grids.md#bpy.types.VOLUME_UL_grids "bpy.types.VOLUME_UL_grids"), [`WORKSPACE_UL_addons_items`](WORKSPACE_UL_addons_items.md#bpy.types.WORKSPACE_UL_addons_items "bpy.types.WORKSPACE_UL_addons_items")

*class* bpy.types.UIList(*bpy\_struct*)[#](#bpy.types.UIList "Link to this definition")
:   UI list containing the elements of a collection

    bitflag\_filter\_item[#](#bpy.types.UIList.bitflag_filter_item "Link to this definition")
    :   The value of the reserved bitflag ‘FILTER\_ITEM’ (in filter\_flags values)

        Type:
        :   int in [0, inf], default 0, (readonly)

    bl\_idname[#](#bpy.types.UIList.bl_idname "Link to this definition")
    :   If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is “OBJECT\_UL\_vgroups”, and bl\_idname is not set by the script, then bl\_idname = “OBJECT\_UL\_vgroups”)

        Type:
        :   string, default “”, (never None)

    filter\_name[#](#bpy.types.UIList.filter_name "Link to this definition")
    :   Only show items matching this name (use ‘\*’ as wildcard)

        Type:
        :   string, default “”, (never None)

    layout\_type[#](#bpy.types.UIList.layout_type "Link to this definition")
    :   Type:
        :   enum in [Uilist Layout Type Items](../../../appendix/bpy_types_enum_items/uilist_layout_type_items.md#rna-enum-uilist-layout-type-items), default ‘DEFAULT’, (readonly)

    list\_id[#](#bpy.types.UIList.list_id "Link to this definition")
    :   Identifier of the list, if any was passed to the “list\_id” parameter of “template\_list()”

        Type:
        :   string, default “”, (readonly, never None)

    use\_filter\_invert[#](#bpy.types.UIList.use_filter_invert "Link to this definition")
    :   Invert filtering (show hidden items, and vice versa)

        Type:
        :   boolean, default False

    use\_filter\_show[#](#bpy.types.UIList.use_filter_show "Link to this definition")
    :   Show filtering options

        Type:
        :   boolean, default False

    use\_filter\_sort\_alpha[#](#bpy.types.UIList.use_filter_sort_alpha "Link to this definition")
    :   Sort items by their name

        Type:
        :   boolean, default False

    use\_filter\_sort\_lock[#](#bpy.types.UIList.use_filter_sort_lock "Link to this definition")
    :   Lock the order of shown items (user cannot change it)

        Type:
        :   boolean, default False

    use\_filter\_sort\_reverse[#](#bpy.types.UIList.use_filter_sort_reverse "Link to this definition")
    :   Reverse the order of shown items

        Type:
        :   boolean, default False

    draw\_item(*context*, *layout*, *data*, *item*, *icon*, *active\_data*, *active\_property*, *index=0*, *flt\_flag=0*)[#](#bpy.types.UIList.draw_item "Link to this definition")
    :   Draw an item in the list (NOTE: when you define your own draw\_item function, you may want to check given ‘item’ is of the right type…)

        Parameters:
        :   * **layout** ([`UILayout`](UILayout.md#bpy.types.UILayout "bpy.types.UILayout"), (never None)) – Layout to draw the item
            * **data** ([`AnyType`](AnyType.md#bpy.types.AnyType "bpy.types.AnyType")) – Data from which to take Collection property
            * **item** ([`AnyType`](AnyType.md#bpy.types.AnyType "bpy.types.AnyType")) – Item of the collection property
            * **icon** (*int in* *[**0**,* *inf**]*) – Icon of the item in the collection
            * **active\_data** ([`AnyType`](AnyType.md#bpy.types.AnyType "bpy.types.AnyType"), (never None)) – Data from which to take property for the active element
            * **active\_property** (*string**,* *(**optional argument**,* *never None**)*) – Identifier of property in active\_data, for the active element
            * **index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Index of the item in the collection
            * **flt\_flag** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – The filter-flag result for this item

    draw\_filter(*context*, *layout*)[#](#bpy.types.UIList.draw_filter "Link to this definition")
    :   Draw filtering options

        Parameters:
        :   **layout** ([`UILayout`](UILayout.md#bpy.types.UILayout "bpy.types.UILayout"), (never None)) – Layout to draw the item

    filter\_items(*context*, *data*, *property*)[#](#bpy.types.UIList.filter_items "Link to this definition")
    :   Filter and/or re-order items of the collection (output filter results in filter\_flags, and reorder results in filter\_neworder arrays)

        Parameters:
        :   * **data** ([`AnyType`](AnyType.md#bpy.types.AnyType "bpy.types.AnyType")) – Data from which to take Collection property
            * **property** (*string**,* *(**never None**)*) – Identifier of property in data, for the collection

        Return (filter\_flags, filter\_neworder):
        :   filter\_flags, An array of filter flags, one for each item in the collection (NOTE: The upper 16 bits, including FILTER\_ITEM, are reserved, only use the lower 16 bits for custom usages), int array of 1 items in [0, inf]

            filter\_neworder, An array of indices, one for each item in the collection, mapping the org index to the new one, int array of 1 items in [0, inf]

    *classmethod* append(*draw\_func*)[#](#bpy.types.UIList.append "Link to this definition")
    :   Append a draw function to this menu,
        takes the same arguments as the menus draw function

    *classmethod* is\_extended()[#](#bpy.types.UIList.is_extended "Link to this definition")

    *classmethod* prepend(*draw\_func*)[#](#bpy.types.UIList.prepend "Link to this definition")
    :   Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

    *classmethod* remove(*draw\_func*)[#](#bpy.types.UIList.remove "Link to this definition")
    :   Remove a draw function that has been added to this menu

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.UIList.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.UIList.bl_rna_get_subclass_py "Link to this definition")
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

UIPieMenu(bpy\_struct)](UIPieMenu.md)
[Previous

UILayout(bpy\_struct)](UILayout.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.UIList.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.UIList.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* UIList(bpy\_struct)
  + [Basic UIList Example](#basic-uilist-example)
  + [Advanced UIList Example - Filtering and Reordering](#advanced-uilist-example-filtering-and-reordering)
    - [`UIList`](#bpy.types.UIList)
      * [`UIList.bitflag_filter_item`](#bpy.types.UIList.bitflag_filter_item)
      * [`UIList.bl_idname`](#bpy.types.UIList.bl_idname)
      * [`UIList.filter_name`](#bpy.types.UIList.filter_name)
      * [`UIList.layout_type`](#bpy.types.UIList.layout_type)
      * [`UIList.list_id`](#bpy.types.UIList.list_id)
      * [`UIList.use_filter_invert`](#bpy.types.UIList.use_filter_invert)
      * [`UIList.use_filter_show`](#bpy.types.UIList.use_filter_show)
      * [`UIList.use_filter_sort_alpha`](#bpy.types.UIList.use_filter_sort_alpha)
      * [`UIList.use_filter_sort_lock`](#bpy.types.UIList.use_filter_sort_lock)
      * [`UIList.use_filter_sort_reverse`](#bpy.types.UIList.use_filter_sort_reverse)
      * [`UIList.draw_item()`](#bpy.types.UIList.draw_item)
      * [`UIList.draw_filter()`](#bpy.types.UIList.draw_filter)
      * [`UIList.filter_items()`](#bpy.types.UIList.filter_items)
      * [`UIList.append()`](#bpy.types.UIList.append)
      * [`UIList.is_extended()`](#bpy.types.UIList.is_extended)
      * [`UIList.prepend()`](#bpy.types.UIList.prepend)
      * [`UIList.remove()`](#bpy.types.UIList.remove)
      * [`UIList.bl_rna_get_subclass()`](#bpy.types.UIList.bl_rna_get_subclass)
      * [`UIList.bl_rna_get_subclass_py()`](#bpy.types.UIList.bl_rna_get_subclass_py)
    - [Inherited Properties](#inherited-properties)
    - [Inherited Functions](#inherited-functions)