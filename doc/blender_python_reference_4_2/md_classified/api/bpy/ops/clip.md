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

# Clip Operators[#](#module-bpy.ops.clip "Link to this heading")

bpy.ops.clip.add\_marker(*location=(0.0, 0.0)*)[#](#bpy.ops.clip.add_marker "Link to this definition")
:   Place new marker at specified location

    Parameters:
    :   **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Location of marker on frame

bpy.ops.clip.add\_marker\_at\_click()[#](#bpy.ops.clip.add_marker_at_click "Link to this definition")
:   Place new marker at the desired (clicked) position

bpy.ops.clip.add\_marker\_move(*CLIP\_OT\_add\_marker=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.clip.add_marker_move "Link to this definition")
:   Add new marker and move it on movie

    Parameters:
    :   * **CLIP\_OT\_add\_marker** (`CLIP_OT_add_marker`, (optional)) – Add Marker, Place new marker at specified location
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.clip.add\_marker\_slide(*CLIP\_OT\_add\_marker=None*, *TRANSFORM\_OT\_translate=None*)[#](#bpy.ops.clip.add_marker_slide "Link to this definition")
:   Add new marker and slide it with mouse until mouse button release

    Parameters:
    :   * **CLIP\_OT\_add\_marker** (`CLIP_OT_add_marker`, (optional)) – Add Marker, Place new marker at specified location
        * **TRANSFORM\_OT\_translate** (`TRANSFORM_OT_translate`, (optional)) – Move, Move selected items

bpy.ops.clip.apply\_solution\_scale(*distance=0.0*)[#](#bpy.ops.clip.apply_solution_scale "Link to this definition")
:   Apply scale on solution itself to make distance between selected tracks equals to desired

    Parameters:
    :   **distance** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Distance, Distance between selected tracks

bpy.ops.clip.average\_tracks(*keep\_original=True*)[#](#bpy.ops.clip.average_tracks "Link to this definition")
:   Average selected tracks into active

    Parameters:
    :   **keep\_original** (*boolean**,* *(**optional**)*) – Keep Original, Keep original tracks

bpy.ops.clip.bundles\_to\_mesh()[#](#bpy.ops.clip.bundles_to_mesh "Link to this definition")
:   Create vertex cloud using coordinates of reconstructed tracks

    File:
    :   [startup/bl\_operators/clip.py:284](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L284)

bpy.ops.clip.camera\_preset\_add(*name=''*, *remove\_name=False*, *remove\_active=False*, *use\_focal\_length=True*)[#](#bpy.ops.clip.camera_preset_add "Link to this definition")
:   Add or remove a Tracking Camera Intrinsics Preset

    Parameters:
    :   * **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the preset, used to make the path name
        * **remove\_name** (*boolean**,* *(**optional**)*) – remove\_name
        * **remove\_active** (*boolean**,* *(**optional**)*) – remove\_active
        * **use\_focal\_length** (*boolean**,* *(**optional**)*) – Include Focal Length, Include focal length into the preset

    File:
    :   [startup/bl\_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.clip.change\_frame(*frame=0*)[#](#bpy.ops.clip.change_frame "Link to this definition")
:   Interactively change the current frame number

    Parameters:
    :   **frame** (*int in* *[**-1048574**,* *1048574**]**,* *(**optional**)*) – Frame

bpy.ops.clip.clean\_tracks(*frames=0*, *error=0.0*, *action='SELECT'*)[#](#bpy.ops.clip.clean_tracks "Link to this definition")
:   Clean tracks with high error values or few frames

    Parameters:
    :   * **frames** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Tracked Frames, Affect tracks which are tracked less than the specified number of frames
        * **error** (*float in* *[**0**,* *inf**]**,* *(**optional**)*) – Reprojection Error, Affect tracks which have a larger reprojection error
        * **action** (*enum in* *[**'SELECT'**,* *'DELETE\_TRACK'**,* *'DELETE\_SEGMENTS'**]**,* *(**optional**)*) –

          Action, Cleanup action to execute

          + `SELECT`
            Select – Select unclean tracks.
          + `DELETE_TRACK`
            Delete Track – Delete unclean tracks.
          + `DELETE_SEGMENTS`
            Delete Segments – Delete unclean segments of tracks.

bpy.ops.clip.clear\_solution()[#](#bpy.ops.clip.clear_solution "Link to this definition")
:   Clear all calculated data

bpy.ops.clip.clear\_track\_path(*action='REMAINED'*, *clear\_active=False*)[#](#bpy.ops.clip.clear_track_path "Link to this definition")
:   Clear tracks after/before current position or clear the whole track

    Parameters:
    :   * **action** (*enum in* *[**'UPTO'**,* *'REMAINED'**,* *'ALL'**]**,* *(**optional**)*) –

          Action, Clear action to execute

          + `UPTO`
            Clear Up To – Clear path up to current frame.
          + `REMAINED`
            Clear Remained – Clear path at remaining frames (after current).
          + `ALL`
            Clear All – Clear the whole path.
        * **clear\_active** (*boolean**,* *(**optional**)*) – Clear Active, Clear active track only instead of all selected tracks

bpy.ops.clip.constraint\_to\_fcurve()[#](#bpy.ops.clip.constraint_to_fcurve "Link to this definition")
:   Create F-Curves for object which will copy object’s movement caused by this constraint

    File:
    :   [startup/bl\_operators/clip.py:522](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L522)

bpy.ops.clip.copy\_tracks()[#](#bpy.ops.clip.copy_tracks "Link to this definition")
:   Copy the selected tracks to the internal clipboard

bpy.ops.clip.create\_plane\_track()[#](#bpy.ops.clip.create_plane_track "Link to this definition")
:   Create new plane track out of selected point tracks

bpy.ops.clip.cursor\_set(*location=(0.0, 0.0)*)[#](#bpy.ops.clip.cursor_set "Link to this definition")
:   Set 2D cursor location

    Parameters:
    :   **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor location in normalized clip coordinates

bpy.ops.clip.delete\_marker(*confirm=True*)[#](#bpy.ops.clip.delete_marker "Link to this definition")
:   Delete marker for current frame from selected tracks

    Parameters:
    :   **confirm** (*boolean**,* *(**optional**)*) – Confirm, Prompt for confirmation

bpy.ops.clip.delete\_proxy()[#](#bpy.ops.clip.delete_proxy "Link to this definition")
:   Delete movie clip proxy files from the hard drive

    File:
    :   [startup/bl\_operators/clip.py:351](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L351)

bpy.ops.clip.delete\_track(*confirm=True*)[#](#bpy.ops.clip.delete_track "Link to this definition")
:   Delete selected tracks

    Parameters:
    :   **confirm** (*boolean**,* *(**optional**)*) – Confirm, Prompt for confirmation

bpy.ops.clip.detect\_features(*placement='FRAME'*, *margin=16*, *threshold=0.5*, *min\_distance=120*)[#](#bpy.ops.clip.detect_features "Link to this definition")
:   Automatically detect features and place markers to track

    Parameters:
    :   * **placement** (*enum in* *[**'FRAME'**,* *'INSIDE\_GPENCIL'**,* *'OUTSIDE\_GPENCIL'**]**,* *(**optional**)*) –

          Placement, Placement for detected features

          + `FRAME`
            Whole Frame – Place markers across the whole frame.
          + `INSIDE_GPENCIL`
            Inside Annotated Area – Place markers only inside areas outlined with the Annotation tool.
          + `OUTSIDE_GPENCIL`
            Outside Annotated Area – Place markers only outside areas outlined with the Annotation tool.
        * **margin** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Margin, Only features further than margin pixels from the image edges are considered
        * **threshold** (*float in* *[**0.0001**,* *inf**]**,* *(**optional**)*) – Threshold, Threshold level to consider feature good enough for tracking
        * **min\_distance** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Distance, Minimal distance accepted between two features

bpy.ops.clip.disable\_markers(*action='DISABLE'*)[#](#bpy.ops.clip.disable_markers "Link to this definition")
:   Disable/enable selected markers

    Parameters:
    :   **action** (*enum in* *[**'DISABLE'**,* *'ENABLE'**,* *'TOGGLE'**]**,* *(**optional**)*) –

        Action, Disable action to execute

        * `DISABLE`
          Disable – Disable selected markers.
        * `ENABLE`
          Enable – Enable selected markers.
        * `TOGGLE`
          Toggle – Toggle disabled flag for selected markers.

bpy.ops.clip.dopesheet\_select\_channel(*location=(0.0, 0.0)*, *extend=False*)[#](#bpy.ops.clip.dopesheet_select_channel "Link to this definition")
:   Select movie tracking channel

    Parameters:
    :   * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location to select channel
        * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection rather than clearing the existing selection

bpy.ops.clip.dopesheet\_view\_all()[#](#bpy.ops.clip.dopesheet_view_all "Link to this definition")
:   Reset viewable area to show full keyframe range

bpy.ops.clip.filter\_tracks(*track\_threshold=5.0*)[#](#bpy.ops.clip.filter_tracks "Link to this definition")
:   Filter tracks which has weirdly looking spikes in motion curves

    Parameters:
    :   **track\_threshold** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Track Threshold, Filter Threshold to select problematic tracks

    File:
    :   [startup/bl\_operators/clip.py:198](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L198)

bpy.ops.clip.frame\_jump(*position='PATHSTART'*)[#](#bpy.ops.clip.frame_jump "Link to this definition")
:   Jump to special frame

    Parameters:
    :   **position** (*enum in* *[**'PATHSTART'**,* *'PATHEND'**,* *'FAILEDPREV'**,* *'FAILNEXT'**]**,* *(**optional**)*) –

        Position, Position to jump to

        * `PATHSTART`
          Path Start – Jump to start of current path.
        * `PATHEND`
          Path End – Jump to end of current path.
        * `FAILEDPREV`
          Previous Failed – Jump to previous failed frame.
        * `FAILNEXT`
          Next Failed – Jump to next failed frame.

bpy.ops.clip.graph\_center\_current\_frame()[#](#bpy.ops.clip.graph_center_current_frame "Link to this definition")
:   Scroll view so current frame would be centered

bpy.ops.clip.graph\_delete\_curve(*confirm=True*)[#](#bpy.ops.clip.graph_delete_curve "Link to this definition")
:   Delete track corresponding to the selected curve

    Parameters:
    :   **confirm** (*boolean**,* *(**optional**)*) – Confirm, Prompt for confirmation

bpy.ops.clip.graph\_delete\_knot()[#](#bpy.ops.clip.graph_delete_knot "Link to this definition")
:   Delete curve knots

bpy.ops.clip.graph\_disable\_markers(*action='DISABLE'*)[#](#bpy.ops.clip.graph_disable_markers "Link to this definition")
:   Disable/enable selected markers

    Parameters:
    :   **action** (*enum in* *[**'DISABLE'**,* *'ENABLE'**,* *'TOGGLE'**]**,* *(**optional**)*) –

        Action, Disable action to execute

        * `DISABLE`
          Disable – Disable selected markers.
        * `ENABLE`
          Enable – Enable selected markers.
        * `TOGGLE`
          Toggle – Toggle disabled flag for selected markers.

bpy.ops.clip.graph\_select(*location=(0.0, 0.0)*, *extend=False*)[#](#bpy.ops.clip.graph_select "Link to this definition")
:   Select graph curves

    Parameters:
    :   * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location to select nearest entity
        * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection rather than clearing the existing selection

bpy.ops.clip.graph\_select\_all\_markers(*action='TOGGLE'*)[#](#bpy.ops.clip.graph_select_all_markers "Link to this definition")
:   Change selection of all markers of active track

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

bpy.ops.clip.graph\_select\_box(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *deselect=False*, *extend=True*)[#](#bpy.ops.clip.graph_select_box "Link to this definition")
:   Select curve points using box selection

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
        * **xmax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Max
        * **ymin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Min
        * **ymax** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y Max
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **deselect** (*boolean**,* *(**optional**)*) – Deselect, Deselect rather than select items
        * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection instead of deselecting everything first

bpy.ops.clip.graph\_view\_all()[#](#bpy.ops.clip.graph_view_all "Link to this definition")
:   View all curves in editor

bpy.ops.clip.hide\_tracks(*unselected=False*)[#](#bpy.ops.clip.hide_tracks "Link to this definition")
:   Hide selected tracks

    Parameters:
    :   **unselected** (*boolean**,* *(**optional**)*) – Unselected, Hide unselected tracks

bpy.ops.clip.hide\_tracks\_clear()[#](#bpy.ops.clip.hide_tracks_clear "Link to this definition")
:   Clear hide selected tracks

bpy.ops.clip.join\_tracks()[#](#bpy.ops.clip.join_tracks "Link to this definition")
:   Join selected tracks

bpy.ops.clip.keyframe\_delete()[#](#bpy.ops.clip.keyframe_delete "Link to this definition")
:   Delete a keyframe from selected tracks at current frame

bpy.ops.clip.keyframe\_insert()[#](#bpy.ops.clip.keyframe_insert "Link to this definition")
:   Insert a keyframe to selected tracks at current frame

bpy.ops.clip.lock\_selection\_toggle()[#](#bpy.ops.clip.lock_selection_toggle "Link to this definition")
:   Toggle Lock Selection option of the current clip editor

bpy.ops.clip.lock\_tracks(*action='LOCK'*)[#](#bpy.ops.clip.lock_tracks "Link to this definition")
:   Lock/unlock selected tracks

    Parameters:
    :   **action** (*enum in* *[**'LOCK'**,* *'UNLOCK'**,* *'TOGGLE'**]**,* *(**optional**)*) –

        Action, Lock action to execute

        * `LOCK`
          Lock – Lock selected tracks.
        * `UNLOCK`
          Unlock – Unlock selected tracks.
        * `TOGGLE`
          Toggle – Toggle locked flag for selected tracks.

bpy.ops.clip.mode\_set(*mode='TRACKING'*)[#](#bpy.ops.clip.mode_set "Link to this definition")
:   Set the clip interaction mode

    Parameters:
    :   **mode** (enum in [Clip Editor Mode Items](../../../appendix/bpy_types_enum_items/clip_editor_mode_items.md#rna-enum-clip-editor-mode-items), (optional)) – Mode

bpy.ops.clip.new\_image\_from\_plane\_marker()[#](#bpy.ops.clip.new_image_from_plane_marker "Link to this definition")
:   Create new image from the content of the plane marker

bpy.ops.clip.open(*directory=''*, *files=None*, *hide\_props\_region=True*, *check\_existing=False*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=True*, *filter\_movie=True*, *filter\_python=False*, *filter\_font=False*, *filter\_sound=False*, *filter\_text=False*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *relative\_path=True*, *show\_multiview=False*, *use\_multiview=False*, *display\_type='DEFAULT'*, *sort\_method=''*)[#](#bpy.ops.clip.open "Link to this definition")
:   Load a sequence of frames or a movie file

    Parameters:
    :   * **directory** (*string**,* *(**optional**,* *never None**)*) – Directory, Directory of the file
        * **files** (`bpy_prop_collection` of `OperatorFileListElement`, (optional)) – Files
        * **hide\_props\_region** (*boolean**,* *(**optional**)*) – Hide Operator Properties, Collapse the region displaying the operator settings
        * **check\_existing** (*boolean**,* *(**optional**)*) – Check Existing, Check and warn on overwriting existing files
        * **filter\_blender** (*boolean**,* *(**optional**)*) – Filter .blend files
        * **filter\_backup** (*boolean**,* *(**optional**)*) – Filter .blend files
        * **filter\_image** (*boolean**,* *(**optional**)*) – Filter image files
        * **filter\_movie** (*boolean**,* *(**optional**)*) – Filter movie files
        * **filter\_python** (*boolean**,* *(**optional**)*) – Filter Python files
        * **filter\_font** (*boolean**,* *(**optional**)*) – Filter font files
        * **filter\_sound** (*boolean**,* *(**optional**)*) – Filter sound files
        * **filter\_text** (*boolean**,* *(**optional**)*) – Filter text files
        * **filter\_archive** (*boolean**,* *(**optional**)*) – Filter archive files
        * **filter\_btx** (*boolean**,* *(**optional**)*) – Filter btx files
        * **filter\_collada** (*boolean**,* *(**optional**)*) – Filter COLLADA files
        * **filter\_alembic** (*boolean**,* *(**optional**)*) – Filter Alembic files
        * **filter\_usd** (*boolean**,* *(**optional**)*) – Filter USD files
        * **filter\_obj** (*boolean**,* *(**optional**)*) – Filter OBJ files
        * **filter\_volume** (*boolean**,* *(**optional**)*) – Filter OpenVDB volume files
        * **filter\_folder** (*boolean**,* *(**optional**)*) – Filter folders
        * **filter\_blenlib** (*boolean**,* *(**optional**)*) – Filter Blender IDs
        * **filemode** (*int in* *[**1**,* *9**]**,* *(**optional**)*) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        * **relative\_path** (*boolean**,* *(**optional**)*) – Relative Path, Select the file relative to the blend file
        * **show\_multiview** (*boolean**,* *(**optional**)*) – Enable Multi-View
        * **use\_multiview** (*boolean**,* *(**optional**)*) – Use Multi-View
        * **display\_type** (*enum in* *[**'DEFAULT'**,* *'LIST\_VERTICAL'**,* *'LIST\_HORIZONTAL'**,* *'THUMBNAIL'**]**,* *(**optional**)*) –

          Display Type

          + `DEFAULT`
            Default – Automatically determine display type for files.
          + `LIST_VERTICAL`
            Short List – Display files as short list.
          + `LIST_HORIZONTAL`
            Long List – Display files as a detailed list.
          + `THUMBNAIL`
            Thumbnails – Display files as thumbnails.
        * **sort\_method** (*enum in* *[**'DEFAULT'**,* *'FILE\_SORT\_ALPHA'**,* *'FILE\_SORT\_EXTENSION'**,* *'FILE\_SORT\_TIME'**,* *'FILE\_SORT\_SIZE'**]**,* *(**optional**)*) –

          File sorting mode

          + `DEFAULT`
            Default – Automatically determine sort method for files.
          + `FILE_SORT_ALPHA`
            Name – Sort the file list alphabetically.
          + `FILE_SORT_EXTENSION`
            Extension – Sort the file list by extension/type.
          + `FILE_SORT_TIME`
            Modified Date – Sort files by modification time.
          + `FILE_SORT_SIZE`
            Size – Sort files by size.

bpy.ops.clip.paste\_tracks()[#](#bpy.ops.clip.paste_tracks "Link to this definition")
:   Paste tracks from the internal clipboard

bpy.ops.clip.prefetch()[#](#bpy.ops.clip.prefetch "Link to this definition")
:   Prefetch frames from disk for faster playback/tracking

bpy.ops.clip.rebuild\_proxy()[#](#bpy.ops.clip.rebuild_proxy "Link to this definition")
:   Rebuild all selected proxies and timecode indices in the background

bpy.ops.clip.refine\_markers(*backwards=False*)[#](#bpy.ops.clip.refine_markers "Link to this definition")
:   Refine selected markers positions by running the tracker from track’s reference to current frame

    Parameters:
    :   **backwards** (*boolean**,* *(**optional**)*) – Backwards, Do backwards tracking

bpy.ops.clip.reload()[#](#bpy.ops.clip.reload "Link to this definition")
:   Reload clip

bpy.ops.clip.select(*extend=False*, *deselect\_all=False*, *location=(0.0, 0.0)*)[#](#bpy.ops.clip.select "Link to this definition")
:   Select tracking markers

    Parameters:
    :   * **extend** (*boolean**,* *(**optional**)*) – Extend, Extend selection rather than clearing the existing selection
        * **deselect\_all** (*boolean**,* *(**optional**)*) – Deselect On Nothing, Deselect all when nothing under the cursor
        * **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds

bpy.ops.clip.select\_all(*action='TOGGLE'*)[#](#bpy.ops.clip.select_all "Link to this definition")
:   Change selection of all tracking markers

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

bpy.ops.clip.select\_box(*xmin=0*, *xmax=0*, *ymin=0*, *ymax=0*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.clip.select_box "Link to this definition")
:   Select markers using box selection

    Parameters:
    :   * **xmin** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X Min
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

bpy.ops.clip.select\_circle(*x=0*, *y=0*, *radius=25*, *wait\_for\_input=True*, *mode='SET'*)[#](#bpy.ops.clip.select_circle "Link to this definition")
:   Select markers using circle selection

    Parameters:
    :   * **x** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X
        * **y** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y
        * **radius** (*int in* *[**1**,* *inf**]**,* *(**optional**)*) – Radius
        * **wait\_for\_input** (*boolean**,* *(**optional**)*) – Wait for Input
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.

bpy.ops.clip.select\_grouped(*group='ESTIMATED'*)[#](#bpy.ops.clip.select_grouped "Link to this definition")
:   Select all tracks from specified group

    Parameters:
    :   **group** (*enum in* *[**'KEYFRAMED'**,* *'ESTIMATED'**,* *'TRACKED'**,* *'LOCKED'**,* *'DISABLED'**,* *'COLOR'**,* *'FAILED'**]**,* *(**optional**)*) –

        Action, Clear action to execute

        * `KEYFRAMED`
          Keyframed Tracks – Select all keyframed tracks.
        * `ESTIMATED`
          Estimated Tracks – Select all estimated tracks.
        * `TRACKED`
          Tracked Tracks – Select all tracked tracks.
        * `LOCKED`
          Locked Tracks – Select all locked tracks.
        * `DISABLED`
          Disabled Tracks – Select all disabled tracks.
        * `COLOR`
          Tracks with Same Color – Select all tracks with same color as active track.
        * `FAILED`
          Failed Tracks – Select all tracks which failed to be reconstructed.

bpy.ops.clip.select\_lasso(*path=None*, *mode='SET'*)[#](#bpy.ops.clip.select_lasso "Link to this definition")
:   Select markers using lasso selection

    Parameters:
    :   * **path** (`bpy_prop_collection` of `OperatorMousePath`, (optional)) – Path
        * **mode** (*enum in* *[**'SET'**,* *'ADD'**,* *'SUB'**]**,* *(**optional**)*) –

          Mode

          + `SET`
            Set – Set a new selection.
          + `ADD`
            Extend – Extend existing selection.
          + `SUB`
            Subtract – Subtract existing selection.

bpy.ops.clip.set\_active\_clip()[#](#bpy.ops.clip.set_active_clip "Link to this definition")
:   Undocumented, consider [contributing](https://developer.blender.org/).

    File:
    :   [startup/bl\_operators/clip.py:213](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L213)

bpy.ops.clip.set\_axis(*axis='X'*)[#](#bpy.ops.clip.set_axis "Link to this definition")
:   Set the direction of a scene axis by rotating the camera (or its parent if present). This assumes that the selected track lies on a real axis connecting it to the origin

    Parameters:
    :   **axis** (*enum in* *[**'X'**,* *'Y'**]**,* *(**optional**)*) –

        Axis, Axis to use to align bundle along

        * `X`
          X – Align bundle align X axis.
        * `Y`
          Y – Align bundle align Y axis.

bpy.ops.clip.set\_origin(*use\_median=False*)[#](#bpy.ops.clip.set_origin "Link to this definition")
:   Set active marker as origin by moving camera (or its parent if present) in 3D space

    Parameters:
    :   **use\_median** (*boolean**,* *(**optional**)*) – Use Median, Set origin to median point of selected bundles

bpy.ops.clip.set\_plane(*plane='FLOOR'*)[#](#bpy.ops.clip.set_plane "Link to this definition")
:   Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space

    Parameters:
    :   **plane** (*enum in* *[**'FLOOR'**,* *'WALL'**]**,* *(**optional**)*) –

        Plane, Plane to be used for orientation

        * `FLOOR`
          Floor – Set floor plane.
        * `WALL`
          Wall – Set wall plane.

bpy.ops.clip.set\_scale(*distance=0.0*)[#](#bpy.ops.clip.set_scale "Link to this definition")
:   Set scale of scene by scaling camera (or its parent if present)

    Parameters:
    :   **distance** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Distance, Distance between selected tracks

bpy.ops.clip.set\_scene\_frames()[#](#bpy.ops.clip.set_scene_frames "Link to this definition")
:   Set scene’s start and end frame to match clip’s start frame and length

bpy.ops.clip.set\_solution\_scale(*distance=0.0*)[#](#bpy.ops.clip.set_solution_scale "Link to this definition")
:   Set object solution scale using distance between two selected tracks

    Parameters:
    :   **distance** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Distance, Distance between selected tracks

bpy.ops.clip.set\_solver\_keyframe(*keyframe='KEYFRAME\_A'*)[#](#bpy.ops.clip.set_solver_keyframe "Link to this definition")
:   Set keyframe used by solver

    Parameters:
    :   **keyframe** (*enum in* *[**'KEYFRAME\_A'**,* *'KEYFRAME\_B'**]**,* *(**optional**)*) – Keyframe, Keyframe to set

bpy.ops.clip.set\_viewport\_background()[#](#bpy.ops.clip.set_viewport_background "Link to this definition")
:   Set current movie clip as a camera background in 3D Viewport (works only when a 3D Viewport is visible)

    File:
    :   [startup/bl\_operators/clip.py:412](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L412)

bpy.ops.clip.setup\_tracking\_scene()[#](#bpy.ops.clip.setup_tracking_scene "Link to this definition")
:   Prepare scene for compositing 3D objects into this footage

    File:
    :   [startup/bl\_operators/clip.py:980](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L980)

bpy.ops.clip.slide\_marker(*offset=(0.0, 0.0)*)[#](#bpy.ops.clip.slide_marker "Link to this definition")
:   Slide marker areas

    Parameters:
    :   **offset** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Offset, Offset in floating-point units, 1.0 is the width and height of the image

bpy.ops.clip.slide\_plane\_marker()[#](#bpy.ops.clip.slide_plane_marker "Link to this definition")
:   Slide plane marker areas

bpy.ops.clip.solve\_camera()[#](#bpy.ops.clip.solve_camera "Link to this definition")
:   Solve camera motion from tracks

bpy.ops.clip.stabilize\_2d\_add()[#](#bpy.ops.clip.stabilize_2d_add "Link to this definition")
:   Add selected tracks to 2D translation stabilization

bpy.ops.clip.stabilize\_2d\_remove()[#](#bpy.ops.clip.stabilize_2d_remove "Link to this definition")
:   Remove selected track from translation stabilization

bpy.ops.clip.stabilize\_2d\_rotation\_add()[#](#bpy.ops.clip.stabilize_2d_rotation_add "Link to this definition")
:   Add selected tracks to 2D rotation stabilization

bpy.ops.clip.stabilize\_2d\_rotation\_remove()[#](#bpy.ops.clip.stabilize_2d_rotation_remove "Link to this definition")
:   Remove selected track from rotation stabilization

bpy.ops.clip.stabilize\_2d\_rotation\_select()[#](#bpy.ops.clip.stabilize_2d_rotation_select "Link to this definition")
:   Select tracks which are used for rotation stabilization

bpy.ops.clip.stabilize\_2d\_select()[#](#bpy.ops.clip.stabilize_2d_select "Link to this definition")
:   Select tracks which are used for translation stabilization

bpy.ops.clip.track\_color\_preset\_add(*name=''*, *remove\_name=False*, *remove\_active=False*)[#](#bpy.ops.clip.track_color_preset_add "Link to this definition")
:   Add or remove a Clip Track Color Preset

    Parameters:
    :   * **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the preset, used to make the path name
        * **remove\_name** (*boolean**,* *(**optional**)*) – remove\_name
        * **remove\_active** (*boolean**,* *(**optional**)*) – remove\_active

    File:
    :   [startup/bl\_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.clip.track\_copy\_color()[#](#bpy.ops.clip.track_copy_color "Link to this definition")
:   Copy color to all selected tracks

bpy.ops.clip.track\_markers(*backwards=False*, *sequence=False*)[#](#bpy.ops.clip.track_markers "Link to this definition")
:   Track selected markers

    Parameters:
    :   * **backwards** (*boolean**,* *(**optional**)*) – Backwards, Do backwards tracking
        * **sequence** (*boolean**,* *(**optional**)*) – Track Sequence, Track marker during image sequence rather than single image

bpy.ops.clip.track\_settings\_as\_default()[#](#bpy.ops.clip.track_settings_as_default "Link to this definition")
:   Copy tracking settings from active track to default settings

    File:
    :   [startup/bl\_operators/clip.py:1009](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L1009)

bpy.ops.clip.track\_settings\_to\_track()[#](#bpy.ops.clip.track_settings_to_track "Link to this definition")
:   Copy tracking settings from active track to selected tracks

    File:
    :   [startup/bl\_operators/clip.py:1058](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L1058)

bpy.ops.clip.track\_to\_empty()[#](#bpy.ops.clip.track_to_empty "Link to this definition")
:   Create an Empty object which will be copying movement of active track

    File:
    :   [startup/bl\_operators/clip.py:260](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/clip.py#L260)

bpy.ops.clip.tracking\_object\_new()[#](#bpy.ops.clip.tracking_object_new "Link to this definition")
:   Add new object for tracking

bpy.ops.clip.tracking\_object\_remove()[#](#bpy.ops.clip.tracking_object_remove "Link to this definition")
:   Remove object for tracking

bpy.ops.clip.tracking\_settings\_preset\_add(*name=''*, *remove\_name=False*, *remove\_active=False*)[#](#bpy.ops.clip.tracking_settings_preset_add "Link to this definition")
:   Add or remove a motion tracking settings preset

    Parameters:
    :   * **name** (*string**,* *(**optional**,* *never None**)*) – Name, Name of the preset, used to make the path name
        * **remove\_name** (*boolean**,* *(**optional**)*) – remove\_name
        * **remove\_active** (*boolean**,* *(**optional**)*) – remove\_active

    File:
    :   [startup/bl\_operators/presets.py:119](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/presets.py#L119)

bpy.ops.clip.update\_image\_from\_plane\_marker()[#](#bpy.ops.clip.update_image_from_plane_marker "Link to this definition")
:   Update current image used by plane marker from the content of the plane marker

bpy.ops.clip.view\_all(*fit\_view=False*)[#](#bpy.ops.clip.view_all "Link to this definition")
:   View whole image with markers

    Parameters:
    :   **fit\_view** (*boolean**,* *(**optional**)*) – Fit View, Fit frame to the viewport

bpy.ops.clip.view\_center\_cursor()[#](#bpy.ops.clip.view_center_cursor "Link to this definition")
:   Center the view so that the cursor is in the middle of the view

bpy.ops.clip.view\_ndof()[#](#bpy.ops.clip.view_ndof "Link to this definition")
:   Use a 3D mouse device to pan/zoom the view

bpy.ops.clip.view\_pan(*offset=(0.0, 0.0)*)[#](#bpy.ops.clip.view_pan "Link to this definition")
:   Pan the view

    Parameters:
    :   **offset** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Offset, Offset in floating-point units, 1.0 is the width and height of the image

bpy.ops.clip.view\_selected()[#](#bpy.ops.clip.view_selected "Link to this definition")
:   View all selected elements

bpy.ops.clip.view\_zoom(*factor=0.0*, *use\_cursor\_init=True*)[#](#bpy.ops.clip.view_zoom "Link to this definition")
:   Zoom in/out the view

    Parameters:
    :   * **factor** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
        * **use\_cursor\_init** (*boolean**,* *(**optional**)*) – Use Mouse Position, Allow the initial mouse position to be used

bpy.ops.clip.view\_zoom\_in(*location=(0.0, 0.0)*)[#](#bpy.ops.clip.view_zoom_in "Link to this definition")
:   Zoom in the view

    Parameters:
    :   **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor location in screen coordinates

bpy.ops.clip.view\_zoom\_out(*location=(0.0, 0.0)*)[#](#bpy.ops.clip.view_zoom_out "Link to this definition")
:   Zoom out the view

    Parameters:
    :   **location** ([`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], (optional)) – Location, Cursor location in normalized (0.0 to 1.0) coordinates

bpy.ops.clip.view\_zoom\_ratio(*ratio=0.0*)[#](#bpy.ops.clip.view_zoom_ratio "Link to this definition")
:   Set the zoom ratio (based on clip size)

    Parameters:
    :   **ratio** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

[Next

Cloth Operators](cloth.md)
[Previous

Camera Operators](camera.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.clip.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.clip.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Clip Operators
  + [`add_marker()`](#bpy.ops.clip.add_marker)
  + [`add_marker_at_click()`](#bpy.ops.clip.add_marker_at_click)
  + [`add_marker_move()`](#bpy.ops.clip.add_marker_move)
  + [`add_marker_slide()`](#bpy.ops.clip.add_marker_slide)
  + [`apply_solution_scale()`](#bpy.ops.clip.apply_solution_scale)
  + [`average_tracks()`](#bpy.ops.clip.average_tracks)
  + [`bundles_to_mesh()`](#bpy.ops.clip.bundles_to_mesh)
  + [`camera_preset_add()`](#bpy.ops.clip.camera_preset_add)
  + [`change_frame()`](#bpy.ops.clip.change_frame)
  + [`clean_tracks()`](#bpy.ops.clip.clean_tracks)
  + [`clear_solution()`](#bpy.ops.clip.clear_solution)
  + [`clear_track_path()`](#bpy.ops.clip.clear_track_path)
  + [`constraint_to_fcurve()`](#bpy.ops.clip.constraint_to_fcurve)
  + [`copy_tracks()`](#bpy.ops.clip.copy_tracks)
  + [`create_plane_track()`](#bpy.ops.clip.create_plane_track)
  + [`cursor_set()`](#bpy.ops.clip.cursor_set)
  + [`delete_marker()`](#bpy.ops.clip.delete_marker)
  + [`delete_proxy()`](#bpy.ops.clip.delete_proxy)
  + [`delete_track()`](#bpy.ops.clip.delete_track)
  + [`detect_features()`](#bpy.ops.clip.detect_features)
  + [`disable_markers()`](#bpy.ops.clip.disable_markers)
  + [`dopesheet_select_channel()`](#bpy.ops.clip.dopesheet_select_channel)
  + [`dopesheet_view_all()`](#bpy.ops.clip.dopesheet_view_all)
  + [`filter_tracks()`](#bpy.ops.clip.filter_tracks)
  + [`frame_jump()`](#bpy.ops.clip.frame_jump)
  + [`graph_center_current_frame()`](#bpy.ops.clip.graph_center_current_frame)
  + [`graph_delete_curve()`](#bpy.ops.clip.graph_delete_curve)
  + [`graph_delete_knot()`](#bpy.ops.clip.graph_delete_knot)
  + [`graph_disable_markers()`](#bpy.ops.clip.graph_disable_markers)
  + [`graph_select()`](#bpy.ops.clip.graph_select)
  + [`graph_select_all_markers()`](#bpy.ops.clip.graph_select_all_markers)
  + [`graph_select_box()`](#bpy.ops.clip.graph_select_box)
  + [`graph_view_all()`](#bpy.ops.clip.graph_view_all)
  + [`hide_tracks()`](#bpy.ops.clip.hide_tracks)
  + [`hide_tracks_clear()`](#bpy.ops.clip.hide_tracks_clear)
  + [`join_tracks()`](#bpy.ops.clip.join_tracks)
  + [`keyframe_delete()`](#bpy.ops.clip.keyframe_delete)
  + [`keyframe_insert()`](#bpy.ops.clip.keyframe_insert)
  + [`lock_selection_toggle()`](#bpy.ops.clip.lock_selection_toggle)
  + [`lock_tracks()`](#bpy.ops.clip.lock_tracks)
  + [`mode_set()`](#bpy.ops.clip.mode_set)
  + [`new_image_from_plane_marker()`](#bpy.ops.clip.new_image_from_plane_marker)
  + [`open()`](#bpy.ops.clip.open)
  + [`paste_tracks()`](#bpy.ops.clip.paste_tracks)
  + [`prefetch()`](#bpy.ops.clip.prefetch)
  + [`rebuild_proxy()`](#bpy.ops.clip.rebuild_proxy)
  + [`refine_markers()`](#bpy.ops.clip.refine_markers)
  + [`reload()`](#bpy.ops.clip.reload)
  + [`select()`](#bpy.ops.clip.select)
  + [`select_all()`](#bpy.ops.clip.select_all)
  + [`select_box()`](#bpy.ops.clip.select_box)
  + [`select_circle()`](#bpy.ops.clip.select_circle)
  + [`select_grouped()`](#bpy.ops.clip.select_grouped)
  + [`select_lasso()`](#bpy.ops.clip.select_lasso)
  + [`set_active_clip()`](#bpy.ops.clip.set_active_clip)
  + [`set_axis()`](#bpy.ops.clip.set_axis)
  + [`set_origin()`](#bpy.ops.clip.set_origin)
  + [`set_plane()`](#bpy.ops.clip.set_plane)
  + [`set_scale()`](#bpy.ops.clip.set_scale)
  + [`set_scene_frames()`](#bpy.ops.clip.set_scene_frames)
  + [`set_solution_scale()`](#bpy.ops.clip.set_solution_scale)
  + [`set_solver_keyframe()`](#bpy.ops.clip.set_solver_keyframe)
  + [`set_viewport_background()`](#bpy.ops.clip.set_viewport_background)
  + [`setup_tracking_scene()`](#bpy.ops.clip.setup_tracking_scene)
  + [`slide_marker()`](#bpy.ops.clip.slide_marker)
  + [`slide_plane_marker()`](#bpy.ops.clip.slide_plane_marker)
  + [`solve_camera()`](#bpy.ops.clip.solve_camera)
  + [`stabilize_2d_add()`](#bpy.ops.clip.stabilize_2d_add)
  + [`stabilize_2d_remove()`](#bpy.ops.clip.stabilize_2d_remove)
  + [`stabilize_2d_rotation_add()`](#bpy.ops.clip.stabilize_2d_rotation_add)
  + [`stabilize_2d_rotation_remove()`](#bpy.ops.clip.stabilize_2d_rotation_remove)
  + [`stabilize_2d_rotation_select()`](#bpy.ops.clip.stabilize_2d_rotation_select)
  + [`stabilize_2d_select()`](#bpy.ops.clip.stabilize_2d_select)
  + [`track_color_preset_add()`](#bpy.ops.clip.track_color_preset_add)
  + [`track_copy_color()`](#bpy.ops.clip.track_copy_color)
  + [`track_markers()`](#bpy.ops.clip.track_markers)
  + [`track_settings_as_default()`](#bpy.ops.clip.track_settings_as_default)
  + [`track_settings_to_track()`](#bpy.ops.clip.track_settings_to_track)
  + [`track_to_empty()`](#bpy.ops.clip.track_to_empty)
  + [`tracking_object_new()`](#bpy.ops.clip.tracking_object_new)
  + [`tracking_object_remove()`](#bpy.ops.clip.tracking_object_remove)
  + [`tracking_settings_preset_add()`](#bpy.ops.clip.tracking_settings_preset_add)
  + [`update_image_from_plane_marker()`](#bpy.ops.clip.update_image_from_plane_marker)
  + [`view_all()`](#bpy.ops.clip.view_all)
  + [`view_center_cursor()`](#bpy.ops.clip.view_center_cursor)
  + [`view_ndof()`](#bpy.ops.clip.view_ndof)
  + [`view_pan()`](#bpy.ops.clip.view_pan)
  + [`view_selected()`](#bpy.ops.clip.view_selected)
  + [`view_zoom()`](#bpy.ops.clip.view_zoom)
  + [`view_zoom_in()`](#bpy.ops.clip.view_zoom_in)
  + [`view_zoom_out()`](#bpy.ops.clip.view_zoom_out)
  + [`view_zoom_ratio()`](#bpy.ops.clip.view_zoom_ratio)