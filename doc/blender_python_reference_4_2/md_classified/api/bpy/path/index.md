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
* [Types (bpy.types)](../types/index.md)[ ]
* [Utilities (bpy.utils)](../utils/index.md)[ ]
* Path Utilities (bpy.path)
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

# Path Utilities (bpy.path)[#](#module-bpy.path "Link to this heading")

This module has a similar scope to os.path, containing utility
functions for dealing with paths in Blender.

bpy.path.abspath(*path*, *\**, *start=None*, *library=None*)[#](#bpy.path.abspath "Link to this definition")
:   Returns the absolute path relative to the current blend file
    using the “//” prefix.

    Parameters:
    :   * **start** (*string* *or* *bytes*) – Relative to this path,
          when not set the current filename is used.
        * **library** ([`bpy.types.Library`](../types/Library.md#bpy.types.Library "bpy.types.Library")) – The library this path is from. This is only included for
          convenience, when the library is not None its path replaces *start*.

    Returns:
    :   The absolute path.

    Return type:
    :   string

bpy.path.basename(*path*)[#](#bpy.path.basename "Link to this definition")
:   Equivalent to `os.path.basename`, but skips a “//” prefix.

    Use for Windows compatibility.

    Returns:
    :   The base name of the given path.

    Return type:
    :   string

bpy.path.clean\_name(*name*, *\**, *replace='\_'*)[#](#bpy.path.clean_name "Link to this definition")
:   Returns a name with characters replaced that
    may cause problems under various circumstances,
    such as writing to a file.

    All characters besides A-Z/a-z, 0-9 are replaced with “\_”
    or the *replace* argument if defined.

    Parameters:
    :   * **name** (*string* *or* *bytes*) – The path name.
        * **replace** (*string*) – The replacement for non-valid characters.

    Returns:
    :   The cleaned name.

    Return type:
    :   string

bpy.path.display\_name(*name*, *\**, *has\_ext=True*, *title\_case=True*)[#](#bpy.path.display_name "Link to this definition")
:   Creates a display string from name to be used menus and the user interface.
    Intended for use with filenames and module names.

    Parameters:
    :   * **name** (*string*) – The name to be used for displaying the user interface.
        * **has\_ext** (*boolean*) – Remove file extension from name.
        * **title\_case** (*boolean*) – Convert lowercase names to title case.

    Returns:
    :   The display string.

    Return type:
    :   string

bpy.path.display\_name\_to\_filepath(*name*)[#](#bpy.path.display_name_to_filepath "Link to this definition")
:   Performs the reverse of display\_name using literal versions of characters
    which aren’t supported in a filepath.

    Parameters:
    :   **name** (*string*) – The display name to convert.

    Returns:
    :   The file path.

    Return type:
    :   string

bpy.path.display\_name\_from\_filepath(*name*)[#](#bpy.path.display_name_from_filepath "Link to this definition")
:   Returns the path stripped of directory and extension,
    ensured to be utf8 compatible.

    Parameters:
    :   **name** (*string*) – The file path to convert.

    Returns:
    :   The display name.

    Return type:
    :   string

bpy.path.ensure\_ext(*filepath*, *ext*, *\**, *case\_sensitive=False*)[#](#bpy.path.ensure_ext "Link to this definition")
:   Return the path with the extension added if it is not already set.

    Parameters:
    :   * **filepath** (*string*) – The file path.
        * **ext** (*string*) – The extension to check for, can be a compound extension. Should
          start with a dot, such as ‘.blend’ or ‘.tar.gz’.
        * **case\_sensitive** (*boolean*) – Check for matching case when comparing extensions.

    Returns:
    :   The file path with the given extension.

    Return type:
    :   string

bpy.path.is\_subdir(*path*, *directory*)[#](#bpy.path.is_subdir "Link to this definition")
:   Returns true if *path* in a subdirectory of *directory*.
    Both paths must be absolute.

    Parameters:
    :   **path** (*string* *or* *bytes*) – An absolute path.

    Returns:
    :   Whether or not the path is a subdirectory.

    Return type:
    :   boolean

bpy.path.module\_names(*path*, *\**, *recursive=False*, *package=''*)[#](#bpy.path.module_names "Link to this definition")
:   Return a list of modules which can be imported from *path*.

    Parameters:
    :   * **path** (*string*) – a directory to scan.
        * **recursive** (*bool*) – Also return submodule names for packages.
        * **package** (*string*) – Optional string, used as the prefix for module names (without the trailing “.”).

    Returns:
    :   a list of string pairs (module\_name, module\_file).

    Return type:
    :   list of strings

bpy.path.native\_pathsep(*path*)[#](#bpy.path.native_pathsep "Link to this definition")
:   Replace the path separator with the systems native `os.sep`.

    Parameters:
    :   **path** (*string*) – The path to replace.

    Returns:
    :   The path with system native separators.

    Return type:
    :   string

bpy.path.reduce\_dirs(*dirs*)[#](#bpy.path.reduce_dirs "Link to this definition")
:   Given a sequence of directories, remove duplicates and
    any directories nested in one of the other paths.
    (Useful for recursive path searching).

    Parameters:
    :   **dirs** (*sequence* *of* *strings*) – Sequence of directory paths.

    Returns:
    :   A unique list of paths.

    Return type:
    :   list of strings

bpy.path.relpath(*path*, *\**, *start=None*)[#](#bpy.path.relpath "Link to this definition")
:   Returns the path relative to the current blend file using the “//” prefix.

    Parameters:
    :   * **path** (*string* *or* *bytes*) – An absolute path.
        * **start** (*string* *or* *bytes*) – Relative to this path,
          when not set the current filename is used.

    Returns:
    :   The relative path.

    Return type:
    :   string

bpy.path.resolve\_ncase(*path*)[#](#bpy.path.resolve_ncase "Link to this definition")
:   Resolve a case insensitive path on a case sensitive system,
    returning a string with the path if found else return the original path.

    Parameters:
    :   **path** (*string*) – The path name to resolve.

    Returns:
    :   The resolved path.

    Return type:
    :   string

[Next

Application Data (bpy.app)](../app/index.md)
[Previous

bpy.utils submodule (bpy.utils.units)](../utils/units.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.path.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.path.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Path Utilities (bpy.path)
  + [`abspath()`](#bpy.path.abspath)
  + [`basename()`](#bpy.path.basename)
  + [`clean_name()`](#bpy.path.clean_name)
  + [`display_name()`](#bpy.path.display_name)
  + [`display_name_to_filepath()`](#bpy.path.display_name_to_filepath)
  + [`display_name_from_filepath()`](#bpy.path.display_name_from_filepath)
  + [`ensure_ext()`](#bpy.path.ensure_ext)
  + [`is_subdir()`](#bpy.path.is_subdir)
  + [`module_names()`](#bpy.path.module_names)
  + [`native_pathsep()`](#bpy.path.native_pathsep)
  + [`reduce_dirs()`](#bpy.path.reduce_dirs)
  + [`relpath()`](#bpy.path.relpath)
  + [`resolve_ncase()`](#bpy.path.resolve_ncase)