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

# Sound Operators[#](#module-bpy.ops.sound "Link to this heading")

bpy.ops.sound.bake\_animation()[#](#bpy.ops.sound.bake_animation "Link to this definition")
:   Update the audio animation cache

bpy.ops.sound.mixdown(*filepath=''*, *check\_existing=True*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=False*, *filter\_python=False*, *filter\_font=False*, *filter\_sound=True*, *filter\_text=False*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *relative\_path=True*, *display\_type='DEFAULT'*, *sort\_method=''*, *accuracy=1024*, *container='FLAC'*, *codec='FLAC'*, *format='S16'*, *bitrate=192*, *split\_channels=False*)[#](#bpy.ops.sound.mixdown "Link to this definition")
:   Mix the scene’s audio to a sound file

    Parameters:
    :   * **filepath** (*string**,* *(**optional**,* *never None**)*) – File Path, Path to file
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
        * **accuracy** (*int in* *[**1**,* *inf**]**,* *(**optional**)*) – Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate)
        * **container** (*enum in* *[**'AC3'**,* *'FLAC'**,* *'MATROSKA'**,* *'MP2'**,* *'MP3'**,* *'OGG'**,* *'WAV'**]**,* *(**optional**)*) –

          Container, File format

          + `AC3`
            ac3 – Dolby Digital ATRAC 3.
          + `FLAC`
            flac – Free Lossless Audio Codec.
          + `MATROSKA`
            mkv – Matroska.
          + `MP2`
            mp2 – MPEG-1 Audio Layer II.
          + `MP3`
            mp3 – MPEG-2 Audio Layer III.
          + `OGG`
            ogg – Xiph.Org Ogg Container.
          + `WAV`
            wav – Waveform Audio File Format.
        * **codec** (*enum in* *[**'AAC'**,* *'AC3'**,* *'FLAC'**,* *'MP2'**,* *'MP3'**,* *'PCM'**,* *'VORBIS'**]**,* *(**optional**)*) –

          Codec, Audio Codec

          + `AAC`
            AAC – Advanced Audio Coding.
          + `AC3`
            AC3 – Dolby Digital ATRAC 3.
          + `FLAC`
            FLAC – Free Lossless Audio Codec.
          + `MP2`
            MP2 – MPEG-1 Audio Layer II.
          + `MP3`
            MP3 – MPEG-2 Audio Layer III.
          + `PCM`
            PCM – Pulse Code Modulation (RAW).
          + `VORBIS`
            Vorbis – Xiph.Org Vorbis Codec.
        * **format** (*enum in* *[**'U8'**,* *'S16'**,* *'S24'**,* *'S32'**,* *'F32'**,* *'F64'**]**,* *(**optional**)*) –

          Format, Sample format

          + `U8`
            U8 – 8-bit unsigned.
          + `S16`
            S16 – 16-bit signed.
          + `S24`
            S24 – 24-bit signed.
          + `S32`
            S32 – 32-bit signed.
          + `F32`
            F32 – 32-bit floating-point.
          + `F64`
            F64 – 64-bit floating-point.
        * **bitrate** (*int in* *[**32**,* *512**]**,* *(**optional**)*) – Bitrate, Bitrate in kbit/s
        * **split\_channels** (*boolean**,* *(**optional**)*) – Split channels, Each channel will be rendered into a mono file

bpy.ops.sound.open(*filepath=''*, *hide\_props\_region=True*, *check\_existing=False*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=True*, *filter\_python=False*, *filter\_font=False*, *filter\_sound=True*, *filter\_text=False*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *relative\_path=True*, *show\_multiview=False*, *use\_multiview=False*, *display\_type='DEFAULT'*, *sort\_method=''*, *cache=False*, *mono=False*)[#](#bpy.ops.sound.open "Link to this definition")
:   Load a sound file

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
        * **sort\_method** (*enum in* *[**]**,* *(**optional**)*) – File sorting mode
        * **cache** (*boolean**,* *(**optional**)*) – Cache, Cache the sound in memory
        * **mono** (*boolean**,* *(**optional**)*) – Mono, Merge all the sound’s channels into one

bpy.ops.sound.open\_mono(*filepath=''*, *hide\_props\_region=True*, *check\_existing=False*, *filter\_blender=False*, *filter\_backup=False*, *filter\_image=False*, *filter\_movie=True*, *filter\_python=False*, *filter\_font=False*, *filter\_sound=True*, *filter\_text=False*, *filter\_archive=False*, *filter\_btx=False*, *filter\_collada=False*, *filter\_alembic=False*, *filter\_usd=False*, *filter\_obj=False*, *filter\_volume=False*, *filter\_folder=True*, *filter\_blenlib=False*, *filemode=9*, *relative\_path=True*, *show\_multiview=False*, *use\_multiview=False*, *display\_type='DEFAULT'*, *sort\_method=''*, *cache=False*, *mono=True*)[#](#bpy.ops.sound.open_mono "Link to this definition")
:   Load a sound file as mono

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
        * **sort\_method** (*enum in* *[**]**,* *(**optional**)*) – File sorting mode
        * **cache** (*boolean**,* *(**optional**)*) – Cache, Cache the sound in memory
        * **mono** (*boolean**,* *(**optional**)*) – Mono, Mixdown the sound to mono

bpy.ops.sound.pack()[#](#bpy.ops.sound.pack "Link to this definition")
:   Pack the sound into the current blend file

bpy.ops.sound.unpack(*method='USE\_LOCAL'*, *id=''*)[#](#bpy.ops.sound.unpack "Link to this definition")
:   Unpack the sound to the samples filename

    Parameters:
    :   * **method** (enum in [Unpack Method Items](../../../appendix/bpy_types_enum_items/unpack_method_items.md#rna-enum-unpack-method-items), (optional)) – Method, How to unpack
        * **id** (*string**,* *(**optional**,* *never None**)*) – Sound Name, Sound data-block name to unpack

bpy.ops.sound.update\_animation\_flags()[#](#bpy.ops.sound.update_animation_flags "Link to this definition")
:   Update animation flags

[Next

Spreadsheet Operators](spreadsheet.md)
[Previous

Sequencer Operators](sequencer.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.sound.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.sound.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Sound Operators
  + [`bake_animation()`](#bpy.ops.sound.bake_animation)
  + [`mixdown()`](#bpy.ops.sound.mixdown)
  + [`open()`](#bpy.ops.sound.open)
  + [`open_mono()`](#bpy.ops.sound.open_mono)
  + [`pack()`](#bpy.ops.sound.pack)
  + [`unpack()`](#bpy.ops.sound.unpack)
  + [`update_animation_flags()`](#bpy.ops.sound.update_animation_flags)