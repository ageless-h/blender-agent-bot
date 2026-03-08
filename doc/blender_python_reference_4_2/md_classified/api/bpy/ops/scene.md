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
* [Operators (bpy.ops)](index.md)[x]
* [Types (bpy.types)](../types/index.md)[ ]
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

# Scene Operators[#](#module-bpy.ops.scene "Link to this heading")

bpy.ops.scene.delete()[#](#bpy.ops.scene.delete "Link to this definition")
:   Delete active scene

bpy.ops.scene.freestyle\_add\_edge\_marks\_to\_keying\_set()[#](#bpy.ops.scene.freestyle_add_edge_marks_to_keying_set "Link to this definition")
:   Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set

    File:
    :   [startup/bl\_operators/freestyle.py:136](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L136)

bpy.ops.scene.freestyle\_add\_face\_marks\_to\_keying\_set()[#](#bpy.ops.scene.freestyle_add_face_marks_to_keying_set "Link to this definition")
:   Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set

    File:
    :   [startup/bl\_operators/freestyle.py:167](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L167)

bpy.ops.scene.freestyle\_alpha\_modifier\_add(*type='ALONG\_STROKE'*)[#](#bpy.ops.scene.freestyle_alpha_modifier_add "Link to this definition")
:   Add an alpha transparency modifier to the line style associated with the active lineset

    Parameters:
    :   **type** (enum in [Linestyle Alpha Modifier Type Items](../../../appendix/bpy_types_enum_items/linestyle_alpha_modifier_type_items.md#rna-enum-linestyle-alpha-modifier-type-items), (optional)) – Type

bpy.ops.scene.freestyle\_color\_modifier\_add(*type='ALONG\_STROKE'*)[#](#bpy.ops.scene.freestyle_color_modifier_add "Link to this definition")
:   Add a line color modifier to the line style associated with the active lineset

    Parameters:
    :   **type** (enum in [Linestyle Color Modifier Type Items](../../../appendix/bpy_types_enum_items/linestyle_color_modifier_type_items.md#rna-enum-linestyle-color-modifier-type-items), (optional)) – Type

bpy.ops.scene.freestyle\_fill\_range\_by\_selection(*type='COLOR'*, *name=''*)[#](#bpy.ops.scene.freestyle_fill_range_by_selection "Link to this definition")
:   Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)

    Parameters:
    :   * **type** (*enum in* *[**'COLOR'**,* *'ALPHA'**,* *'THICKNESS'**]**,* *(**optional**)*) –

          Type, Type of the modifier to work on

          + `COLOR`
            Color – Color modifier type.
          + `ALPHA`
            Alpha – Alpha modifier type.
          + `THICKNESS`
            Thickness – Thickness modifier type.
        * **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the modifier to work on

    File:
    :   [startup/bl\_operators/freestyle.py:42](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L42)

bpy.ops.scene.freestyle\_geometry\_modifier\_add(*type='2D\_OFFSET'*)[#](#bpy.ops.scene.freestyle_geometry_modifier_add "Link to this definition")
:   Add a stroke geometry modifier to the line style associated with the active lineset

    Parameters:
    :   **type** (enum in [Linestyle Geometry Modifier Type Items](../../../appendix/bpy_types_enum_items/linestyle_geometry_modifier_type_items.md#rna-enum-linestyle-geometry-modifier-type-items), (optional)) – Type

bpy.ops.scene.freestyle\_lineset\_add()[#](#bpy.ops.scene.freestyle_lineset_add "Link to this definition")
:   Add a line set into the list of line sets

bpy.ops.scene.freestyle\_lineset\_copy()[#](#bpy.ops.scene.freestyle_lineset_copy "Link to this definition")
:   Copy the active line set to the internal clipboard

bpy.ops.scene.freestyle\_lineset\_move(*direction='UP'*)[#](#bpy.ops.scene.freestyle_lineset_move "Link to this definition")
:   Change the position of the active line set within the list of line sets

    Parameters:
    :   **direction** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Direction, Direction to move the active line set towards

bpy.ops.scene.freestyle\_lineset\_paste()[#](#bpy.ops.scene.freestyle_lineset_paste "Link to this definition")
:   Paste the internal clipboard content to the active line set

bpy.ops.scene.freestyle\_lineset\_remove()[#](#bpy.ops.scene.freestyle_lineset_remove "Link to this definition")
:   Remove the active line set from the list of line sets

bpy.ops.scene.freestyle\_linestyle\_new()[#](#bpy.ops.scene.freestyle_linestyle_new "Link to this definition")
:   Create a new line style, reusable by multiple line sets

bpy.ops.scene.freestyle\_modifier\_copy()[#](#bpy.ops.scene.freestyle_modifier_copy "Link to this definition")
:   Duplicate the modifier within the list of modifiers

bpy.ops.scene.freestyle\_modifier\_move(*direction='UP'*)[#](#bpy.ops.scene.freestyle_modifier_move "Link to this definition")
:   Move the modifier within the list of modifiers

    Parameters:
    :   **direction** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Direction, Direction to move the chosen modifier towards

bpy.ops.scene.freestyle\_modifier\_remove()[#](#bpy.ops.scene.freestyle_modifier_remove "Link to this definition")
:   Remove the modifier from the list of modifiers

bpy.ops.scene.freestyle\_module\_add()[#](#bpy.ops.scene.freestyle_module_add "Link to this definition")
:   Add a style module into the list of modules

bpy.ops.scene.freestyle\_module\_move(*direction='UP'*)[#](#bpy.ops.scene.freestyle_module_move "Link to this definition")
:   Change the position of the style module within in the list of style modules

    Parameters:
    :   **direction** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Direction, Direction to move the chosen style module towards

bpy.ops.scene.freestyle\_module\_open(*filepath=''*, *make\_internal=True*)[#](#bpy.ops.scene.freestyle_module_open "Link to this definition")
:   Open a style module file

    Parameters:
    :   * **filepath** (*string**,* *(**optional**,* *never None**)*) – filepath
        * **make\_internal** (*boolean**,* *(**optional**)*) – Make internal, Make module file internal after loading

    File:
    :   [startup/bl\_operators/freestyle.py:211](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/freestyle.py#L211)

bpy.ops.scene.freestyle\_module\_remove()[#](#bpy.ops.scene.freestyle_module_remove "Link to this definition")
:   Remove the style module from the stack

bpy.ops.scene.freestyle\_stroke\_material\_create()[#](#bpy.ops.scene.freestyle_stroke_material_create "Link to this definition")
:   Create Freestyle stroke material for testing

bpy.ops.scene.freestyle\_thickness\_modifier\_add(*type='ALONG\_STROKE'*)[#](#bpy.ops.scene.freestyle_thickness_modifier_add "Link to this definition")
:   Add a line thickness modifier to the line style associated with the active lineset

    Parameters:
    :   **type** (enum in [Linestyle Thickness Modifier Type Items](../../../appendix/bpy_types_enum_items/linestyle_thickness_modifier_type_items.md#rna-enum-linestyle-thickness-modifier-type-items), (optional)) – Type

bpy.ops.scene.gltf2\_action\_filter\_refresh()[#](#bpy.ops.scene.gltf2_action_filter_refresh "Link to this definition")
:   Refresh list of actions

    File:
    :   [addons\_core/io\_scene\_gltf2/blender/com/gltf2\_blender\_ui.py:596](https://projects.blender.org/blender/blender-addons/addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py#L596)

bpy.ops.scene.gpencil\_brush\_preset\_add(*name=''*, *remove\_name=False*, *remove\_active=False*)[#](#bpy.ops.scene.gpencil_brush_preset_add "Link to this definition")
:   Add or remove grease pencil brush preset

    Parameters:
    :   * **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the preset, used to make the path name
        * **remove\_name** (*boolean**,* *(**optional**)*) – remove\_name
        * **remove\_active** (*boolean**,* *(**optional**)*) – remove\_active

    File:
    :   [startup/bl\_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.scene.gpencil\_material\_preset\_add(*name=''*, *remove\_name=False*, *remove\_active=False*)[#](#bpy.ops.scene.gpencil_material_preset_add "Link to this definition")
:   Add or remove grease pencil material preset

    Parameters:
    :   * **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the preset, used to make the path name
        * **remove\_name** (*boolean**,* *(**optional**)*) – remove\_name
        * **remove\_active** (*boolean**,* *(**optional**)*) – remove\_active

    File:
    :   [startup/bl\_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.scene.new(*type='NEW'*)[#](#bpy.ops.scene.new "Link to this definition")
:   Add new scene by type

    Parameters:
    :   **type** (*enum in* *[**'NEW'**,* *'EMPTY'**,* *'LINK\_COPY'**,* *'FULL\_COPY'**]**,* *(**optional**)*) –

        Type

        * `NEW`
          New – Add a new, empty scene with default settings.
        * `EMPTY`
          Copy Settings – Add a new, empty scene, and copy settings from the current scene.
        * `LINK_COPY`
          Linked Copy – Link in the collections from the current scene (shallow copy).
        * `FULL_COPY`
          Full Copy – Make a full copy of the current scene.

bpy.ops.scene.new\_sequencer(*type='NEW'*)[#](#bpy.ops.scene.new_sequencer "Link to this definition")
:   Add new scene by type in the sequence editor and assign to active strip

    Parameters:
    :   **type** (*enum in* *[**'NEW'**,* *'EMPTY'**,* *'LINK\_COPY'**,* *'FULL\_COPY'**]**,* *(**optional**)*) –

        Type

        * `NEW`
          New – Add a new, empty scene with default settings.
        * `EMPTY`
          Copy Settings – Add a new, empty scene, and copy settings from the current scene.
        * `LINK_COPY`
          Linked Copy – Link in the collections from the current scene (shallow copy).
        * `FULL_COPY`
          Full Copy – Make a full copy of the current scene.

bpy.ops.scene.render\_view\_add()[#](#bpy.ops.scene.render_view_add "Link to this definition")
:   Add a render view

bpy.ops.scene.render\_view\_remove()[#](#bpy.ops.scene.render_view_remove "Link to this definition")
:   Remove the selected render view

bpy.ops.scene.view\_layer\_add(*type='NEW'*)[#](#bpy.ops.scene.view_layer_add "Link to this definition")
:   Add a view layer

    Parameters:
    :   **type** (*enum in* *[**'NEW'**,* *'COPY'**,* *'EMPTY'**]**,* *(**optional**)*) –

        Type

        * `NEW`
          New – Add a new view layer.
        * `COPY`
          Copy Settings – Copy settings of current view layer.
        * `EMPTY`
          Blank – Add a new view layer with all collections disabled.

bpy.ops.scene.view\_layer\_add\_aov()[#](#bpy.ops.scene.view_layer_add_aov "Link to this definition")
:   Add a Shader AOV

bpy.ops.scene.view\_layer\_add\_lightgroup(*name=''*)[#](#bpy.ops.scene.view_layer_add_lightgroup "Link to this definition")
:   Add a Light Group

    Parameters:
    :   **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of newly created lightgroup

bpy.ops.scene.view\_layer\_add\_used\_lightgroups()[#](#bpy.ops.scene.view_layer_add_used_lightgroups "Link to this definition")
:   Add all used Light Groups

bpy.ops.scene.view\_layer\_remove()[#](#bpy.ops.scene.view_layer_remove "Link to this definition")
:   Remove the selected view layer

bpy.ops.scene.view\_layer\_remove\_aov()[#](#bpy.ops.scene.view_layer_remove_aov "Link to this definition")
:   Remove Active AOV

bpy.ops.scene.view\_layer\_remove\_lightgroup()[#](#bpy.ops.scene.view_layer_remove_lightgroup "Link to this definition")
:   Remove Active Lightgroup

bpy.ops.scene.view\_layer\_remove\_unused\_lightgroups()[#](#bpy.ops.scene.view_layer_remove_unused_lightgroups "Link to this definition")
:   Remove all unused Light Groups

[Next

Screen Operators](screen.md)
[Previous

Rigidbody Operators](rigidbody.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.scene.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.scene.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Scene Operators
  + [`delete()`](#bpy.ops.scene.delete)
  + [`freestyle_add_edge_marks_to_keying_set()`](#bpy.ops.scene.freestyle_add_edge_marks_to_keying_set)
  + [`freestyle_add_face_marks_to_keying_set()`](#bpy.ops.scene.freestyle_add_face_marks_to_keying_set)
  + [`freestyle_alpha_modifier_add()`](#bpy.ops.scene.freestyle_alpha_modifier_add)
  + [`freestyle_color_modifier_add()`](#bpy.ops.scene.freestyle_color_modifier_add)
  + [`freestyle_fill_range_by_selection()`](#bpy.ops.scene.freestyle_fill_range_by_selection)
  + [`freestyle_geometry_modifier_add()`](#bpy.ops.scene.freestyle_geometry_modifier_add)
  + [`freestyle_lineset_add()`](#bpy.ops.scene.freestyle_lineset_add)
  + [`freestyle_lineset_copy()`](#bpy.ops.scene.freestyle_lineset_copy)
  + [`freestyle_lineset_move()`](#bpy.ops.scene.freestyle_lineset_move)
  + [`freestyle_lineset_paste()`](#bpy.ops.scene.freestyle_lineset_paste)
  + [`freestyle_lineset_remove()`](#bpy.ops.scene.freestyle_lineset_remove)
  + [`freestyle_linestyle_new()`](#bpy.ops.scene.freestyle_linestyle_new)
  + [`freestyle_modifier_copy()`](#bpy.ops.scene.freestyle_modifier_copy)
  + [`freestyle_modifier_move()`](#bpy.ops.scene.freestyle_modifier_move)
  + [`freestyle_modifier_remove()`](#bpy.ops.scene.freestyle_modifier_remove)
  + [`freestyle_module_add()`](#bpy.ops.scene.freestyle_module_add)
  + [`freestyle_module_move()`](#bpy.ops.scene.freestyle_module_move)
  + [`freestyle_module_open()`](#bpy.ops.scene.freestyle_module_open)
  + [`freestyle_module_remove()`](#bpy.ops.scene.freestyle_module_remove)
  + [`freestyle_stroke_material_create()`](#bpy.ops.scene.freestyle_stroke_material_create)
  + [`freestyle_thickness_modifier_add()`](#bpy.ops.scene.freestyle_thickness_modifier_add)
  + [`gltf2_action_filter_refresh()`](#bpy.ops.scene.gltf2_action_filter_refresh)
  + [`gpencil_brush_preset_add()`](#bpy.ops.scene.gpencil_brush_preset_add)
  + [`gpencil_material_preset_add()`](#bpy.ops.scene.gpencil_material_preset_add)
  + [`new()`](#bpy.ops.scene.new)
  + [`new_sequencer()`](#bpy.ops.scene.new_sequencer)
  + [`render_view_add()`](#bpy.ops.scene.render_view_add)
  + [`render_view_remove()`](#bpy.ops.scene.render_view_remove)
  + [`view_layer_add()`](#bpy.ops.scene.view_layer_add)
  + [`view_layer_add_aov()`](#bpy.ops.scene.view_layer_add_aov)
  + [`view_layer_add_lightgroup()`](#bpy.ops.scene.view_layer_add_lightgroup)
  + [`view_layer_add_used_lightgroups()`](#bpy.ops.scene.view_layer_add_used_lightgroups)
  + [`view_layer_remove()`](#bpy.ops.scene.view_layer_remove)
  + [`view_layer_remove_aov()`](#bpy.ops.scene.view_layer_remove_aov)
  + [`view_layer_remove_lightgroup()`](#bpy.ops.scene.view_layer_remove_lightgroup)
  + [`view_layer_remove_unused_lightgroups()`](#bpy.ops.scene.view_layer_remove_unused_lightgroups)