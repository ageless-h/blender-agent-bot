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

# Image(ID)[#](#image-id "Link to this heading")

## Image Data[#](#image-data "Link to this heading")

The Image data-block is a shallow wrapper around image or video file(s)
(on disk, as packed data, or generated).

All actual data like the pixel buffer, size, resolution etc. is
cached in an [`imbuf.types.ImBuf`](../../imbuf/types/index.md#imbuf.types.ImBuf "imbuf.types.ImBuf") image buffer (or several buffers
in some cases, like UDIM textures, multi-views, animations…).

Several properties and functions of the Image data-block are then actually
using/modifying its image buffer, and not the Image data-block itself.

Warning

One key limitation is that image buffers are not shared between different
Image data-blocks, and they are not duplicated when copying an image.

So until a modified image buffer is saved on disk, duplicating its Image
data-block will not propagate the underlying buffer changes to the new Image.

This example script generates an Image data-block with a given size,
change its first pixel, rescale it, and duplicates the image.

The duplicated image still has the same size and colors as the original image
at its creation, all editing in the original image’s buffer is ‘lost’ in its copy.

```
import bpy

image_src = bpy.data.images.new('src', 1024, 102)
print(image_src.size)
print(image_src.pixels[0:4])

image_src.scale(1024, 720)
image_src.pixels[0:4] = (0.5, 0.5, 0.5, 0.5)
image_src.update()
print(image_src.size)
print(image_src.pixels[0:4])

image_dest = image_src.copy()
image_dest.update()
print(image_dest.size)
print(image_dest.pixels[0:4])
```

