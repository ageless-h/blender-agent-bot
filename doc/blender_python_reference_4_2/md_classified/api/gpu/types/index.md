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

* [Context Access (bpy.context)](../../bpy/context/index.md)
* [Data Access (bpy.data)](../../bpy/data/index.md)
* [Message Bus (bpy.msgbus)](../../bpy/msgbus/index.md)
* [Operators (bpy.ops)](../../bpy/ops/index.md)[ ]
* [Types (bpy.types)](../../bpy/types/index.md)[ ]
* [Utilities (bpy.utils)](../../bpy/utils/index.md)[ ]
* [Path Utilities (bpy.path)](../../bpy/path/index.md)
* [Application Data (bpy.app)](../../bpy/app/index.md)[ ]

  Toggle navigation of Application Data (bpy.app)

  + [Application Handlers (bpy.app.handlers)](../../bpy/app/handlers.md)
  + [Application Translations (bpy.app.translations)](../../bpy/app/translations.md)
  + [Application Icons (bpy.app.icons)](../../bpy/app/icons.md)
  + [Application Timers (bpy.app.timers)](../../bpy/app/timers.md)
* [Property Definitions (bpy.props)](../../bpy/props/index.md)

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
* [GPU Module (gpu)](../../../meta/index.md)[x]

  Toggle navigation of GPU Module (gpu)

  + GPU Types (gpu.types)
  + [GPU Matrix Utilities (gpu.matrix)](../matrix/index.md)
  + [GPU Select Utilities (gpu.select)](../select/index.md)
  + [GPU Shader Utilities (gpu.shader)](../shader/index.md)
  + [GPU State Utilities (gpu.state)](../state/index.md)
  + [GPU Texture Utilities (gpu.texture)](../texture/index.md)
  + [GPU Platform Utilities (gpu.platform)](../platform/index.md)
  + [GPU Capabilities Utilities (gpu.capabilities)](../capabilities/index.md)
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

# GPU Types (gpu.types)[#](#module-gpu.types "Link to this heading")

