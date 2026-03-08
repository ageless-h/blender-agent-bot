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

# Font Operators[#](#module-bpy.ops.font "Link to this heading")

bpy.ops.font.case\_set(*case='LOWER'*)[#](#bpy.ops.font.case_set "Link to this definition")
:   Set font case

    Parameters:
    :   **case** (*enum in* *[**'LOWER'**,* *'UPPER'**]**,* *(**optional**)*) – Case, Lower or upper case

bpy.ops.font.case\_toggle()[#](#bpy.ops.font.case_toggle "Link to this definition")
:   Toggle font case

bpy.ops.font.change\_character(*delta=1*)[#](#bpy.ops.font.change_character "Link to this definition")
:   Change font character code

    Parameters:
    :   **delta** (*int in* *[**-255**,* *255**]**,* *(**optional**)*) – Delta, Number to increase or decrease character code with

bpy.ops.font.change\_spacing(*delta=1.0*)[#](#bpy.ops.font.change_spacing "Link to this definition")
:   Change font spacing

    Parameters:
    :   **delta** (*float in* *[**-inf**,* *inf**]**,* *(**optional**)*) – Delta, Amount to decrease or increase character spacing with

bpy.ops.font.delete(*type='PREVIOUS\_CHARACTER'*)[#](#bpy.ops.font.delete "Link to this definition")
:   Delete text by cursor position

    Parameters:
    :   **type** (*enum in* *[**'NEXT\_CHARACTER'**,* *'PREVIOUS\_CHARACTER'**,* *'NEXT\_WORD'**,* *'PREVIOUS\_WORD'**,* *'SELECTION'**,* *'NEXT\_OR\_SELECTION'**,* *'PREVIOUS\_OR\_SELECTION'**]**,* *(**optional**)*) – Type, Which part of the text to delete

bpy.ops.font.line\_break()[#](#bpy.ops.font.line_break "Link to this definition")
:   Insert line break at cursor position

bpy.ops.font.move(*type='LINE\_BEGIN'*)[#](#bpy.ops.font.move "Link to this definition")
:   Move cursor to position type

    Parameters:
    :   **type** (*enum in* *[**'LINE\_BEGIN'**,* *'LINE\_END'**,* *'TEXT\_BEGIN'**,* *'TEXT\_END'**,* *'PREVIOUS\_CHARACTER'**,* *'NEXT\_CHARACTER'**,* *'PREVIOUS\_WORD'**,* *'NEXT\_WORD'**,* *'PREVIOUS\_LINE'**,* *'NEXT\_LINE'**,* *'PREVIOUS\_PAGE'**,* *'NEXT\_PAGE'**]**,* *(**optional**)*) – Type, Where to move cursor to

bpy.ops.font.move\_select(*type='LINE\_BEGIN'*)[#](#bpy.ops.font.move_select "Link to this definition")
:   Move the cursor while selecting

    Parameters:
    :   **type** (*enum in* *[**'LINE\_BEGIN'**,* *'LINE\_END'**,* *'TEXT\_BEGIN'**,* *'TEXT\_END'**,* *'PREVIOUS\_CHARACTER'**,* *'NEXT\_CHARACTER'**,* *'PREVIOUS\_WORD'**,* *'NEXT\_WORD'**,* *'PREVIOUS\_LINE'**,* *'NEXT\_LINE'**,* *'PREVIOUS\_PAGE'**,* *'NEXT\_PAGE'**]**,* *(**optional**)*) – Type, Where to move cursor to, to make a selection

bpy.ops.font.open(*filepath=''*, *hide\_props\_region=True*, *check\_existing=False*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=False*, *filter\_python=False*, *filter\_font=True*, *filter\_sound=False*, *filter\_text=False*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *relative\_path=True*, *display\_type='THUMBNAIL'*, *sort\_method=''*)[#](#bpy.ops.font.open "Link to this definition")
:   Load a new font from a file

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
        * **relative\_path** (*boolean**,* *(**optional**)*) – Relative Path, Select the file relative to the blend file
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

bpy.ops.font.select\_all()[#](#bpy.ops.font.select_all "Link to this definition")
:   Select all text

bpy.ops.font.select\_word()[#](#bpy.ops.font.select_word "Link to this definition")
:   Select word under cursor

bpy.ops.font.selection\_set()[#](#bpy.ops.font.selection_set "Link to this definition")
:   Set cursor selection

bpy.ops.font.style\_set(*style='BOLD'*, *clear=False*)[#](#bpy.ops.font.style_set "Link to this definition")
:   Set font style

    Parameters:
    :   * **style** (*enum in* *[**'BOLD'**,* *'ITALIC'**,* *'UNDERLINE'**,* *'SMALL\_CAPS'**]**,* *(**optional**)*) – Style, Style to set selection to
        * **clear** (*boolean**,* *(**optional**)*) – Clear, Clear style rather than setting it

bpy.ops.font.style\_toggle(*style='BOLD'*)[#](#bpy.ops.font.style_toggle "Link to this definition")
:   Toggle font style

    Parameters:
    :   **style** (*enum in* *[**'BOLD'**,* *'ITALIC'**,* *'UNDERLINE'**,* *'SMALL\_CAPS'**]**,* *(**optional**)*) – Style, Style to set selection to

bpy.ops.font.text\_copy()[#](#bpy.ops.font.text_copy "Link to this definition")
:   Copy selected text to clipboard

bpy.ops.font.text\_cut()[#](#bpy.ops.font.text_cut "Link to this definition")
:   Cut selected text to clipboard

bpy.ops.font.text\_insert(*text=''*, *accent=False*)[#](#bpy.ops.font.text_insert "Link to this definition")
:   Insert text at cursor position

    Parameters:
    :   * **text** (*string**,* *(**optional**,* *never None**)*) – Text, Text to insert at the cursor position
        * **accent** (*boolean**,* *(**optional**)*) – Accent Mode, Next typed character will strike through previous, for special character input

bpy.ops.font.text\_insert\_unicode()[#](#bpy.ops.font.text_insert_unicode "Link to this definition")
:   Insert Unicode Character

bpy.ops.font.text\_paste(*selection=False*)[#](#bpy.ops.font.text_paste "Link to this definition")
:   Paste text from clipboard

    Parameters:
    :   **selection** (*boolean**,* *(**optional**)*) – Selection, Paste text selected elsewhere rather than copied (X11/Wayland only)

bpy.ops.font.text\_paste\_from\_file(*filepath=''*, *hide\_props\_region=True*, *check\_existing=False*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=False*, *filter\_python=False*, *filter\_font=False*, *filter\_sound=False*, *filter\_text=True*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *display\_type='DEFAULT'*, *sort\_method=''*)[#](#bpy.ops.font.text_paste_from_file "Link to this definition")
:   Paste contents from file

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

bpy.ops.font.textbox\_add()[#](#bpy.ops.font.textbox_add "Link to this definition")
:   Add a new text box

bpy.ops.font.textbox\_remove(*index=0*)[#](#bpy.ops.font.textbox_remove "Link to this definition")
:   Remove the text box

    Parameters:
    :   **index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Index, The current text box

bpy.ops.font.unlink()[#](#bpy.ops.font.unlink "Link to this definition")
:   Unlink active font data-block

[Next

Geometry Operators](geometry.md)
[Previous

Fluid Operators](fluid.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.font.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.font.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Font Operators
  + [`case_set()`](#bpy.ops.font.case_set)
  + [`case_toggle()`](#bpy.ops.font.case_toggle)
  + [`change_character()`](#bpy.ops.font.change_character)
  + [`change_spacing()`](#bpy.ops.font.change_spacing)
  + [`delete()`](#bpy.ops.font.delete)
  + [`line_break()`](#bpy.ops.font.line_break)
  + [`move()`](#bpy.ops.font.move)
  + [`move_select()`](#bpy.ops.font.move_select)
  + [`open()`](#bpy.ops.font.open)
  + [`select_all()`](#bpy.ops.font.select_all)
  + [`select_word()`](#bpy.ops.font.select_word)
  + [`selection_set()`](#bpy.ops.font.selection_set)
  + [`style_set()`](#bpy.ops.font.style_set)
  + [`style_toggle()`](#bpy.ops.font.style_toggle)
  + [`text_copy()`](#bpy.ops.font.text_copy)
  + [`text_cut()`](#bpy.ops.font.text_cut)
  + [`text_insert()`](#bpy.ops.font.text_insert)
  + [`text_insert_unicode()`](#bpy.ops.font.text_insert_unicode)
  + [`text_paste()`](#bpy.ops.font.text_paste)
  + [`text_paste_from_file()`](#bpy.ops.font.text_paste_from_file)
  + [`textbox_add()`](#bpy.ops.font.textbox_add)
  + [`textbox_remove()`](#bpy.ops.font.textbox_remove)
  + [`unlink()`](#bpy.ops.font.unlink)