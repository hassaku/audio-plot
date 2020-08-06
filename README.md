[![Build Status](https://travis-ci.org/hassaku/audio-plot.png)](https://travis-ci.org/hassaku/audio-plot)

Converts a line graph to sound and returns an object that can be played
in Jupyter notebook or Google Colab.

Values are represented by pitches, and the timeline is represented by left and right pans.

It was created to make data science fun for the visually impaired.

# Install

```
$ sudo apt-get install libavformat-dev libavfilter-dev libavdevice-dev ffmpeg  # if necessary
$ pip install audio-plot
```

# Usage

See and run demo notebook also. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hassaku/audio-plot/blob/master/demo.ipynb)

```
y = np.sin(np.arange(0, np.pi*2, 0.1))
yy = np.array([y, -y]).T
plot(yy)  # audio control will be appeared on notebook.
```

[The audio is as follows for this example]
```
tts > minimum value is -1.0
(Low sinusoidal sound)
tts > maximum value is 1.0
(High sinusoidal sound)
tts > line 1
(Sound in response to changes in the line 1 graph)
tts > line 2
(Sound in response to changes in the line 2 graph)
```

# Example

## Two inverted sinusoidale data

![Two inverted sinusoidale data graph](/assets/demo1.png?raw=true)

```
audio_plot.plot(yy)
```

[result](/assets/demo1-1.mp3)


```
audio_plot.plot(yy, ptype="overlay")
```

[result](/assets/demo1-2.mp3)

```
audio_plot.plot(yy, duration=200, min_freq=130.813/2, max_freq=130.813*3, labels=["A", "B"])
```

[result](/assets/demo1-3.mp3)

## COVID-19 deaths data in U.S.

![COVID-19 deaths data graph](/assets/demo2.png?raw=true)

```
audio_plot.plot(np.array([new_york, texas]).T, labels=["new york", "texas"])
```

[result](/assets/demo2.mp3)

# For developer

## Update PyPI

```
$ nosetests -vs
$ pip install twine # if necessary
$ cat ~/.pypirc  # if necessary
[distutils]
index-servers = pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: YOUR_USERNAME
password: YOUR_PASSWORD
$ rm -rf audio_plot.egg-info dist # if necessary
$ python setup.py sdist
$ twine upload --repository pypi dist
$ pip --no-cache-dir install --upgrade audio-plot
```

## Contributing

- Fork the repository on Github
- Create a named feature branch (like add_component_x)
- Write your change
- Write tests for your change (if applicable)
- Run the tests, ensuring they all pass
- Submit a Pull Request using Github

# License

MIT