*class* gpu.types.Buffer(*format*, *dimensions*, *data*)[#](#gpu.types.Buffer "Link to this definition")
:   For Python access to GPU functions requiring a pointer.

    Parameters:
    :   * **format** (*str*) – Format type to interpret the buffer.
          Possible values are FLOAT, INT, UINT, UBYTE, UINT\_24\_8 and 10\_11\_11\_REV.
        * **dimensions** (*int*) – Array describing the dimensions.
        * **data** (*sequence*) – Optional data array.

    return the buffer as a list

    dimensions[#](#gpu.types.Buffer.dimensions "Link to this definition")
    :   Undocumented, consider [contributing](https://developer.blender.org/).

*class* gpu.types.GPUBatch(*type*, *buf*, *elem=None*)[#](#gpu.types.GPUBatch "Link to this definition")
:   Reusable container for drawable geometry.

    Parameters:
    :   * **type** (*str*) – The primitive type of geometry to be drawn.
          Possible values are POINTS, LINES, TRIS, LINE\_STRIP, LINE\_LOOP, TRI\_STRIP, TRI\_FAN, LINES\_ADJ, TRIS\_ADJ and LINE\_STRIP\_ADJ.
        * **buf** ([`gpu.types.GPUVertBuf`](#gpu.types.GPUVertBuf "gpu.types.GPUVertBuf")) – Vertex buffer containing all or some of the attributes required for drawing.
        * **elem** ([`gpu.types.GPUIndexBuf`](#gpu.types.GPUIndexBuf "gpu.types.GPUIndexBuf")) – An optional index buffer.

    draw(*program=None*)[#](#gpu.types.GPUBatch.draw "Link to this definition")
    :   Run the drawing program with the parameters assigned to the batch.

        Parameters:
        :   **program** ([`gpu.types.GPUShader`](#gpu.types.GPUShader "gpu.types.GPUShader")) – Program that performs the drawing operations.
            If `None` is passed, the last program set to this batch will run.

    draw\_instanced(*program*, *\**, *instance\_start=0*, *instance\_count=0*)[#](#gpu.types.GPUBatch.draw_instanced "Link to this definition")
    :   Draw multiple instances of the drawing program with the parameters assigned
        to the batch. In the vertex shader, gl\_InstanceID will contain the instance
        number being drawn.

        Parameters:
        :   * **program** ([`gpu.types.GPUShader`](#gpu.types.GPUShader "gpu.types.GPUShader")) – Program that performs the drawing operations.
            * **instance\_start** (*int*) – Number of the first instance to draw.
            * **instance\_count** (*int*) – Number of instances to draw. When not provided or set to 0
              the number of instances will be determined by the number of rows in the first
              vertex buffer.

    draw\_range(*program*, *\**, *elem\_start=0*, *elem\_count=0*)[#](#gpu.types.GPUBatch.draw_range "Link to this definition")
    :   Run the drawing program with the parameters assigned to the batch. Only draw
        the elem\_count elements of the index buffer starting at elem\_start

        Parameters:
        :   * **program** ([`gpu.types.GPUShader`](#gpu.types.GPUShader "gpu.types.GPUShader")) – Program that performs the drawing operations.
            * **elem\_start** (*int*) – First index to draw. When not provided or set to 0 drawing
              will start from the first element of the index buffer.
            * **elem\_count** (*int*) – Number of elements of the index buffer to draw. When not
              provided or set to 0 all elements from elem\_start to the end of the
              index buffer will be drawn.

    program\_set(*program*)[#](#gpu.types.GPUBatch.program_set "Link to this definition")
    :   Assign a shader to this batch that will be used for drawing when not overwritten later.
        Note: This method has to be called in the draw context that the batch will be drawn in.
        This function does not need to be called when you always
        set the shader when calling [`gpu.types.GPUBatch.draw()`](#gpu.types.GPUBatch.draw "gpu.types.GPUBatch.draw").

        Parameters:
        :   **program** ([`gpu.types.GPUShader`](#gpu.types.GPUShader "gpu.types.GPUShader")) – The program/shader the batch will use in future draw calls.

    vertbuf\_add(*buf*)[#](#gpu.types.GPUBatch.vertbuf_add "Link to this definition")
    :   Add another vertex buffer to the Batch.
        It is not possible to add more vertices to the batch using this method.
        Instead it can be used to add more attributes to the existing vertices.
        A good use case would be when you have a separate
        vertex buffer for vertex positions and vertex normals.
        Current a batch can have at most 16 vertex buffers.

        Parameters:
        :   **buf** ([`gpu.types.GPUVertBuf`](#gpu.types.GPUVertBuf "gpu.types.GPUVertBuf")) – The vertex buffer that will be added to the batch.

*class* gpu.types.GPUFrameBuffer(*depth\_slot=None*, *color\_slots=None*)[#](#gpu.types.GPUFrameBuffer "Link to this definition")
:   This object gives access to framebuffer functionalities.
    When a ‘layer’ is specified in a argument, a single layer of a 3D or array texture is attached to the frame-buffer.
    For cube map textures, layer is translated into a cube map face.

    Parameters:
    :   * **depth\_slot** ([`gpu.types.GPUTexture`](#gpu.types.GPUTexture "gpu.types.GPUTexture"), dict or Nonetype) – GPUTexture to attach or a dict containing keywords: ‘texture’, ‘layer’ and ‘mip’.
        * **color\_slots** (*tuple* *or* *Nonetype*) – Tuple where each item can be a GPUTexture or a dict containing keywords: ‘texture’, ‘layer’ and ‘mip’.

    bind()[#](#gpu.types.GPUFrameBuffer.bind "Link to this definition")
    :   Context manager to ensure balanced bind calls, even in the case of an error.

    clear(*color=None*, *depth=None*, *stencil=None*)[#](#gpu.types.GPUFrameBuffer.clear "Link to this definition")
    :   Fill color, depth and stencil textures with specific value.
        Common values: color=(0.0, 0.0, 0.0, 1.0), depth=1.0, stencil=0.

        Parameters:
        :   * **color** (*sequence* *of* *3* *or* *4 floats*) – float sequence each representing `(r, g, b, a)`.
            * **depth** (*float*) – depth value.
            * **stencil** (*int*) – stencil value.

    read\_color(*x*, *y*, *xsize*, *ysize*, *channels*, *slot*, *format*, *data=data*)[#](#gpu.types.GPUFrameBuffer.read_color "Link to this definition")
    :   Read a block of pixels from the frame buffer.

        Parameters:
        :   * **y** (*x**,*) – Lower left corner of a rectangular block of pixels.
            * **ysize** (*xsize**,*) – Dimensions of the pixel rectangle.
            * **channels** (*int*) – Number of components to read.
            * **slot** (*int*) – The framebuffer slot to read data from.
            * **format** (*str*) – The format that describes the content of a single channel.
              Possible values are FLOAT, INT, UINT, UBYTE, UINT\_24\_8 and 10\_11\_11\_REV.
            * **data** ([`gpu.types.Buffer`](#gpu.types.Buffer "gpu.types.Buffer")) – Optional Buffer object to fill with the pixels values.

        Returns:
        :   The Buffer with the read pixels.

        Return type:
        :   [`gpu.types.Buffer`](#gpu.types.Buffer "gpu.types.Buffer")

    read\_depth(*x*, *y*, *xsize*, *ysize*, *data=data*)[#](#gpu.types.GPUFrameBuffer.read_depth "Link to this definition")
    :   Read a pixel depth block from the frame buffer.

        Parameters:
        :   * **y** (*x**,*) – Lower left corner of a rectangular block of pixels.
            * **ysize** (*xsize**,*) – Dimensions of the pixel rectangle.
            * **data** ([`gpu.types.Buffer`](#gpu.types.Buffer "gpu.types.Buffer")) – Optional Buffer object to fill with the pixels values.

        Returns:
        :   The Buffer with the read pixels.

        Return type:
        :   [`gpu.types.Buffer`](#gpu.types.Buffer "gpu.types.Buffer")

    viewport\_get()[#](#gpu.types.GPUFrameBuffer.viewport_get "Link to this definition")
    :   Returns position and dimension to current viewport.

    viewport\_set(*x*, *y*, *xsize*, *ysize*)[#](#gpu.types.GPUFrameBuffer.viewport_set "Link to this definition")
    :   Set the viewport for this framebuffer object.
        Note: The viewport state is not saved upon framebuffer rebind.

        Parameters:
        :   * **y** (*x**,*) – lower left corner of the viewport\_set rectangle, in pixels.
            * **ysize** (*xsize**,*) – width and height of the viewport\_set.

    is\_bound[#](#gpu.types.GPUFrameBuffer.is_bound "Link to this definition")
    :   Checks if this is the active framebuffer in the context.

*class* gpu.types.GPUIndexBuf(*type*, *seq*)[#](#gpu.types.GPUIndexBuf "Link to this definition")
:   Contains an index buffer.

    Parameters:
    :   * **type** (*str*) – The primitive type this index buffer is composed of.
          Possible values are POINTS, LINES, TRIS and LINE\_STRIP\_ADJ.
        * **seq** (*1D* *or* *2D sequence*) – Indices this index buffer will contain.
          Whether a 1D or 2D sequence is required depends on the type.
          Optionally the sequence can support the buffer protocol.

*class* gpu.types.GPUOffScreen(*width*, *height*, *\**, *format='RGBA8'*)[#](#gpu.types.GPUOffScreen "Link to this definition")
:   This object gives access to off screen buffers.

    Parameters:
    :   * **width** (*int*) – Horizontal dimension of the buffer.
        * **height** (*int*) – Vertical dimension of the buffer.
        * **format** (*str*) – Internal data format inside GPU memory for color attachment texture. Possible values are:
          RGBA8,
          RGBA16,
          RGBA16F,
          RGBA32F,

    bind()[#](#gpu.types.GPUOffScreen.bind "Link to this definition")
    :   Context manager to ensure balanced bind calls, even in the case of an error.

    draw\_view3d(*scene*, *view\_layer*, *view3d*, *region*, *view\_matrix*, *projection\_matrix*, *do\_color\_management=False*, *draw\_background=True*)[#](#gpu.types.GPUOffScreen.draw_view3d "Link to this definition")
    :   Draw the 3d viewport in the offscreen object.

        Parameters:
        :   * **scene** ([`bpy.types.Scene`](../../bpy/types/Scene.md#bpy.types.Scene "bpy.types.Scene")) – Scene to draw.
            * **view\_layer** ([`bpy.types.ViewLayer`](../../bpy/types/ViewLayer.md#bpy.types.ViewLayer "bpy.types.ViewLayer")) – View layer to draw.
            * **view3d** ([`bpy.types.SpaceView3D`](../../bpy/types/SpaceView3D.md#bpy.types.SpaceView3D "bpy.types.SpaceView3D")) – 3D View to get the drawing settings from.
            * **region** ([`bpy.types.Region`](../../bpy/types/Region.md#bpy.types.Region "bpy.types.Region")) – Region of the 3D View (required as temporary draw target).
            * **view\_matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – View Matrix (e.g. `camera.matrix_world.inverted()`).
            * **projection\_matrix** ([`mathutils.Matrix`](../../mathutils/index.md#mathutils.Matrix "mathutils.Matrix")) – Projection Matrix (e.g. `camera.calc_matrix_camera(...)`).
            * **do\_color\_management** (*bool*) – Color manage the output.
            * **draw\_background** (*bool*) – Draw background.

    free()[#](#gpu.types.GPUOffScreen.free "Link to this definition")
    :   Free the offscreen object.
        The framebuffer, texture and render objects will no longer be accessible.

    unbind(*restore=True*)[#](#gpu.types.GPUOffScreen.unbind "Link to this definition")
    :   Unbind the offscreen object.

        Parameters:
        :   **restore** (*bool*) – Restore the OpenGL state, can only be used when the state has been saved before.

    color\_texture[#](#gpu.types.GPUOffScreen.color_texture "Link to this definition")
    :   OpenGL bindcode for the color texture.

        Type:
        :   int

    height[#](#gpu.types.GPUOffScreen.height "Link to this definition")
    :   Height of the texture.

        Type:
        :   int

    texture\_color[#](#gpu.types.GPUOffScreen.texture_color "Link to this definition")
    :   The color texture attached.

        Type:
        :   [`gpu.types.GPUTexture`](#gpu.types.GPUTexture "gpu.types.GPUTexture")

    width[#](#gpu.types.GPUOffScreen.width "Link to this definition")
    :   Width of the texture.

        Type:
        :   int

*class* gpu.types.GPUShader(*vertexcode*, *fragcode*, *geocode=None*, *libcode=None*, *defines=None*, *name='pyGPUShader'*)[#](#gpu.types.GPUShader "Link to this definition")
:   GPUShader combines multiple GLSL shaders into a program used for drawing.
    It must contain at least a vertex and fragment shaders.

    The GLSL `#version` directive is automatically included at the top of shaders,
    and set to 330. Some preprocessor directives are automatically added according to
    the Operating System or availability: `GPU_ATI`, `GPU_NVIDIA` and `GPU_INTEL`.

    The following extensions are enabled by default if supported by the GPU:
    `GL_ARB_texture_gather`, `GL_ARB_texture_cube_map_array`
    and `GL_ARB_shader_draw_parameters`.

    For drawing user interface elements and gizmos, use
    `fragOutput = blender_srgb_to_framebuffer_space(fragOutput)`
    to transform the output sRGB colors to the frame-buffer color-space.

    Parameters:
    :   * **vertexcode** (*str*) – Vertex shader code.
        * **fragcode** – Fragment shader code.
        * **geocode** – Geometry shader code.
        * **libcode** – Code with functions and presets to be shared between shaders.
        * **defines** – Preprocessor directives.
        * **name** – Name of shader code, for debugging purposes.

    attr\_from\_name(*name*)[#](#gpu.types.GPUShader.attr_from_name "Link to this definition")
    :   Get attribute location by name.

        Parameters:
        :   **name** (*str*) – The name of the attribute variable whose location is to be queried.

        Returns:
        :   The location of an attribute variable.

        Return type:
        :   int

    attrs\_info\_get()[#](#gpu.types.GPUShader.attrs_info_get "Link to this definition")
    :   Information about the attributes used in the Shader.

        Returns:
        :   tuples containing information about the attributes in order (name, type)

        Return type:
        :   tuple

    bind()[#](#gpu.types.GPUShader.bind "Link to this definition")
    :   Bind the shader object. Required to be able to change uniforms of this shader.

    format\_calc()[#](#gpu.types.GPUShader.format_calc "Link to this definition")
    :   Build a new format based on the attributes of the shader.

        Returns:
        :   vertex attribute format for the shader

        Return type:
        :   [`gpu.types.GPUVertFormat`](#gpu.types.GPUVertFormat "gpu.types.GPUVertFormat")

    image(*name*, *texture*)[#](#gpu.types.GPUShader.image "Link to this definition")
    :   Specify the value of an image variable for the current GPUShader.

        Parameters:
        :   * **name** (*str*) – Name of the image variable to which the texture is to be bound.
            * **texture** ([`gpu.types.GPUTexture`](#gpu.types.GPUTexture "gpu.types.GPUTexture")) – Texture to attach.

    uniform\_block(*name*, *ubo*)[#](#gpu.types.GPUShader.uniform_block "Link to this definition")
    :   Specify the value of an uniform buffer object variable for the current GPUShader.

        Parameters:
        :   * **name** (*str*) – name of the uniform variable whose UBO is to be specified.
            * **ubo** – Uniform Buffer to attach.

    uniform\_block\_from\_name(*name*)[#](#gpu.types.GPUShader.uniform_block_from_name "Link to this definition")
    :   Get uniform block location by name.

        Parameters:
        :   **name** (*str*) – Name of the uniform block variable whose location is to be queried.

        Returns:
        :   The location of the uniform block variable.

        Return type:
        :   int

    uniform\_bool(*name*, *value*)[#](#gpu.types.GPUShader.uniform_bool "Link to this definition")
    :   Specify the value of a uniform variable for the current program object.

        Parameters:
        :   * **name** (*str*) – Name of the uniform variable whose value is to be changed.
            * **value** (*bool* *or* *sequence* *of* *bools*) – Value that will be used to update the specified uniform variable.

    uniform\_float(*name*, *value*)[#](#gpu.types.GPUShader.uniform_float "Link to this definition")
    :   Specify the value of a uniform variable for the current program object.

        Parameters:
        :   * **name** (*str*) – Name of the uniform variable whose value is to be changed.
            * **value** (*single number* *or* *sequence* *of* *numbers*) – Value that will be used to update the specified uniform variable.

    uniform\_from\_name(*name*)[#](#gpu.types.GPUShader.uniform_from_name "Link to this definition")
    :   Get uniform location by name.

        Parameters:
        :   **name** (*str*) – Name of the uniform variable whose location is to be queried.

        Returns:
        :   Location of the uniform variable.

        Return type:
        :   int

    uniform\_int(*name*, *seq*)[#](#gpu.types.GPUShader.uniform_int "Link to this definition")
    :   Specify the value of a uniform variable for the current program object.

        Parameters:
        :   * **name** (*str*) – name of the uniform variable whose value is to be changed.
            * **seq** (*sequence* *of* *numbers*) – Value that will be used to update the specified uniform variable.

    uniform\_sampler(*name*, *texture*)[#](#gpu.types.GPUShader.uniform_sampler "Link to this definition")
    :   Specify the value of a texture uniform variable for the current GPUShader.

        Parameters:
        :   * **name** (*str*) – name of the uniform variable whose texture is to be specified.
            * **texture** ([`gpu.types.GPUTexture`](#gpu.types.GPUTexture "gpu.types.GPUTexture")) – Texture to attach.

    uniform\_vector\_float(*location*, *buffer*, *length*, *count*)[#](#gpu.types.GPUShader.uniform_vector_float "Link to this definition")
    :   Set the buffer to fill the uniform.

        Parameters:
        :   * **location** (*int*) – Location of the uniform variable to be modified.
            * **buffer** (*sequence* *of* *floats*) – The data that should be set. Can support the buffer protocol.
            * **length** (*int*) –

              Size of the uniform data type:

              + 1: float
              + 2: vec2 or float[2]
              + 3: vec3 or float[3]
              + 4: vec4 or float[4]
              + 9: mat3
              + 16: mat4
            * **count** (*int*) – Specifies the number of elements, vector or matrices that are to be modified.

    uniform\_vector\_int(*location*, *buffer*, *length*, *count*)[#](#gpu.types.GPUShader.uniform_vector_int "Link to this definition")
    :   See GPUShader.uniform\_vector\_float(…) description.

    name[#](#gpu.types.GPUShader.name "Link to this definition")
    :   The name of the shader object for debugging purposes (read-only).

        Type:
        :   str

    program[#](#gpu.types.GPUShader.program "Link to this definition")
    :   The name of the program object for use by the OpenGL API (read-only).

        Type:
        :   int

*class* gpu.types.GPUShaderCreateInfo[#](#gpu.types.GPUShaderCreateInfo "Link to this definition")
:   Stores and describes types and variables that are used in shader sources.

    compute\_source(*source*)[#](#gpu.types.GPUShaderCreateInfo.compute_source "Link to this definition")
    :   compute shader source code written in GLSL.

        Example:

        ```
        """void main() {
           int2 index = int2(gl_GlobalInvocationID.xy);
           vec4 color = vec4(0.0, 0.0, 0.0, 1.0);
           imageStore(img_output, index, color);
        }"""
        ```

        Parameters:
        :   **source** (*str*) – The compute shader source code.

        See also

        [GLSL Cross Compilation](https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/)

    define(*name*, *value*)[#](#gpu.types.GPUShaderCreateInfo.define "Link to this definition")
    :   Add a preprocessing define directive. In GLSL it would be something like:

    ```
    #define name value

    :arg name: Token name.
    :type name: str
    :arg value: Text that replaces token occurrences.
    :type value: str
    ```

    fragment\_out(*slot*, *type*, *name*, *blend='NONE'*)[#](#gpu.types.GPUShaderCreateInfo.fragment_out "Link to this definition")
    :   Specify a fragment output corresponding to a framebuffer target slot.

        Parameters:
        :   * **slot** (*int*) – The attribute index.
            * **type** (*str*) –

              One of these types:

              + `FLOAT`
              + `VEC2`
              + `VEC3`
              + `VEC4`
              + `MAT3`
              + `MAT4`
              + `UINT`
              + `UVEC2`
              + `UVEC3`
              + `UVEC4`
              + `INT`
              + `IVEC2`
              + `IVEC3`
              + `IVEC4`
              + `BOOL`
            * **name** (*str*) – Name of the attribute.
            * **blend** (*str*) – Dual Source Blending Index. It can be ‘NONE’, ‘SRC\_0’ or ‘SRC\_1’.

    fragment\_source(*source*)[#](#gpu.types.GPUShaderCreateInfo.fragment_source "Link to this definition")
    :   Fragment shader source code written in GLSL.

        Example:

        ```
        "void main {fragColor = vec4(0.0, 0.0, 0.0, 1.0);}"
        ```

        Parameters:
        :   **source** (*str*) – The fragment shader source code.

        See also

        [GLSL Cross Compilation](https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/)

    image(*slot*, *format*, *type*, *name*, *qualifiers={'NO\_RESTRICT'}*)[#](#gpu.types.GPUShaderCreateInfo.image "Link to this definition")
    :   Specify an image resource used for arbitrary load and store operations.

        Parameters:
        :   * **slot** (*int*) – The image resource index.
            * **format** (*str*) –

              The GPUTexture format that is passed to the shader. Possible values are:

              + `RGBA8UI`
              + `RGBA8I`
              + `RGBA8`
              + `RGBA32UI`
              + `RGBA32I`
              + `RGBA32F`
              + `RGBA16UI`
              + `RGBA16I`
              + `RGBA16F`
              + `RGBA16`
              + `RG8UI`
              + `RG8I`
              + `RG8`
              + `RG32UI`
              + `RG32I`
              + `RG32F`
              + `RG16UI`
              + `RG16I`
              + `RG16F`
              + `RG16`
              + `R8UI`
              + `R8I`
              + `R8`
              + `R32UI`
              + `R32I`
              + `R32F`
              + `R16UI`
              + `R16I`
              + `R16F`
              + `R16`
              + `R11F_G11F_B10F`
              + `DEPTH32F_STENCIL8`
              + `DEPTH24_STENCIL8`
              + `SRGB8_A8`
              + `RGB16F`
              + `SRGB8_A8_DXT1`
              + `SRGB8_A8_DXT3`
              + `SRGB8_A8_DXT5`
              + `RGBA8_DXT1`
              + `RGBA8_DXT3`
              + `RGBA8_DXT5`
              + `DEPTH_COMPONENT32F`
              + `DEPTH_COMPONENT24`
              + `DEPTH_COMPONENT16`
            * **type** (*str*) –

              The data type describing how the image is to be read in the shader. Possible values are:

              + `FLOAT_BUFFER`
              + `FLOAT_1D`
              + `FLOAT_1D_ARRAY`
              + `FLOAT_2D`
              + `FLOAT_2D_ARRAY`
              + `FLOAT_3D`
              + `FLOAT_CUBE`
              + `FLOAT_CUBE_ARRAY`
              + `INT_BUFFER`
              + `INT_1D`
              + `INT_1D_ARRAY`
              + `INT_2D`
              + `INT_2D_ARRAY`
              + `INT_3D`
              + `INT_CUBE`
              + `INT_CUBE_ARRAY`
              + `UINT_BUFFER`
              + `UINT_1D`
              + `UINT_1D_ARRAY`
              + `UINT_2D`
              + `UINT_2D_ARRAY`
              + `UINT_3D`
              + `UINT_CUBE`
              + `UINT_CUBE_ARRAY`
              + `SHADOW_2D`
              + `SHADOW_2D_ARRAY`
              + `SHADOW_CUBE`
              + `SHADOW_CUBE_ARRAY`
              + `DEPTH_2D`
              + `DEPTH_2D_ARRAY`
              + `DEPTH_CUBE`
              + `DEPTH_CUBE_ARRAY`
            * **name** (*str*) – The image resource name.
            * **qualifiers** (*set*) – Set containing values that describe how the image resource is to be read or written. Possible values are:
              - `NO_RESTRICT`
              - `READ`
              - `WRITE`

    local\_group\_size(*x*, *y=1*, *z=1*)[#](#gpu.types.GPUShaderCreateInfo.local_group_size "Link to this definition")
    :   Specify the local group size for compute shaders.

        Parameters:
        :   * **x** (*int*) – The local group size in the x dimension.
            * **y** (*int*) – The local group size in the y dimension. Optional. Defaults to 1.
            * **z** (*int*) – The local group size in the z dimension. Optional. Defaults to 1.

    push\_constant(*type*, *name*, *size=0*)[#](#gpu.types.GPUShaderCreateInfo.push_constant "Link to this definition")
    :   Specify a global access constant.

        Parameters:
        :   * **type** (*str*) –

              One of these types:

              + `FLOAT`
              + `VEC2`
              + `VEC3`
              + `VEC4`
              + `MAT3`
              + `MAT4`
              + `UINT`
              + `UVEC2`
              + `UVEC3`
              + `UVEC4`
              + `INT`
              + `IVEC2`
              + `IVEC3`
              + `IVEC4`
              + `BOOL`
            * **name** (*str*) – Name of the constant.
            * **size** (*uint*) – If not zero, indicates that the constant is an array with the specified size.

    sampler(*slot*, *type*, *name*)[#](#gpu.types.GPUShaderCreateInfo.sampler "Link to this definition")
    :   Specify an image texture sampler.

        Parameters:
        :   * **slot** (*int*) – The image texture sampler index.
            * **type** (*str*) –

              The data type describing the format of each sampler unit. Possible values are:

              + `FLOAT_BUFFER`
              + `FLOAT_1D`
              + `FLOAT_1D_ARRAY`
              + `FLOAT_2D`
              + `FLOAT_2D_ARRAY`
              + `FLOAT_3D`
              + `FLOAT_CUBE`
              + `FLOAT_CUBE_ARRAY`
              + `INT_BUFFER`
              + `INT_1D`
              + `INT_1D_ARRAY`
              + `INT_2D`
              + `INT_2D_ARRAY`
              + `INT_3D`
              + `INT_CUBE`
              + `INT_CUBE_ARRAY`
              + `UINT_BUFFER`
              + `UINT_1D`
              + `UINT_1D_ARRAY`
              + `UINT_2D`
              + `UINT_2D_ARRAY`
              + `UINT_3D`
              + `UINT_CUBE`
              + `UINT_CUBE_ARRAY`
              + `SHADOW_2D`
              + `SHADOW_2D_ARRAY`
              + `SHADOW_CUBE`
              + `SHADOW_CUBE_ARRAY`
              + `DEPTH_2D`
              + `DEPTH_2D_ARRAY`
              + `DEPTH_CUBE`
              + `DEPTH_CUBE_ARRAY`
            * **name** (*str*) – The image texture sampler name.

    typedef\_source(*source*)[#](#gpu.types.GPUShaderCreateInfo.typedef_source "Link to this definition")
    :   Source code included before resource declaration. Useful for defining structs used by Uniform Buffers.

        Example:

    ```
    "struct MyType {int foo; float bar;};"

    :arg source: The source code defining types.
    :type source: str
    ```

    uniform\_buf(*slot*, *type\_name*, *name*)[#](#gpu.types.GPUShaderCreateInfo.uniform_buf "Link to this definition")
    :   Specify a uniform variable whose type can be one of those declared in typedef\_source.

        Parameters:
        :   * **slot** (*int*) – The uniform variable index.
            * **type\_name** (*str*) – Name of the data type. It can be a struct type defined in the source passed through the [`gpu.types.GPUShaderCreateInfo.typedef_source()`](#gpu.types.GPUShaderCreateInfo.typedef_source "gpu.types.GPUShaderCreateInfo.typedef_source").
            * **name** (*str*) – The uniform variable name.

    vertex\_in(*slot*, *type*, *name*)[#](#gpu.types.GPUShaderCreateInfo.vertex_in "Link to this definition")
    :   Add a vertex shader input attribute.

        Parameters:
        :   * **slot** (*int*) – The attribute index.
            * **type** (*str*) –

              One of these types:

              + `FLOAT`
              + `VEC2`
              + `VEC3`
              + `VEC4`
              + `MAT3`
              + `MAT4`
              + `UINT`
              + `UVEC2`
              + `UVEC3`
              + `UVEC4`
              + `INT`
              + `IVEC2`
              + `IVEC3`
              + `IVEC4`
              + `BOOL`
            * **name** (*str*) – name of the attribute.

    vertex\_out(*interface*)[#](#gpu.types.GPUShaderCreateInfo.vertex_out "Link to this definition")
    :   Add a vertex shader output interface block.

        Parameters:
        :   **interface** ([`gpu.types.GPUStageInterfaceInfo`](#gpu.types.GPUStageInterfaceInfo "gpu.types.GPUStageInterfaceInfo")) – Object describing the block.

    vertex\_source(*source*)[#](#gpu.types.GPUShaderCreateInfo.vertex_source "Link to this definition")
    :   Vertex shader source code written in GLSL.

        Example:

        ```
        "void main {gl_Position = vec4(pos, 1.0);}"
        ```

        Parameters:
        :   **source** (*str*) – The vertex shader source code.

        See also

        [GLSL Cross Compilation](https://developer.blender.org/docs/features/gpu/glsl_cross_compilation/)

*class* gpu.types.GPUStageInterfaceInfo(*name*)[#](#gpu.types.GPUStageInterfaceInfo "Link to this definition")
:   List of varyings between shader stages.

    Parameters:
    :   **name** – Name of the interface block.

    flat(*type*, *name*)[#](#gpu.types.GPUStageInterfaceInfo.flat "Link to this definition")
    :   Add an attribute with qualifier of type flat to the interface block.

        Parameters:
        :   * **type** (*str*) –

              One of these types:

              + `FLOAT`
              + `VEC2`
              + `VEC3`
              + `VEC4`
              + `MAT3`
              + `MAT4`
              + `UINT`
              + `UVEC2`
              + `UVEC3`
              + `UVEC4`
              + `INT`
              + `IVEC2`
              + `IVEC3`
              + `IVEC4`
              + `BOOL`
            * **name** (*str*) – name of the attribute.

    no\_perspective(*type*, *name*)[#](#gpu.types.GPUStageInterfaceInfo.no_perspective "Link to this definition")
    :   Add an attribute with qualifier of type no\_perspective to the interface block.

        Parameters:
        :   * **type** (*str*) –

              One of these types:

              + `FLOAT`
              + `VEC2`
              + `VEC3`
              + `VEC4`
              + `MAT3`
              + `MAT4`
              + `UINT`
              + `UVEC2`
              + `UVEC3`
              + `UVEC4`
              + `INT`
              + `IVEC2`
              + `IVEC3`
              + `IVEC4`
              + `BOOL`
            * **name** (*str*) – name of the attribute.

    smooth(*type*, *name*)[#](#gpu.types.GPUStageInterfaceInfo.smooth "Link to this definition")
    :   Add an attribute with qualifier of type smooth to the interface block.

        Parameters:
        :   * **type** (*str*) –

              One of these types:

              + `FLOAT`
              + `VEC2`
              + `VEC3`
              + `VEC4`
              + `MAT3`
              + `MAT4`
              + `UINT`
              + `UVEC2`
              + `UVEC3`
              + `UVEC4`
              + `INT`
              + `IVEC2`
              + `IVEC3`
              + `IVEC4`
              + `BOOL`
            * **name** (*str*) – name of the attribute.

    name[#](#gpu.types.GPUStageInterfaceInfo.name "Link to this definition")
    :   Name of the interface block.

        Type:
        :   str

*class* gpu.types.GPUTexture(*size*, *layers=0*, *is\_cubemap=False*, *format='RGBA8'*, *data=None*)[#](#gpu.types.GPUTexture "Link to this definition")
:   This object gives access to off GPU textures.

    Parameters:
    :   * **size** (*tuple* *or* *int*) – Dimensions of the texture 1D, 2D, 3D or cubemap.
        * **layers** (*int*) – Number of layers in texture array or number of cubemaps in cubemap array
        * **is\_cubemap** (*int*) – Indicates the creation of a cubemap texture.
        * **format** (*str*) – Internal data format inside GPU memory. Possible values are:
          RGBA8UI,
          RGBA8I,
          RGBA8,
          RGBA32UI,
          RGBA32I,
          RGBA32F,
          RGBA16UI,
          RGBA16I,
          RGBA16F,
          RGBA16,
          RG8UI,
          RG8I,
          RG8,
          RG32UI,
          RG32I,
          RG32F,
          RG16UI,
          RG16I,
          RG16F,
          RG16,
          R8UI,
          R8I,
          R8,
          R32UI,
          R32I,
          R32F,
          R16UI,
          R16I,
          R16F,
          R16,
          R11F\_G11F\_B10F,
          DEPTH32F\_STENCIL8,
          DEPTH24\_STENCIL8,
          SRGB8\_A8,
          RGB16F,
          SRGB8\_A8\_DXT1,
          SRGB8\_A8\_DXT3,
          SRGB8\_A8\_DXT5,
          RGBA8\_DXT1,
          RGBA8\_DXT3,
          RGBA8\_DXT5,
          DEPTH\_COMPONENT32F,
          DEPTH\_COMPONENT24,
          DEPTH\_COMPONENT16,
        * **data** ([`gpu.types.Buffer`](#gpu.types.Buffer "gpu.types.Buffer")) – Buffer object to fill the texture.

    clear(*format='FLOAT'*, *value=(0.0, 0.0, 0.0, 1.0)*)[#](#gpu.types.GPUTexture.clear "Link to this definition")
    :   Fill texture with specific value.

        Parameters:
        :   * **format** (*str*) – The format that describes the content of a single item.
              Possible values are FLOAT, INT, UINT, UBYTE, UINT\_24\_8 and 10\_11\_11\_REV.
            * **value** (*sequence* *of* *1**,* *2**,* *3* *or* *4 values*) – sequence each representing the value to fill.

    read()[#](#gpu.types.GPUTexture.read "Link to this definition")
    :   Creates a buffer with the value of all pixels.

    format[#](#gpu.types.GPUTexture.format "Link to this definition")
    :   Format of the texture.

        Type:
        :   str

    height[#](#gpu.types.GPUTexture.height "Link to this definition")
    :   Height of the texture.

        Type:
        :   int

    width[#](#gpu.types.GPUTexture.width "Link to this definition")
    :   Width of the texture.

        Type:
        :   int

*class* gpu.types.GPUUniformBuf(*data*)[#](#gpu.types.GPUUniformBuf "Link to this definition")
:   This object gives access to off uniform buffers.

    Parameters:
    :   **data** (*object exposing buffer interface*) – Data to fill the buffer.

    update(*data*)[#](#gpu.types.GPUUniformBuf.update "Link to this definition")
    :   Update the data of the uniform buffer object.

*class* gpu.types.GPUVertBuf(*format*, *len*)[#](#gpu.types.GPUVertBuf "Link to this definition")
:   Contains a VBO.

    Parameters:
    :   * **format** ([`gpu.types.GPUVertFormat`](#gpu.types.GPUVertFormat "gpu.types.GPUVertFormat")) – Vertex format.
        * **len** (*int*) – Amount of vertices that will fit into this buffer.

    attr\_fill(*id*, *data*)[#](#gpu.types.GPUVertBuf.attr_fill "Link to this definition")
    :   Insert data into the buffer for a single attribute.

        Parameters:
        :   * **id** (*int* *or* *str*) – Either the name or the id of the attribute.
            * **data** (*sequence* *of* *floats**,* *ints**,* *vectors* *or* *matrices*) – Sequence of data that should be stored in the buffer

*class* gpu.types.GPUVertFormat[#](#gpu.types.GPUVertFormat "Link to this definition")
:   This object contains information about the structure of a vertex buffer.

    attr\_add(*id*, *comp\_type*, *len*, *fetch\_mode*)[#](#gpu.types.GPUVertFormat.attr_add "Link to this definition")
    :   Add a new attribute to the format.

        Parameters:
        :   * **id** (*str*) – Name the attribute. Often position, normal, …
            * **comp\_type** (*str*) – The data type that will be used store the value in memory.
              Possible values are I8, U8, I16, U16, I32, U32, F32 and I10.
            * **len** (*int*) – How many individual values the attribute consists of
              (e.g. 2 for uv coordinates).
            * **fetch\_mode** (*str*) – How values from memory will be converted when used in the shader.
              This is mainly useful for memory optimizations when you want to store values with
              reduced precision. E.g. you can store a float in only 1 byte but it will be
              converted to a normal 4 byte float when used.
              Possible values are FLOAT, INT, INT\_TO\_FLOAT\_UNIT and INT\_TO\_FLOAT.

[Next

GPU Matrix Utilities (gpu.matrix)](../matrix/index.md)
[Previous

GPU Module (gpu)](../../../meta/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60gpu.types.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fgpu.types.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* GPU Types (gpu.types)
  + [`Buffer`](#gpu.types.Buffer)
    - [`Buffer.dimensions`](#gpu.types.Buffer.dimensions)
  + [`GPUBatch`](#gpu.types.GPUBatch)
    - [`GPUBatch.draw()`](#gpu.types.GPUBatch.draw)
    - [`GPUBatch.draw_instanced()`](#gpu.types.GPUBatch.draw_instanced)
    - [`GPUBatch.draw_range()`](#gpu.types.GPUBatch.draw_range)
    - [`GPUBatch.program_set()`](#gpu.types.GPUBatch.program_set)
    - [`GPUBatch.vertbuf_add()`](#gpu.types.GPUBatch.vertbuf_add)
  + [`GPUFrameBuffer`](#gpu.types.GPUFrameBuffer)
    - [`GPUFrameBuffer.bind()`](#gpu.types.GPUFrameBuffer.bind)
    - [`GPUFrameBuffer.clear()`](#gpu.types.GPUFrameBuffer.clear)
    - [`GPUFrameBuffer.read_color()`](#gpu.types.GPUFrameBuffer.read_color)
    - [`GPUFrameBuffer.read_depth()`](#gpu.types.GPUFrameBuffer.read_depth)
    - [`GPUFrameBuffer.viewport_get()`](#gpu.types.GPUFrameBuffer.viewport_get)
    - [`GPUFrameBuffer.viewport_set()`](#gpu.types.GPUFrameBuffer.viewport_set)
    - [`GPUFrameBuffer.is_bound`](#gpu.types.GPUFrameBuffer.is_bound)
  + [`GPUIndexBuf`](#gpu.types.GPUIndexBuf)
  + [`GPUOffScreen`](#gpu.types.GPUOffScreen)
    - [`GPUOffScreen.bind()`](#gpu.types.GPUOffScreen.bind)
    - [`GPUOffScreen.draw_view3d()`](#gpu.types.GPUOffScreen.draw_view3d)
    - [`GPUOffScreen.free()`](#gpu.types.GPUOffScreen.free)
    - [`GPUOffScreen.unbind()`](#gpu.types.GPUOffScreen.unbind)
    - [`GPUOffScreen.color_texture`](#gpu.types.GPUOffScreen.color_texture)
    - [`GPUOffScreen.height`](#gpu.types.GPUOffScreen.height)
    - [`GPUOffScreen.texture_color`](#gpu.types.GPUOffScreen.texture_color)
    - [`GPUOffScreen.width`](#gpu.types.GPUOffScreen.width)
  + [`GPUShader`](#gpu.types.GPUShader)
    - [`GPUShader.attr_from_name()`](#gpu.types.GPUShader.attr_from_name)
    - [`GPUShader.attrs_info_get()`](#gpu.types.GPUShader.attrs_info_get)
    - [`GPUShader.bind()`](#gpu.types.GPUShader.bind)
    - [`GPUShader.format_calc()`](#gpu.types.GPUShader.format_calc)
    - [`GPUShader.image()`](#gpu.types.GPUShader.image)
    - [`GPUShader.uniform_block()`](#gpu.types.GPUShader.uniform_block)
    - [`GPUShader.uniform_block_from_name()`](#gpu.types.GPUShader.uniform_block_from_name)
    - [`GPUShader.uniform_bool()`](#gpu.types.GPUShader.uniform_bool)
    - [`GPUShader.uniform_float()`](#gpu.types.GPUShader.uniform_float)
    - [`GPUShader.uniform_from_name()`](#gpu.types.GPUShader.uniform_from_name)
    - [`GPUShader.uniform_int()`](#gpu.types.GPUShader.uniform_int)
    - [`GPUShader.uniform_sampler()`](#gpu.types.GPUShader.uniform_sampler)
    - [`GPUShader.uniform_vector_float()`](#gpu.types.GPUShader.uniform_vector_float)
    - [`GPUShader.uniform_vector_int()`](#gpu.types.GPUShader.uniform_vector_int)
    - [`GPUShader.name`](#gpu.types.GPUShader.name)
    - [`GPUShader.program`](#gpu.types.GPUShader.program)
  + [`GPUShaderCreateInfo`](#gpu.types.GPUShaderCreateInfo)
    - [`GPUShaderCreateInfo.compute_source()`](#gpu.types.GPUShaderCreateInfo.compute_source)
    - [`GPUShaderCreateInfo.define()`](#gpu.types.GPUShaderCreateInfo.define)
    - [`GPUShaderCreateInfo.fragment_out()`](#gpu.types.GPUShaderCreateInfo.fragment_out)
    - [`GPUShaderCreateInfo.fragment_source()`](#gpu.types.GPUShaderCreateInfo.fragment_source)
    - [`GPUShaderCreateInfo.image()`](#gpu.types.GPUShaderCreateInfo.image)
    - [`GPUShaderCreateInfo.local_group_size()`](#gpu.types.GPUShaderCreateInfo.local_group_size)
    - [`GPUShaderCreateInfo.push_constant()`](#gpu.types.GPUShaderCreateInfo.push_constant)
    - [`GPUShaderCreateInfo.sampler()`](#gpu.types.GPUShaderCreateInfo.sampler)
    - [`GPUShaderCreateInfo.typedef_source()`](#gpu.types.GPUShaderCreateInfo.typedef_source)
    - [`GPUShaderCreateInfo.uniform_buf()`](#gpu.types.GPUShaderCreateInfo.uniform_buf)
    - [`GPUShaderCreateInfo.vertex_in()`](#gpu.types.GPUShaderCreateInfo.vertex_in)
    - [`GPUShaderCreateInfo.vertex_out()`](#gpu.types.GPUShaderCreateInfo.vertex_out)
    - [`GPUShaderCreateInfo.vertex_source()`](#gpu.types.GPUShaderCreateInfo.vertex_source)
  + [`GPUStageInterfaceInfo`](#gpu.types.GPUStageInterfaceInfo)
    - [`GPUStageInterfaceInfo.flat()`](#gpu.types.GPUStageInterfaceInfo.flat)
    - [`GPUStageInterfaceInfo.no_perspective()`](#gpu.types.GPUStageInterfaceInfo.no_perspective)
    - [`GPUStageInterfaceInfo.smooth()`](#gpu.types.GPUStageInterfaceInfo.smooth)
    - [`GPUStageInterfaceInfo.name`](#gpu.types.GPUStageInterfaceInfo.name)
  + [`GPUTexture`](#gpu.types.GPUTexture)
    - [`GPUTexture.clear()`](#gpu.types.GPUTexture.clear)
    - [`GPUTexture.read()`](#gpu.types.GPUTexture.read)
    - [`GPUTexture.format`](#gpu.types.GPUTexture.format)
    - [`GPUTexture.height`](#gpu.types.GPUTexture.height)
    - [`GPUTexture.width`](#gpu.types.GPUTexture.width)
  + [`GPUUniformBuf`](#gpu.types.GPUUniformBuf)
    - [`GPUUniformBuf.update()`](#gpu.types.GPUUniformBuf.update)
  + [`GPUVertBuf`](#gpu.types.GPUVertBuf)
    - [`GPUVertBuf.attr_fill()`](#gpu.types.GPUVertBuf.attr_fill)
  + [`GPUVertFormat`](#gpu.types.GPUVertFormat)
    - [`GPUVertFormat.attr_add()`](#gpu.types.GPUVertFormat.attr_add)