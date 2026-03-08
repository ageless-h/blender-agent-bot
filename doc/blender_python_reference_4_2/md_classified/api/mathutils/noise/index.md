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
* [Math Types & Utilities (mathutils)](../../../meta/index.md)[x]

  Toggle navigation of Math Types & Utilities (mathutils)

  + [Geometry Utilities (mathutils.geometry)](../geometry/index.md)
  + [BVHTree Utilities (mathutils.bvhtree)](../bvhtree/index.md)
  + [KDTree Utilities (mathutils.kdtree)](../kdtree/index.md)
  + [Interpolation Utilities (mathutils.interpolate)](../interpolate/index.md)
  + Noise Utilities (mathutils.noise)

* 4.2

  Versions

  + Loading...

Note

You are not using the most up to date version of the documentation.
 is the newest version.

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Noise Utilities (mathutils.noise)[#](#module-mathutils.noise "Link to this heading")

The Blender noise module

mathutils.noise.cell(*position*)[#](#mathutils.noise.cell "Link to this definition")
:   Returns cell noise value at the specified position.

    Parameters:
    :   **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.

    Returns:
    :   The cell noise value.

    Return type:
    :   float

mathutils.noise.cell\_vector(*position*)[#](#mathutils.noise.cell_vector "Link to this definition")
:   Returns cell noise vector at the specified position.

    Parameters:
    :   **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.

    Returns:
    :   The cell noise vector.

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.noise.fractal(*position*, *H*, *lacunarity*, *octaves*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.fractal "Link to this definition")
:   Returns the fractal Brownian motion (fBm) noise value from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **H** (*float*) – The fractal increment factor.
        * **lacunarity** (*float*) – The gap between successive frequencies.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The fractal Brownian motion noise value.

    Return type:
    :   float

mathutils.noise.hetero\_terrain(*position*, *H*, *lacunarity*, *octaves*, *offset*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.hetero_terrain "Link to this definition")
:   Returns the heterogeneous terrain value from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **H** (*float*) – The fractal dimension of the roughest areas.
        * **lacunarity** (*float*) – The gap between successive frequencies.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **offset** (*float*) – The height of the terrain above ‘sea level’.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The heterogeneous terrain value.

    Return type:
    :   float

mathutils.noise.hybrid\_multi\_fractal(*position*, *H*, *lacunarity*, *octaves*, *offset*, *gain*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.hybrid_multi_fractal "Link to this definition")
:   Returns hybrid multifractal value from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **H** (*float*) – The fractal dimension of the roughest areas.
        * **lacunarity** (*float*) – The gap between successive frequencies.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **offset** (*float*) – The height of the terrain above ‘sea level’.
        * **gain** (*float*) – Scaling applied to the values.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The hybrid multifractal value.

    Return type:
    :   float

mathutils.noise.multi\_fractal(*position*, *H*, *lacunarity*, *octaves*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.multi_fractal "Link to this definition")
:   Returns multifractal noise value from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **H** (*float*) – The fractal increment factor.
        * **lacunarity** (*float*) – The gap between successive frequencies.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The multifractal noise value.

    Return type:
    :   float

mathutils.noise.noise(*position*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.noise "Link to this definition")
:   Returns noise value from the noise basis at the position specified.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The noise value.

    Return type:
    :   float

mathutils.noise.noise\_vector(*position*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.noise_vector "Link to this definition")
:   Returns the noise vector from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The noise vector.

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.noise.random()[#](#mathutils.noise.random "Link to this definition")
:   Returns a random number in the range [0, 1).

    Returns:
    :   The random number.

    Return type:
    :   float

mathutils.noise.random\_unit\_vector(*size=3*)[#](#mathutils.noise.random_unit_vector "Link to this definition")
:   Returns a unit vector with random entries.

    Parameters:
    :   **size** (*int*) – The size of the vector to be produced, in the range [2, 4].

    Returns:
    :   The random unit vector.

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.noise.random\_vector(*size=3*)[#](#mathutils.noise.random_vector "Link to this definition")
:   Returns a vector with random entries in the range (-1, 1).

    Parameters:
    :   **size** (*int*) – The size of the vector to be produced.

    Returns:
    :   The random vector.

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.noise.ridged\_multi\_fractal(*position*, *H*, *lacunarity*, *octaves*, *offset*, *gain*, *noise\_basis='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.ridged_multi_fractal "Link to this definition")
:   Returns ridged multifractal value from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **H** (*float*) – The fractal dimension of the roughest areas.
        * **lacunarity** (*float*) – The gap between successive frequencies.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **offset** (*float*) – The height of the terrain above ‘sea level’.
        * **gain** (*float*) – Scaling applied to the values.
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The ridged multifractal value.

    Return type:
    :   float

mathutils.noise.seed\_set(*seed*)[#](#mathutils.noise.seed_set "Link to this definition")
:   Sets the random seed used for random\_unit\_vector, and random.

    Parameters:
    :   **seed** (*int*) – Seed used for the random generator.
        When seed is zero, the current time will be used instead.

mathutils.noise.turbulence(*position*, *octaves*, *hard*, *noise\_basis='PERLIN\_ORIGINAL'*, *amplitude\_scale=0.5*, *frequency\_scale=2.0*)[#](#mathutils.noise.turbulence "Link to this definition")
:   Returns the turbulence value from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **hard** (*boolean*) – Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].
        * **amplitude\_scale** (*float*) – The amplitude scaling factor.
        * **frequency\_scale** (*float*) – The frequency scaling factor

    Returns:
    :   The turbulence value.

    Return type:
    :   float

mathutils.noise.turbulence\_vector(*position*, *octaves*, *hard*, *noise\_basis='PERLIN\_ORIGINAL'*, *amplitude\_scale=0.5*, *frequency\_scale=2.0*)[#](#mathutils.noise.turbulence_vector "Link to this definition")
:   Returns the turbulence vector from the noise basis at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **octaves** (*int*) – The number of different noise frequencies used.
        * **hard** (*boolean*) – Specifies whether returned turbulence is hard (sharp transitions) or soft (smooth transitions).
        * **noise\_basis** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].
        * **amplitude\_scale** (*float*) – The amplitude scaling factor.
        * **frequency\_scale** (*float*) – The frequency scaling factor

    Returns:
    :   The turbulence vector.

    Return type:
    :   [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")

mathutils.noise.variable\_lacunarity(*position*, *distortion*, *noise\_type1='PERLIN\_ORIGINAL'*, *noise\_type2='PERLIN\_ORIGINAL'*)[#](#mathutils.noise.variable_lacunarity "Link to this definition")
:   Returns variable lacunarity noise value, a distorted variety of noise, from noise type 1 distorted by noise type 2 at the specified position.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **distortion** (*float*) – The amount of distortion.
        * **noise\_type1** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].
        * **noise\_type2** (*string*) – Enumerator in [‘BLENDER’, ‘PERLIN\_ORIGINAL’, ‘PERLIN\_NEW’, ‘VORONOI\_F1’, ‘VORONOI\_F2’, ‘VORONOI\_F3’, ‘VORONOI\_F4’, ‘VORONOI\_F2F1’, ‘VORONOI\_CRACKLE’, ‘CELLNOISE’].

    Returns:
    :   The variable lacunarity noise value.

    Return type:
    :   float

mathutils.noise.voronoi(*position*, *distance\_metric='DISTANCE'*, *exponent=2.5*)[#](#mathutils.noise.voronoi "Link to this definition")
:   Returns a list of distances to the four closest features and their locations.

    Parameters:
    :   * **position** ([`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector")) – The position to evaluate the selected noise function.
        * **distance\_metric** (*string*) – Enumerator in [‘DISTANCE’, ‘DISTANCE\_SQUARED’, ‘MANHATTAN’, ‘CHEBYCHEV’, ‘MINKOVSKY’, ‘MINKOVSKY\_HALF’, ‘MINKOVSKY\_FOUR’].
        * **exponent** (*float*) – The exponent for Minkowski distance metric.

    Returns:
    :   A list of distances to the four closest features and their locations.

    Return type:
    :   list of four floats, list of four [`mathutils.Vector`](../index.md#mathutils.Vector "mathutils.Vector") types

[Previous

Interpolation Utilities (mathutils.interpolate)](../interpolate/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60mathutils.noise.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fmathutils.noise.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Noise Utilities (mathutils.noise)
  + [`cell()`](#mathutils.noise.cell)
  + [`cell_vector()`](#mathutils.noise.cell_vector)
  + [`fractal()`](#mathutils.noise.fractal)
  + [`hetero_terrain()`](#mathutils.noise.hetero_terrain)
  + [`hybrid_multi_fractal()`](#mathutils.noise.hybrid_multi_fractal)
  + [`multi_fractal()`](#mathutils.noise.multi_fractal)
  + [`noise()`](#mathutils.noise.noise)
  + [`noise_vector()`](#mathutils.noise.noise_vector)
  + [`random()`](#mathutils.noise.random)
  + [`random_unit_vector()`](#mathutils.noise.random_unit_vector)
  + [`random_vector()`](#mathutils.noise.random_vector)
  + [`ridged_multi_fractal()`](#mathutils.noise.ridged_multi_fractal)
  + [`seed_set()`](#mathutils.noise.seed_set)
  + [`turbulence()`](#mathutils.noise.turbulence)
  + [`turbulence_vector()`](#mathutils.noise.turbulence_vector)
  + [`variable_lacunarity()`](#mathutils.noise.variable_lacunarity)
  + [`voronoi()`](#mathutils.noise.voronoi)