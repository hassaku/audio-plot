[![Build Status](https://travis-ci.org/hassaku/audio-plot.png)](https://travis-ci.org/hassaku/audio-plot)

Converts a line graph to sound and returns an object that can be played
in Jupyter notebook or Google Colab.
It was created to make data science fun for the visually impaired.

# Install

```
$ pip install audio-plot
```

# Usage

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

# Update PyPI

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

# Contributing

- Fork the repository on Github
- Create a named feature branch (like add_component_x)
- Write your change
- Write tests for your change (if applicable)
- Run the tests, ensuring they all pass
- Submit a Pull Request using Github

# License

MIT
