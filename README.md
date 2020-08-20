[![Build Status](https://travis-ci.org/hassaku/audio-plot.png)](https://travis-ci.org/hassaku/audio-plot)

Converts a line graph to sound and returns an object that can be played
in Jupyter notebook or Google Colab.

Values are represented by pitches, and the timeline is represented by left and right pans.

It was created to make data science fun for the visually impaired.

# Dependency

ffmpeg library is needed to provide a descriptive guide to the graph. 

## Google Colab

No additional installation is required.

## Linux

```
$ sudo apt-get install libavformat-dev libavfilter-dev libavdevice-dev ffmpeg
```

## Others

It's under investigation. If you know of any, please make a pull request. Thanks.

# Install

```
$ pip install audio-plot  # !pip install audio-plot for Colab or Notebook
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

[Example Results Page](https://hassaku.github.io/audio-plot/)

# Supplement

If using Jupyter Notebook with a screen reader is inconvenient for you, you may want to consider using the following NVDA add-on.

https://github.com/mltony/nvda-browser-nav

# For contributer

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
