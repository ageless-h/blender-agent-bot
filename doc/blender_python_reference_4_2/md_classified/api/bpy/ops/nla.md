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

# Nla Operators[#](#module-bpy.ops.nla "Link to this heading")

bpy.ops.nla.action\_pushdown(*track\_index=-1*)[#](#bpy.ops.nla.action_pushdown "Link to this definition")
:   Push action down onto the top of the NLA stack as a new strip

    Parameters:
    :   **track\_index** (*int in* *[**-1**,* *inf**]**,* *(**optional**)*) – Track Index, Index of NLA action track to perform pushdown operation on

bpy.ops.nla.action\_sync\_length(*active=True*)[#](#bpy.ops.nla.action_sync_length "Link to this definition")
:   Synchronize the length of the referenced Action with the length used in the strip

    Parameters:
    :   **active** (*boolean**,* *(**optional**)*) – Active Strip Only, Only sync the active length for the active strip

bpy.ops.nla.action\_unlink(*force\_delete=False*)[#](#bpy.ops.nla.action_unlink "Link to this definition")
:   Unlink this action from the active action slot (and/or exit Tweak Mode)

    Parameters:
    :   **force\_delete** (*boolean**,* *(**optional**)*) – Force Delete, Clear Fake User and remove copy stashed in this data-block’s NLA stack

bpy.ops.nla.actionclip\_add(*action=''*)[#](#bpy.ops.nla.actionclip_add "Link to this definition")
:   Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

    Parameters:
    :   **action** (*enum in* *[**]**,* *(**optional**)*) – Action

bpy.ops.nla.apply\_scale()[#](#bpy.ops.nla.apply_scale "Link to this definition")
:   Apply scaling of selected strips to their referenced Actions

bpy.ops.nla.bake(*frame\_start=1*, *frame\_end=250*, *step=1*, *only\_selected=True*, *visual\_keying=False*, *clear\_constraints=False*, *clear\_parents=False*, *use\_current\_action=False*, *clean\_curves=False*, *bake\_types={'POSE'}*, *channel\_types={'BBONE', 'LOCATION', 'PROPS', 'ROTATION', 'SCALE'}*)[#](#bpy.ops.nla.bake "Link to this definition")
:   Bake all selected objects location/scale/rotation animation to an action

    Parameters:
    :   * **frame\_start** (*int in* *[**0**,* *300000**]**,* *(**optional**)*) – Start Frame, Start frame for baking
        * **frame\_end** (*int in* *[**1**,* *300000**]**,* *(**optional**)*) – End Frame, End frame for baking
        * **step** (*int in* *[**1**,* *120**]**,* *(**optional**)*) – Frame Step, Number of frames to skip forward while baking each frame
        * **only\_selected** (*boolean**,* *(**optional**)*) – Only Selected Bones, Only key selected bones (Pose baking only)
        * **visual\_keying** (*boolean**,* *(**optional**)*) – Visual Keying, Keyframe from the final transformations (with constraints applied)
        * **clear\_constraints** (*boolean**,* *(**optional**)*) – Clear Local Constraints, Remove all constraints from keyed object/bones, and do ‘visual’ keying
        * **clear\_parents** (*boolean**,* *(**optional**)*) – Clear Parents, Bake animation onto the object then clear parents (objects only)
        * **use\_current\_action** (*boolean**,* *(**optional**)*) – Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)
        * **clean\_curves** (*boolean**,* *(**optional**)*) – Clean Curves, After baking curves, remove redundant keys
        * **bake\_types** (*enum set in {'POSE'**,* *'OBJECT'}**,* *(**optional**)*) –

          Bake Data, Which data’s transformations to bake

          + `POSE`
            Pose – Bake bones transformations.
          + `OBJECT`
            Object – Bake object transformations.
        * **channel\_types** (*enum set in {'LOCATION'**,* *'ROTATION'**,* *'SCALE'**,* *'BBONE'**,* *'PROPS'}**,* *(**optional**)*) –

          Channels, Which channels to bake

          + `LOCATION`
            Location – Bake location channels.
          + `ROTATION`
            Rotation – Bake rotation channels.
          + `SCALE`
            Scale – Bake scale channels.
          + `BBONE`
            B-Bone – Bake B-Bone channels.
          + `PROPS`
            Custom Properties – Bake custom properties.

    File:
    :   [startup/bl\_operators/anim.py:270](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/anim.py#L270)

bpy.ops.nla.channels\_click(*extend=False*)[#](#bpy.ops.nla.channels_click "Link to this definition")
:   Handle clicks to select NLA tracks

    Parameters:
    :   **extend** (*boolean**,* *(**optional**)*) – Extend Select

bpy.ops.nla.clear\_scale()[#](#bpy.ops.nla.clear_scale "Link to this definition")
:   Reset scaling of selected strips

bpy.ops.nla.click\_select(*wait\_to\_deselect\_others=False*, *mouse\_x=0*, *mouse\_y=0*, *extend=False*, *deselect\_all=False*)[#](#bpy.ops.nla.click_select "Link to this definition")
:   Handle clicks to select NLA Strips

    Parameters:
    :   * **wait\_to\_deselect\_others** (*boolean**,* *(**optional**)*) – Wait to Deselect Others
        * **mouse\_x** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Mouse X
        * **mouse\_y** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Mouse Y
        * **extend** (*boolean**,* *(**optional**)*) – Extend Select
        * **deselect\_all** (*boolean**,* *(**optional**)*) – Deselect On Nothing, Deselect all when nothing under the cursor

bpy.ops.nla.delete()[#](#bpy.ops.nla.delete "Link to this definition")
:   Delete selected strips

bpy.ops.nla.duplicate(*linked=False*)[#](#bpy.ops.nla.duplicate "Link to this definition")
:   Duplicate selected NLA-Strips, adding the new strips to new track(s)

    Parameters:
    :   **linked** (*boolean**,* *(**optional**)*) – Linked, When duplicating strips, assign new copies of the actions they use

bpy.ops.nla.duplicate\_linked\_move(*NLA\_OT\_duplicate=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.nla.duplicate_linked_move "Link to this definition")
:   Duplicate Linked selected NLA-Strips, adding the new strips to new track(s)

    Parameters:
    :   * **NLA\_OT\_duplicate** (`NLA_OT_duplicate`, (optional)) – Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.nla.duplicate\_move(*NLA\_OT\_duplicate=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.nla.duplicate_move "Link to this definition")
:   Duplicate selected NLA-Strips, adding the new strips to new track(s)

    Parameters:
    :   * **NLA\_OT\_duplicate** (`NLA_OT_duplicate`, (optional)) – Duplicate Strips, Duplicate selected NLA-Strips, adding the new strips to new track(s)
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.nla.fmodifier\_add(*type='NULL'*, *only\_active=True*)[#](#bpy.ops.nla.fmodifier_add "Link to this definition")
:   Add F-Modifier to the active/selected NLA-Strips

    Parameters:
    :   * **type** (enum in [Fmodifier Type Items](../../../appendix/bpy_types_enum_items/fmodifier_type_items.md#rna-enum-fmodifier-type-items), (optional)) – Type
        * **only\_active** (*boolean**,* *(**optional**)*) – Only Active, Only add a F-Modifier of the specified type to the active strip

bpy.ops.nla.fmodifier\_copy()[#](#bpy.ops.nla.fmodifier_copy "Link to this definition")
:   Copy the F-Modifier(s) of the active NLA-Strip

bpy.ops.nla.fmodifier\_paste(*only\_active=True*, *replace=False*)[#](#bpy.ops.nla.fmodifier_paste "Link to this definition")
:   Add copied F-Modifiers to the selected NLA-Strips

    Parameters:
    :   * **only\_active** (*boolean**,* *(**optional**)*) – Only Active, Only paste F-Modifiers on active strip
        * **replace** (*boolean**,* *(**optional**)*) – Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list

bpy.ops.nla.make\_single\_user(*confirm=True*)[#](#bpy.ops.nla.make_single_user "Link to this definition")
:   Make linked action local to each strip

    Parameters:
    :   **confirm** (*boolean**,* *(**optional**)*) – Confirm, Prompt for confirmation

bpy.ops.nla.meta\_add()[#](#bpy.ops.nla.meta_add "Link to this definition")
:   Add new meta-strips incorporating the selected strips

bpy.ops.nla.meta\_remove()[#](#bpy.ops.nla.meta_remove "Link to this definition")
:   Separate out the strips held by the selected meta-strips

bpy.ops.nla.move\_down()[#](#bpy.ops.nla.move_down "Link to this definition")
:   Move selected strips down a track if there’s room

bpy.ops.nla.move\_up()[#](#bpy.ops.nla.move_up "Link to this definition")
:   Move selected strips up a track if there’s room

bpy.ops.nla.mute\_toggle()[#](#bpy.ops.nla.mute_toggle "Link to this definition")
:   Mute or un-mute selected strips

bpy.ops.nla.previewrange\_set()[#](#bpy.ops.nla.previewrange_set "Link to this definition")
:   Set Preview Range based on extends of selected strips

bpy.ops.nla.select\_all(*action='TOGGLE'*)[#](#bpy.ops.nla.select_all "Link to this definition")
:   Select or deselect all NLA-Strips

    Parameters:
    :   **action** (*enum in* *[**'TOGGLE'**,* *'SELECT'**,* *'DESELECT'**,* *'INVERT'**]**,* *(**optional**)*) –

        Action, Selection action to execute

        * `TOGGLE`
          Toggle – Toggle selection for all elements.
        * `SELECT`
          Select – Select all elements.
        * `DESELECT`
          Deselect – Deselect all elements.
        * `INVERT`
          Invert – Invert selection of all elements.

bpy.ops.nla.select\_box(*axis\_range=False*, *tweak=False*, *xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.nla.select_box "Link to this definition")
:   Use box selection to grab NLA-Strips

    Parameters:
    :   * **axis\_range** (*boolean**,* *(**optional**)*) – Axis Range
        * **tweak** (*boolean**,* *(**optional**)*) – Tweak, Operator has been activated using a click-drag event
        * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.

bpy.ops.nla.select\_leftright(*mode='CHECK'*, *extend=False*)[#](#bpy.ops.nla.select_leftright "Link to this definition")
:   Select strips to the left or the right of the current frame

    Parameters:
    :   * **mode** (*enum in* *[**'CHECK'**,* *'LEFT'**,* *'RIGHT'**]**,* *(**optional**)*) – Mode
        * **extend** (*boolean**,* *(**optional**)*) – Extend Select

bpy.ops.nla.selected\_objects\_add()[#](#bpy.ops.nla.selected_objects_add "Link to this definition")
:   Make selected objects appear in NLA Editor by adding Animation Data

bpy.ops.nla.snap(*type='CFRA'*)[#](#bpy.ops.nla.snap "Link to this definition")
:   Move start of strips to specified time

    Parameters:
    :   **type** (*enum in* *[**'CFRA'**,* *'NEAREST\_FRAME'**,* *'NEAREST\_SECOND'**,* *'NEAREST\_MARKER'**]**,* *(**optional**)*) – Type

bpy.ops.nla.soundclip\_add()[#](#bpy.ops.nla.soundclip_add "Link to this definition")
:   Add a strip for controlling when speaker plays its sound clip

bpy.ops.nla.split()[#](#bpy.ops.nla.split "Link to this definition")
:   Split selected strips at their midpoints

bpy.ops.nla.swap()[#](#bpy.ops.nla.swap "Link to this definition")
:   Swap order of selected strips within tracks

bpy.ops.nla.tracks\_add(*above\_selected=False*)[#](#bpy.ops.nla.tracks_add "Link to this definition")
:   Add NLA-Tracks above/after the selected tracks

    Parameters:
    :   **above\_selected** (*boolean**,* *(**optional**)*) – Above Selected, Add a new NLA Track above every existing selected one

bpy.ops.nla.tracks\_delete()[#](#bpy.ops.nla.tracks_delete "Link to this definition")
:   Delete selected NLA-Tracks and the strips they contain

bpy.ops.nla.transition\_add()[#](#bpy.ops.nla.transition_add "Link to this definition")
:   Add a transition strip between two adjacent selected strips

bpy.ops.nla.tweakmode\_enter(*isolate\_action=False*, *use\_upper\_stack\_evaluation=False*)[#](#bpy.ops.nla.tweakmode_enter "Link to this definition")
:   Enter tweaking mode for the action referenced by the active strip to edit its keyframes

    Parameters:
    :   * **isolate\_action** (*boolean**,* *(**optional**)*) – Isolate Action, Enable ‘solo’ on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack
        * **use\_upper\_stack\_evaluation** (*boolean**,* *(**optional**)*) – Evaluate Upper Stack, In tweak mode, display the effects of the tracks above the tweak strip

bpy.ops.nla.tweakmode\_exit(*isolate\_action=False*)[#](#bpy.ops.nla.tweakmode_exit "Link to this definition")
:   Exit tweaking mode for the action referenced by the active strip

    Parameters:
    :   **isolate\_action** (*boolean**,* *(**optional**)*) – Isolate Action, Disable ‘solo’ on any of the NLA Tracks after exiting tweak mode to get things back to normal

bpy.ops.nla.view\_all()[#](#bpy.ops.nla.view_all "Link to this definition")
:   Reset viewable area to show full strips range

bpy.ops.nla.view\_frame()[#](#bpy.ops.nla.view_frame "Link to this definition")
:   Move the view to the current frame

bpy.ops.nla.view\_selected()[#](#bpy.ops.nla.view_selected "Link to this definition")
:   Reset viewable area to show selected strips range

[Next

Node Operators](node.md)
[Previous

Mesh Operators](mesh.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.nla.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.nla.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Nla Operators
  + [`action_pushdown()`](#bpy.ops.nla.action_pushdown)
  + [`action_sync_length()`](#bpy.ops.nla.action_sync_length)
  + [`action_unlink()`](#bpy.ops.nla.action_unlink)
  + [`actionclip_add()`](#bpy.ops.nla.actionclip_add)
  + [`apply_scale()`](#bpy.ops.nla.apply_scale)
  + [`bake()`](#bpy.ops.nla.bake)
  + [`channels_click()`](#bpy.ops.nla.channels_click)
  + [`clear_scale()`](#bpy.ops.nla.clear_scale)
  + [`click_select()`](#bpy.ops.nla.click_select)
  + [`delete()`](#bpy.ops.nla.delete)
  + [`duplicate()`](#bpy.ops.nla.duplicate)
  + [`duplicate_linked_move()`](#bpy.ops.nla.duplicate_linked_move)
  + [`duplicate_move()`](#bpy.ops.nla.duplicate_move)
  + [`fmodifier_add()`](#bpy.ops.nla.fmodifier_add)
  + [`fmodifier_copy()`](#bpy.ops.nla.fmodifier_copy)
  + [`fmodifier_paste()`](#bpy.ops.nla.fmodifier_paste)
  + [`make_single_user()`](#bpy.ops.nla.make_single_user)
  + [`meta_add()`](#bpy.ops.nla.meta_add)
  + [`meta_remove()`](#bpy.ops.nla.meta_remove)
  + [`move_down()`](#bpy.ops.nla.move_down)
  + [`move_up()`](#bpy.ops.nla.move_up)
  + [`mute_toggle()`](#bpy.ops.nla.mute_toggle)
  + [`previewrange_set()`](#bpy.ops.nla.previewrange_set)
  + [`select_all()`](#bpy.ops.nla.select_all)
  + [`select_box()`](#bpy.ops.nla.select_box)
  + [`select_leftright()`](#bpy.ops.nla.select_leftright)
  + [`selected_objects_add()`](#bpy.ops.nla.selected_objects_add)
  + [`snap()`](#bpy.ops.nla.snap)
  + [`soundclip_add()`](#bpy.ops.nla.soundclip_add)
  + [`split()`](#bpy.ops.nla.split)
  + [`swap()`](#bpy.ops.nla.swap)
  + [`tracks_add()`](#bpy.ops.nla.tracks_add)
  + [`tracks_delete()`](#bpy.ops.nla.tracks_delete)
  + [`transition_add()`](#bpy.ops.nla.transition_add)
  + [`tweakmode_enter()`](#bpy.ops.nla.tweakmode_enter)
  + [`tweakmode_exit()`](#bpy.ops.nla.tweakmode_exit)
  + [`view_all()`](#bpy.ops.nla.view_all)
  + [`view_frame()`](#bpy.ops.nla.view_frame)
  + [`view_selected()`](#bpy.ops.nla.view_selected)