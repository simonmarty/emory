# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE
# WRITTEN BY OTHER STUDENTS.
# Simon Marty

import numpy as np
import numpy.testing as npt
import time


def gen_random_samples():
    """
    Generate 5 million random samples using the
    numpy random.randn module.

    Returns
    ----------
    sample : 1d array of size 5 million
        An array of 5 million random samples
    """
    return np.random.randn(5000000)


def sum_squares_for(samples: list):
    """
    Compute the sum of squares using a forloop

    Parameters
    ----------
    samples : 1d-array with shape n
        An array of numbers.

    Returns
    -------
    ss : float
        The sum of squares of the samples
    timeElapse: float
        The time it took to calculate the sum of squares (in seconds)
    """
    start_time = time.time()
    ss = 0
    mean = np.mean(samples)
    for i in samples:
        ss += pow((i - mean), 2)
    return ss, time.time() - start_time


def sum_squares_np(samples: list):
    """
    Compute the sum of squares using Numpy's dot module

    Parameters
    ----------
    samples : 1d-array with shape n
        An array of numbers.

    Returns
    -------
    ss : float
        The sum of squares of the samples
    timeElapse: float
        The time it took to calculate the sum of squares (in seconds)
    """
    start_time = time.time()
    ss = 0

    l = samples - np.mean(samples)
    ss = np.dot(l, l)

    return ss, time.time() - start_time


def main():
    # generate the random samples
    samples = gen_random_samples()
    # call the sum of squares
    ssFor, timeFor = sum_squares_for(samples)
    # call the numpy version
    ssNp, timeNp = sum_squares_np(samples)
    # make sure they're the same value
    npt.assert_almost_equal(ssFor, ssNp, decimal=5)
    # print out the values
    print("Time [sec] (for loop):", timeFor)
    print(f"SS: {ssFor}")
    print("Time [sec] (np loop):", timeNp)
    print(f"SS: {ssNp}")


if __name__ == "__main__":
    main()
