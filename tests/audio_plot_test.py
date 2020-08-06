import os

from mock import patch
from unittest import TestCase
from nose.tools import raises, ok_

import audio_plot
import numpy as np
from pydub import AudioSegment

class AudioPlotTestCase(TestCase):
    def test_normal(self):
        ret = audio_plot.plot(np.random.rand(10, 2))
        ok_(type(ret) == AudioSegment)


    @raises(AttributeError)
    def test_passed_not_numpy_array(self):
        ret = audio_plot.plot([1, 2])

