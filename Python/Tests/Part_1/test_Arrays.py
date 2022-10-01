from HackerRank.Arrays import arrays
import numpy

def test_arrays_true():
    numpy.testing.assert_equal(arrays((1, 2, 3, 4, -8, -10)), [-10., -8., 4., 3. ,2., 1.])

def test_arrays_false():
    with numpy.testing.assert_raises(AssertionError):
        numpy.testing.assert_equal(arrays((1, 2, 3, 4, -8, -10)), [-10., -8., 4., 3. ,2., 2.])