import os
import wave

def is_wav_file(filename):
    return filename.lower().endswith('.wav')

def get_audio_duration(file_path):
    if not is_wav_file(file_path):
        raise ValueError("Only WAV files are supported.")
    with wave.open(file_path, 'rb') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration = frames / float(rate)
        return duration
