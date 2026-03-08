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
* [Path Utilities (bpy.path)](../path/index.md)
* [Application Data (bpy.app)](index.md)[x]

  Toggle navigation of Application Data (bpy.app)

  + [Application Handlers (bpy.app.handlers)](handlers.md)
  + [Application Translations (bpy.app.translations)](translations.md)
  + [Application Icons (bpy.app.icons)](icons.md)
  + Application Timers (bpy.app.timers)
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

# Application Timers (bpy.app.timers)[#](#module-bpy.app.timers "Link to this heading")

## Run a Function in x Seconds[#](#run-a-function-in-x-seconds "Link to this heading")

```
import bpy

def in_5_seconds():
    print("Hello World")

bpy.app.timers.register(in_5_seconds, first_interval=5)
```

## Run a Function every x Seconds[#](#run-a-function-every-x-seconds "Link to this heading")

```
import bpy

def every_2_seconds():
    print("Hello World")
    return 2.0

bpy.app.timers.register(every_2_seconds)
```

## Run a Function n times every x seconds[#](#run-a-function-n-times-every-x-seconds "Link to this heading")

```
import bpy

counter = 0

def run_10_times():
    global counter
    counter += 1
    print(counter)
    if counter == 10:
        return None
    return 0.1

bpy.app.timers.register(run_10_times)
```

## Assign parameters to functions[#](#assign-parameters-to-functions "Link to this heading")

```
import bpy
import functools

def print_message(message):
    print("Message:", message)

bpy.app.timers.register(functools.partial(print_message, "Hello"), first_interval=2.0)
bpy.app.timers.register(functools.partial(print_message, "World"), first_interval=3.0)
```

## Use a Timer to react to events in another thread[#](#use-a-timer-to-react-to-events-in-another-thread "Link to this heading")

You should never modify Blender data at arbitrary points in time in separate threads.
However you can use a queue to collect all the actions that should be executed when Blender is in the right state again.
Pythons queue.Queue can be used here, because it implements the required locking semantics.

```
import bpy
import queue

execution_queue = queue.Queue()

# This function can safely be called in another thread.
# The function will be executed when the timer runs the next time.
def run_in_main_thread(function):
    execution_queue.put(function)

def execute_queued_functions():
    while not execution_queue.empty():
        function = execution_queue.get()
        function()
    return 1.0

bpy.app.timers.register(execute_queued_functions)
```

bpy.app.timers.is\_registered(*function*)[#](#bpy.app.timers.is_registered "Link to this definition")
:   Check if this function is registered as a timer.

    Parameters:
    :   **function** (*int*) – Function to check.

    Returns:
    :   True when this function is registered, otherwise False.

    Return type:
    :   bool

bpy.app.timers.register(*function*, *first\_interval=0*, *persistent=False*)[#](#bpy.app.timers.register "Link to this definition")
:   Add a new function that will be called after the specified amount of seconds.
    The function gets no arguments and is expected to return either None or a float.
    If `None` is returned, the timer will be unregistered.
    A returned number specifies the delay until the function is called again.
    `functools.partial` can be used to assign some parameters.

    Parameters:
    :   * **function** (*Callable**[**[**]**,* *Union**[**float**,* *None**]**]*) – The function that should called.
        * **first\_interval** (*float*) – Seconds until the callback should be called the first time.
        * **persistent** (*bool*) – Don’t remove timer when a new file is loaded.

bpy.app.timers.unregister(*function*)[#](#bpy.app.timers.unregister "Link to this definition")
:   Unregister timer.

    Parameters:
    :   **function** (*function*) – Function to unregister.

[Next

Property Definitions (bpy.props)](../props/index.md)
[Previous

Application Icons (bpy.app.icons)](icons.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.app.timers.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.app.timers.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Application Timers (bpy.app.timers)
  + [Run a Function in x Seconds](#run-a-function-in-x-seconds)
  + [Run a Function every x Seconds](#run-a-function-every-x-seconds)
  + [Run a Function n times every x seconds](#run-a-function-n-times-every-x-seconds)
  + [Assign parameters to functions](#assign-parameters-to-functions)
  + [Use a Timer to react to events in another thread](#use-a-timer-to-react-to-events-in-another-thread)
    - [`is_registered()`](#bpy.app.timers.is_registered)
    - [`register()`](#bpy.app.timers.register)
    - [`unregister()`](#bpy.app.timers.unregister)