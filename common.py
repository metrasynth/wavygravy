import numpy as np


def midi_to_hz(note):
    return 440.0 * (2 ** ((note - 69) / 12.0))


def samples_per_cycle(hz, sample_rate):
    return int(sample_rate / (hz / 2))


def normalize(audio):
    return audio / np.max(np.abs(audio))


def correct_dc_offset(audio):
    return audio - np.mean(audio)


def dump_param_details(synth):
    for k in sorted(synth.parameters):
        print(synth.parameters[k])


def dump_param_vars(synth):
    for k in sorted(synth.parameters):
        print(f"synth.{k} = {getattr(synth, k)!r}")
