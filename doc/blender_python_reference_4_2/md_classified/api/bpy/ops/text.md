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

# Text Operators[#](#module-bpy.ops.text "Link to this heading")

bpy.ops.text.autocomplete()[#](#bpy.ops.text.autocomplete "Link to this definition")
:   Show a list of used text in the open document

bpy.ops.text.comment\_toggle(*type='TOGGLE'*)[#](#bpy.ops.text.comment_toggle "Link to this definition")
:   Undocumented, consider [contributing](https://developer.blender.org/).

    Parameters:
    :   **type** (*enum in* *[**'TOGGLE'**,* *'COMMENT'**,* *'UNCOMMENT'**]**,* *(**optional**)*) – Type, Add or remove comments

bpy.ops.text.convert\_whitespace(*type='SPACES'*)[#](#bpy.ops.text.convert_whitespace "Link to this definition")
:   Convert whitespaces by type

    Parameters:
    :   **type** (*enum in* *[**'SPACES'**,* *'TABS'**]**,* *(**optional**)*) – Type, Type of whitespace to convert to

bpy.ops.text.copy()[#](#bpy.ops.text.copy "Link to this definition")
:   Copy selected text to clipboard

bpy.ops.text.cursor\_set(*x=0*, *y=0*)[#](#bpy.ops.text.cursor_set "Link to this definition")
:   Set cursor position

    Parameters:
    :   * **x** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – X
        * **y** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Y

bpy.ops.text.cut()[#](#bpy.ops.text.cut "Link to this definition")
:   Cut selected text to clipboard

bpy.ops.text.delete(*type='NEXT\_CHARACTER'*)[#](#bpy.ops.text.delete "Link to this definition")
:   Delete text by cursor position

    Parameters:
    :   **type** (*enum in* *[**'NEXT\_CHARACTER'**,* *'PREVIOUS\_CHARACTER'**,* *'NEXT\_WORD'**,* *'PREVIOUS\_WORD'**]**,* *(**optional**)*) – Type, Which part of the text to delete

bpy.ops.text.duplicate\_line()[#](#bpy.ops.text.duplicate_line "Link to this definition")
:   Duplicate the current line

bpy.ops.text.find()[#](#bpy.ops.text.find "Link to this definition")
:   Find specified text

bpy.ops.text.find\_set\_selected()[#](#bpy.ops.text.find_set_selected "Link to this definition")
:   Find specified text and set as selected

bpy.ops.text.indent()[#](#bpy.ops.text.indent "Link to this definition")
:   Indent selected text

bpy.ops.text.indent\_or\_autocomplete()[#](#bpy.ops.text.indent_or_autocomplete "Link to this definition")
:   Indent selected text or autocomplete

bpy.ops.text.insert(*text=''*)[#](#bpy.ops.text.insert "Link to this definition")
:   Insert text at cursor position

    Parameters:
    :   **text** (*string**,* *(**optional**,* *never None**)*) – Text, Text to insert at the cursor position

bpy.ops.text.jump(*line=1*)[#](#bpy.ops.text.jump "Link to this definition")
:   Jump cursor to line

    Parameters:
    :   **line** (*int in* *[**1**,* *inf**]**,* *(**optional**)*) – Line, Line number to jump to

bpy.ops.text.jump\_to\_file\_at\_point(*filepath=''*, *line=0*, *column=0*)[#](#bpy.ops.text.jump_to_file_at_point "Link to this definition")
:   Jump to a file for the text editor

    Parameters:
    :   * **filepath** (*string**,* *(**optional**,* *never None**)*) – Filepath
        * **line** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Line, Line to jump to
        * **column** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Column, Column to jump to

bpy.ops.text.line\_break()[#](#bpy.ops.text.line_break "Link to this definition")
:   Insert line break at cursor position

bpy.ops.text.line\_number()[#](#bpy.ops.text.line_number "Link to this definition")
:   The current line number

bpy.ops.text.make\_internal()[#](#bpy.ops.text.make_internal "Link to this definition")
:   Make active text file internal

bpy.ops.text.move(*type='LINE\_BEGIN'*)[#](#bpy.ops.text.move "Link to this definition")
:   Move cursor to position type

    Parameters:
    :   **type** (*enum in* *[**'LINE\_BEGIN'**,* *'LINE\_END'**,* *'FILE\_TOP'**,* *'FILE\_BOTTOM'**,* *'PREVIOUS\_CHARACTER'**,* *'NEXT\_CHARACTER'**,* *'PREVIOUS\_WORD'**,* *'NEXT\_WORD'**,* *'PREVIOUS\_LINE'**,* *'NEXT\_LINE'**,* *'PREVIOUS\_PAGE'**,* *'NEXT\_PAGE'**]**,* *(**optional**)*) – Type, Where to move cursor to

bpy.ops.text.move\_lines(*direction='DOWN'*)[#](#bpy.ops.text.move_lines "Link to this definition")
:   Move the currently selected line(s) up/down

    Parameters:
    :   **direction** (*enum in* *[**'UP'**,* *'DOWN'**]**,* *(**optional**)*) – Direction

bpy.ops.text.move\_select(*type='LINE\_BEGIN'*)[#](#bpy.ops.text.move_select "Link to this definition")
:   Move the cursor while selecting

    Parameters:
    :   **type** (*enum in* *[**'LINE\_BEGIN'**,* *'LINE\_END'**,* *'FILE\_TOP'**,* *'FILE\_BOTTOM'**,* *'PREVIOUS\_CHARACTER'**,* *'NEXT\_CHARACTER'**,* *'PREVIOUS\_WORD'**,* *'NEXT\_WORD'**,* *'PREVIOUS\_LINE'**,* *'NEXT\_LINE'**,* *'PREVIOUS\_PAGE'**,* *'NEXT\_PAGE'**]**,* *(**optional**)*) – Type, Where to move cursor to, to make a selection

bpy.ops.text.new()[#](#bpy.ops.text.new "Link to this definition")
:   Create a new text data-block

bpy.ops.text.open(*filepath=''*, *hide\_props\_region=True*, *check\_existing=False*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=False*, *filter\_python=True*, *filter\_font=False*, *filter\_sound=False*, *filter\_text=True*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *display\_type='DEFAULT'*, *sort\_method=''*, *internal=False*)[#](#bpy.ops.text.open "Link to this definition")
:   Open a new text data-block

    Parameters:
    :   * **filepath** (*string**,* *(**optional**,* *never None**)*) – File Path, Path to file
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
        * **internal** (*boolean**,* *(**optional**)*) – Make Internal, Make text file internal after loading

bpy.ops.text.overwrite\_toggle()[#](#bpy.ops.text.overwrite_toggle "Link to this definition")
:   Toggle overwrite while typing

bpy.ops.text.paste(*selection=False*)[#](#bpy.ops.text.paste "Link to this definition")
:   Paste text from clipboard

    Parameters:
    :   **selection** (*boolean**,* *(**optional**)*) – Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)

bpy.ops.text.refresh\_pyconstraints()[#](#bpy.ops.text.refresh_pyconstraints "Link to this definition")
:   Refresh all pyconstraints

bpy.ops.text.reload()[#](#bpy.ops.text.reload "Link to this definition")
:   Reload active text data-block from its file

bpy.ops.text.replace(*all=False*)[#](#bpy.ops.text.replace "Link to this definition")
:   Replace text with the specified text

    Parameters:
    :   **all** (*boolean**,* *(**optional**)*) – Replace All, Replace all occurrences

bpy.ops.text.replace\_set\_selected()[#](#bpy.ops.text.replace_set_selected "Link to this definition")
:   Replace text with specified text and set as selected

bpy.ops.text.resolve\_conflict(*resolution='IGNORE'*)[#](#bpy.ops.text.resolve_conflict "Link to this definition")
:   When external text is out of sync, resolve the conflict

    Parameters:
    :   **resolution** (*enum in* *[**'IGNORE'**,* *'RELOAD'**,* *'SAVE'**,* *'MAKE\_INTERNAL'**]**,* *(**optional**)*) – Resolution, How to solve conflict due to differences in internal and external text

bpy.ops.text.run\_script()[#](#bpy.ops.text.run_script "Link to this definition")
:   Run active script

bpy.ops.text.save()[#](#bpy.ops.text.save "Link to this definition")
:   Save active text data-block

bpy.ops.text.save\_as(*filepath=''*, *hide\_props\_region=True*, *check\_existing=True*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=False*, *filter\_python=True*, *filter\_font=False*, *filter\_sound=False*, *filter\_text=True*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *display\_type='DEFAULT'*, *sort\_method=''*)[#](#bpy.ops.text.save_as "Link to this definition")
:   Save active text file with options

    Parameters:
    :   * **filepath** (*string**,* *(**optional**,* *never None**)*) – File Path, Path to file
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
        * **sort\_method** (*enum in* *[**]**,* *(**optional**)*) – File sorting mode

bpy.ops.text.scroll(*lines=1*)[#](#bpy.ops.text.scroll "Link to this definition")
:   Undocumented, consider [contributing](https://developer.blender.org/).

    Parameters:
    :   **lines** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Lines, Number of lines to scroll

bpy.ops.text.scroll\_bar(*lines=1*)[#](#bpy.ops.text.scroll_bar "Link to this definition")
:   Undocumented, consider [contributing](https://developer.blender.org/).

    Parameters:
    :   **lines** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Lines, Number of lines to scroll

bpy.ops.text.select\_all()[#](#bpy.ops.text.select_all "Link to this definition")
:   Select all text

bpy.ops.text.select\_line()[#](#bpy.ops.text.select_line "Link to this definition")
:   Select text by line

bpy.ops.text.select\_word()[#](#bpy.ops.text.select_word "Link to this definition")
:   Select word under cursor

bpy.ops.text.selection\_set()[#](#bpy.ops.text.selection_set "Link to this definition")
:   Set text selection

bpy.ops.text.start\_find()[#](#bpy.ops.text.start_find "Link to this definition")
:   Start searching text

bpy.ops.text.to\_3d\_object(*split\_lines=False*)[#](#bpy.ops.text.to_3d_object "Link to this definition")
:   Create 3D text object from active text data-block

    Parameters:
    :   **split\_lines** (*boolean**,* *(**optional**)*) – Split Lines, Create one object per line in the text

bpy.ops.text.unindent()[#](#bpy.ops.text.unindent "Link to this definition")
:   Unindent selected text

bpy.ops.text.unlink()[#](#bpy.ops.text.unlink "Link to this definition")
:   Unlink active text data-block

[Next

Text Editor Operators](text_editor.md)
[Previous

Surface Operators](surface.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.text.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.text.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Text Operators
  + [`autocomplete()`](#bpy.ops.text.autocomplete)
  + [`comment_toggle()`](#bpy.ops.text.comment_toggle)
  + [`convert_whitespace()`](#bpy.ops.text.convert_whitespace)
  + [`copy()`](#bpy.ops.text.copy)
  + [`cursor_set()`](#bpy.ops.text.cursor_set)
  + [`cut()`](#bpy.ops.text.cut)
  + [`delete()`](#bpy.ops.text.delete)
  + [`duplicate_line()`](#bpy.ops.text.duplicate_line)
  + [`find()`](#bpy.ops.text.find)
  + [`find_set_selected()`](#bpy.ops.text.find_set_selected)
  + [`indent()`](#bpy.ops.text.indent)
  + [`indent_or_autocomplete()`](#bpy.ops.text.indent_or_autocomplete)
  + [`insert()`](#bpy.ops.text.insert)
  + [`jump()`](#bpy.ops.text.jump)
  + [`jump_to_file_at_point()`](#bpy.ops.text.jump_to_file_at_point)
  + [`line_break()`](#bpy.ops.text.line_break)
  + [`line_number()`](#bpy.ops.text.line_number)
  + [`make_internal()`](#bpy.ops.text.make_internal)
  + [`move()`](#bpy.ops.text.move)
  + [`move_lines()`](#bpy.ops.text.move_lines)
  + [`move_select()`](#bpy.ops.text.move_select)
  + [`new()`](#bpy.ops.text.new)
  + [`open()`](#bpy.ops.text.open)
  + [`overwrite_toggle()`](#bpy.ops.text.overwrite_toggle)
  + [`paste()`](#bpy.ops.text.paste)
  + [`refresh_pyconstraints()`](#bpy.ops.text.refresh_pyconstraints)
  + [`reload()`](#bpy.ops.text.reload)
  + [`replace()`](#bpy.ops.text.replace)
  + [`replace_set_selected()`](#bpy.ops.text.replace_set_selected)
  + [`resolve_conflict()`](#bpy.ops.text.resolve_conflict)
  + [`run_script()`](#bpy.ops.text.run_script)
  + [`save()`](#bpy.ops.text.save)
  + [`save_as()`](#bpy.ops.text.save_as)
  + [`scroll()`](#bpy.ops.text.scroll)
  + [`scroll_bar()`](#bpy.ops.text.scroll_bar)
  + [`select_all()`](#bpy.ops.text.select_all)
  + [`select_line()`](#bpy.ops.text.select_line)
  + [`select_word()`](#bpy.ops.text.select_word)
  + [`selection_set()`](#bpy.ops.text.selection_set)
  + [`start_find()`](#bpy.ops.text.start_find)
  + [`to_3d_object()`](#bpy.ops.text.to_3d_object)
  + [`unindent()`](#bpy.ops.text.unindent)
  + [`unlink()`](#bpy.ops.text.unlink)