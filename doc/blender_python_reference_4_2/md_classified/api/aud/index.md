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

[Blender Python API](../../meta/index.md)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

[![Logo](_static/blender_logo.svg)

Blender Python API](index.md)

Documentation

* [Quickstart](../../guides/quickstart.md)
* [API Overview](../../guides/overview.md)
* [API Reference Usage](../../guides/api_reference.md)
* [Best Practice](../../guides/best_practice.md)
* [Tips and Tricks](../../guides/tips_and_tricks.md)
* [Gotchas](../../guides/gotchas/index.md)
* [Advanced](../../guides/advanced/index.md)[ ]
* [Change Log](../../guides/change_log.md)

Application Modules

* [Context Access (bpy.context)](../bpy/context/index.md)
* [Data Access (bpy.data)](../bpy/data/index.md)
* [Message Bus (bpy.msgbus)](../bpy/msgbus/index.md)
* [Operators (bpy.ops)](../bpy/ops/index.md)[ ]
* [Types (bpy.types)](../bpy/types/index.md)[ ]
* [Utilities (bpy.utils)](../bpy/utils/index.md)[ ]
* [Path Utilities (bpy.path)](../bpy/path/index.md)
* [Application Data (bpy.app)](../bpy/app/index.md)[ ]

  Toggle navigation of Application Data (bpy.app)

  + [Application Handlers (bpy.app.handlers)](../bpy/app/handlers.md)
  + [Application Translations (bpy.app.translations)](../bpy/app/translations.md)
  + [Application Icons (bpy.app.icons)](../bpy/app/icons.md)
  + [Application Timers (bpy.app.timers)](../bpy/app/timers.md)
* [Property Definitions (bpy.props)](../bpy/props/index.md)

Standalone Modules

* Audio System (aud)
* [OpenGL Wrapper (bgl)](../bgl/index.md)
* [Additional Math Functions (bl\_math)](../bl_math/index.md)
* [Font Drawing (blf)](../blf/index.md)
* [BMesh Module (bmesh)](../bmesh/index.md)[ ]

  Toggle navigation of BMesh Module (bmesh)

  + [BMesh Operators (bmesh.ops)](../bmesh/ops/index.md)
  + [BMesh Types (bmesh.types)](../bmesh/types/index.md)
  + [BMesh Utilities (bmesh.utils)](../bmesh/utils/index.md)
  + [BMesh Geometry Utilities (bmesh.geometry)](../bmesh/geometry/index.md)
* [Extra Utilities (bpy\_extras)](../bpy_extras/index.md)[ ]

  Toggle navigation of Extra Utilities (bpy\_extras)

  + [bpy\_extras submodule (bpy\_extras.anim\_utils)](../bpy_extras/anim_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.asset\_utils)](../bpy_extras/asset_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.object\_utils)](../bpy_extras/object_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.io\_utils)](../bpy_extras/io_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.image\_utils)](../bpy_extras/image_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.keyconfig\_utils)](../bpy_extras/keyconfig_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.mesh\_utils)](../bpy_extras/mesh_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.node\_utils)](../bpy_extras/node_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.view3d\_utils)](../bpy_extras/view3d_utils/index.md)
  + [bpy\_extras submodule (bpy\_extras.id\_map\_utils)](../bpy_extras/id_map_utils/index.md)
* [Freestyle Module (freestyle)](../freestyle/index.md)[ ]

  Toggle navigation of Freestyle Module (freestyle)

  + [Freestyle Types (freestyle.types)](../freestyle/types/index.md)
  + [Freestyle Predicates (freestyle.predicates)](../freestyle/predicates/index.md)
  + [Freestyle Functions (freestyle.functions)](../freestyle/functions/index.md)
  + [Freestyle Chaining Iterators (freestyle.chainingiterators)](../freestyle/chainingiterators/index.md)
  + [Freestyle Shaders (freestyle.shaders)](../freestyle/shaders/index.md)
  + [Freestyle Utilities (freestyle.utils)](../freestyle/utils/index.md)[ ]

    Toggle navigation of Freestyle Utilities (freestyle.utils)

    - [freestyle.utils submodule (freestyle.utils.ContextFunctions)](../freestyle/utils/ContextFunctions.md)
* [GPU Module (gpu)](../gpu/index.md)[ ]

  Toggle navigation of GPU Module (gpu)

  + [GPU Types (gpu.types)](../gpu/types/index.md)
  + [GPU Matrix Utilities (gpu.matrix)](../gpu/matrix/index.md)
  + [GPU Select Utilities (gpu.select)](../gpu/select/index.md)
  + [GPU Shader Utilities (gpu.shader)](../gpu/shader/index.md)
  + [GPU State Utilities (gpu.state)](../gpu/state/index.md)
  + [GPU Texture Utilities (gpu.texture)](../gpu/texture/index.md)
  + [GPU Platform Utilities (gpu.platform)](../gpu/platform/index.md)
  + [GPU Capabilities Utilities (gpu.capabilities)](../gpu/capabilities/index.md)
* [GPU Utilities (gpu\_extras)](../gpu_extras/index.md)[ ]

  Toggle navigation of GPU Utilities (gpu\_extras)

  + [gpu\_extras submodule (gpu\_extras.batch)](../gpu_extras/batch/index.md)
  + [gpu\_extras submodule (gpu\_extras.presets)](../gpu_extras/presets/index.md)
* [ID Property Access (idprop.types)](../idprop/types/index.md)
* [Image Buffer (imbuf)](../imbuf/index.md)[ ]

  Toggle navigation of Image Buffer (imbuf)

  + [Image Buffer Types (imbuf.types)](../imbuf/types/index.md)
* [Math Types & Utilities (mathutils)](../mathutils/index.md)[ ]

  Toggle navigation of Math Types & Utilities (mathutils)

  + [Geometry Utilities (mathutils.geometry)](../mathutils/geometry/index.md)
  + [BVHTree Utilities (mathutils.bvhtree)](../mathutils/bvhtree/index.md)
  + [KDTree Utilities (mathutils.kdtree)](../mathutils/kdtree/index.md)
  + [Interpolation Utilities (mathutils.interpolate)](../mathutils/interpolate/index.md)
  + [Noise Utilities (mathutils.noise)](../mathutils/noise/index.md)

* 4.2

  Versions

  + Loading...

Note

