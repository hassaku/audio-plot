import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, Pulse, Square, Sawtooth, Triangle, WhiteNoise
from gtts import gTTS

def __tts(utter: str):
    tts = gTTS(utter)
    tts.save("tmp.mp3")
    return AudioSegment.from_mp3("tmp.mp3")


def __sample(freq: float):
    return Sine(freq).to_audio_segment(duration=1000).apply_gain(-10).fade_in(20).fade_out(20)


def __overlay_plot(tones, lines, labels, min_freq, min_value, tic, duration, gain):
    assert lines.shape[1] <= 5

    for t in range(lines.shape[1]):
        tones += __tts("{} is {} sound".format(labels[t], ["Sine", "Pulse", "Square", "Sawtooth", "Triangle"][t]))

    __tones = None
    for t in range(lines.shape[1]):
        __tones_t = AudioSegment.silent(duration=0)

        for x, y in enumerate(lines[:, t]):
            gen = [Sine, Pulse, Square, Sawtooth, Triangle][t](min_freq + (y - min_value) * tic)
            wav = gen.to_audio_segment(duration=duration).apply_gain(gain)
            wav = wav.fade_in(duration/4).fade_out(duration/4).pan(-1.0 + x / lines.shape[0]*2)
            __tones_t += wav

        if __tones is None:
            __tones = __tones_t
        else:
            __tones = __tones.overlay(__tones_t)

    return tones + __tones


def __sequential_plot(tones, lines, labels, min_freq, min_value, tic, duration, gain):
    for t in range(lines.shape[1]):
        #if t > 0:
        #    # interlude
        #    tones += WhiteNoise().to_audio_segment(duration=1000).apply_gain(-20).fade_in(duration/4).fade_out(duration/4)
        tones += __tts(labels[t])

        for x, y in enumerate(lines[:, t]):
            gen = Sine(min_freq + (y - min_value) * tic)
            sine = gen.to_audio_segment(duration=duration).apply_gain(gain)
            sine = sine.fade_in(duration/4).fade_out(duration/4).pan(-1.0 + x / lines.shape[0] * 2)
            tones += sine

    return tones


def plot(lines: np.array, labels: list=None, ptype: str="sequential", duration: int=50, gain: int=-5,
         min_freq: float=130.813, max_freq: float=130.813*4, decimals=1) -> AudioSegment:
    """
    Converts a line graph to sound and returns an object that can be played
    in Jupyter notebook or Google Colab.

    Parameters
    ----------
    lines : numpy array of values
        The array of lines. 0-dim is time. 1-dim is number of lines.
    labels : list of str, optional
        Graph legend
    ptype : string, optional
        Type of graph, default is sequential. Another is overlay.
    WIP

    Returns
    -------
    tones
        pydub.AudioSegment object.

    Examples
    --------
    ::
        y = np.sin(np.arange(0, np.pi*2, 0.1))
        yy = np.array([y, -y]).T
        plot(yy)  # audio control will be appeared on notebook.

        [The audio is as follows for this example]
        tts > minimum value is -1.0
        (Low sinusoidal sound)
        tts > maximum value is 1.0
        (High sinusoidal sound)
        tts > line 1
        (Sound in response to changes in the line 1 graph)
        tts > line 2
        (Sound in response to changes in the line 2 graph)
    """
    assert lines.ndim == 2
    assert lines.shape[0] > lines.shape[1]

    if labels is None:
        labels = ["line {}".format(l+1) for l in range(lines.shape[1])]
    else:
        assert len(labels) == lines.shape[1]

    min_value = np.nanmin(lines)
    max_value = np.nanmax(lines)
    tic = (max_freq - min_freq) / (max_value - min_value)

    tones = AudioSegment.silent(duration=0)

    # describe yaxis
    tones += __tts("minimum value is {}".format(np.round(min_value, decimals)))
    tones += __sample(min_freq)
    tones += __tts("maximum value is {}".format(np.round(max_value, decimals)))
    tones += __sample(max_freq)

    # plot lines
    if ptype == "sequential":
        tones = __sequential_plot(tones, lines, labels, min_freq, min_value, tic, duration, gain)
    elif ptype == "overlay":
        tones = __overlay_plot(tones, lines, labels, min_freq, min_value, tic, duration, gain)
    else:
        raise NotImplementedError("ptype must be sequential or overlay")

    return tones

