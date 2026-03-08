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
* [Utilities (bpy.utils)](index.md)[x]
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

# bpy.utils submodule (bpy.utils.previews)[#](#module-bpy.utils.previews "Link to this heading")

This module contains utility functions to handle custom previews.

It behaves as a high-level ‘cached’ previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
(‘icon\_value’ for UILayout functions).

## Custom Icon Example[#](#custom-icon-example "Link to this heading")

```
# This sample script demonstrates how to place a custom icon on a button or
# menu entry.
#
# IMPORTANT NOTE: if you run this sample, there will be no icon in the button
# You need to replace the image path with a real existing one.
# For distributable scripts, it is recommended to place the icons inside the
# addon folder and access it relative to the py script file for portability
#
#
# Other use cases for UI-previews:
# - provide a fixed list of previews to select from
# - provide a dynamic list of preview (eg. calculated from reading a directory)
#
# For the above use cases, see the template 'ui_previews_dynamic_enum.py"

import os
import bpy

class PreviewsExamplePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Previews Example Panel"
    bl_idname = "OBJECT_PT_previews"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        pcoll = preview_collections["main"]

        row = layout.row()
        my_icon = pcoll["my_icon"]
        row.operator("render.render", icon_value=my_icon.icon_id)

        # my_icon.icon_id can be used in any UI function that accepts
        # icon_value # try also setting text=""
        # to get an icon only operator button

# We can store multiple preview collections here,
# however in this example we only store "main"
preview_collections = {}

def register():

    # Note that preview collections returned by bpy.utils.previews
    # are regular py objects - you can use them to store custom data.
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # path to the folder where the icon is
    # the path is calculated relative to this py file inside the addon folder
    my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("my_icon", os.path.join(my_icons_dir, "icon-image.png"), 'IMAGE')

    preview_collections["main"] = pcoll

    bpy.utils.register_class(PreviewsExamplePanel)

def unregister():

    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

    bpy.utils.unregister_class(PreviewsExamplePanel)

if __name__ == "__main__":
    register()
```

bpy.utils.previews.new()[#](#bpy.utils.previews.new "Link to this definition")
:   Returns:
    :   a new preview collection.

    Return type:
    :   [`ImagePreviewCollection`](#bpy.utils.previews.ImagePreviewCollection "bpy.utils.previews.ImagePreviewCollection")

bpy.utils.previews.remove(*pcoll*)[#](#bpy.utils.previews.remove "Link to this definition")
:   Remove the specified previews collection.

    Parameters:
    :   **pcoll** ([`ImagePreviewCollection`](#bpy.utils.previews.ImagePreviewCollection "bpy.utils.previews.ImagePreviewCollection")) – Preview collection to close.

*class* bpy.utils.previews.ImagePreviewCollection[#](#bpy.utils.previews.ImagePreviewCollection "Link to this definition")
:   Dictionary-like class of previews.

    This is a subclass of Python’s built-in dict type,
    used to store multiple image previews.

    Note

    * instance with [`bpy.utils.previews.new`](#bpy.utils.previews.new "bpy.utils.previews.new")
    * keys must be `str` type.
    * values will be [`bpy.types.ImagePreview`](../types/ImagePreview.md#bpy.types.ImagePreview "bpy.types.ImagePreview")

    clear()[#](#bpy.utils.previews.ImagePreviewCollection.clear "Link to this definition")
    :   Clear all previews.

    close()[#](#bpy.utils.previews.ImagePreviewCollection.close "Link to this definition")
    :   Close the collection and clear all previews.

    load(*name*, *filepath*, *filetype*, *force\_reload=False*)[#](#bpy.utils.previews.ImagePreviewCollection.load "Link to this definition")
    :   Generate a new preview from given file path.

        Parameters:
        :   * **name** (*string*) – The name (unique id) identifying the preview.
            * **filepath** (*string* *or* *bytes*) – The file path to generate the preview from.
            * **filetype** (*string*) – The type of file, needed to generate the preview in [‘IMAGE’, ‘MOVIE’, ‘BLEND’, ‘FONT’].
            * **force\_reload** (*bool*) – If True, force running thumbnail manager even if preview already exists in cache.

        Returns:
        :   The Preview matching given name, or a new empty one.

        Return type:
        :   [`bpy.types.ImagePreview`](../types/ImagePreview.md#bpy.types.ImagePreview "bpy.types.ImagePreview")

        Raises:
        :   **KeyError** – if `name` already exists.

    new(*name*)[#](#bpy.utils.previews.ImagePreviewCollection.new "Link to this definition")
    :   Generate a new empty preview.

        Parameters:
        :   **name** (*string*) – The name (unique id) identifying the preview.

        Returns:
        :   The Preview matching given name, or a new empty one.

        Return type:
        :   [`bpy.types.ImagePreview`](../types/ImagePreview.md#bpy.types.ImagePreview "bpy.types.ImagePreview")

        Raises:
        :   **KeyError** – if `name` already exists.

[Next

bpy.utils submodule (bpy.utils.units)](units.md)
[Previous

Utilities (bpy.utils)](index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.utils.previews.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.utils.previews.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* bpy.utils submodule (bpy.utils.previews)
  + [Custom Icon Example](#custom-icon-example)
    - [`new()`](#bpy.utils.previews.new)
    - [`remove()`](#bpy.utils.previews.remove)
    - [`ImagePreviewCollection`](#bpy.utils.previews.ImagePreviewCollection)
      * [`ImagePreviewCollection.clear()`](#bpy.utils.previews.ImagePreviewCollection.clear)
      * [`ImagePreviewCollection.close()`](#bpy.utils.previews.ImagePreviewCollection.close)
      * [`ImagePreviewCollection.load()`](#bpy.utils.previews.ImagePreviewCollection.load)
      * [`ImagePreviewCollection.new()`](#bpy.utils.previews.ImagePreviewCollection.new)