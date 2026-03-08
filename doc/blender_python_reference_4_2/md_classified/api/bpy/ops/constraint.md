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

# Constraint Operators[#](#module-bpy.ops.constraint "Link to this heading")

bpy.ops.constraint.add\_target()[#](#bpy.ops.constraint.add_target "Link to this definition")
:   Add a target to the constraint

    File:
    :   [startup/bl\_operators/constraint.py:26](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L26)

bpy.ops.constraint.apply(*constraint=''*, *owner='OBJECT'*, *report=False*)[#](#bpy.ops.constraint.apply "Link to this definition")
:   Apply constraint and remove from the stack

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.
        * **report** (*boolean**,* *(**optional**)*) – Report, Create a notification after the operation

bpy.ops.constraint.childof\_clear\_inverse(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.childof_clear_inverse "Link to this definition")
:   Clear inverse correction for Child Of constraint

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.childof\_set\_inverse(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.childof_set_inverse "Link to this definition")
:   Set inverse correction for Child Of constraint

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.copy(*constraint=''*, *owner='OBJECT'*, *report=False*)[#](#bpy.ops.constraint.copy "Link to this definition")
:   Duplicate constraint at the same position in the stack

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.
        * **report** (*boolean**,* *(**optional**)*) – Report, Create a notification after the operation

bpy.ops.constraint.copy\_to\_selected(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.copy_to_selected "Link to this definition")
:   Copy constraint to other selected objects/bones

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.delete(*constraint=''*, *owner='OBJECT'*, *report=False*)[#](#bpy.ops.constraint.delete "Link to this definition")
:   Remove constraint from constraint stack

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.
        * **report** (*boolean**,* *(**optional**)*) – Report, Create a notification after the operation

bpy.ops.constraint.disable\_keep\_transform()[#](#bpy.ops.constraint.disable_keep_transform "Link to this definition")
:   Set the influence of this constraint to zero while trying to maintain the object’s transformation. Other active constraints can still influence the final transformation

    File:
    :   [startup/bl\_operators/constraint.py:86](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L86)

bpy.ops.constraint.followpath\_path\_animate(*constraint=''*, *owner='OBJECT'*, *frame\_start=1*, *length=100*)[#](#bpy.ops.constraint.followpath_path_animate "Link to this definition")
:   Add default animation for path used by constraint if it isn’t animated already

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.
        * **frame\_start** (*int in* *[**-1048574**,* *1048574**]**,* *(**optional**)*) – Start Frame, First frame of path animation
        * **length** (*int in* *[**0**,* *1048574**]**,* *(**optional**)*) – Length, Number of frames that path animation should take

bpy.ops.constraint.limitdistance\_reset(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.limitdistance_reset "Link to this definition")
:   Reset limiting distance for Limit Distance Constraint

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.move\_down(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.move_down "Link to this definition")
:   Move constraint down in constraint stack

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.move\_to\_index(*constraint=''*, *owner='OBJECT'*, *index=0*)[#](#bpy.ops.constraint.move_to_index "Link to this definition")
:   Change the constraint’s position in the list so it evaluates after the set number of others

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.
        * **index** (*int in* *[**0**,* *inf**]**,* *(**optional**)*) – Index, The index to move the constraint to

bpy.ops.constraint.move\_up(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.move_up "Link to this definition")
:   Move constraint up in constraint stack

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.normalize\_target\_weights()[#](#bpy.ops.constraint.normalize_target_weights "Link to this definition")
:   Normalize weights of all target bones

    File:
    :   [startup/bl\_operators/constraint.py:61](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L61)

bpy.ops.constraint.objectsolver\_clear\_inverse(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.objectsolver_clear_inverse "Link to this definition")
:   Clear inverse correction for Object Solver constraint

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.objectsolver\_set\_inverse(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.objectsolver_set_inverse "Link to this definition")
:   Set inverse correction for Object Solver constraint

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

bpy.ops.constraint.remove\_target(*index=0*)[#](#bpy.ops.constraint.remove_target "Link to this definition")
:   Remove the target from the constraint

    Parameters:
    :   **index** (*int in* *[**-inf**,* *inf**]**,* *(**optional**)*) – index

    File:
    :   [startup/bl\_operators/constraint.py:44](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/constraint.py#L44)

bpy.ops.constraint.stretchto\_reset(*constraint=''*, *owner='OBJECT'*)[#](#bpy.ops.constraint.stretchto_reset "Link to this definition")
:   Reset original length of bone for Stretch To Constraint

    Parameters:
    :   * **constraint** (*string**,* *(**optional**,* *never None**)*) – Constraint, Name of the constraint to edit
        * **owner** (*enum in* *[**'OBJECT'**,* *'BONE'**]**,* *(**optional**)*) –

          Owner, The owner of this constraint

          + `OBJECT`
            Object – Edit a constraint on the active object.
          + `BONE`
            Bone – Edit a constraint on the active bone.

[Next

Curve Operators](curve.md)
[Previous

Console Operators](console.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60bpy.ops.constraint.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Fbpy.ops.constraint.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Constraint Operators
  + [`add_target()`](#bpy.ops.constraint.add_target)
  + [`apply()`](#bpy.ops.constraint.apply)
  + [`childof_clear_inverse()`](#bpy.ops.constraint.childof_clear_inverse)
  + [`childof_set_inverse()`](#bpy.ops.constraint.childof_set_inverse)
  + [`copy()`](#bpy.ops.constraint.copy)
  + [`copy_to_selected()`](#bpy.ops.constraint.copy_to_selected)
  + [`delete()`](#bpy.ops.constraint.delete)
  + [`disable_keep_transform()`](#bpy.ops.constraint.disable_keep_transform)
  + [`followpath_path_animate()`](#bpy.ops.constraint.followpath_path_animate)
  + [`limitdistance_reset()`](#bpy.ops.constraint.limitdistance_reset)
  + [`move_down()`](#bpy.ops.constraint.move_down)
  + [`move_to_index()`](#bpy.ops.constraint.move_to_index)
  + [`move_up()`](#bpy.ops.constraint.move_up)
  + [`normalize_target_weights()`](#bpy.ops.constraint.normalize_target_weights)
  + [`objectsolver_clear_inverse()`](#bpy.ops.constraint.objectsolver_clear_inverse)
  + [`objectsolver_set_inverse()`](#bpy.ops.constraint.objectsolver_set_inverse)
  + [`remove_target()`](#bpy.ops.constraint.remove_target)
  + [`stretchto_reset()`](#bpy.ops.constraint.stretchto_reset)