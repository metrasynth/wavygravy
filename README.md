WAVy Gravy
==========

This is a collection of scripts for extracting single-cycle wavetables from synth plugins.

They leverage the [Pedalboard](https://spotify.github.io/pedalboard/) Python library
to load plugins and render audio.

Old way:
1. 🔌 Load a plugin into your favorite DAW.
2. 🎛️ Configure the plugin's parameters.
3. 🎵 Sequence a single note.
4. 💾 Render the audio to a WAV file.
5. 🔁 Repeat steps 2-4 at least 127 more times to get all the variations of a single parameter.
6. 🧑‍💻 Load a rendered WAV files in your favorite editor.
7. 😵‍💫 Manually select a single cycle to extract.
8. ✂️ Copy and paste the cycle into your wavetable.
9. 😩 Go to bed mentally exhausted because you've spent all day making a wavetable.

New way:
1. 🐍 Run a WAVy Gravy script.
2. 💾 Load the resulting wavetable into your favorite synth.
3. 😁 Crack on with making tunes!

Disclaimer
----------

WAVy Gravy helps with the drudgery of recording, extracting, and stitching together wavetables.

You will still need to spend some time figuring out which parameters to modulate,
and how to set up the initial patch to get a stable waveform.
You'll also need to experiment with which offset to use to get the best waveforms.

Installation
------------

1. Install [uv](https://docs.astral.sh/uv/), a package manager for Python.

2. Download and unzip this repository (or clone it using `git` if you prefer 🤓).

Running scripts
---------------

From a command prompt / terminal:

```bash
uv run script_name.py
```

Now you should have some wavetables in the `output` directory!

Note: Depending on your OS and how you have plugins installed,
you may need to edit the script to point to the correct plugin location.

Writing new scripts
-------------------

1. Copy an existing script as a starting point.
2. Edit the new script to your liking.
3. Run the script.
4. Try out the new wavetable(s).

Some ideas of how to change scripts:

- Load a different plugin. (VST3 or AU)
- Mutate a different parameter.
- Mutate multiple parameters at once.
- Mutate over a different range of values for a parameter.
- Change the note. (Many synths will render different waveforms depending on the note.)
- Change the offset. (Some synths will render slightly different cycles even when there's no modulating parameters.)

How to find the location of plugins
-----------------------------------

Do this first, or whenever you add another plugin. It'll take a few moments:

```bash
uv run plugin_scan.py
```

List the plugins that were found, and their default parameters:

```bash
uv run plugin_list.py | less
```

These tools depend on [Pedalboard Pluginary](https://pypi.org/project/pedalboard-pluginary/) and may not be perfect.
The WAVy Gravy project may try to fix some of the bugs over time.