base classes — [`bpy_struct`](bpy_struct.md#bpy.types.bpy_struct "bpy.types.bpy_struct"), [`ID`](ID.md#bpy.types.ID "bpy.types.ID")

*class* bpy.types.Image(*ID*)[#](#bpy.types.Image "Link to this definition")
:   Image data-block referencing an external or packed image

    alpha\_mode[#](#bpy.types.Image.alpha_mode "Link to this definition")
    :   Representation of alpha in the image file, to convert to and from when saving and loading the image

        * `STRAIGHT`
          Straight – Store RGB and alpha channels separately with alpha acting as a mask, also known as unassociated alpha. Commonly used by image editing applications and file formats like PNG.
        * `PREMUL`
          Premultiplied – Store RGB channels with alpha multiplied in, also known as associated alpha. The natural format for renders and used by file formats like OpenEXR.
        * `CHANNEL_PACKED`
          Channel Packed – Different images are packed in the RGB and alpha channels, and they should not affect each other. Channel packing is commonly used by game engines to save memory.
        * `NONE`
          None – Ignore alpha channel from the file and make image fully opaque.

        Type:
        :   enum in [‘STRAIGHT’, ‘PREMUL’, ‘CHANNEL\_PACKED’, ‘NONE’], default ‘STRAIGHT’

    bindcode[#](#bpy.types.Image.bindcode "Link to this definition")
    :   OpenGL bindcode

        Type:
        :   int in [0, inf], default 0, (readonly)

    channels[#](#bpy.types.Image.channels "Link to this definition")
    :   Number of channels in pixels buffer

        Type:
        :   int in [0, inf], default 0, (readonly)

    colorspace\_settings[#](#bpy.types.Image.colorspace_settings "Link to this definition")
    :   Input color space settings

        Type:
        :   [`ColorManagedInputColorspaceSettings`](ColorManagedInputColorspaceSettings.md#bpy.types.ColorManagedInputColorspaceSettings "bpy.types.ColorManagedInputColorspaceSettings"), (readonly)

    depth[#](#bpy.types.Image.depth "Link to this definition")
    :   Image bit depth

        Type:
        :   int in [0, inf], default 0, (readonly)

    display\_aspect[#](#bpy.types.Image.display_aspect "Link to this definition")
    :   Display Aspect for this image, does not affect rendering

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [0.1, inf], default (1.0, 1.0)

    file\_format[#](#bpy.types.Image.file_format "Link to this definition")
    :   Format used for re-saving this file

        Type:
        :   enum in [Image Type Items](../../../appendix/bpy_types_enum_items/image_type_items.md#rna-enum-image-type-items), default ‘TARGA’

    filepath[#](#bpy.types.Image.filepath "Link to this definition")
    :   Image/Movie file name

        Type:
        :   string, default “”, (never None)

    filepath\_raw[#](#bpy.types.Image.filepath_raw "Link to this definition")
    :   Image/Movie file name (without data refreshing)

        Type:
        :   string, default “”, (never None)

    frame\_duration[#](#bpy.types.Image.frame_duration "Link to this definition")
    :   Duration (in frames) of the image (1 when not a video/sequence)

        Type:
        :   int in [0, inf], default 0, (readonly)

    generated\_color[#](#bpy.types.Image.generated_color "Link to this definition")
    :   Fill color for the generated image

        Type:
        :   float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)

    generated\_height[#](#bpy.types.Image.generated_height "Link to this definition")
    :   Generated image height

        Type:
        :   int in [1, 65536], default 1024

    generated\_type[#](#bpy.types.Image.generated_type "Link to this definition")
    :   Generated image type

        Type:
        :   enum in [Image Generated Type Items](../../../appendix/bpy_types_enum_items/image_generated_type_items.md#rna-enum-image-generated-type-items), default ‘UV\_GRID’

    generated\_width[#](#bpy.types.Image.generated_width "Link to this definition")
    :   Generated image width

        Type:
        :   int in [1, 65536], default 1024

    has\_data[#](#bpy.types.Image.has_data "Link to this definition")
    :   True if the image data is loaded into memory

        Type:
        :   boolean, default False, (readonly)

    is\_dirty[#](#bpy.types.Image.is_dirty "Link to this definition")
    :   Image has changed and is not saved

        Type:
        :   boolean, default False, (readonly)

    is\_float[#](#bpy.types.Image.is_float "Link to this definition")
    :   True if this image is stored in floating-point buffer

        Type:
        :   boolean, default False, (readonly)

    is\_multiview[#](#bpy.types.Image.is_multiview "Link to this definition")
    :   Image has more than one view

        Type:
        :   boolean, default False, (readonly)

    is\_stereo\_3d[#](#bpy.types.Image.is_stereo_3d "Link to this definition")
    :   Image has left and right views

        Type:
        :   boolean, default False, (readonly)

    packed\_file[#](#bpy.types.Image.packed_file "Link to this definition")
    :   First packed file of the image

        Type:
        :   [`PackedFile`](PackedFile.md#bpy.types.PackedFile "bpy.types.PackedFile"), (readonly)

    packed\_files[#](#bpy.types.Image.packed_files "Link to this definition")
    :   Collection of packed images

        Type:
        :   [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`ImagePackedFile`](ImagePackedFile.md#bpy.types.ImagePackedFile "bpy.types.ImagePackedFile"), (readonly)

    pixels[#](#bpy.types.Image.pixels "Link to this definition")
    :   Image buffer pixels in floating-point values

        Type:
        :   float in [-inf, inf], default 0.0

    render\_slots[#](#bpy.types.Image.render_slots "Link to this definition")
    :   Render slots of the image

        Type:
        :   [`RenderSlots`](RenderSlots.md#bpy.types.RenderSlots "bpy.types.RenderSlots") [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`RenderSlot`](RenderSlot.md#bpy.types.RenderSlot "bpy.types.RenderSlot"), (readonly)

    resolution[#](#bpy.types.Image.resolution "Link to this definition")
    :   X/Y pixels per meter, for the image buffer

        Type:
        :   [`mathutils.Vector`](../../mathutils/index.md#mathutils.Vector "mathutils.Vector") of 2 items in [-inf, inf], default (0.0, 0.0)

    seam\_margin[#](#bpy.types.Image.seam_margin "Link to this definition")
    :   Margin to take into account when fixing UV seams during painting. Higher number would improve seam-fixes for mipmaps, but decreases performance

        Type:
        :   int in [-32768, 32767], default 8

    size[#](#bpy.types.Image.size "Link to this definition")
    :   Width and height of the image buffer in pixels, zero when image data can’t be loaded

        Type:
        :   int array of 2 items in [-inf, inf], default (0, 0), (readonly)

    source[#](#bpy.types.Image.source "Link to this definition")
    :   Where the image comes from

        * `FILE`
          Single Image – Single image file.
        * `SEQUENCE`
          Image Sequence – Multiple image files, as a sequence.
        * `MOVIE`
          Movie – Movie file.
        * `GENERATED`
          Generated – Generated image.
        * `VIEWER`
          Viewer – Compositing node viewer.
        * `TILED`
          UDIM Tiles – Tiled UDIM image texture.

        Type:
        :   enum in [‘FILE’, ‘SEQUENCE’, ‘MOVIE’, ‘GENERATED’, ‘VIEWER’, ‘TILED’], default ‘FILE’

    stereo\_3d\_format[#](#bpy.types.Image.stereo_3d_format "Link to this definition")
    :   Settings for stereo 3d

        Type:
        :   [`Stereo3dFormat`](Stereo3dFormat.md#bpy.types.Stereo3dFormat "bpy.types.Stereo3dFormat"), (readonly, never None)

    tiles[#](#bpy.types.Image.tiles "Link to this definition")
    :   Tiles of the image

        Type:
        :   [`UDIMTiles`](UDIMTiles.md#bpy.types.UDIMTiles "bpy.types.UDIMTiles") [`bpy_prop_collection`](bpy_prop_collection.md#bpy.types.bpy_prop_collection "bpy.types.bpy_prop_collection") of [`UDIMTile`](UDIMTile.md#bpy.types.UDIMTile "bpy.types.UDIMTile"), (readonly)

    type[#](#bpy.types.Image.type "Link to this definition")
    :   How to generate the image

        Type:
        :   enum in [‘IMAGE’, ‘MULTILAYER’, ‘UV\_TEST’, ‘RENDER\_RESULT’, ‘COMPOSITING’], default ‘IMAGE’, (readonly)

    use\_deinterlace[#](#bpy.types.Image.use_deinterlace "Link to this definition")
    :   Deinterlace movie file on load

        Type:
        :   boolean, default False

    use\_generated\_float[#](#bpy.types.Image.use_generated_float "Link to this definition")
    :   Generate floating-point buffer

        Type:
        :   boolean, default False

    use\_half\_precision[#](#bpy.types.Image.use_half_precision "Link to this definition")
    :   Use 16 bits per channel to lower the memory usage during rendering

        Type:
        :   boolean, default False

    use\_multiview[#](#bpy.types.Image.use_multiview "Link to this definition")
    :   Use Multiple Views (when available)

        Type:
        :   boolean, default False

    use\_view\_as\_render[#](#bpy.types.Image.use_view_as_render "Link to this definition")
    :   Apply render part of display transformation when displaying this image on the screen

        Type:
        :   boolean, default False

    views\_format[#](#bpy.types.Image.views_format "Link to this definition")
    :   Mode to load image views

        Type:
        :   enum in [Views Format Items](../../../appendix/bpy_types_enum_items/views_format_items.md#rna-enum-views-format-items), default ‘INDIVIDUAL’

    save\_render(*filepath*, *scene=None*, *quality=0*)[#](#bpy.types.Image.save_render "Link to this definition")
    :   Save image to a specific path using a scenes render settings

        Parameters:
        :   * **filepath** (*string**,* *(**never None**)*) – Output path
            * **scene** ([`Scene`](Scene.md#bpy.types.Scene "bpy.types.Scene"), (optional)) – Scene to take image parameters from
            * **quality** (*int in* *[**0**,* *100**]**,* *(**optional**)*) – Quality, Quality for image formats that support lossy compression, uses default quality if not specified

    save(*filepath=''*, *quality=0*)[#](#bpy.types.Image.save "Link to this definition")
    :   Save image

        Parameters:
        :   * **filepath** (*string**,* *(**optional**,* *never None**)*) – Output path, uses image data-block filepath if not specified
            * **quality** (*int in* *[**0**,* *100**]**,* *(**optional**)*) – Quality, Quality for image formats that support lossy compression, uses default quality if not specified

    pack(*data=''*, *data\_len=0*)[#](#bpy.types.Image.pack "Link to this definition")
    :   Pack an image as embedded data into the .blend file

        Parameters:
        :   * **data** (*string**,* *(**optional**,* *never None**)*) – data, Raw data (bytes, exact content of the embedded file)
            * **data\_len** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – data\_len, length of given data (mandatory if data is provided)

    unpack(*method='USE\_LOCAL'*)[#](#bpy.types.Image.unpack "Link to this definition")
    :   Save an image packed in the .blend file to disk

        Parameters:
        :   **method** (enum in [Unpack Method Items](../../../appendix/bpy_types_enum_items/unpack_method_items.md#rna-enum-unpack-method-items), (optional)) – method, How to unpack

    reload()[#](#bpy.types.Image.reload "Link to this definition")
    :   Reload the image from its source path

    update()[#](#bpy.types.Image.update "Link to this definition")
    :   Update the display image from the floating-point buffer

    scale(*width*, *height*, *frame=0*, *tile\_index=0*)[#](#bpy.types.Image.scale "Link to this definition")
    :   Scale the buffer of the image, in pixels

        Parameters:
        :   * **width** (*int in* *[**1**,* *inf**]*) – Width
            * **height** (*int in* *[**1**,* *inf**]*) – Height
            * **frame** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Frame, Frame (for image sequences)
            * **tile\_index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Tile, Tile index (for tiled images)

    gl\_touch(*frame=0*, *layer\_index=0*, *pass\_index=0*)[#](#bpy.types.Image.gl_touch "Link to this definition")
    :   Delay the image from being cleaned from the cache due inactivity

        Parameters:
        :   * **frame** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Frame, Frame of image sequence or movie
            * **layer\_index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Layer, Index of layer that should be loaded
            * **pass\_index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Pass, Index of pass that should be loaded

        Returns:
        :   Error, OpenGL error value

        Return type:
        :   int in [-inf, inf]

    gl\_load(*frame=0*, *layer\_index=0*, *pass\_index=0*)[#](#bpy.types.Image.gl_load "Link to this definition")
    :   Load the image into an OpenGL texture. On success, image.bindcode will contain the OpenGL texture bindcode. Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode

        Parameters:
        :   * **frame** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Frame, Frame of image sequence or movie
            * **layer\_index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Layer, Index of layer that should be loaded
            * **pass\_index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Pass, Index of pass that should be loaded

        Returns:
        :   Error, OpenGL error value

        Return type:
        :   int in [-inf, inf]

    gl\_free()[#](#bpy.types.Image.gl_free "Link to this definition")
    :   Free the image from OpenGL graphics memory

    filepath\_from\_user(*image\_user=None*)[#](#bpy.types.Image.filepath_from_user "Link to this definition")
    :   Return the absolute path to the filepath of an image frame specified by the image user

        Parameters:
        :   **image\_user** ([`ImageUser`](ImageUser.md#bpy.types.ImageUser "bpy.types.ImageUser"), (optional)) – Image user of the image to get filepath for

        Returns:
        :   File Path, The resulting filepath from the image and its user

        Return type:
        :   string, (never None)

    buffers\_free()[#](#bpy.types.Image.buffers_free "Link to this definition")
    :   Free the image buffers from memory

    *classmethod* bl\_rna\_get\_subclass(*id*, *default=None*)[#](#bpy.types.Image.bl_rna_get_subclass "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The RNA type or default when not found.

        Return type:
        :   [`bpy.types.Struct`](Struct.md#bpy.types.Struct "bpy.types.Struct") subclass

    *classmethod* bl\_rna\_get\_subclass\_py(*id*, *default=None*)[#](#bpy.types.Image.bl_rna_get_subclass_py "Link to this definition")
    :   Parameters:
        :   **id** (*string*) – The RNA type identifier.

        Returns:
        :   The class or default when not found.

        Return type:
        :   [type](#bpy.types.Image.type "bpy.types.Image.type")

### Inherited Properties[#](#inherited-properties "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.id_data`](bpy_struct.md#bpy.types.bpy_struct.id_data "bpy.types.bpy_struct.id_data") * [`ID.name`](ID.md#bpy.types.ID.name "bpy.types.ID.name") * [`ID.name_full`](ID.md#bpy.types.ID.name_full "bpy.types.ID.name_full") * [`ID.id_type`](ID.md#bpy.types.ID.id_type "bpy.types.ID.id_type") * [`ID.session_uid`](ID.md#bpy.types.ID.session_uid "bpy.types.ID.session_uid") * [`ID.is_evaluated`](ID.md#bpy.types.ID.is_evaluated "bpy.types.ID.is_evaluated") * [`ID.original`](ID.md#bpy.types.ID.original "bpy.types.ID.original") * [`ID.users`](ID.md#bpy.types.ID.users "bpy.types.ID.users") * [`ID.use_fake_user`](ID.md#bpy.types.ID.use_fake_user "bpy.types.ID.use_fake_user") * [`ID.use_extra_user`](ID.md#bpy.types.ID.use_extra_user "bpy.types.ID.use_extra_user") * [`ID.is_embedded_data`](ID.md#bpy.types.ID.is_embedded_data "bpy.types.ID.is_embedded_data") | * [`ID.is_missing`](ID.md#bpy.types.ID.is_missing "bpy.types.ID.is_missing") * [`ID.is_runtime_data`](ID.md#bpy.types.ID.is_runtime_data "bpy.types.ID.is_runtime_data") * [`ID.is_editable`](ID.md#bpy.types.ID.is_editable "bpy.types.ID.is_editable") * [`ID.tag`](ID.md#bpy.types.ID.tag "bpy.types.ID.tag") * [`ID.is_library_indirect`](ID.md#bpy.types.ID.is_library_indirect "bpy.types.ID.is_library_indirect") * [`ID.library`](ID.md#bpy.types.ID.library "bpy.types.ID.library") * [`ID.library_weak_reference`](ID.md#bpy.types.ID.library_weak_reference "bpy.types.ID.library_weak_reference") * [`ID.asset_data`](ID.md#bpy.types.ID.asset_data "bpy.types.ID.asset_data") * [`ID.override_library`](ID.md#bpy.types.ID.override_library "bpy.types.ID.override_library") * [`ID.preview`](ID.md#bpy.types.ID.preview "bpy.types.ID.preview") |

### Inherited Functions[#](#inherited-functions "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy_struct.as_pointer`](bpy_struct.md#bpy.types.bpy_struct.as_pointer "bpy.types.bpy_struct.as_pointer") * [`bpy_struct.driver_add`](bpy_struct.md#bpy.types.bpy_struct.driver_add "bpy.types.bpy_struct.driver_add") * [`bpy_struct.driver_remove`](bpy_struct.md#bpy.types.bpy_struct.driver_remove "bpy.types.bpy_struct.driver_remove") * [`bpy_struct.get`](bpy_struct.md#bpy.types.bpy_struct.get "bpy.types.bpy_struct.get") * [`bpy_struct.id_properties_clear`](bpy_struct.md#bpy.types.bpy_struct.id_properties_clear "bpy.types.bpy_struct.id_properties_clear") * [`bpy_struct.id_properties_ensure`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ensure "bpy.types.bpy_struct.id_properties_ensure") * [`bpy_struct.id_properties_ui`](bpy_struct.md#bpy.types.bpy_struct.id_properties_ui "bpy.types.bpy_struct.id_properties_ui") * [`bpy_struct.is_property_hidden`](bpy_struct.md#bpy.types.bpy_struct.is_property_hidden "bpy.types.bpy_struct.is_property_hidden") * [`bpy_struct.is_property_overridable_library`](bpy_struct.md#bpy.types.bpy_struct.is_property_overridable_library "bpy.types.bpy_struct.is_property_overridable_library") * [`bpy_struct.is_property_readonly`](bpy_struct.md#bpy.types.bpy_struct.is_property_readonly "bpy.types.bpy_struct.is_property_readonly") * [`bpy_struct.is_property_set`](bpy_struct.md#bpy.types.bpy_struct.is_property_set "bpy.types.bpy_struct.is_property_set") * [`bpy_struct.items`](bpy_struct.md#bpy.types.bpy_struct.items "bpy.types.bpy_struct.items") * [`bpy_struct.keyframe_delete`](bpy_struct.md#bpy.types.bpy_struct.keyframe_delete "bpy.types.bpy_struct.keyframe_delete") * [`bpy_struct.keyframe_insert`](bpy_struct.md#bpy.types.bpy_struct.keyframe_insert "bpy.types.bpy_struct.keyframe_insert") * [`bpy_struct.keys`](bpy_struct.md#bpy.types.bpy_struct.keys "bpy.types.bpy_struct.keys") * [`bpy_struct.path_from_id`](bpy_struct.md#bpy.types.bpy_struct.path_from_id "bpy.types.bpy_struct.path_from_id") * [`bpy_struct.path_resolve`](bpy_struct.md#bpy.types.bpy_struct.path_resolve "bpy.types.bpy_struct.path_resolve") * [`bpy_struct.pop`](bpy_struct.md#bpy.types.bpy_struct.pop "bpy.types.bpy_struct.pop") * [`bpy_struct.property_overridable_library_set`](bpy_struct.md#bpy.types.bpy_struct.property_overridable_library_set "bpy.types.bpy_struct.property_overridable_library_set") * [`bpy_struct.property_unset`](bpy_struct.md#bpy.types.bpy_struct.property_unset "bpy.types.bpy_struct.property_unset") | * [`bpy_struct.type_recast`](bpy_struct.md#bpy.types.bpy_struct.type_recast "bpy.types.bpy_struct.type_recast") * [`bpy_struct.values`](bpy_struct.md#bpy.types.bpy_struct.values "bpy.types.bpy_struct.values") * [`ID.evaluated_get`](ID.md#bpy.types.ID.evaluated_get "bpy.types.ID.evaluated_get") * [`ID.copy`](ID.md#bpy.types.ID.copy "bpy.types.ID.copy") * [`ID.asset_mark`](ID.md#bpy.types.ID.asset_mark "bpy.types.ID.asset_mark") * [`ID.asset_clear`](ID.md#bpy.types.ID.asset_clear "bpy.types.ID.asset_clear") * [`ID.asset_generate_preview`](ID.md#bpy.types.ID.asset_generate_preview "bpy.types.ID.asset_generate_preview") * [`ID.override_create`](ID.md#bpy.types.ID.override_create "bpy.types.ID.override_create") * [`ID.override_hierarchy_create`](ID.md#bpy.types.ID.override_hierarchy_create "bpy.types.ID.override_hierarchy_create") * [`ID.user_clear`](ID.md#bpy.types.ID.user_clear "bpy.types.ID.user_clear") * [`ID.user_remap`](ID.md#bpy.types.ID.user_remap "bpy.types.ID.user_remap") * [`ID.make_local`](ID.md#bpy.types.ID.make_local "bpy.types.ID.make_local") * [`ID.user_of_id`](ID.md#bpy.types.ID.user_of_id "bpy.types.ID.user_of_id") * [`ID.animation_data_create`](ID.md#bpy.types.ID.animation_data_create "bpy.types.ID.animation_data_create") * [`ID.animation_data_clear`](ID.md#bpy.types.ID.animation_data_clear "bpy.types.ID.animation_data_clear") * [`ID.update_tag`](ID.md#bpy.types.ID.update_tag "bpy.types.ID.update_tag") * [`ID.preview_ensure`](ID.md#bpy.types.ID.preview_ensure "bpy.types.ID.preview_ensure") * [`ID.bl_rna_get_subclass`](ID.md#bpy.types.ID.bl_rna_get_subclass "bpy.types.ID.bl_rna_get_subclass") * [`ID.bl_rna_get_subclass_py`](ID.md#bpy.types.ID.bl_rna_get_subclass_py "bpy.types.ID.bl_rna_get_subclass_py") |

### References[#](#references "Link to this heading")

|  |  |
| --- | --- |
| * [`bpy.context.edit_image`](../context/index.md#bpy.context.edit_image "bpy.context.edit_image") * [`BlendData.images`](BlendData.md#bpy.types.BlendData.images "bpy.types.BlendData.images") * [`BlendDataImages.load`](BlendDataImages.md#bpy.types.BlendDataImages.load "bpy.types.BlendDataImages.load") * [`BlendDataImages.new`](BlendDataImages.md#bpy.types.BlendDataImages.new "bpy.types.BlendDataImages.new") * [`BlendDataImages.remove`](BlendDataImages.md#bpy.types.BlendDataImages.remove "bpy.types.BlendDataImages.remove") * [`Brush.clone_image`](Brush.md#bpy.types.Brush.clone_image "bpy.types.Brush.clone_image") * [`CameraBackgroundImage.image`](CameraBackgroundImage.md#bpy.types.CameraBackgroundImage.image "bpy.types.CameraBackgroundImage.image") * [`CompositorNodeCryptomatteV2.image`](CompositorNodeCryptomatteV2.md#bpy.types.CompositorNodeCryptomatteV2.image "bpy.types.CompositorNodeCryptomatteV2.image") * [`CompositorNodeImage.image`](CompositorNodeImage.md#bpy.types.CompositorNodeImage.image "bpy.types.CompositorNodeImage.image") * [`GeometryNodeInputImage.image`](GeometryNodeInputImage.md#bpy.types.GeometryNodeInputImage.image "bpy.types.GeometryNodeInputImage.image") * [`ImagePaint.canvas`](ImagePaint.md#bpy.types.ImagePaint.canvas "bpy.types.ImagePaint.canvas") * [`ImagePaint.clone_image`](ImagePaint.md#bpy.types.ImagePaint.clone_image "bpy.types.ImagePaint.clone_image") * [`ImagePaint.stencil_image`](ImagePaint.md#bpy.types.ImagePaint.stencil_image "bpy.types.ImagePaint.stencil_image") | * [`ImageTexture.image`](ImageTexture.md#bpy.types.ImageTexture.image "bpy.types.ImageTexture.image") * [`Material.texture_paint_images`](Material.md#bpy.types.Material.texture_paint_images "bpy.types.Material.texture_paint_images") * [`MaterialGPencilStyle.fill_image`](MaterialGPencilStyle.md#bpy.types.MaterialGPencilStyle.fill_image "bpy.types.MaterialGPencilStyle.fill_image") * [`MaterialGPencilStyle.stroke_image`](MaterialGPencilStyle.md#bpy.types.MaterialGPencilStyle.stroke_image "bpy.types.MaterialGPencilStyle.stroke_image") * [`MovieTrackingPlaneTrack.image`](MovieTrackingPlaneTrack.md#bpy.types.MovieTrackingPlaneTrack.image "bpy.types.MovieTrackingPlaneTrack.image") * [`NodeSocketImage.default_value`](NodeSocketImage.md#bpy.types.NodeSocketImage.default_value "bpy.types.NodeSocketImage.default_value") * [`NodeTreeInterfaceSocketImage.default_value`](NodeTreeInterfaceSocketImage.md#bpy.types.NodeTreeInterfaceSocketImage.default_value "bpy.types.NodeTreeInterfaceSocketImage.default_value") * [`PaintModeSettings.canvas_image`](PaintModeSettings.md#bpy.types.PaintModeSettings.canvas_image "bpy.types.PaintModeSettings.canvas_image") * [`ShaderNodeTexEnvironment.image`](ShaderNodeTexEnvironment.md#bpy.types.ShaderNodeTexEnvironment.image "bpy.types.ShaderNodeTexEnvironment.image") * [`ShaderNodeTexImage.image`](ShaderNodeTexImage.md#bpy.types.ShaderNodeTexImage.image "bpy.types.ShaderNodeTexImage.image") * [`SpaceImageEditor.image`](SpaceImageEditor.md#bpy.types.SpaceImageEditor.image "bpy.types.SpaceImageEditor.image") * [`TextureNodeImage.image`](TextureNodeImage.md#bpy.types.TextureNodeImage.image "bpy.types.TextureNodeImage.image") * [`UILayout.template_image_layers`](UILayout.md#bpy.types.UILayout.template_image_layers "bpy.types.UILayout.template_image_layers") |

[Next

ImageFormatSettings(bpy\_struct)](ImageFormatSettings.md)
[Previous

IO\_FH\_gltf2(FileHandler)](IO_FH_gltf2.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.types.Image.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.types.Image.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Image(ID)
  + [Image Data](#image-data)
    - [`Image`](#bpy.types.Image)
      * [`Image.alpha_mode`](#bpy.types.Image.alpha_mode)
      * [`Image.bindcode`](#bpy.types.Image.bindcode)
      * [`Image.channels`](#bpy.types.Image.channels)
      * [`Image.colorspace_settings`](#bpy.types.Image.colorspace_settings)
      * [`Image.depth`](#bpy.types.Image.depth)
      * [`Image.display_aspect`](#bpy.types.Image.display_aspect)
      * [`Image.file_format`](#bpy.types.Image.file_format)
      * [`Image.filepath`](#bpy.types.Image.filepath)
      * [`Image.filepath_raw`](#bpy.types.Image.filepath_raw)
      * [`Image.frame_duration`](#bpy.types.Image.frame_duration)
      * [`Image.generated_color`](#bpy.types.Image.generated_color)
      * [`Image.generated_height`](#bpy.types.Image.generated_height)
      * [`Image.generated_type`](#bpy.types.Image.generated_type)
      * [`Image.generated_width`](#bpy.types.Image.generated_width)
      * [`Image.has_data`](#bpy.types.Image.has_data)
      * [`Image.is_dirty`](#bpy.types.Image.is_dirty)
      * [`Image.is_float`](#bpy.types.Image.is_float)
      * [`Image.is_multiview`](#bpy.types.Image.is_multiview)
      * [`Image.is_stereo_3d`](#bpy.types.Image.is_stereo_3d)
      * [`Image.packed_file`](#bpy.types.Image.packed_file)
      * [`Image.packed_files`](#bpy.types.Image.packed_files)
      * [`Image.pixels`](#bpy.types.Image.pixels)
      * [`Image.render_slots`](#bpy.types.Image.render_slots)
      * [`Image.resolution`](#bpy.types.Image.resolution)
      * [`Image.seam_margin`](#bpy.types.Image.seam_margin)
      * [`Image.size`](#bpy.types.Image.size)
      * [`Image.source`](#bpy.types.Image.source)
      * [`Image.stereo_3d_format`](#bpy.types.Image.stereo_3d_format)
      * [`Image.tiles`](#bpy.types.Image.tiles)
      * [`Image.type`](#bpy.types.Image.type)
      * [`Image.use_deinterlace`](#bpy.types.Image.use_deinterlace)
      * [`Image.use_generated_float`](#bpy.types.Image.use_generated_float)
      * [`Image.use_half_precision`](#bpy.types.Image.use_half_precision)
      * [`Image.use_multiview`](#bpy.types.Image.use_multiview)
      * [`Image.use_view_as_render`](#bpy.types.Image.use_view_as_render)
      * [`Image.views_format`](#bpy.types.Image.views_format)
      * [`Image.save_render()`](#bpy.types.Image.save_render)
      * [`Image.save()`](#bpy.types.Image.save)
      * [`Image.pack()`](#bpy.types.Image.pack)
      * [`Image.unpack()`](#bpy.types.Image.unpack)
      * [`Image.reload()`](#bpy.types.Image.reload)
      * [`Image.update()`](#bpy.types.Image.update)
      * [`Image.scale()`](#bpy.types.Image.scale)
      * [`Image.gl_touch()`](#bpy.types.Image.gl_touch)
      * [`Image.gl_load()`](#bpy.types.Image.gl_load)
      * [`Image.gl_free()`](#bpy.types.Image.gl_free)
      * [`Image.filepath_from_user()`](#bpy.types.Image.filepath_from_user)
      * [`Image.buffers_free()`](#bpy.types.Image.buffers_free)
      * [`Image.bl_rna_get_subclass()`](#bpy.types.Image.bl_rna_get_subclass)
      * [`Image.bl_rna_get_subclass_py()`](#bpy.types.Image.bl_rna_get_subclass_py)
    - [Inherited Properties](#inherited-properties)
    - [Inherited Functions](#inherited-functions)
    - [References](#references)