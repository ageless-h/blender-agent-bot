Contents

Menu

Expand

Light mode

Dark mode

Auto light/dark, in light mode

Auto light/dark, in dark mode

[ ]
[ ]

Hide navigation sidebar

Hide table of contents sidebar

[Skip to content](#furo-main-content)

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
* [Gotchas](../../../guides/gotchas/index.md)[ ]
* [Advanced](../../../guides/advanced/index.md)[ ]
* [Change Log](../../../guides/change_log.md)

Application Modules

* [Context Access (bpy.context)](../context/index.md)
* [Data Access (bpy.data)](../data/index.md)
* [Message Bus (bpy.msgbus)](../msgbus/index.md)
* [Operators (bpy.ops)](../ops/index.md)[ ]
* [Types (bpy.types)](../types/index.md)[ ]
* [Utilities (bpy.utils)](../utils/index.md)[ ]

  Toggle navigation of Utilities (bpy.utils)

  + [bpy.utils submodule (bpy.utils.previews)](../utils/previews.md)
  + [bpy.utils submodule (bpy.utils.units)](../utils/units.md)
* [Path Utilities (bpy.path)](../path/index.md)
* Application Data (bpy.app)[x]

  Toggle navigation of Application Data (bpy.app)

  + [Application Handlers (bpy.app.handlers)](handlers.md)
  + [Application Translations (bpy.app.translations)](translations.md)
  + [Application Icons (bpy.app.icons)](icons.md)
  + [Application Timers (bpy.app.timers)](timers.md)
* [Property Definitions (bpy.props)](../props/index.md)

Standalone Modules

* [Audio System (aud)](../../aud/index.md)
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

* 5.0

  Versions

  + Loading...

Note

You are not using the most up to date version of the documentation.
 is the newest version.

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Application Data (bpy.app)[¶](#module-bpy.app "Link to this heading")

This module contains application values that remain unchanged during runtime.

Submodules

* [Application Handlers (bpy.app.handlers)](handlers.md)
* [Application Translations (bpy.app.translations)](translations.md)
* [Application Icons (bpy.app.icons)](icons.md)
* [Application Timers (bpy.app.timers)](timers.md)

bpy.app.autoexec\_fail[¶](#bpy.app.autoexec_fail "Link to this definition")
:   Boolean, True when auto-execution of scripts failed (read-only).

    Type:
    :   bool

bpy.app.autoexec\_fail\_message[¶](#bpy.app.autoexec_fail_message "Link to this definition")
:   String, message describing the auto-execution failure (read-only).

    Type:
    :   str

bpy.app.autoexec\_fail\_quiet[¶](#bpy.app.autoexec_fail_quiet "Link to this definition")
:   Boolean, True when auto-execution failure should be quiet, set after the warning is shown once for the current blend file (read-only).

    Type:
    :   bool

bpy.app.binary\_path[¶](#bpy.app.binary_path "Link to this definition")
:   The location of Blender’s executable, useful for utilities that open new instances. Read-only unless Blender is built as a Python module - in this case the value is an empty string which script authors may point to a Blender binary.

    Type:
    :   str

bpy.app.debug[¶](#bpy.app.debug "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_depsgraph[¶](#bpy.app.debug_depsgraph "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_depsgraph\_build[¶](#bpy.app.debug_depsgraph_build "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_depsgraph\_eval[¶](#bpy.app.debug_depsgraph_eval "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_depsgraph\_pretty[¶](#bpy.app.debug_depsgraph_pretty "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_depsgraph\_tag[¶](#bpy.app.debug_depsgraph_tag "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_depsgraph\_time[¶](#bpy.app.debug_depsgraph_time "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_events[¶](#bpy.app.debug_events "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_freestyle[¶](#bpy.app.debug_freestyle "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_handlers[¶](#bpy.app.debug_handlers "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_io[¶](#bpy.app.debug_io "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_python[¶](#bpy.app.debug_python "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_simdata[¶](#bpy.app.debug_simdata "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.debug\_value[¶](#bpy.app.debug_value "Link to this definition")
:   Short, number which can be set to non-zero values for testing purposes.

    Type:
    :   int

bpy.app.debug\_wm[¶](#bpy.app.debug_wm "Link to this definition")
:   Boolean, for debug info (started with `--debug` / `--debug-*` matching this attribute name).

    Type:
    :   bool

bpy.app.driver\_namespace[¶](#bpy.app.driver_namespace "Link to this definition")
:   Dictionary for drivers namespace, editable in-place, reset on file load (read-only).

    Type:
    :   dict[str, Any]

    File Loading & Order of Initialization
    :   Since drivers may be evaluated immediately after loading a blend-file it is necessary
        to ensure the driver name-space is initialized beforehand.

        This can be done by registering text data-blocks to execute on startup,
        which executes the scripts before drivers are evaluated.
        See *Text -> Register* from Blender’s text editor.

        Hint

        You may prefer to use external files instead of Blender’s text-blocks.
        This can be done using a text-block which executes an external file.

        This example runs `driver_namespace.py` located in the same directory as the text-blocks blend-file:

        ```
        import os
        import bpy
        blend_dir = os.path.normalize(os.path.join(__file__, "..", ".."))
        bpy.utils.execfile(os.path.join(blend_dir, "driver_namespace.py"))
        ```

        Using `__file__` ensures the text resolves to the expected path even when library-linked from another file.

        Other methods of populating the drivers name-space can be made to work but tend to be error prone:

        Using The `--python` command line argument to populate name-space often fails to achieve the desired goal
        because the initial evaluation will lookup a function that doesn’t exist yet,
        marking the driver as invalid - preventing further evaluation.

        Populating the driver name-space before the blend-file loads also doesn’t work
        since opening a file clears the name-space.

        It is possible to run a script via the `--python` command line argument, before the blend file.
        This can register a load-post handler ([`bpy.app.handlers.load_post`](handlers.md#bpy.app.handlers.load_post "bpy.app.handlers.load_post")) that initialized the name-space.
        While this works for background tasks it has the downside that opening the file from the file selector
        won’t setup the name-space.

bpy.app.online\_access[¶](#bpy.app.online_access "Link to this definition")
:   Boolean, true when internet access is allowed by Blender & 3rd party scripts (read-only).

    Type:
    :   bool

bpy.app.online\_access\_override[¶](#bpy.app.online_access_override "Link to this definition")
:   Boolean, true when internet access preference is overridden by the command line (read-only).

    Type:
    :   bool

bpy.app.python\_args[¶](#bpy.app.python_args "Link to this definition")
:   Leading arguments to use when calling Python directly (via `sys.executable`). These arguments match settings Blender uses to ensure Python runs with a compatible environment (read-only).

    Type:
    :   tuple[str, …]

bpy.app.render\_icon\_size[¶](#bpy.app.render_icon_size "Link to this definition")
:   Reference size for icon/preview renders (read-only).

    Type:
    :   int

bpy.app.render\_preview\_size[¶](#bpy.app.render_preview_size "Link to this definition")
:   Reference size for icon/preview renders (read-only).

    Type:
    :   int

bpy.app.tempdir[¶](#bpy.app.tempdir "Link to this definition")
:   String, the temp directory used by blender (read-only).

    Type:
    :   str

bpy.app.use\_event\_simulate[¶](#bpy.app.use_event_simulate "Link to this definition")
:   Boolean, for application behavior (started with `--enable-*` matching this attribute name)

    Type:
    :   bool

bpy.app.use\_userpref\_skip\_save\_on\_exit[¶](#bpy.app.use_userpref_skip_save_on_exit "Link to this definition")
:   Boolean, for application behavior (started with `--enable-*` matching this attribute name)

    Type:
    :   bool

bpy.app.background[¶](#bpy.app.background "Link to this definition")
:   Boolean, True when blender is running without a user interface (started with -b)

    Type:
    :   bool

bpy.app.factory\_startup[¶](#bpy.app.factory_startup "Link to this definition")
:   Boolean, True when blender is running with –factory-startup

    Type:
    :   bool

bpy.app.module[¶](#bpy.app.module "Link to this definition")
:   Boolean, True when running Blender as a python module

    Type:
    :   bool

bpy.app.portable[¶](#bpy.app.portable "Link to this definition")
:   Boolean, True unless blender was built to reference absolute paths (on UNIX).

    Type:
    :   bool

bpy.app.build\_branch[¶](#bpy.app.build_branch "Link to this definition")
:   The branch this blender instance was built from

    Type:
    :   bytes

bpy.app.build\_cflags[¶](#bpy.app.build_cflags "Link to this definition")
:   C compiler flags

    Type:
    :   bytes

bpy.app.build\_commit\_date[¶](#bpy.app.build_commit_date "Link to this definition")
:   The date of commit this blender instance was built

    Type:
    :   bytes

bpy.app.build\_commit\_time[¶](#bpy.app.build_commit_time "Link to this definition")
:   The time of commit this blender instance was built

    Type:
    :   bytes

bpy.app.build\_cxxflags[¶](#bpy.app.build_cxxflags "Link to this definition")
:   C++ compiler flags

    Type:
    :   bytes

bpy.app.build\_date[¶](#bpy.app.build_date "Link to this definition")
:   The date this blender instance was built

    Type:
    :   bytes

bpy.app.build\_hash[¶](#bpy.app.build_hash "Link to this definition")
:   The commit hash this blender instance was built with

    Type:
    :   bytes

bpy.app.build\_linkflags[¶](#bpy.app.build_linkflags "Link to this definition")
:   Binary linking flags

    Type:
    :   bytes

bpy.app.build\_platform[¶](#bpy.app.build_platform "Link to this definition")
:   The platform this blender instance was built for

    Type:
    :   bytes

bpy.app.build\_system[¶](#bpy.app.build_system "Link to this definition")
:   Build system used

    Type:
    :   bytes

bpy.app.build\_time[¶](#bpy.app.build_time "Link to this definition")
:   The time this blender instance was built

    Type:
    :   bytes

bpy.app.build\_type[¶](#bpy.app.build_type "Link to this definition")
:   The type of build (Release, Debug)

    Type:
    :   bytes

bpy.app.build\_commit\_timestamp[¶](#bpy.app.build_commit_timestamp "Link to this definition")
:   The unix timestamp of commit this blender instance was built

    Type:
    :   int

bpy.app.version\_cycle[¶](#bpy.app.version_cycle "Link to this definition")
:   The release status of this build alpha/beta/rc/release

    Type:
    :   str

bpy.app.version\_string[¶](#bpy.app.version_string "Link to this definition")
:   The Blender version formatted as a string

    Type:
    :   str

bpy.app.version[¶](#bpy.app.version "Link to this definition")
:   The Blender version as a tuple of 3 numbers (major, minor, micro). eg. (4, 3, 1)

    Type:
    :   tuple[int, int, int]

bpy.app.version\_file[¶](#bpy.app.version_file "Link to this definition")
:   The Blender File version, as a tuple of 3 numbers (major, minor, file sub-version), that will be used to save a .blend file. The last item in this tuple indicates the file sub-version, which is different from the release micro version (the last item of the `bpy.app.version` tuple). The file sub-version can be incremented multiple times while a Blender version is under development. This value is, and should be, used for handling compatibility changes between Blender versions

    Type:
    :   tuple[int, int, int]

bpy.app.alembic[¶](#bpy.app.alembic "Link to this definition")
:   Constant value bpy.app.alembic(supported=True, version=(1, 8, 3), version\_string=’ 1, 8, 3’)

bpy.app.build\_options[¶](#bpy.app.build_options "Link to this definition")
:   Constant value bpy.app.build\_options(bullet=True, codec\_avi=False, codec\_ffmpeg=True, codec\_sndfile=True, compositor\_cpu=True, cycles=True, cycles\_osl=True, freestyle=True, image\_cineon=True, image\_dds=True, image\_hdr=True, image\_openexr=True, image\_openjpeg=True, image\_tiff=True, image\_webp=True, input\_ndof=True, audaspace=True, international=True, openal=True, opensubdiv=True, sdl=False, coreaudio=False, jack=True, pulseaudio=True, wasapi=False, libmv=True, mod\_oceansim=True, mod\_remesh=True, io\_wavefront\_obj=True, io\_ply=True, io\_stl=True, io\_fbx=True, io\_gpencil=True, opencolorio=True, openmp=False, openvdb=True, alembic=True, usd=True, fluid=True, xr\_openxr=True, potrace=True, pugixml=True, haru=True, experimental\_features=False)

bpy.app.ffmpeg[¶](#bpy.app.ffmpeg "Link to this definition")
:   Constant value bpy.app.ffmpeg(supported=True, avcodec\_version=(61, 19, 101), avcodec\_version\_string=’61, 19, 101’, avdevice\_version=(61, 3, 100), avdevice\_version\_string=’61, 3, 100’, avformat\_version=(61, 7, 100), avformat\_version\_string=’61, 7, 100’, avutil\_version=(59, 39, 100), avutil\_version\_string=’59, 39, 100’, swscale\_version=(8, 3, 100), swscale\_version\_string=’ 8, 3, 100’)

bpy.app.ocio[¶](#bpy.app.ocio "Link to this definition")
:   Constant value bpy.app.ocio(supported=True, version=(2, 4, 2), version\_string=’ 2, 4, 2’)

bpy.app.oiio[¶](#bpy.app.oiio "Link to this definition")
:   Constant value bpy.app.oiio(supported=True, version=(3, 0, 9), version\_string=’ 3, 0, 9’)

bpy.app.opensubdiv[¶](#bpy.app.opensubdiv "Link to this definition")
:   Constant value bpy.app.opensubdiv(supported=True, version=(3, 6, 0), version\_string=’ 3, 6, 0’)

bpy.app.openvdb[¶](#bpy.app.openvdb "Link to this definition")
:   Constant value bpy.app.openvdb(supported=True, version=(12, 0, 0), version\_string=’12, 0, 0’)

bpy.app.sdl[¶](#bpy.app.sdl "Link to this definition")
:   Constant value bpy.app.sdl(supported=False, version=(0, 0, 0), version\_string=’Unknown’)

bpy.app.usd[¶](#bpy.app.usd "Link to this definition")
:   Constant value bpy.app.usd(supported=True, version=(0, 25, 8), version\_string=’ 0, 25, 8’)

*static* bpy.app.help\_text(*\**, *all=False*)[¶](#bpy.app.help_text "Link to this definition")
:   Return the help text as a string.

    Parameters:
    :   **all** (*bool*) – Return all arguments, even those which aren’t available for the current platform.

    Returns:
    :   Help text.

    Return type:
    :   str

*static* bpy.app.is\_job\_running(*job\_type*)[¶](#bpy.app.is_job_running "Link to this definition")
:   Check whether a job of the given type is running.

    Parameters:
    :   **job\_type** (*str*) – job type in [Wm Job Type Items](../../../appendix/bpy_types_enum_items/wm_job_type_items.md#rna-enum-wm-job-type-items).

    Returns:
    :   Whether a job of the given type is currently running.

    Return type:
    :   bool

*static* bpy.app.memory\_usage\_undo()[¶](#bpy.app.memory_usage_undo "Link to this definition")
:   Get undo memory usage information.

    Returns:
    :   Memory usage of the undo stack in bytes.

    Return type:
    :   int

[Next

Application Handlers (bpy.app.handlers)](handlers.md)
[Previous

Path Utilities (bpy.path)](../path/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.app.rst%60%0D%0ABlender+Version%3A+%605.0%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F5.0%2Fbpy.app.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Application Data (bpy.app)
  + [`autoexec_fail`](#bpy.app.autoexec_fail)
  + [`autoexec_fail_message`](#bpy.app.autoexec_fail_message)
  + [`autoexec_fail_quiet`](#bpy.app.autoexec_fail_quiet)
  + [`binary_path`](#bpy.app.binary_path)
  + [`debug`](#bpy.app.debug)
  + [`debug_depsgraph`](#bpy.app.debug_depsgraph)
  + [`debug_depsgraph_build`](#bpy.app.debug_depsgraph_build)
  + [`debug_depsgraph_eval`](#bpy.app.debug_depsgraph_eval)
  + [`debug_depsgraph_pretty`](#bpy.app.debug_depsgraph_pretty)
  + [`debug_depsgraph_tag`](#bpy.app.debug_depsgraph_tag)
  + [`debug_depsgraph_time`](#bpy.app.debug_depsgraph_time)
  + [`debug_events`](#bpy.app.debug_events)
  + [`debug_freestyle`](#bpy.app.debug_freestyle)
  + [`debug_handlers`](#bpy.app.debug_handlers)
  + [`debug_io`](#bpy.app.debug_io)
  + [`debug_python`](#bpy.app.debug_python)
  + [`debug_simdata`](#bpy.app.debug_simdata)
  + [`debug_value`](#bpy.app.debug_value)
  + [`debug_wm`](#bpy.app.debug_wm)
  + [`driver_namespace`](#bpy.app.driver_namespace)
  + [`online_access`](#bpy.app.online_access)
  + [`online_access_override`](#bpy.app.online_access_override)
  + [`python_args`](#bpy.app.python_args)
  + [`render_icon_size`](#bpy.app.render_icon_size)
  + [`render_preview_size`](#bpy.app.render_preview_size)
  + [`tempdir`](#bpy.app.tempdir)
  + [`use_event_simulate`](#bpy.app.use_event_simulate)
  + [`use_userpref_skip_save_on_exit`](#bpy.app.use_userpref_skip_save_on_exit)
  + [`background`](#bpy.app.background)
  + [`factory_startup`](#bpy.app.factory_startup)
  + [`module`](#bpy.app.module)
  + [`portable`](#bpy.app.portable)
  + [`build_branch`](#bpy.app.build_branch)
  + [`build_cflags`](#bpy.app.build_cflags)
  + [`build_commit_date`](#bpy.app.build_commit_date)
  + [`build_commit_time`](#bpy.app.build_commit_time)
  + [`build_cxxflags`](#bpy.app.build_cxxflags)
  + [`build_date`](#bpy.app.build_date)
  + [`build_hash`](#bpy.app.build_hash)
  + [`build_linkflags`](#bpy.app.build_linkflags)
  + [`build_platform`](#bpy.app.build_platform)
  + [`build_system`](#bpy.app.build_system)
  + [`build_time`](#bpy.app.build_time)
  + [`build_type`](#bpy.app.build_type)
  + [`build_commit_timestamp`](#bpy.app.build_commit_timestamp)
  + [`version_cycle`](#bpy.app.version_cycle)
  + [`version_string`](#bpy.app.version_string)
  + [`version`](#bpy.app.version)
  + [`version_file`](#bpy.app.version_file)
  + [`alembic`](#bpy.app.alembic)
  + [`build_options`](#bpy.app.build_options)
  + [`ffmpeg`](#bpy.app.ffmpeg)
  + [`ocio`](#bpy.app.ocio)
  + [`oiio`](#bpy.app.oiio)
  + [`opensubdiv`](#bpy.app.opensubdiv)
  + [`openvdb`](#bpy.app.openvdb)
  + [`sdl`](#bpy.app.sdl)
  + [`usd`](#bpy.app.usd)
  + [`help_text()`](#bpy.app.help_text)
  + [`is_job_running()`](#bpy.app.is_job_running)
  + [`memory_usage_undo()`](#bpy.app.memory_usage_undo)