You are not using the most up to date version of the documentation.
 is the newest version.

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Audio System (aud)[#](#module-aud "Link to this heading")

Audaspace (pronounced “outer space”) is a high level audio library.

## Basic Sound Playback[#](#basic-sound-playback "Link to this heading")

This script shows how to use the classes: [`Device`](#aud.Device "aud.Device"), [`Sound`](#aud.Sound "aud.Sound") and
[`Handle`](#aud.Handle "aud.Handle").

```
import aud

device = aud.Device()
# load sound file (it can be a video file with audio)
sound = aud.Sound('music.ogg')

# play the audio, this return a handle to control play/pause
handle = device.play(sound)
# if the audio is not too big and will be used often you can buffer it
sound_buffered = aud.Sound.cache(sound)
handle_buffered = device.play(sound_buffered)

# stop the sounds (otherwise they play until their ends)
handle.stop()
handle_buffered.stop()
```

aud.AP\_LOCATION[#](#aud.AP_LOCATION "Link to this definition")
:   Constant value 3

aud.AP\_ORIENTATION[#](#aud.AP_ORIENTATION "Link to this definition")
:   Constant value 4

aud.AP\_PANNING[#](#aud.AP_PANNING "Link to this definition")
:   Constant value 1

aud.AP\_PITCH[#](#aud.AP_PITCH "Link to this definition")
:   Constant value 2

aud.AP\_VOLUME[#](#aud.AP_VOLUME "Link to this definition")
:   Constant value 0

aud.CHANNELS\_INVALID[#](#aud.CHANNELS_INVALID "Link to this definition")
:   Constant value 0

aud.CHANNELS\_MONO[#](#aud.CHANNELS_MONO "Link to this definition")
:   Constant value 1

aud.CHANNELS\_STEREO[#](#aud.CHANNELS_STEREO "Link to this definition")
:   Constant value 2

aud.CHANNELS\_STEREO\_LFE[#](#aud.CHANNELS_STEREO_LFE "Link to this definition")
:   Constant value 3

aud.CHANNELS\_SURROUND4[#](#aud.CHANNELS_SURROUND4 "Link to this definition")
:   Constant value 4

aud.CHANNELS\_SURROUND5[#](#aud.CHANNELS_SURROUND5 "Link to this definition")
:   Constant value 5

aud.CHANNELS\_SURROUND51[#](#aud.CHANNELS_SURROUND51 "Link to this definition")
:   Constant value 6

aud.CHANNELS\_SURROUND61[#](#aud.CHANNELS_SURROUND61 "Link to this definition")
:   Constant value 7

aud.CHANNELS\_SURROUND71[#](#aud.CHANNELS_SURROUND71 "Link to this definition")
:   Constant value 8

aud.CODEC\_AAC[#](#aud.CODEC_AAC "Link to this definition")
:   Constant value 1

aud.CODEC\_AC3[#](#aud.CODEC_AC3 "Link to this definition")
:   Constant value 2

aud.CODEC\_FLAC[#](#aud.CODEC_FLAC "Link to this definition")
:   Constant value 3

aud.CODEC\_INVALID[#](#aud.CODEC_INVALID "Link to this definition")
:   Constant value 0

aud.CODEC\_MP2[#](#aud.CODEC_MP2 "Link to this definition")
:   Constant value 4

aud.CODEC\_MP3[#](#aud.CODEC_MP3 "Link to this definition")
:   Constant value 5

aud.CODEC\_OPUS[#](#aud.CODEC_OPUS "Link to this definition")
:   Constant value 8

aud.CODEC\_PCM[#](#aud.CODEC_PCM "Link to this definition")
:   Constant value 6

aud.CODEC\_VORBIS[#](#aud.CODEC_VORBIS "Link to this definition")
:   Constant value 7

aud.CONTAINER\_AC3[#](#aud.CONTAINER_AC3 "Link to this definition")
:   Constant value 1

aud.CONTAINER\_FLAC[#](#aud.CONTAINER_FLAC "Link to this definition")
:   Constant value 2

aud.CONTAINER\_INVALID[#](#aud.CONTAINER_INVALID "Link to this definition")
:   Constant value 0

aud.CONTAINER\_MATROSKA[#](#aud.CONTAINER_MATROSKA "Link to this definition")
:   Constant value 3

aud.CONTAINER\_MP2[#](#aud.CONTAINER_MP2 "Link to this definition")
:   Constant value 4

aud.CONTAINER\_MP3[#](#aud.CONTAINER_MP3 "Link to this definition")
:   Constant value 5

aud.CONTAINER\_OGG[#](#aud.CONTAINER_OGG "Link to this definition")
:   Constant value 6

aud.CONTAINER\_WAV[#](#aud.CONTAINER_WAV "Link to this definition")
:   Constant value 7

aud.DISTANCE\_MODEL\_EXPONENT[#](#aud.DISTANCE_MODEL_EXPONENT "Link to this definition")
:   Constant value 5

aud.DISTANCE\_MODEL\_EXPONENT\_CLAMPED[#](#aud.DISTANCE_MODEL_EXPONENT_CLAMPED "Link to this definition")
:   Constant value 6

aud.DISTANCE\_MODEL\_INVALID[#](#aud.DISTANCE_MODEL_INVALID "Link to this definition")
:   Constant value 0

aud.DISTANCE\_MODEL\_INVERSE[#](#aud.DISTANCE_MODEL_INVERSE "Link to this definition")
:   Constant value 1

aud.DISTANCE\_MODEL\_INVERSE\_CLAMPED[#](#aud.DISTANCE_MODEL_INVERSE_CLAMPED "Link to this definition")
:   Constant value 2

aud.DISTANCE\_MODEL\_LINEAR[#](#aud.DISTANCE_MODEL_LINEAR "Link to this definition")
:   Constant value 3

aud.DISTANCE\_MODEL\_LINEAR\_CLAMPED[#](#aud.DISTANCE_MODEL_LINEAR_CLAMPED "Link to this definition")
:   Constant value 4

aud.FORMAT\_FLOAT32[#](#aud.FORMAT_FLOAT32 "Link to this definition")
:   Constant value 36

aud.FORMAT\_FLOAT64[#](#aud.FORMAT_FLOAT64 "Link to this definition")
:   Constant value 40

aud.FORMAT\_INVALID[#](#aud.FORMAT_INVALID "Link to this definition")
:   Constant value 0

aud.FORMAT\_S16[#](#aud.FORMAT_S16 "Link to this definition")
:   Constant value 18

aud.FORMAT\_S24[#](#aud.FORMAT_S24 "Link to this definition")
:   Constant value 19

aud.FORMAT\_S32[#](#aud.FORMAT_S32 "Link to this definition")
:   Constant value 20

aud.FORMAT\_U8[#](#aud.FORMAT_U8 "Link to this definition")
:   Constant value 1

aud.RATE\_11025[#](#aud.RATE_11025 "Link to this definition")
:   Constant value 11025

aud.RATE\_16000[#](#aud.RATE_16000 "Link to this definition")
:   Constant value 16000

aud.RATE\_192000[#](#aud.RATE_192000 "Link to this definition")
:   Constant value 192000

aud.RATE\_22050[#](#aud.RATE_22050 "Link to this definition")
:   Constant value 22050

aud.RATE\_32000[#](#aud.RATE_32000 "Link to this definition")
:   Constant value 32000

aud.RATE\_44100[#](#aud.RATE_44100 "Link to this definition")
:   Constant value 44100

aud.RATE\_48000[#](#aud.RATE_48000 "Link to this definition")
:   Constant value 48000

aud.RATE\_8000[#](#aud.RATE_8000 "Link to this definition")
:   Constant value 8000

aud.RATE\_88200[#](#aud.RATE_88200 "Link to this definition")
:   Constant value 88200

aud.RATE\_96000[#](#aud.RATE_96000 "Link to this definition")
:   Constant value 96000

aud.RATE\_INVALID[#](#aud.RATE_INVALID "Link to this definition")
:   Constant value 0

aud.STATUS\_INVALID[#](#aud.STATUS_INVALID "Link to this definition")
:   Constant value 0

aud.STATUS\_PAUSED[#](#aud.STATUS_PAUSED "Link to this definition")
:   Constant value 2

aud.STATUS\_PLAYING[#](#aud.STATUS_PLAYING "Link to this definition")
:   Constant value 1

aud.STATUS\_STOPPED[#](#aud.STATUS_STOPPED "Link to this definition")
:   Constant value 3

*class* aud.Device[#](#aud.Device "Link to this definition")
:   Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.

    lock()[#](#aud.Device.lock "Link to this definition")
    :   Locks the device so that it’s guaranteed, that no samples are
        read from the streams until [`unlock()`](#aud.Device.unlock "aud.Device.unlock") is called.
        This is useful if you want to do start/stop/pause/resume some
        sounds at the same time.

        Note

        The device has to be unlocked as often as locked to be
        able to continue playback.

        Warning

        Make sure the time between locking and unlocking is
        as short as possible to avoid clicks.

    play(*sound*, *keep=False*)[#](#aud.Device.play "Link to this definition")
    :   Plays a sound.

        Parameters:
        :   * **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound to play.
            * **keep** (*bool*) – See [`Handle.keep`](#aud.Handle.keep "aud.Handle.keep").

        Returns:
        :   The playback handle with which playback can be
            controlled with.

        Return type:
        :   [`Handle`](#aud.Handle "aud.Handle")

    stopAll()[#](#aud.Device.stopAll "Link to this definition")
    :   Stops all playing and paused sounds.

    unlock()[#](#aud.Device.unlock "Link to this definition")
    :   Unlocks the device after a lock call, see [`lock()`](#aud.Device.lock "aud.Device.lock") for
        details.

    channels[#](#aud.Device.channels "Link to this definition")
    :   The channel count of the device.

    distance\_model[#](#aud.Device.distance_model "Link to this definition")
    :   The distance model of the device.

        See also

        [OpenAL Documentation](https://www.openal.org/documentation/)

    doppler\_factor[#](#aud.Device.doppler_factor "Link to this definition")
    :   The doppler factor of the device.
        This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.

    format[#](#aud.Device.format "Link to this definition")
    :   The native sample format of the device.

    listener\_location[#](#aud.Device.listener_location "Link to this definition")
    :   The listeners’s location in 3D space, a 3D tuple of floats.

    listener\_orientation[#](#aud.Device.listener_orientation "Link to this definition")
    :   The listener’s orientation in 3D space as quaternion, a 4 float tuple.

    listener\_velocity[#](#aud.Device.listener_velocity "Link to this definition")
    :   The listener’s velocity in 3D space, a 3D tuple of floats.

    rate[#](#aud.Device.rate "Link to this definition")
    :   The sampling rate of the device in Hz.

    speed\_of\_sound[#](#aud.Device.speed_of_sound "Link to this definition")
    :   The speed of sound of the device.
        The speed of sound in air is typically 343.3 m/s.

    volume[#](#aud.Device.volume "Link to this definition")
    :   The overall volume of the device.

*class* aud.DynamicMusic[#](#aud.DynamicMusic "Link to this definition")
:   The DynamicMusic object allows to play music depending on a current scene, scene changes are managed by the class, with the possibility of custom transitions.
    The default transition is a crossfade effect, and the default scene is silent and has id 0

    addScene(*scene*)[#](#aud.DynamicMusic.addScene "Link to this definition")
    :   Adds a new scene.

        Parameters:
        :   **scene** ([`Sound`](#aud.Sound "aud.Sound")) – The scene sound.

        Returns:
        :   The new scene id.

        Return type:
        :   int

    addTransition(*ini*, *end*, *transition*)[#](#aud.DynamicMusic.addTransition "Link to this definition")
    :   Adds a new scene.

        Parameters:
        :   * **ini** (*int*) – the initial scene foor the transition.
            * **end** (*int*) – The final scene for the transition.
            * **transition** ([`Sound`](#aud.Sound "aud.Sound")) – The transition sound.

        Returns:
        :   false if the ini or end scenes don’t exist, true othrwise.

        Return type:
        :   bool

    pause()[#](#aud.DynamicMusic.pause "Link to this definition")
    :   Pauses playback of the scene.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    resume()[#](#aud.DynamicMusic.resume "Link to this definition")
    :   Resumes playback of the scene.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    stop()[#](#aud.DynamicMusic.stop "Link to this definition")
    :   Stops playback of the scene.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    fadeTime[#](#aud.DynamicMusic.fadeTime "Link to this definition")
    :   The length in seconds of the crossfade transition

    position[#](#aud.DynamicMusic.position "Link to this definition")
    :   The playback position of the scene in seconds.

    scene[#](#aud.DynamicMusic.scene "Link to this definition")
    :   The current scene

    status[#](#aud.DynamicMusic.status "Link to this definition")
    :   Whether the scene is playing, paused or stopped (=invalid).

    volume[#](#aud.DynamicMusic.volume "Link to this definition")
    :   The volume of the scene.

*class* aud.HRTF[#](#aud.HRTF "Link to this definition")
:   An HRTF object represents a set of head related transfer functions as impulse responses. It’s used for binaural sound

    loadLeftHrtfSet(*extension*, *directory*)[#](#aud.HRTF.loadLeftHrtfSet "Link to this definition")
    :   Loads all HRTFs from a directory.

        Parameters:
        :   * **extension** (*string*) – The file extension of the hrtfs.
            * **directory** – The path to where the HRTF files are located.

        Returns:
        :   The loaded [`HRTF`](#aud.HRTF "aud.HRTF") object.

        Return type:
        :   [`HRTF`](#aud.HRTF "aud.HRTF")

    loadLeftHrtfSet(*extension*, *directory*)[#](#id0 "Link to this definition")
    :   Loads all HRTFs from a directory.

        Parameters:
        :   * **extension** (*string*) – The file extension of the hrtfs.
            * **directory** – The path to where the HRTF files are located.

        Returns:
        :   The loaded [`HRTF`](#aud.HRTF "aud.HRTF") object.

        Return type:
        :   [`HRTF`](#aud.HRTF "aud.HRTF")

    addImpulseResponseFromSound(*sound*, *azimuth*, *elevation*)[#](#aud.HRTF.addImpulseResponseFromSound "Link to this definition")
    :   Adds a new hrtf to the HRTF object

        Parameters:
        :   * **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound that contains the hrtf.
            * **azimuth** (*float*) – The azimuth angle of the hrtf.
            * **elevation** (*float*) – The elevation angle of the hrtf.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

*class* aud.Handle[#](#aud.Handle "Link to this definition")
:   Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.

    pause()[#](#aud.Handle.pause "Link to this definition")
    :   Pauses playback.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    resume()[#](#aud.Handle.resume "Link to this definition")
    :   Resumes playback.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    stop()[#](#aud.Handle.stop "Link to this definition")
    :   Stops playback.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

        Note

        This makes the handle invalid.

    attenuation[#](#aud.Handle.attenuation "Link to this definition")
    :   This factor is used for distance based attenuation of the source.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    cone\_angle\_inner[#](#aud.Handle.cone_angle_inner "Link to this definition")
    :   The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the [`location`](#aud.Handle.location "aud.Handle.location") of the source and with infinite height, heading in the direction of the source’s [`orientation`](#aud.Handle.orientation "aud.Handle.orientation").
        In the inner cone the volume is normal. Outside the outer cone the volume will be [`cone_volume_outer`](#aud.Handle.cone_volume_outer "aud.Handle.cone_volume_outer") and in the area between the volume will be interpolated linearly.

    cone\_angle\_outer[#](#aud.Handle.cone_angle_outer "Link to this definition")
    :   The opening angle of the outer cone of the source.

        See also

        [`cone_angle_inner`](#aud.Handle.cone_angle_inner "aud.Handle.cone_angle_inner")

    cone\_volume\_outer[#](#aud.Handle.cone_volume_outer "Link to this definition")
    :   The volume outside the outer cone of the source.

        See also

        [`cone_angle_inner`](#aud.Handle.cone_angle_inner "aud.Handle.cone_angle_inner")

    distance\_maximum[#](#aud.Handle.distance_maximum "Link to this definition")
    :   The maximum distance of the source.
        If the listener is further away the source volume will be 0.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    distance\_reference[#](#aud.Handle.distance_reference "Link to this definition")
    :   The reference distance of the source.
        At this distance the volume will be exactly [`volume`](#aud.Handle.volume "aud.Handle.volume").

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    keep[#](#aud.Handle.keep "Link to this definition")
    :   Whether the sound should be kept paused in the device when its end is reached.
        This can be used to seek the sound to some position and start playback again.

        Warning

        If this is set to true and you forget stopping this equals a memory leak as the handle exists until the device is destroyed.

    location[#](#aud.Handle.location "Link to this definition")
    :   The source’s location in 3D space, a 3D tuple of floats.

    loop\_count[#](#aud.Handle.loop_count "Link to this definition")
    :   The (remaining) loop count of the sound. A negative value indicates infinity.

    orientation[#](#aud.Handle.orientation "Link to this definition")
    :   The source’s orientation in 3D space as quaternion, a 4 float tuple.

    pitch[#](#aud.Handle.pitch "Link to this definition")
    :   The pitch of the sound.

    position[#](#aud.Handle.position "Link to this definition")
    :   The playback position of the sound in seconds.

    relative[#](#aud.Handle.relative "Link to this definition")
    :   Whether the source’s location, velocity and orientation is relative or absolute to the listener.

    status[#](#aud.Handle.status "Link to this definition")
    :   Whether the sound is playing, paused or stopped (=invalid).

    velocity[#](#aud.Handle.velocity "Link to this definition")
    :   The source’s velocity in 3D space, a 3D tuple of floats.

    volume[#](#aud.Handle.volume "Link to this definition")
    :   The volume of the sound.

    volume\_maximum[#](#aud.Handle.volume_maximum "Link to this definition")
    :   The maximum volume of the source.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    volume\_minimum[#](#aud.Handle.volume_minimum "Link to this definition")
    :   The minimum volume of the source.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

*class* aud.ImpulseResponse[#](#aud.ImpulseResponse "Link to this definition")
:   An ImpulseResponse object represents a filter with which to convolve a sound.

*class* aud.PlaybackManager[#](#aud.PlaybackManager "Link to this definition")
:   A PlabackManager object allows to easily control groups os sounds organized in categories.

    addCategory(*volume*)[#](#aud.PlaybackManager.addCategory "Link to this definition")
    :   Adds a category with a custom volume.

        Parameters:
        :   **volume** (*float*) – The volume for ther new category.

        Returns:
        :   The key of the new category.

        Return type:
        :   int

    clean()[#](#aud.PlaybackManager.clean "Link to this definition")
    :   Cleans all the invalid and finished sound from the playback manager.

    getVolume(*catKey*)[#](#aud.PlaybackManager.getVolume "Link to this definition")
    :   Retrieves the volume of a category.

        Parameters:
        :   **catKey** (*int*) – the key of the category.

        Returns:
        :   The volume of the cateogry.

        Return type:
        :   float

    pause(*catKey*)[#](#aud.PlaybackManager.pause "Link to this definition")
    :   Pauses playback of the category.

        Parameters:
        :   **catKey** (*int*) – the key of the category.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    play(*sound*, *catKey*)[#](#aud.PlaybackManager.play "Link to this definition")
    :   Plays a sound through the playback manager and assigns it to a category.

        Parameters:
        :   * **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound to play.
            * **catKey** (*int*) – the key of the category in which the sound will be added,
              if it doesn’t exist, a new one will be created.

        Returns:
        :   The playback handle with which playback can be controlled with.

        Return type:
        :   [`Handle`](#aud.Handle "aud.Handle")

    resume(*catKey*)[#](#aud.PlaybackManager.resume "Link to this definition")
    :   Resumes playback of the catgory.

        Parameters:
        :   **catKey** (*int*) – the key of the category.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

    setVolume(*volume*, *catKey*)[#](#aud.PlaybackManager.setVolume "Link to this definition")
    :   Changes the volume of a category.

        Parameters:
        :   * **volume** (*float*) – the new volume value.
            * **catKey** (*int*) – the key of the category.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   int

    stop(*catKey*)[#](#aud.PlaybackManager.stop "Link to this definition")
    :   Stops playback of the category.

        Parameters:
        :   **catKey** (*int*) – the key of the category.

        Returns:
        :   Whether the action succeeded.

        Return type:
        :   bool

*class* aud.Sequence[#](#aud.Sequence "Link to this definition")
:   This sound represents sequenced entries to play a sound sequence.

    add()[#](#aud.Sequence.add "Link to this definition")
    :   Adds a new entry to the sequence.

        Parameters:
        :   * **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound this entry should play.
            * **begin** (*double*) – The start time.
            * **end** (*double*) – The end time or a negative value if determined by the sound.
            * **skip** (*double*) – How much seconds should be skipped at the beginning.

        Returns:
        :   The entry added.

        Return type:
        :   [`SequenceEntry`](#aud.SequenceEntry "aud.SequenceEntry")

    remove()[#](#aud.Sequence.remove "Link to this definition")
    :   Removes an entry from the sequence.

        Parameters:
        :   **entry** ([`SequenceEntry`](#aud.SequenceEntry "aud.SequenceEntry")) – The entry to remove.

    setAnimationData()[#](#aud.Sequence.setAnimationData "Link to this definition")
    :   Writes animation data to a sequence.

        Parameters:
        :   * **type** (*int*) – The type of animation data.
            * **frame** (*int*) – The frame this data is for.
            * **data** (*sequence* *of* *float*) – The data to write.
            * **animated** (*bool*) – Whether the attribute is animated.

    channels[#](#aud.Sequence.channels "Link to this definition")
    :   The channel count of the sequence.

    distance\_model[#](#aud.Sequence.distance_model "Link to this definition")
    :   The distance model of the sequence.

        See also

        [OpenAL Documentation](https://www.openal.org/documentation/)

    doppler\_factor[#](#aud.Sequence.doppler_factor "Link to this definition")
    :   The doppler factor of the sequence.
        This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity.

    fps[#](#aud.Sequence.fps "Link to this definition")
    :   The listeners’s location in 3D space, a 3D tuple of floats.

    muted[#](#aud.Sequence.muted "Link to this definition")
    :   Whether the whole sequence is muted.

    rate[#](#aud.Sequence.rate "Link to this definition")
    :   The sampling rate of the sequence in Hz.

    speed\_of\_sound[#](#aud.Sequence.speed_of_sound "Link to this definition")
    :   The speed of sound of the sequence.
        The speed of sound in air is typically 343.3 m/s.

*class* aud.SequenceEntry[#](#aud.SequenceEntry "Link to this definition")
:   SequenceEntry objects represent an entry of a sequenced sound.

    move()[#](#aud.SequenceEntry.move "Link to this definition")
    :   Moves the entry.

        Parameters:
        :   * **begin** (*double*) – The new start time.
            * **end** (*double*) – The new end time or a negative value if unknown.
            * **skip** (*double*) – How many seconds to skip at the beginning.

    setAnimationData()[#](#aud.SequenceEntry.setAnimationData "Link to this definition")
    :   Writes animation data to a sequenced entry.

        Parameters:
        :   * **type** (*int*) – The type of animation data.
            * **frame** (*int*) – The frame this data is for.
            * **data** (*sequence* *of* *float*) – The data to write.
            * **animated** (*bool*) – Whether the attribute is animated.

    attenuation[#](#aud.SequenceEntry.attenuation "Link to this definition")
    :   This factor is used for distance based attenuation of the source.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    cone\_angle\_inner[#](#aud.SequenceEntry.cone_angle_inner "Link to this definition")
    :   The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the `location` of the source and with infinite height, heading in the direction of the source’s `orientation`.
        In the inner cone the volume is normal. Outside the outer cone the volume will be [`cone_volume_outer`](#aud.SequenceEntry.cone_volume_outer "aud.SequenceEntry.cone_volume_outer") and in the area between the volume will be interpolated linearly.

    cone\_angle\_outer[#](#aud.SequenceEntry.cone_angle_outer "Link to this definition")
    :   The opening angle of the outer cone of the source.

        See also

        [`cone_angle_inner`](#aud.SequenceEntry.cone_angle_inner "aud.SequenceEntry.cone_angle_inner")

    cone\_volume\_outer[#](#aud.SequenceEntry.cone_volume_outer "Link to this definition")
    :   The volume outside the outer cone of the source.

        See also

        [`cone_angle_inner`](#aud.SequenceEntry.cone_angle_inner "aud.SequenceEntry.cone_angle_inner")

    distance\_maximum[#](#aud.SequenceEntry.distance_maximum "Link to this definition")
    :   The maximum distance of the source.
        If the listener is further away the source volume will be 0.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    distance\_reference[#](#aud.SequenceEntry.distance_reference "Link to this definition")
    :   The reference distance of the source.
        At this distance the volume will be exactly `volume`.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    muted[#](#aud.SequenceEntry.muted "Link to this definition")
    :   Whether the entry is muted.

    relative[#](#aud.SequenceEntry.relative "Link to this definition")
    :   Whether the source’s location, velocity and orientation is relative or absolute to the listener.

    sound[#](#aud.SequenceEntry.sound "Link to this definition")
    :   The sound the entry is representing and will be played in the sequence.

    volume\_maximum[#](#aud.SequenceEntry.volume_maximum "Link to this definition")
    :   The maximum volume of the source.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

    volume\_minimum[#](#aud.SequenceEntry.volume_minimum "Link to this definition")
    :   The minimum volume of the source.

        See also

        [`Device.distance_model`](#aud.Device.distance_model "aud.Device.distance_model")

*class* aud.Sound[#](#aud.Sound "Link to this definition")
:   Sound objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback.

    *classmethod* buffer(*data*, *rate*)[#](#aud.Sound.buffer "Link to this definition")
    :   Creates a sound from a data buffer.

        Parameters:
        :   * **data** (`numpy.ndarray`) – The data as two dimensional numpy array.
            * **rate** (*double*) – The sample rate.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    *classmethod* file(*filename*)[#](#aud.Sound.file "Link to this definition")
    :   Creates a sound object of a sound file.

        Parameters:
        :   **filename** (*string*) – Path of the file.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Warning

        If the file doesn’t exist or can’t be read you will
        not get an exception immediately, but when you try to start
        playback of that sound.

    *classmethod* list()[#](#aud.Sound.list "Link to this definition")
    :   Creates an empty sound list that can contain several sounds.

        Parameters:
        :   **random** (*int*) – whether the playback will be random or not.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    *classmethod* sawtooth(*frequency*, *rate=48000*)[#](#aud.Sound.sawtooth "Link to this definition")
    :   Creates a sawtooth sound which plays a sawtooth wave.

        Parameters:
        :   * **frequency** (*float*) – The frequency of the sawtooth wave in Hz.
            * **rate** (*int*) – The sampling rate in Hz. It’s recommended to set this
              value to the playback device’s samling rate to avoid resamping.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    *classmethod* silence(*rate=48000*)[#](#aud.Sound.silence "Link to this definition")
    :   Creates a silence sound which plays simple silence.

        Parameters:
        :   **rate** (*int*) – The sampling rate in Hz. It’s recommended to set this
            value to the playback device’s samling rate to avoid resamping.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    *classmethod* sine(*frequency*, *rate=48000*)[#](#aud.Sound.sine "Link to this definition")
    :   Creates a sine sound which plays a sine wave.

        Parameters:
        :   * **frequency** (*float*) – The frequency of the sine wave in Hz.
            * **rate** (*int*) – The sampling rate in Hz. It’s recommended to set this
              value to the playback device’s samling rate to avoid resamping.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    *classmethod* square(*frequency*, *rate=48000*)[#](#aud.Sound.square "Link to this definition")
    :   Creates a square sound which plays a square wave.

        Parameters:
        :   * **frequency** (*float*) – The frequency of the square wave in Hz.
            * **rate** (*int*) – The sampling rate in Hz. It’s recommended to set this
              value to the playback device’s samling rate to avoid resamping.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    *classmethod* triangle(*frequency*, *rate=48000*)[#](#aud.Sound.triangle "Link to this definition")
    :   Creates a triangle sound which plays a triangle wave.

        Parameters:
        :   * **frequency** (*float*) – The frequency of the triangle wave in Hz.
            * **rate** (*int*) – The sampling rate in Hz. It’s recommended to set this
              value to the playback device’s samling rate to avoid resamping.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    ADSR(*attack*, *decay*, *sustain*, *release*)[#](#aud.Sound.ADSR "Link to this definition")
    :   Attack-Decay-Sustain-Release envelopes the volume of a sound.
        Note: there is currently no way to trigger the release with this API.

        Parameters:
        :   * **attack** (*float*) – The attack time in seconds.
            * **decay** (*float*) – The decay time in seconds.
            * **sustain** (*float*) – The sustain level.
            * **release** (*float*) – The release level.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    accumulate(*additive=False*)[#](#aud.Sound.accumulate "Link to this definition")
    :   Accumulates a sound by summing over positive input
        differences thus generating a monotonic sigal.
        If additivity is set to true negative input differences get added too,
        but positive ones with a factor of two.

        Note that with additivity the signal is not monotonic anymore.

        Parameters:
        :   **additive** – Whether the accumulation should be additive or not.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    addSound(*sound*)[#](#aud.Sound.addSound "Link to this definition")
    :   Adds a new sound to a sound list.

        Parameters:
        :   **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound that will be added to the list.

        Note

        You can only add a sound to a sound list.

    binaural()[#](#aud.Sound.binaural "Link to this definition")
    :   Creates a binaural sound using another sound as source. The original sound must be mono

        Parameters:
        :   * **hrtfs** – An HRTF set.
            * **source** ([`Source`](#aud.Source "aud.Source")) – An object representing the source position of the sound.
            * **threadPool** ([`ThreadPool`](#aud.ThreadPool "aud.ThreadPool")) – A thread pool used to parallelize convolution.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    cache()[#](#aud.Sound.cache "Link to this definition")
    :   Caches a sound into RAM.

        This saves CPU usage needed for decoding and file access if the
        underlying sound reads from a file on the harddisk,
        but it consumes a lot of memory.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        Only known-length factories can be buffered.

        Warning

        Raw PCM data needs a lot of space, only buffer
        short factories.

    convolver()[#](#aud.Sound.convolver "Link to this definition")
    :   Creates a sound that will apply convolution to another sound.

        Parameters:
        :   * **impulseResponse** ([`ImpulseResponse`](#aud.ImpulseResponse "aud.ImpulseResponse")) – The filter with which convolve the sound.
            * **threadPool** ([`ThreadPool`](#aud.ThreadPool "aud.ThreadPool")) – A thread pool used to parallelize convolution.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    data()[#](#aud.Sound.data "Link to this definition")
    :   Retrieves the data of the sound as numpy array.

        Returns:
        :   A two dimensional numpy float array.

        Return type:
        :   `numpy.ndarray`

        Note

        Best efficiency with cached sounds.

    delay(*time*)[#](#aud.Sound.delay "Link to this definition")
    :   Delays by playing adding silence in front of the other sound’s data.

        Parameters:
        :   **time** (*float*) – How many seconds of silence should be added before the sound.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    envelope(*attack*, *release*, *threshold*, *arthreshold*)[#](#aud.Sound.envelope "Link to this definition")
    :   Delays by playing adding silence in front of the other sound’s data.

        Parameters:
        :   * **attack** (*float*) – The attack factor.
            * **release** (*float*) – The release factor.
            * **threshold** (*float*) – The general threshold value.
            * **arthreshold** (*float*) – The attack/release threshold value.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    fadein(*start*, *length*)[#](#aud.Sound.fadein "Link to this definition")
    :   Fades a sound in by raising the volume linearly in the given
        time interval.

        Parameters:
        :   * **start** (*float*) – Time in seconds when the fading should start.
            * **length** (*float*) – Time in seconds how long the fading should last.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        Before the fade starts it plays silence.

    fadeout(*start*, *length*)[#](#aud.Sound.fadeout "Link to this definition")
    :   Fades a sound in by lowering the volume linearly in the given
        time interval.

        Parameters:
        :   * **start** (*float*) – Time in seconds when the fading should start.
            * **length** (*float*) – Time in seconds how long the fading should last.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        After the fade this sound plays silence, so that
        the length of the sound is not altered.

    filter(*b*, *a=1*)[#](#aud.Sound.filter "Link to this definition")
    :   Filters a sound with the supplied IIR filter coefficients.
        Without the second parameter you’ll get a FIR filter.

        If the first value of the a sequence is 0,
        it will be set to 1 automatically.
        If the first value of the a sequence is neither 0 nor 1, all
        filter coefficients will be scaled by this value so that it is 1
        in the end, you don’t have to scale yourself.

        Parameters:
        :   * **b** (*sequence* *of* *float*) – The nominator filter coefficients.
            * **a** (*sequence* *of* *float*) – The denominator filter coefficients.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    highpass(*frequency*, *Q=0.5*)[#](#aud.Sound.highpass "Link to this definition")
    :   Creates a second order highpass filter based on the transfer
        function \(H(s) = s^2 / (s^2 + s/Q + 1)\)

        Parameters:
        :   * **frequency** (*float*) – The cut off trequency of the highpass.
            * **Q** (*float*) – Q factor of the lowpass.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    join(*sound*)[#](#aud.Sound.join "Link to this definition")
    :   Plays two factories in sequence.

        Parameters:
        :   **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound to play second.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        The two factories have to have the same specifications
        (channels and samplerate).

    limit(*start*, *end*)[#](#aud.Sound.limit "Link to this definition")
    :   Limits a sound within a specific start and end time.

        Parameters:
        :   * **start** (*float*) – Start time in seconds.
            * **end** (*float*) – End time in seconds.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    loop(*count*)[#](#aud.Sound.loop "Link to this definition")
    :   Loops a sound.

        Parameters:
        :   **count** (*integer*) – How often the sound should be looped.
            Negative values mean endlessly.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        This is a filter function, you might consider using
        [`Handle.loop_count`](#aud.Handle.loop_count "aud.Handle.loop_count") instead.

    lowpass(*frequency*, *Q=0.5*)[#](#aud.Sound.lowpass "Link to this definition")
    :   Creates a second order lowpass filter based on the transfer function \(H(s) = 1 / (s^2 + s/Q + 1)\)

        Parameters:
        :   * **frequency** (*float*) – The cut off trequency of the lowpass.
            * **Q** (*float*) – Q factor of the lowpass.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    mix(*sound*)[#](#aud.Sound.mix "Link to this definition")
    :   Mixes two factories.

        Parameters:
        :   **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound to mix over the other.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        The two factories have to have the same specifications
        (channels and samplerate).

    modulate(*sound*)[#](#aud.Sound.modulate "Link to this definition")
    :   Modulates two factories.

        Parameters:
        :   **sound** ([`Sound`](#aud.Sound "aud.Sound")) – The sound to modulate over the other.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        The two factories have to have the same specifications
        (channels and samplerate).

    mutable()[#](#aud.Sound.mutable "Link to this definition")
    :   Creates a sound that will be restarted when sought backwards.
        If the original sound is a sound list, the playing sound can change.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    pingpong()[#](#aud.Sound.pingpong "Link to this definition")
    :   Plays a sound forward and then backward.
        This is like joining a sound with its reverse.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    pitch(*factor*)[#](#aud.Sound.pitch "Link to this definition")
    :   Changes the pitch of a sound with a specific factor.

        Parameters:
        :   **factor** (*float*) – The factor to change the pitch with.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        This is done by changing the sample rate of the
        underlying sound, which has to be an integer, so the factor
        value rounded and the factor may not be 100 % accurate.

        Note

        This is a filter function, you might consider using
        [`Handle.pitch`](#aud.Handle.pitch "aud.Handle.pitch") instead.

    rechannel(*channels*)[#](#aud.Sound.rechannel "Link to this definition")
    :   Rechannels the sound.

        Parameters:
        :   **channels** (*int*) – The new channel configuration.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    resample(*rate*, *quality*)[#](#aud.Sound.resample "Link to this definition")
    :   Resamples the sound.

        Parameters:
        :   * **rate** (*double*) – The new sample rate.
            * **quality** (*int*) – Resampler performance vs quality choice (0=fastest, 3=slowest).

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    reverse()[#](#aud.Sound.reverse "Link to this definition")
    :   Plays a sound reversed.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        The sound has to have a finite length and has to be seekable.
        It’s recommended to use this only with factories with
        fast and accurate seeking, which is not true for encoded audio
        files, such ones should be buffered using [`cache()`](#aud.Sound.cache "aud.Sound.cache") before
        being played reversed.

        Warning

        If seeking is not accurate in the underlying sound
        you’ll likely hear skips/jumps/cracks.

    sum()[#](#aud.Sound.sum "Link to this definition")
    :   Sums the samples of a sound.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    threshold(*threshold=0*)[#](#aud.Sound.threshold "Link to this definition")
    :   Makes a threshold wave out of an audio wave by setting all samples
        with a amplitude >= threshold to 1, all <= -threshold to -1 and
        all between to 0.

        Parameters:
        :   **threshold** (*float*) – Threshold value over which an amplitude counts
            non-zero.

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

    volume(*volume*)[#](#aud.Sound.volume "Link to this definition")
    :   Changes the volume of a sound.

        Parameters:
        :   **volume** (*float*) – The new volume..

        Returns:
        :   The created [`Sound`](#aud.Sound "aud.Sound") object.

        Return type:
        :   [`Sound`](#aud.Sound "aud.Sound")

        Note

        Should be in the range [0, 1] to avoid clipping.

        Note

        This is a filter function, you might consider using
        [`Handle.volume`](#aud.Handle.volume "aud.Handle.volume") instead.

    write(*filename*, *rate*, *channels*, *format*, *container*, *codec*, *bitrate*, *buffersize*)[#](#aud.Sound.write "Link to this definition")
    :   Writes the sound to a file.

        Parameters:
        :   * **filename** (*string*) – The path to write to.
            * **rate** (*int*) – The sample rate to write with.
            * **channels** (*int*) – The number of channels to write with.
            * **format** (*int*) – The sample format to write with.
            * **container** (*int*) – The container format for the file.
            * **codec** (*int*) – The codec to use in the file.
            * **bitrate** (*int*) – The bitrate to write with.
            * **buffersize** (*int*) – The size of the writing buffer.

    length[#](#aud.Sound.length "Link to this definition")
    :   The sample specification of the sound as a tuple with rate and channel count.

    specs[#](#aud.Sound.specs "Link to this definition")
    :   The sample specification of the sound as a tuple with rate and channel count.

*class* aud.Source[#](#aud.Source "Link to this definition")
:   The source object represents the source position of a binaural sound.

    azimuth[#](#aud.Source.azimuth "Link to this definition")
    :   The azimuth angle.

    distance[#](#aud.Source.distance "Link to this definition")
    :   The distance value. 0 is min, 1 is max.

    elevation[#](#aud.Source.elevation "Link to this definition")
    :   The elevation angle.

*class* aud.ThreadPool[#](#aud.ThreadPool "Link to this definition")
:   A ThreadPool is used to parallelize convolution efficiently.

*class* aud.error[#](#aud.error "Link to this definition")

[Next

OpenGL Wrapper (bgl)](../bgl/index.md)
[Previous

Property Definitions (bpy.props)](../bpy/props/index.md)

Copyright © Blender Authors

Made with
[Furo](https://github.com/pradyunsg/furo)

* [Report issue
  on this page](https://projects.blender.org/blender/blender/issues/new?template=.gitea/issue_template/api_docs.yaml&field:body=%2A%2APage+Information%2A%2A%0D%0AFile%3A+%60aud.rst%60%0D%0ABlender+Version%3A+%604.2%60%0D%0A%5BPermanent+Link%5D%28https%3A%2F%2Fdocs.blender.org%2Fapi%2F4.2%2Faud.html%29%0D%0A%0D%0A%2A%2AShort+description+of+error%2A%2A%0D%0A%5BPlease+fill+out+a+short+description+of+the+error+here%5D%0D%0A)

On this page

* Audio System (aud)
  + [Basic Sound Playback](#basic-sound-playback)
    - [`AP_LOCATION`](#aud.AP_LOCATION)
    - [`AP_ORIENTATION`](#aud.AP_ORIENTATION)
    - [`AP_PANNING`](#aud.AP_PANNING)
    - [`AP_PITCH`](#aud.AP_PITCH)
    - [`AP_VOLUME`](#aud.AP_VOLUME)
    - [`CHANNELS_INVALID`](#aud.CHANNELS_INVALID)
    - [`CHANNELS_MONO`](#aud.CHANNELS_MONO)
    - [`CHANNELS_STEREO`](#aud.CHANNELS_STEREO)
    - [`CHANNELS_STEREO_LFE`](#aud.CHANNELS_STEREO_LFE)
    - [`CHANNELS_SURROUND4`](#aud.CHANNELS_SURROUND4)
    - [`CHANNELS_SURROUND5`](#aud.CHANNELS_SURROUND5)
    - [`CHANNELS_SURROUND51`](#aud.CHANNELS_SURROUND51)
    - [`CHANNELS_SURROUND61`](#aud.CHANNELS_SURROUND61)
    - [`CHANNELS_SURROUND71`](#aud.CHANNELS_SURROUND71)
    - [`CODEC_AAC`](#aud.CODEC_AAC)
    - [`CODEC_AC3`](#aud.CODEC_AC3)
    - [`CODEC_FLAC`](#aud.CODEC_FLAC)
    - [`CODEC_INVALID`](#aud.CODEC_INVALID)
    - [`CODEC_MP2`](#aud.CODEC_MP2)
    - [`CODEC_MP3`](#aud.CODEC_MP3)
    - [`CODEC_OPUS`](#aud.CODEC_OPUS)
    - [`CODEC_PCM`](#aud.CODEC_PCM)
    - [`CODEC_VORBIS`](#aud.CODEC_VORBIS)
    - [`CONTAINER_AC3`](#aud.CONTAINER_AC3)
    - [`CONTAINER_FLAC`](#aud.CONTAINER_FLAC)
    - [`CONTAINER_INVALID`](#aud.CONTAINER_INVALID)
    - [`CONTAINER_MATROSKA`](#aud.CONTAINER_MATROSKA)
    - [`CONTAINER_MP2`](#aud.CONTAINER_MP2)
    - [`CONTAINER_MP3`](#aud.CONTAINER_MP3)
    - [`CONTAINER_OGG`](#aud.CONTAINER_OGG)
    - [`CONTAINER_WAV`](#aud.CONTAINER_WAV)
    - [`DISTANCE_MODEL_EXPONENT`](#aud.DISTANCE_MODEL_EXPONENT)
    - [`DISTANCE_MODEL_EXPONENT_CLAMPED`](#aud.DISTANCE_MODEL_EXPONENT_CLAMPED)
    - [`DISTANCE_MODEL_INVALID`](#aud.DISTANCE_MODEL_INVALID)
    - [`DISTANCE_MODEL_INVERSE`](#aud.DISTANCE_MODEL_INVERSE)
    - [`DISTANCE_MODEL_INVERSE_CLAMPED`](#aud.DISTANCE_MODEL_INVERSE_CLAMPED)
    - [`DISTANCE_MODEL_LINEAR`](#aud.DISTANCE_MODEL_LINEAR)
    - [`DISTANCE_MODEL_LINEAR_CLAMPED`](#aud.DISTANCE_MODEL_LINEAR_CLAMPED)
    - [`FORMAT_FLOAT32`](#aud.FORMAT_FLOAT32)
    - [`FORMAT_FLOAT64`](#aud.FORMAT_FLOAT64)
    - [`FORMAT_INVALID`](#aud.FORMAT_INVALID)
    - [`FORMAT_S16`](#aud.FORMAT_S16)
    - [`FORMAT_S24`](#aud.FORMAT_S24)
    - [`FORMAT_S32`](#aud.FORMAT_S32)
    - [`FORMAT_U8`](#aud.FORMAT_U8)
    - [`RATE_11025`](#aud.RATE_11025)
    - [`RATE_16000`](#aud.RATE_16000)
    - [`RATE_192000`](#aud.RATE_192000)
    - [`RATE_22050`](#aud.RATE_22050)
    - [`RATE_32000`](#aud.RATE_32000)
    - [`RATE_44100`](#aud.RATE_44100)
    - [`RATE_48000`](#aud.RATE_48000)
    - [`RATE_8000`](#aud.RATE_8000)
    - [`RATE_88200`](#aud.RATE_88200)
    - [`RATE_96000`](#aud.RATE_96000)
    - [`RATE_INVALID`](#aud.RATE_INVALID)
    - [`STATUS_INVALID`](#aud.STATUS_INVALID)
    - [`STATUS_PAUSED`](#aud.STATUS_PAUSED)
    - [`STATUS_PLAYING`](#aud.STATUS_PLAYING)
    - [`STATUS_STOPPED`](#aud.STATUS_STOPPED)
    - [`Device`](#aud.Device)
      * [`Device.lock()`](#aud.Device.lock)
      * [`Device.play()`](#aud.Device.play)
      * [`Device.stopAll()`](#aud.Device.stopAll)
      * [`Device.unlock()`](#aud.Device.unlock)
      * [`Device.channels`](#aud.Device.channels)
      * [`Device.distance_model`](#aud.Device.distance_model)
      * [`Device.doppler_factor`](#aud.Device.doppler_factor)
      * [`Device.format`](#aud.Device.format)
      * [`Device.listener_location`](#aud.Device.listener_location)
      * [`Device.listener_orientation`](#aud.Device.listener_orientation)
      * [`Device.listener_velocity`](#aud.Device.listener_velocity)
      * [`Device.rate`](#aud.Device.rate)
      * [`Device.speed_of_sound`](#aud.Device.speed_of_sound)
      * [`Device.volume`](#aud.Device.volume)
    - [`DynamicMusic`](#aud.DynamicMusic)
      * [`DynamicMusic.addScene()`](#aud.DynamicMusic.addScene)
      * [`DynamicMusic.addTransition()`](#aud.DynamicMusic.addTransition)
      * [`DynamicMusic.pause()`](#aud.DynamicMusic.pause)
      * [`DynamicMusic.resume()`](#aud.DynamicMusic.resume)
      * [`DynamicMusic.stop()`](#aud.DynamicMusic.stop)
      * [`DynamicMusic.fadeTime`](#aud.DynamicMusic.fadeTime)
      * [`DynamicMusic.position`](#aud.DynamicMusic.position)
      * [`DynamicMusic.scene`](#aud.DynamicMusic.scene)
      * [`DynamicMusic.status`](#aud.DynamicMusic.status)
      * [`DynamicMusic.volume`](#aud.DynamicMusic.volume)
    - [`HRTF`](#aud.HRTF)
      * [`HRTF.loadLeftHrtfSet()`](#aud.HRTF.loadLeftHrtfSet)
      * [`HRTF.loadLeftHrtfSet()`](#id0)
      * [`HRTF.addImpulseResponseFromSound()`](#aud.HRTF.addImpulseResponseFromSound)
    - [`Handle`](#aud.Handle)
      * [`Handle.pause()`](#aud.Handle.pause)
      * [`Handle.resume()`](#aud.Handle.resume)
      * [`Handle.stop()`](#aud.Handle.stop)
      * [`Handle.attenuation`](#aud.Handle.attenuation)
      * [`Handle.cone_angle_inner`](#aud.Handle.cone_angle_inner)
      * [`Handle.cone_angle_outer`](#aud.Handle.cone_angle_outer)
      * [`Handle.cone_volume_outer`](#aud.Handle.cone_volume_outer)
      * [`Handle.distance_maximum`](#aud.Handle.distance_maximum)
      * [`Handle.distance_reference`](#aud.Handle.distance_reference)
      * [`Handle.keep`](#aud.Handle.keep)
      * [`Handle.location`](#aud.Handle.location)
      * [`Handle.loop_count`](#aud.Handle.loop_count)
      * [`Handle.orientation`](#aud.Handle.orientation)
      * [`Handle.pitch`](#aud.Handle.pitch)
      * [`Handle.position`](#aud.Handle.position)
      * [`Handle.relative`](#aud.Handle.relative)
      * [`Handle.status`](#aud.Handle.status)
      * [`Handle.velocity`](#aud.Handle.velocity)
      * [`Handle.volume`](#aud.Handle.volume)
      * [`Handle.volume_maximum`](#aud.Handle.volume_maximum)
      * [`Handle.volume_minimum`](#aud.Handle.volume_minimum)
    - [`ImpulseResponse`](#aud.ImpulseResponse)
    - [`PlaybackManager`](#aud.PlaybackManager)
      * [`PlaybackManager.addCategory()`](#aud.PlaybackManager.addCategory)
      * [`PlaybackManager.clean()`](#aud.PlaybackManager.clean)
      * [`PlaybackManager.getVolume()`](#aud.PlaybackManager.getVolume)
      * [`PlaybackManager.pause()`](#aud.PlaybackManager.pause)
      * [`PlaybackManager.play()`](#aud.PlaybackManager.play)
      * [`PlaybackManager.resume()`](#aud.PlaybackManager.resume)
      * [`PlaybackManager.setVolume()`](#aud.PlaybackManager.setVolume)
      * [`PlaybackManager.stop()`](#aud.PlaybackManager.stop)
    - [`Sequence`](#aud.Sequence)
      * [`Sequence.add()`](#aud.Sequence.add)
      * [`Sequence.remove()`](#aud.Sequence.remove)
      * [`Sequence.setAnimationData()`](#aud.Sequence.setAnimationData)
      * [`Sequence.channels`](#aud.Sequence.channels)
      * [`Sequence.distance_model`](#aud.Sequence.distance_model)
      * [`Sequence.doppler_factor`](#aud.Sequence.doppler_factor)
      * [`Sequence.fps`](#aud.Sequence.fps)
      * [`Sequence.muted`](#aud.Sequence.muted)
      * [`Sequence.rate`](#aud.Sequence.rate)
      * [`Sequence.speed_of_sound`](#aud.Sequence.speed_of_sound)
    - [`SequenceEntry`](#aud.SequenceEntry)
      * [`SequenceEntry.move()`](#aud.SequenceEntry.move)
      * [`SequenceEntry.setAnimationData()`](#aud.SequenceEntry.setAnimationData)
      * [`SequenceEntry.attenuation`](#aud.SequenceEntry.attenuation)
      * [`SequenceEntry.cone_angle_inner`](#aud.SequenceEntry.cone_angle_inner)
      * [`SequenceEntry.cone_angle_outer`](#aud.SequenceEntry.cone_angle_outer)
      * [`SequenceEntry.cone_volume_outer`](#aud.SequenceEntry.cone_volume_outer)
      * [`SequenceEntry.distance_maximum`](#aud.SequenceEntry.distance_maximum)
      * [`SequenceEntry.distance_reference`](#aud.SequenceEntry.distance_reference)
      * [`SequenceEntry.muted`](#aud.SequenceEntry.muted)
      * [`SequenceEntry.relative`](#aud.SequenceEntry.relative)
      * [`SequenceEntry.sound`](#aud.SequenceEntry.sound)
      * [`SequenceEntry.volume_maximum`](#aud.SequenceEntry.volume_maximum)
      * [`SequenceEntry.volume_minimum`](#aud.SequenceEntry.volume_minimum)
    - [`Sound`](#aud.Sound)
      * [`Sound.buffer()`](#aud.Sound.buffer)
      * [`Sound.file()`](#aud.Sound.file)
      * [`Sound.list()`](#aud.Sound.list)
      * [`Sound.sawtooth()`](#aud.Sound.sawtooth)
      * [`Sound.silence()`](#aud.Sound.silence)
      * [`Sound.sine()`](#aud.Sound.sine)
      * [`Sound.square()`](#aud.Sound.square)
      * [`Sound.triangle()`](#aud.Sound.triangle)
      * [`Sound.ADSR()`](#aud.Sound.ADSR)
      * [`Sound.accumulate()`](#aud.Sound.accumulate)
      * [`Sound.addSound()`](#aud.Sound.addSound)
      * [`Sound.binaural()`](#aud.Sound.binaural)
      * [`Sound.cache()`](#aud.Sound.cache)
      * [`Sound.convolver()`](#aud.Sound.convolver)
      * [`Sound.data()`](#aud.Sound.data)
      * [`Sound.delay()`](#aud.Sound.delay)
      * [`Sound.envelope()`](#aud.Sound.envelope)
      * [`Sound.fadein()`](#aud.Sound.fadein)
      * [`Sound.fadeout()`](#aud.Sound.fadeout)
      * [`Sound.filter()`](#aud.Sound.filter)
      * [`Sound.highpass()`](#aud.Sound.highpass)
      * [`Sound.join()`](#aud.Sound.join)
      * [`Sound.limit()`](#aud.Sound.limit)
      * [`Sound.loop()`](#aud.Sound.loop)
      * [`Sound.lowpass()`](#aud.Sound.lowpass)
      * [`Sound.mix()`](#aud.Sound.mix)
      * [`Sound.modulate()`](#aud.Sound.modulate)
      * [`Sound.mutable()`](#aud.Sound.mutable)
      * [`Sound.pingpong()`](#aud.Sound.pingpong)
      * [`Sound.pitch()`](#aud.Sound.pitch)
      * [`Sound.rechannel()`](#aud.Sound.rechannel)
      * [`Sound.resample()`](#aud.Sound.resample)
      * [`Sound.reverse()`](#aud.Sound.reverse)
      * [`Sound.sum()`](#aud.Sound.sum)
      * [`Sound.threshold()`](#aud.Sound.threshold)
      * [`Sound.volume()`](#aud.Sound.volume)
      * [`Sound.write()`](#aud.Sound.write)
      * [`Sound.length`](#aud.Sound.length)
      * [`Sound.specs`](#aud.Sound.specs)
    - [`Source`](#aud.Source)
      * [`Source.azimuth`](#aud.Source.azimuth)
      * [`Source.distance`](#aud.Source.distance)
      * [`Source.elevation`](#aud.Source.elevation)
    - [`ThreadPool`](#aud.ThreadPool)
    - [`error`](#aud.error)