from pathlib import Path

import numpy as np
from mido import Message
from pedalboard import load_plugin
from pedalboard_native.io import AudioFile

from common import correct_dc_offset, dump_param_details, dump_param_vars, midi_to_hz, normalize, \
    samples_per_cycle


PLUGIN_PATH = Path("/Library/Audio/Plug-Ins/VST3/ReDominator1x.vst3")
OUTPUT_BASE_FILENAME = "redominator_pwm_saw"
OUTPUT_DIR = Path(__file__).parent / "output"
SAMPLE_RATE = 44100


def main():
    synth = load_plugin(str(PLUGIN_PATH))

    # Configure initial state
    synth.master_volume = 127
    synth.dco_pulse = "3(PWM)"
    synth.dco_saw = "3(PWM)"
    synth.dco_pwm = 32

    # Render some audio
    duration = 1  # second
    note = 60  # middle C
    midi_stream = [
        Message("note_on", note=note, velocity=127),
        Message("note_off", note=note, time=duration),
    ]
    audio = synth(midi_stream, duration=duration, sample_rate=SAMPLE_RATE)
    audio = audio[0]
    audio = correct_dc_offset(audio)
    audio = normalize(audio)
    filename = f"{OUTPUT_BASE_FILENAME}-note{note}-reference.wav"
    with AudioFile(str(OUTPUT_DIR / filename), "w", SAMPLE_RATE, num_channels=1, bit_depth=32) as o:
        o.write(audio)

    # Render wavetables using C base notes across four octaves
    base_note = 24  # C
    for octave in range(4):
        note = base_note + 12 * octave
        midi_stream = [
            Message("note_on", note=note, velocity=127),
            Message("note_off", note=note, time=duration),
        ]
        wavetable_frames = []
        samples_per_frame = samples_per_cycle(midi_to_hz(note), SAMPLE_RATE)
        for dco_pwm in range(0, 128):
            synth.dco_pwm = dco_pwm
            audio = synth(midi_stream, duration=duration, sample_rate=SAMPLE_RATE)
            audio = audio[0]

            offset = samples_per_frame + 100  # skip initial ramp from 0
            single_cycle = audio[offset:offset + samples_per_frame]
            single_cycle = correct_dc_offset(single_cycle)
            single_cycle = normalize(single_cycle)

            wavetable_frames.append(single_cycle)
        wavetable = np.concatenate(wavetable_frames)
        filename = f"{OUTPUT_BASE_FILENAME}-note{note}-spf{samples_per_frame}.wav"
        with AudioFile(str(OUTPUT_DIR / filename), "w", SAMPLE_RATE, num_channels=1, bit_depth=32) as o:
            o.write(wavetable)

    dump_param_details(synth)
    dump_param_vars(synth)


if __name__ == "__main__":
    main()
