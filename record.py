import sounddevice
from numpy import ndarray


def record(duration: int, FS: int) -> ndarray:
    """
    Function to record audio with microphone
    """
    recording = sounddevice.rec(int(duration * FS), samplerate=FS, channels=1)
    sounddevice.wait()

    return recording.flatten()
