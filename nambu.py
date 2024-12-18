# WORK IN PROGRESS

from pathlib import Path

import numpy as np
from mido import Message
from pedalboard import load_plugin
from pedalboard_native.io import AudioFile

from common import (
    correct_dc_offset,
    dump_param_details,
    dump_param_vars,
    midi_to_hz,
    normalize,
    samples_per_cycle,
)


PLUGIN_PATH = Path("/Applications/Nambu.app/Wrapper/Nambu.app/PlugIns/Plugin.appex")
OUTPUT_BASE_FILENAME = "nambu"
OUTPUT_DIR = Path(__file__).parent / "output"
SAMPLE_RATE = 44100


def main():
    synth = load_plugin(str(PLUGIN_PATH))

    # Configure initial state
    synth.arpeggiator = 0.0
    synth.effects_chorus_depth = 0.5
    synth.effects_chorus_feedback = 0.0
    synth.effects_chorus_mix = 0.501157
    synth.effects_chorus_on_off = 1.0
    synth.effects_chorus_rate = 0.5
    synth.effects_chorus_spread = 0.5
    synth.effects_chorus_time = 0.5
    synth.effects_comp_attacktime = 0.153384
    synth.effects_comp_makeupgain = 0.5
    synth.effects_comp_on_off = 1.0
    synth.effects_comp_ratio = 0.487884
    synth.effects_comp_releasetime = 0.25
    synth.effects_comp_threshold = 0.645036
    synth.effects_delay_feedback = 0.767439
    synth.effects_delay_filter_cutoff = 0.5
    synth.effects_delay_filter_drive = 0.0
    synth.effects_delay_filter_mix = 0.0
    synth.effects_delay_filter_modulation_depth = 0.0
    synth.effects_delay_filter_modulation_rate = 0.5
    synth.effects_delay_filter_modulation_temposync = 0.0
    synth.effects_delay_filter_resonance = 0.0
    synth.effects_delay_hidamp = 0.237455
    synth.effects_delay_hpf = 0.311962
    synth.effects_delay_mix = 0.264617
    synth.effects_delay_modulation_depth = 0.253423
    synth.effects_delay_modulation_rate = 0.569733
    synth.effects_delay_modulation_temposync = 0.0
    synth.effects_delay_on_off = 1.0
    synth.effects_delay_timel = 0.5
    synth.effects_delay_timemode = 0.0
    synth.effects_delay_timer = 0.5
    synth.effects_eq_eq_bass = 0.5
    synth.effects_eq_eq_mid_freq = 0.5
    synth.effects_eq_eq_mid_gain = 0.5
    synth.effects_eq_eq_treble = 0.5
    synth.effects_eq_on_off = 0.0
    synth.effects_preamp_eq_comp = 1.0
    synth.effects_preamp_gain = 0.5
    synth.effects_reverb_er_tail = 0.200763
    synth.effects_reverb_hidamp = 0.283533
    synth.effects_reverb_hpf = 0.30355
    synth.effects_reverb_lpf = 0.719116
    synth.effects_reverb_mix = 0.433076
    synth.effects_reverb_on_off = 1.0
    synth.effects_reverb_predelay = 0.194536
    synth.effects_reverb_size = 0.455036
    synth.effects_reverb_time = 0.509085
    synth.effects_saturator_bias = 0.5
    synth.effects_saturator_gain = 0.5
    synth.effects_saturator_level = 0.5
    synth.effects_saturator_on_off = 0.0
    synth.keyboard_hold = 0.0
    synth.master_transpose = 0.503937
    synth.master_tune = 0.5
    synth.master_volume = 0.75
    synth.matrix_op1_op2 = 0.0
    synth.matrix_op1_op3 = 0.0
    synth.matrix_op1_op4 = 0.0
    synth.matrix_op1_op5 = 0.0
    synth.matrix_op1_op6 = 0.0
    synth.matrix_op1_out = 0.707031
    synth.matrix_op2_op3 = 0.36472
    synth.matrix_op2_op4 = 0.001835
    synth.matrix_op2_op5 = 0.0
    synth.matrix_op2_op6 = 0.0
    synth.matrix_op2_out = 0.0
    synth.matrix_op3_op4 = 0.0
    synth.matrix_op3_op5 = 0.0
    synth.matrix_op3_op6 = 0.0
    synth.matrix_op3_out = 0.495448
    synth.matrix_op4_op5 = 0.0
    synth.matrix_op4_op6 = 0.545015
    synth.matrix_op4_out = 0.0
    synth.matrix_op5_op6 = 0.895514
    synth.matrix_op5_out = 0.0
    synth.matrix_op6_out = 0.387271
    synth.maximum_polyphony = 0.0629921
    synth.modulators_env1_attack1_level = 1.0
    synth.modulators_env1_attack1_time = 0.0
    synth.modulators_env1_attack2_level = 1.0
    synth.modulators_env1_attack2_time = 0.0
    synth.modulators_env1_curvescale = 0.5
    synth.modulators_env1_decay_time = 0.5
    synth.modulators_env1_level = 0.5
    synth.modulators_env1_levelmod = 0.5
    synth.modulators_env1_release1_level = 0.5
    synth.modulators_env1_release1_time = 0.5
    synth.modulators_env1_release2_time = 0.0
    synth.modulators_env1_sustain_level = 0.5
    synth.modulators_env1_type = 0.0
    synth.modulators_env2_attack1_level = 1.0
    synth.modulators_env2_attack1_time = 0.0
    synth.modulators_env2_attack2_level = 1.0
    synth.modulators_env2_attack2_time = 0.0
    synth.modulators_env2_curvescale = 0.5
    synth.modulators_env2_decay_time = 0.5
    synth.modulators_env2_level = 0.5
    synth.modulators_env2_levelmod = 0.5
    synth.modulators_env2_release1_level = 0.5
    synth.modulators_env2_release1_time = 0.5
    synth.modulators_env2_release2_time = 0.0
    synth.modulators_env2_sustain_level = 0.5
    synth.modulators_env2_type = 0.0
    synth.modulators_env3_attack1_level = 1.0
    synth.modulators_env3_attack1_time = 0.0
    synth.modulators_env3_attack2_level = 1.0
    synth.modulators_env3_attack2_time = 0.0
    synth.modulators_env3_curvescale = 0.5
    synth.modulators_env3_decay_time = 0.5
    synth.modulators_env3_level = 0.5
    synth.modulators_env3_levelmod = 0.5
    synth.modulators_env3_release1_level = 0.5
    synth.modulators_env3_release1_time = 0.5
    synth.modulators_env3_release2_time = 0.0
    synth.modulators_env3_sustain_level = 0.5
    synth.modulators_env3_type = 0.0
    synth.modulators_keyboard1_level = 0.5
    synth.modulators_keyboard1_transformer_high_y = 1.0
    synth.modulators_keyboard1_transformer_low_y = 0.0
    synth.modulators_keyboard1_transformer_mid_h = 0.5
    synth.modulators_keyboard1_transformer_mid_w = 0.0
    synth.modulators_keyboard1_transformer_mid_x = 0.5
    synth.modulators_keyboard1_transformer_mid_y = 0.5
    synth.modulators_keyboard2_level = 0.5
    synth.modulators_keyboard2_transformer_high_y = 1.0
    synth.modulators_keyboard2_transformer_low_y = 0.0
    synth.modulators_keyboard2_transformer_mid_h = 0.5
    synth.modulators_keyboard2_transformer_mid_w = 0.0
    synth.modulators_keyboard2_transformer_mid_x = 0.5
    synth.modulators_keyboard2_transformer_mid_y = 0.5
    synth.modulators_lfo1_level = 0.5
    synth.modulators_lfo1_levelfallrise = 0.5
    synth.modulators_lfo1_levelmod = 0.5
    synth.modulators_lfo1_monopole = 0.0
    synth.modulators_lfo1_phaseshift = 0.5
    synth.modulators_lfo1_phasesync = 0.00787402
    synth.modulators_lfo1_range = 0.0
    synth.modulators_lfo1_rate = 0.5
    synth.modulators_lfo1_rateenvdepth = 0.5
    synth.modulators_lfo1_rateenvtime = 0.5
    synth.modulators_lfo1_waveform = 0.5
    synth.modulators_lfo1_wavetype = 0.0
    synth.modulators_lfo2_level = 0.5
    synth.modulators_lfo2_levelfallrise = 0.5
    synth.modulators_lfo2_levelmod = 0.5
    synth.modulators_lfo2_monopole = 0.0
    synth.modulators_lfo2_phaseshift = 0.5
    synth.modulators_lfo2_phasesync = 0.00787402
    synth.modulators_lfo2_range = 0.023622
    synth.modulators_lfo2_rate = 0.375
    synth.modulators_lfo2_rateenvdepth = 0.5
    synth.modulators_lfo2_rateenvtime = 0.5
    synth.modulators_lfo2_waveform = 0.5
    synth.modulators_lfo2_wavetype = 0.0
    synth.modulators_lfo3_level = 0.5
    synth.modulators_lfo3_levelfallrise = 0.5
    synth.modulators_lfo3_levelmod = 0.5
    synth.modulators_lfo3_monopole = 0.0
    synth.modulators_lfo3_phaseshift = 0.5
    synth.modulators_lfo3_phasesync = 0.00787402
    synth.modulators_lfo3_range = 0.0
    synth.modulators_lfo3_rate = 0.5
    synth.modulators_lfo3_rateenvdepth = 0.5
    synth.modulators_lfo3_rateenvtime = 0.5
    synth.modulators_lfo3_waveform = 0.5
    synth.modulators_lfo3_wavetype = 0.0
    synth.modulators_lfo4_level = 0.5
    synth.modulators_lfo4_levelfallrise = 0.5
    synth.modulators_lfo4_levelmod = 0.5
    synth.modulators_lfo4_monopole = 0.0
    synth.modulators_lfo4_phaseshift = 0.5
    synth.modulators_lfo4_phasesync = 0.00787402
    synth.modulators_lfo4_range = 0.0
    synth.modulators_lfo4_rate = 0.5
    synth.modulators_lfo4_rateenvdepth = 0.5
    synth.modulators_lfo4_rateenvtime = 0.5
    synth.modulators_lfo4_waveform = 0.5
    synth.modulators_lfo4_wavetype = 0.0
    synth.modulators_macro1_level = 0.5
    synth.modulators_macro1_transformer_high_y = 1.0
    synth.modulators_macro1_transformer_low_y = 0.0
    synth.modulators_macro1_transformer_mid_h = 0.5
    synth.modulators_macro1_transformer_mid_w = 0.0
    synth.modulators_macro1_transformer_mid_x = 0.5
    synth.modulators_macro1_transformer_mid_y = 0.5
    synth.modulators_macro1_value = 0.5
    synth.modulators_macro2_level = 0.5
    synth.modulators_macro2_transformer_high_y = 1.0
    synth.modulators_macro2_transformer_low_y = 0.0
    synth.modulators_macro2_transformer_mid_h = 0.5
    synth.modulators_macro2_transformer_mid_w = 0.0
    synth.modulators_macro2_transformer_mid_x = 0.5
    synth.modulators_macro2_transformer_mid_y = 0.5
    synth.modulators_macro2_value = 0.5
    synth.modulators_seq1_envelope = 0.75
    synth.modulators_seq1_gatetime = 1.0
    synth.modulators_seq1_level = 0.5
    synth.modulators_seq1_levelmod = 0.5
    synth.modulators_seq1_rate = 0.0
    synth.modulators_seq1_smoothing = 0.0
    synth.modulators_seq1_steplength = 0.11811
    synth.modulators_seq2_envelope = 0.75
    synth.modulators_seq2_gatetime = 1.0
    synth.modulators_seq2_level = 0.5
    synth.modulators_seq2_levelmod = 0.5
    synth.modulators_seq2_rate = 0.0
    synth.modulators_seq2_smoothing = 0.0
    synth.modulators_seq2_steplength = 0.11811
    synth.modulators_velocity1_level = 0.5
    synth.modulators_velocity1_transformer_high_y = 1.0
    synth.modulators_velocity1_transformer_low_y = 0.0
    synth.modulators_velocity1_transformer_mid_h = 0.5
    synth.modulators_velocity1_transformer_mid_w = 0.0
    synth.modulators_velocity1_transformer_mid_x = 0.5
    synth.modulators_velocity1_transformer_mid_y = 0.5
    synth.modulators_velocity2_level = 0.5
    synth.modulators_velocity2_transformer_high_y = 1.0
    synth.modulators_velocity2_transformer_low_y = 0.0
    synth.modulators_velocity2_transformer_mid_h = 0.5
    synth.modulators_velocity2_transformer_mid_w = 0.0
    synth.modulators_velocity2_transformer_mid_x = 0.5
    synth.modulators_velocity2_transformer_mid_y = 0.5
    synth.monomode = 0.0
    synth.octave = 0.503937
    synth.op1_enable = 1.0
    synth.op1_env_attack1_level = 1.0
    synth.op1_env_attack1_time = 0.361692
    synth.op1_env_attack2_level = 1.0
    synth.op1_env_attack2_time = 0.0
    synth.op1_env_curvescale = 0.632217
    synth.op1_env_decay_time = 0.373289
    synth.op1_env_group = 0.0
    synth.op1_env_release1_level = 0.0
    synth.op1_env_release1_time = 0.447757
    synth.op1_env_release2_time = 0.0
    synth.op1_env_sustain_level = 0.659432
    synth.op1_filter_drive = 0.0
    synth.op1_filter_frequency_course = 1.0
    synth.op1_filter_frequency_env1 = 0.5
    synth.op1_filter_frequency_env2 = 0.5
    synth.op1_filter_frequency_env2_a = 0.0
    synth.op1_filter_frequency_env2_d = 0.5
    synth.op1_filter_frequency_fine = 0.5
    synth.op1_filter_frequency_keyboard = 0.5
    synth.op1_filter_frequency_lfo = 0.5
    synth.op1_filter_frequency_velocity = 0.5
    synth.op1_filter_resonance = 0.0
    synth.op1_filter_type = 0.0
    synth.op1_fm_bend = 0.5
    synth.op1_fm_feedback = 0.679011
    synth.op1_fm_invert = 0.0
    synth.op1_fm_pitch_coarse = 0.1
    synth.op1_fm_pitch_detunr = 0.5
    synth.op1_fm_pitch_env = 1.0
    synth.op1_fm_pitch_fine = 0.5
    synth.op1_fm_pitch_fixed = 0.0
    synth.op1_fm_pitch_vibrato = 1.0
    synth.op1_fm_wavetype = 0.00787402
    synth.op1_fm_width = 1.0
    synth.op1_inputlevel = 0.5
    synth.op1_lfo_depth = 0.0
    synth.op1_lfo_depthvelocity = 0.5
    synth.op1_lfo_randomlevel = 0.0
    synth.op1_lfo_randomtime = 0.0
    synth.op1_lfo_rate = 0.5
    synth.op1_lfo_ratetemposync = 0.0
    synth.op1_lfo_waveform = 0.5
    synth.op1_noise_impulse_decay = 1.0
    synth.op1_noise_impulse_density = 0.5
    synth.op1_noise_impulse_level = 0.0
    synth.op1_noise_impulse_rate = 0.5
    synth.op1_noise_noise_cutoff = 0.5
    synth.op1_noise_noise_digitalmix = 0.0
    synth.op1_noise_noise_digitalrate = 0.5
    synth.op1_noise_noise_fluctuationdepth = 0.0
    synth.op1_noise_noise_fluctuationspeed = 0.5
    synth.op1_noise_noise_level = 0.5
    synth.op1_noise_noise_resonance = 0.0
    synth.op1_osc_invert = 0.0
    synth.op1_osc_oscsyncfreq = 0.0
    synth.op1_osc_pitch_cent = 0.5
    synth.op1_osc_pitch_drift = 0.0
    synth.op1_osc_pitch_env = 1.0
    synth.op1_osc_pitch_octave = 0.503937
    synth.op1_osc_pitch_semitone = 0.5
    synth.op1_osc_pitch_vibrato = 1.0
    synth.op1_osc_shape = 0.0
    synth.op1_osc_wavetype = 0.0
    synth.op1_outputlevel = 0.5
    synth.op1_outputlevel_velocity = 0.793611
    synth.op1_resonator_color = 0.5
    synth.op1_resonator_fdbkfilter = 1.0
    synth.op1_resonator_fdbkfiltermode = 0.0
    synth.op1_resonator_fdbksaturator = 0.0
    synth.op1_resonator_feedback = 0.5
    synth.op1_resonator_pitch_cent = 0.5
    synth.op1_resonator_pitch_env = 1.0
    synth.op1_resonator_pitch_fixed = 0.0
    synth.op1_resonator_pitch_octave = 0.503937
    synth.op1_resonator_pitch_semitone = 0.5
    synth.op1_resonator_pitch_vibrato = 1.0
    synth.op1_resonator_prefilter = 0.5
    synth.op1_texture_delay = 0.0
    synth.op1_texture_pitch_cent = 0.5
    synth.op1_texture_pitch_env = 1.0
    synth.op1_texture_pitch_fixed = 0.0
    synth.op1_texture_pitch_octave = 0.503937
    synth.op1_texture_pitch_semitone = 0.5
    synth.op1_texture_pitch_vibrato = 1.0
    synth.op1_texture_rpeator = 0.0
    synth.op1_texture_start = 0.0
    synth.op1_texture_tempo = 0.0
    synth.op1_texture_texture = 0.0
    synth.op1_texture_trigger = 0.0
    synth.op1_type = 0.0
    synth.op2_enable = 1.0
    synth.op2_env_attack1_level = 1.0
    synth.op2_env_attack1_time = 0.172588
    synth.op2_env_attack2_level = 1.0
    synth.op2_env_attack2_time = 0.0
    synth.op2_env_curvescale = 0.639465
    synth.op2_env_decay_time = 0.753331
    synth.op2_env_group = 0.00787402
    synth.op2_env_release1_level = 0.0
    synth.op2_env_release1_time = 0.322972
    synth.op2_env_release2_time = 0.0
    synth.op2_env_sustain_level = 0.0
    synth.op2_filter_drive = 0.0
    synth.op2_filter_frequency_course = 1.0
    synth.op2_filter_frequency_env1 = 0.5
    synth.op2_filter_frequency_env2 = 0.5
    synth.op2_filter_frequency_env2_a = 0.0
    synth.op2_filter_frequency_env2_d = 0.5
    synth.op2_filter_frequency_fine = 0.5
    synth.op2_filter_frequency_keyboard = 0.5
    synth.op2_filter_frequency_lfo = 0.5
    synth.op2_filter_frequency_velocity = 0.5
    synth.op2_filter_resonance = 0.0
    synth.op2_filter_type = 0.0
    synth.op2_fm_bend = 0.5
    synth.op2_fm_feedback = 0.5
    synth.op2_fm_invert = 0.0
    synth.op2_fm_pitch_coarse = 0.3
    synth.op2_fm_pitch_detunr = 0.5
    synth.op2_fm_pitch_env = 1.0
    synth.op2_fm_pitch_fine = 0.749111
    synth.op2_fm_pitch_fixed = 0.0
    synth.op2_fm_pitch_vibrato = 1.0
    synth.op2_fm_wavetype = 0.0
    synth.op2_fm_width = 1.0
    synth.op2_inputlevel = 0.5
    synth.op2_lfo_depth = 0.0
    synth.op2_lfo_depthvelocity = 0.5
    synth.op2_lfo_randomlevel = 0.0
    synth.op2_lfo_randomtime = 0.0
    synth.op2_lfo_rate = 0.5
    synth.op2_lfo_ratetemposync = 0.0
    synth.op2_lfo_waveform = 0.5
    synth.op2_noise_impulse_decay = 1.0
    synth.op2_noise_impulse_density = 0.5
    synth.op2_noise_impulse_level = 0.0
    synth.op2_noise_impulse_rate = 0.5
    synth.op2_noise_noise_cutoff = 0.5
    synth.op2_noise_noise_digitalmix = 0.0
    synth.op2_noise_noise_digitalrate = 0.5
    synth.op2_noise_noise_fluctuationdepth = 0.0
    synth.op2_noise_noise_fluctuationspeed = 0.5
    synth.op2_noise_noise_level = 0.5
    synth.op2_noise_noise_resonance = 0.0
    synth.op2_osc_invert = 0.0
    synth.op2_osc_oscsyncfreq = 0.0
    synth.op2_osc_pitch_cent = 0.5
    synth.op2_osc_pitch_drift = 0.0
    synth.op2_osc_pitch_env = 1.0
    synth.op2_osc_pitch_octave = 0.503937
    synth.op2_osc_pitch_semitone = 0.5
    synth.op2_osc_pitch_vibrato = 1.0
    synth.op2_osc_shape = 0.0
    synth.op2_osc_wavetype = 0.0
    synth.op2_outputlevel = 0.257771
    synth.op2_outputlevel_velocity = 0.701858
    synth.op2_resonator_color = 0.5
    synth.op2_resonator_fdbkfilter = 1.0
    synth.op2_resonator_fdbkfiltermode = 0.0
    synth.op2_resonator_fdbksaturator = 0.0
    synth.op2_resonator_feedback = 0.5
    synth.op2_resonator_pitch_cent = 0.5
    synth.op2_resonator_pitch_env = 1.0
    synth.op2_resonator_pitch_fixed = 0.0
    synth.op2_resonator_pitch_octave = 0.503937
    synth.op2_resonator_pitch_semitone = 0.5
    synth.op2_resonator_pitch_vibrato = 1.0
    synth.op2_resonator_prefilter = 0.5
    synth.op2_texture_delay = 0.0
    synth.op2_texture_pitch_cent = 0.5
    synth.op2_texture_pitch_env = 1.0
    synth.op2_texture_pitch_fixed = 0.0
    synth.op2_texture_pitch_octave = 0.503937
    synth.op2_texture_pitch_semitone = 0.5
    synth.op2_texture_pitch_vibrato = 1.0
    synth.op2_texture_rpeator = 0.0
    synth.op2_texture_start = 0.0
    synth.op2_texture_tempo = 0.0
    synth.op2_texture_texture = 0.0
    synth.op2_texture_trigger = 0.0
    synth.op2_type = 0.0
    synth.op3_enable = 1.0
    synth.op3_env_attack1_level = 1.0
    synth.op3_env_attack1_time = 0.172588
    synth.op3_env_attack2_level = 1.0
    synth.op3_env_attack2_time = 0.0
    synth.op3_env_curvescale = 0.639465
    synth.op3_env_decay_time = 0.753331
    synth.op3_env_group = 0.00787402
    synth.op3_env_release1_level = 0.0
    synth.op3_env_release1_time = 0.322972
    synth.op3_env_release2_time = 0.0
    synth.op3_env_sustain_level = 0.0
    synth.op3_filter_drive = 0.0
    synth.op3_filter_frequency_course = 1.0
    synth.op3_filter_frequency_env1 = 0.5
    synth.op3_filter_frequency_env2 = 0.5
    synth.op3_filter_frequency_env2_a = 0.0
    synth.op3_filter_frequency_env2_d = 0.5
    synth.op3_filter_frequency_fine = 0.5
    synth.op3_filter_frequency_keyboard = 0.5
    synth.op3_filter_frequency_lfo = 0.5
    synth.op3_filter_frequency_velocity = 0.5
    synth.op3_filter_resonance = 0.0
    synth.op3_filter_type = 0.0
    synth.op3_fm_bend = 0.5
    synth.op3_fm_feedback = 0.5
    synth.op3_fm_invert = 0.0
    synth.op3_fm_pitch_coarse = 0.1
    synth.op3_fm_pitch_detunr = 0.5
    synth.op3_fm_pitch_env = 1.0
    synth.op3_fm_pitch_fine = 0.5
    synth.op3_fm_pitch_fixed = 0.0
    synth.op3_fm_pitch_vibrato = 1.0
    synth.op3_fm_wavetype = 0.0
    synth.op3_fm_width = 1.0
    synth.op3_inputlevel = 0.5
    synth.op3_lfo_depth = 0.0
    synth.op3_lfo_depthvelocity = 0.5
    synth.op3_lfo_randomlevel = 0.0
    synth.op3_lfo_randomtime = 0.0
    synth.op3_lfo_rate = 0.5
    synth.op3_lfo_ratetemposync = 0.0
    synth.op3_lfo_waveform = 0.5
    synth.op3_noise_impulse_decay = 1.0
    synth.op3_noise_impulse_density = 0.5
    synth.op3_noise_impulse_level = 0.0
    synth.op3_noise_impulse_rate = 0.5
    synth.op3_noise_noise_cutoff = 0.5
    synth.op3_noise_noise_digitalmix = 0.0
    synth.op3_noise_noise_digitalrate = 0.5
    synth.op3_noise_noise_fluctuationdepth = 0.0
    synth.op3_noise_noise_fluctuationspeed = 0.5
    synth.op3_noise_noise_level = 0.5
    synth.op3_noise_noise_resonance = 0.0
    synth.op3_osc_invert = 0.0
    synth.op3_osc_oscsyncfreq = 0.0
    synth.op3_osc_pitch_cent = 0.5
    synth.op3_osc_pitch_drift = 0.0
    synth.op3_osc_pitch_env = 1.0
    synth.op3_osc_pitch_octave = 0.503937
    synth.op3_osc_pitch_semitone = 0.5
    synth.op3_osc_pitch_vibrato = 1.0
    synth.op3_osc_shape = 0.0
    synth.op3_osc_wavetype = 0.0
    synth.op3_outputlevel = 0.5
    synth.op3_outputlevel_velocity = 0.789941
    synth.op3_resonator_color = 0.5
    synth.op3_resonator_fdbkfilter = 1.0
    synth.op3_resonator_fdbkfiltermode = 0.0
    synth.op3_resonator_fdbksaturator = 0.0
    synth.op3_resonator_feedback = 0.5
    synth.op3_resonator_pitch_cent = 0.5
    synth.op3_resonator_pitch_env = 1.0
    synth.op3_resonator_pitch_fixed = 0.0
    synth.op3_resonator_pitch_octave = 0.503937
    synth.op3_resonator_pitch_semitone = 0.5
    synth.op3_resonator_pitch_vibrato = 1.0
    synth.op3_resonator_prefilter = 0.5
    synth.op3_texture_delay = 0.0
    synth.op3_texture_pitch_cent = 0.5
    synth.op3_texture_pitch_env = 1.0
    synth.op3_texture_pitch_fixed = 0.0
    synth.op3_texture_pitch_octave = 0.503937
    synth.op3_texture_pitch_semitone = 0.5
    synth.op3_texture_pitch_vibrato = 1.0
    synth.op3_texture_rpeator = 0.0
    synth.op3_texture_start = 0.0
    synth.op3_texture_tempo = 0.0
    synth.op3_texture_texture = 0.0
    synth.op3_texture_trigger = 0.0
    synth.op3_type = 0.0
    synth.op4_enable = 1.0
    synth.op4_env_attack1_level = 1.0
    synth.op4_env_attack1_time = 0.086248
    synth.op4_env_attack2_level = 1.0
    synth.op4_env_attack2_time = 0.0
    synth.op4_env_curvescale = 0.659651
    synth.op4_env_decay_time = 0.554961
    synth.op4_env_group = 0.0
    synth.op4_env_release1_level = 0.0
    synth.op4_env_release1_time = 0.322972
    synth.op4_env_release2_time = 0.0
    synth.op4_env_sustain_level = 0.417937
    synth.op4_filter_drive = 0.0
    synth.op4_filter_frequency_course = 1.0
    synth.op4_filter_frequency_env1 = 0.5
    synth.op4_filter_frequency_env2 = 0.5
    synth.op4_filter_frequency_env2_a = 0.0
    synth.op4_filter_frequency_env2_d = 0.5
    synth.op4_filter_frequency_fine = 0.5
    synth.op4_filter_frequency_keyboard = 0.5
    synth.op4_filter_frequency_lfo = 0.5
    synth.op4_filter_frequency_velocity = 0.5
    synth.op4_filter_resonance = 0.0
    synth.op4_filter_type = 0.0
    synth.op4_fm_bend = 0.5
    synth.op4_fm_feedback = 0.5
    synth.op4_fm_invert = 0.0
    synth.op4_fm_pitch_coarse = 0.4
    synth.op4_fm_pitch_detunr = 0.5
    synth.op4_fm_pitch_env = 1.0
    synth.op4_fm_pitch_fine = 0.747551
    synth.op4_fm_pitch_fixed = 0.0
    synth.op4_fm_pitch_vibrato = 1.0
    synth.op4_fm_wavetype = 0.0
    synth.op4_fm_width = 1.0
    synth.op4_inputlevel = 0.5
    synth.op4_lfo_depth = 0.0
    synth.op4_lfo_depthvelocity = 0.5
    synth.op4_lfo_randomlevel = 0.0
    synth.op4_lfo_randomtime = 0.0
    synth.op4_lfo_rate = 0.5
    synth.op4_lfo_ratetemposync = 0.0
    synth.op4_lfo_waveform = 0.5
    synth.op4_noise_impulse_decay = 1.0
    synth.op4_noise_impulse_density = 0.5
    synth.op4_noise_impulse_level = 0.0
    synth.op4_noise_impulse_rate = 0.5
    synth.op4_noise_noise_cutoff = 0.5
    synth.op4_noise_noise_digitalmix = 0.0
    synth.op4_noise_noise_digitalrate = 0.5
    synth.op4_noise_noise_fluctuationdepth = 0.0
    synth.op4_noise_noise_fluctuationspeed = 0.5
    synth.op4_noise_noise_level = 0.5
    synth.op4_noise_noise_resonance = 0.0
    synth.op4_osc_invert = 0.0
    synth.op4_osc_oscsyncfreq = 0.0
    synth.op4_osc_pitch_cent = 0.5
    synth.op4_osc_pitch_drift = 0.0
    synth.op4_osc_pitch_env = 1.0
    synth.op4_osc_pitch_octave = 0.503937
    synth.op4_osc_pitch_semitone = 0.5
    synth.op4_osc_pitch_vibrato = 1.0
    synth.op4_osc_shape = 0.0
    synth.op4_osc_wavetype = 0.0
    synth.op4_outputlevel = 0.5
    synth.op4_outputlevel_velocity = 0.5
    synth.op4_resonator_color = 0.5
    synth.op4_resonator_fdbkfilter = 1.0
    synth.op4_resonator_fdbkfiltermode = 0.0
    synth.op4_resonator_fdbksaturator = 0.0
    synth.op4_resonator_feedback = 0.5
    synth.op4_resonator_pitch_cent = 0.5
    synth.op4_resonator_pitch_env = 1.0
    synth.op4_resonator_pitch_fixed = 0.0
    synth.op4_resonator_pitch_octave = 0.503937
    synth.op4_resonator_pitch_semitone = 0.5
    synth.op4_resonator_pitch_vibrato = 1.0
    synth.op4_resonator_prefilter = 0.5
    synth.op4_texture_delay = 0.31554
    synth.op4_texture_pitch_cent = 0.5
    synth.op4_texture_pitch_env = 1.0
    synth.op4_texture_pitch_fixed = 0.0
    synth.op4_texture_pitch_octave = 0.503937
    synth.op4_texture_pitch_semitone = 0.5
    synth.op4_texture_pitch_vibrato = 1.0
    synth.op4_texture_rpeator = 0.583333
    synth.op4_texture_start = 0.0
    synth.op4_texture_tempo = 1.0
    synth.op4_texture_texture = 0.598425
    synth.op4_texture_trigger = 0.0
    synth.op4_type = 0.023622
    synth.op5_enable = 1.0
    synth.op5_env_attack1_level = 1.0
    synth.op5_env_attack1_time = 0.0
    synth.op5_env_attack2_level = 1.0
    synth.op5_env_attack2_time = 0.0
    synth.op5_env_curvescale = 0.672588
    synth.op5_env_decay_time = 0.753331
    synth.op5_env_group = 0.0
    synth.op5_env_release1_level = 0.0
    synth.op5_env_release1_time = 0.322972
    synth.op5_env_release2_time = 0.0
    synth.op5_env_sustain_level = 0.0
    synth.op5_filter_drive = 0.0
    synth.op5_filter_frequency_course = 1.0
    synth.op5_filter_frequency_env1 = 0.5
    synth.op5_filter_frequency_env2 = 0.5
    synth.op5_filter_frequency_env2_a = 0.0
    synth.op5_filter_frequency_env2_d = 0.5
    synth.op5_filter_frequency_fine = 0.5
    synth.op5_filter_frequency_keyboard = 0.5
    synth.op5_filter_frequency_lfo = 0.5
    synth.op5_filter_frequency_velocity = 0.5
    synth.op5_filter_resonance = 0.0
    synth.op5_filter_type = 0.0
    synth.op5_fm_bend = 0.5
    synth.op5_fm_feedback = 0.5
    synth.op5_fm_invert = 0.0
    synth.op5_fm_pitch_coarse = 0.4
    synth.op5_fm_pitch_detunr = 0.5
    synth.op5_fm_pitch_env = 1.0
    synth.op5_fm_pitch_fine = 0.5
    synth.op5_fm_pitch_fixed = 0.0
    synth.op5_fm_pitch_vibrato = 1.0
    synth.op5_fm_wavetype = 0.0
    synth.op5_fm_width = 1.0
    synth.op5_inputlevel = 0.5
    synth.op5_lfo_depth = 0.0
    synth.op5_lfo_depthvelocity = 0.5
    synth.op5_lfo_randomlevel = 0.0
    synth.op5_lfo_randomtime = 0.0
    synth.op5_lfo_rate = 0.5
    synth.op5_lfo_ratetemposync = 0.0
    synth.op5_lfo_waveform = 0.5
    synth.op5_noise_impulse_decay = 1.0
    synth.op5_noise_impulse_density = 0.5
    synth.op5_noise_impulse_level = 0.0
    synth.op5_noise_impulse_rate = 0.5
    synth.op5_noise_noise_cutoff = 0.5
    synth.op5_noise_noise_digitalmix = 0.0
    synth.op5_noise_noise_digitalrate = 0.5
    synth.op5_noise_noise_fluctuationdepth = 0.0
    synth.op5_noise_noise_fluctuationspeed = 0.5
    synth.op5_noise_noise_level = 0.5
    synth.op5_noise_noise_resonance = 0.0
    synth.op5_osc_invert = 0.0
    synth.op5_osc_oscsyncfreq = 0.0
    synth.op5_osc_pitch_cent = 0.5
    synth.op5_osc_pitch_drift = 0.0
    synth.op5_osc_pitch_env = 1.0
    synth.op5_osc_pitch_octave = 0.503937
    synth.op5_osc_pitch_semitone = 0.5
    synth.op5_osc_pitch_vibrato = 1.0
    synth.op5_osc_shape = 0.0
    synth.op5_osc_wavetype = 0.0
    synth.op5_outputlevel = 0.5
    synth.op5_outputlevel_velocity = 0.652035
    synth.op5_resonator_color = 0.5
    synth.op5_resonator_fdbkfilter = 1.0
    synth.op5_resonator_fdbkfiltermode = 0.0
    synth.op5_resonator_fdbksaturator = 0.0
    synth.op5_resonator_feedback = 0.5
    synth.op5_resonator_pitch_cent = 0.5
    synth.op5_resonator_pitch_env = 1.0
    synth.op5_resonator_pitch_fixed = 0.0
    synth.op5_resonator_pitch_octave = 0.503937
    synth.op5_resonator_pitch_semitone = 0.5
    synth.op5_resonator_pitch_vibrato = 1.0
    synth.op5_resonator_prefilter = 0.5
    synth.op5_texture_delay = 0.0
    synth.op5_texture_pitch_cent = 0.5
    synth.op5_texture_pitch_env = 1.0
    synth.op5_texture_pitch_fixed = 0.0
    synth.op5_texture_pitch_octave = 0.496063
    synth.op5_texture_pitch_semitone = 0.5
    synth.op5_texture_pitch_vibrato = 1.0
    synth.op5_texture_rpeator = 0.0
    synth.op5_texture_start = 0.0
    synth.op5_texture_tempo = 0.0
    synth.op5_texture_texture = 0.173228
    synth.op5_texture_trigger = 0.0
    synth.op5_type = 0.023622
    synth.op6_enable = 1.0
    synth.op6_env_attack1_level = 1.0
    synth.op6_env_attack1_time = 0.172405
    synth.op6_env_attack2_level = 1.0
    synth.op6_env_attack2_time = 0.0
    synth.op6_env_curvescale = 0.654146
    synth.op6_env_decay_time = 0.753331
    synth.op6_env_group = 0.0
    synth.op6_env_release1_level = 0.0
    synth.op6_env_release1_time = 0.293611
    synth.op6_env_release2_time = 0.0
    synth.op6_env_sustain_level = 1.0
    synth.op6_filter_drive = 0.0
    synth.op6_filter_frequency_course = 1.0
    synth.op6_filter_frequency_env1 = 0.5
    synth.op6_filter_frequency_env2 = 0.5
    synth.op6_filter_frequency_env2_a = 0.0
    synth.op6_filter_frequency_env2_d = 0.5
    synth.op6_filter_frequency_fine = 0.5
    synth.op6_filter_frequency_keyboard = 0.5
    synth.op6_filter_frequency_lfo = 0.5
    synth.op6_filter_frequency_velocity = 0.5
    synth.op6_filter_resonance = 0.0
    synth.op6_filter_type = 0.0
    synth.op6_fm_bend = 0.5
    synth.op6_fm_feedback = 0.5
    synth.op6_fm_invert = 0.0
    synth.op6_fm_pitch_coarse = 0.094403
    synth.op6_fm_pitch_detunr = 0.5
    synth.op6_fm_pitch_env = 1.0
    synth.op6_fm_pitch_fine = 0.5
    synth.op6_fm_pitch_fixed = 1.0
    synth.op6_fm_pitch_vibrato = 1.0
    synth.op6_fm_wavetype = 0.0
    synth.op6_fm_width = 1.0
    synth.op6_inputlevel = 0.5
    synth.op6_lfo_depth = 0.0
    synth.op6_lfo_depthvelocity = 0.5
    synth.op6_lfo_randomlevel = 0.0
    synth.op6_lfo_randomtime = 0.0
    synth.op6_lfo_rate = 0.5
    synth.op6_lfo_ratetemposync = 0.0
    synth.op6_lfo_waveform = 0.5
    synth.op6_noise_impulse_decay = 1.0
    synth.op6_noise_impulse_density = 0.5
    synth.op6_noise_impulse_level = 0.0
    synth.op6_noise_impulse_rate = 0.5
    synth.op6_noise_noise_cutoff = 0.5
    synth.op6_noise_noise_digitalmix = 0.0
    synth.op6_noise_noise_digitalrate = 0.5
    synth.op6_noise_noise_fluctuationdepth = 0.0
    synth.op6_noise_noise_fluctuationspeed = 0.5
    synth.op6_noise_noise_level = 0.5
    synth.op6_noise_noise_resonance = 0.0
    synth.op6_osc_invert = 0.0
    synth.op6_osc_oscsyncfreq = 0.0
    synth.op6_osc_pitch_cent = 0.5
    synth.op6_osc_pitch_drift = 0.0
    synth.op6_osc_pitch_env = 1.0
    synth.op6_osc_pitch_octave = 0.503937
    synth.op6_osc_pitch_semitone = 0.5
    synth.op6_osc_pitch_vibrato = 1.0
    synth.op6_osc_shape = 0.0
    synth.op6_osc_wavetype = 0.0
    synth.op6_outputlevel = 0.5
    synth.op6_outputlevel_velocity = 0.839396
    synth.op6_resonator_color = 0.5
    synth.op6_resonator_fdbkfilter = 0.820163
    synth.op6_resonator_fdbkfiltermode = 0.0
    synth.op6_resonator_fdbksaturator = 0.0
    synth.op6_resonator_feedback = 0.848755
    synth.op6_resonator_pitch_cent = 0.5
    synth.op6_resonator_pitch_env = 1.0
    synth.op6_resonator_pitch_fixed = 0.0
    synth.op6_resonator_pitch_octave = 0.503937
    synth.op6_resonator_pitch_semitone = 0.5
    synth.op6_resonator_pitch_vibrato = 1.0
    synth.op6_resonator_prefilter = 0.5
    synth.op6_texture_delay = 0.0
    synth.op6_texture_pitch_cent = 0.5
    synth.op6_texture_pitch_env = 1.0
    synth.op6_texture_pitch_fixed = 0.0
    synth.op6_texture_pitch_octave = 0.503937
    synth.op6_texture_pitch_semitone = 0.5
    synth.op6_texture_pitch_vibrato = 1.0
    synth.op6_texture_rpeator = 0.0
    synth.op6_texture_start = 0.0
    synth.op6_texture_tempo = 0.0
    synth.op6_texture_texture = 0.0
    synth.op6_texture_trigger = 0.0
    synth.op6_type = 0.0314961
    synth.pitch_bend_range = 0.00787402
    synth.pitch_env_amount = 0.5
    synth.pitch_env_attacklevel = 1.0
    synth.pitch_env_attacktime = 0.0
    synth.pitch_env_curve = 0.5
    synth.pitch_env_decaytime = 0.5
    synth.pitch_env_envtype = 0.0
    synth.pitch_env_releaselevel = 0.5
    synth.pitch_env_releasetime = 0.0
    synth.pitch_env_velocity = 0.5
    synth.pitch_vibrato_amount = 0.0
    synth.pitch_vibrato_modwheel = 0.634418
    synth.pitch_vibrato_range = 0.0
    synth.pitch_vibrato_rate = 0.580468
    synth.pitch_vibrato_rise_fall = 0.5
    synth.portamento = 0.0
    synth.volume = 0.662794

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
    with AudioFile(
        str(OUTPUT_DIR / filename), "w", SAMPLE_RATE, num_channels=1, bit_depth=32
    ) as o:
        o.write(audio)

    # Render wavetables using C base notes across four octaves
    base_note = 24  # C
    for octave in range(1):
        note = base_note + 12 * octave
        print(f"{note=}")
        midi_stream = [
            Message("note_on", note=note, velocity=127),
            Message("note_off", note=note, time=duration),
        ]
        wavetable_frames = []
        samples_per_frame = samples_per_cycle(midi_to_hz(note), SAMPLE_RATE)
        for dco_pwm in range(0, 128):
            print(f"{dco_pwm=}")
            synth.dco_pwm = dco_pwm
            audio = synth(midi_stream, duration=duration, sample_rate=SAMPLE_RATE)
            audio = audio[0]

            offset = samples_per_frame + 100  # skip initial ramp from 0
            single_cycle = audio[offset : offset + samples_per_frame]
            single_cycle = correct_dc_offset(single_cycle)
            single_cycle = normalize(single_cycle)

            wavetable_frames.append(single_cycle)
        wavetable = np.concatenate(wavetable_frames)
        filename = f"{OUTPUT_BASE_FILENAME}-note{note}-spf{samples_per_frame}.wav"
        with AudioFile(
            str(OUTPUT_DIR / filename), "w", SAMPLE_RATE, num_channels=1, bit_depth=32
        ) as o:
            o.write(wavetable)

    dump_param_details(synth)
    dump_param_vars(synth)


if __name__ == "__main__":
    main()
