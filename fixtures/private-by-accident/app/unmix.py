"""Spectral unmixing for the sorting line: the part of Heron that is the customer's edge."""
import numpy as np


def unmix(spectrum, endmembers):
    """Least-squares abundances of each endmember in one pixel's spectrum."""
    abundances, *_ = np.linalg.lstsq(endmembers.T, spectrum, rcond=None)
    return np.clip(abundances, 0, None)
