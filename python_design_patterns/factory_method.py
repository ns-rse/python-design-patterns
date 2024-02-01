"""Factory Method Example"""

from typing import Callable
import numpy as np

# pylint: disable=no-name-in-module
from skimage.filters import (
    threshold_li,
    threshold_mean,
    threshold_otsu,
    threshold_yen,
    threshold_triangle,
)


def threshold(data: np.ndarray, method: str, **kwargs: dict) -> float:
    """Derive threshold for filtering of the given array using the specified filter.

    Parameters
    ----------
    data: np.ndarray
        Numpy array representing the image to be filtered.
    filter: str
        Filter method from Scikit-image to apply. Options are 'mean' (default), 'li', otsu', 'triangle', and 'yen'

    Returns
    -------
    np.ndarray
        Filtered array.
    """
    filter_threshold = _get_threshold(method)
    return filter_threshold(data, **kwargs)


def _get_threshold(method: str) -> Callable:
    """Creator component which determines which filter method to use.

    Parameters
    ----------
    data: np.ndarray
        Numpy array representing the image to be filtered.
    filter: str
        Filter method from Scikit-image to apply.

    Returns
    -------
    np.ndarray
        Filtered array.
    """
    if method == "mean":
        return _mean
    if method == "otsu":
        return _otsu
    if method == "triangle":
        return _triangle
    if method == "yen":
        return _yen
    if method == "li":
        return _li
    raise ValueError(method)


def _li(data: np.ndarray, **kwargs: dict) -> float:
    """Threshold based on Li method."""
    return threshold_li(data, **kwargs)


def _mean(data: np.ndarray, **kwargs: dict) -> float:
    """Threshold based on mean method."""
    return threshold_mean(data, **kwargs)


def _otsu(data: np.ndarray, **kwargs: dict) -> float:
    """Threshold based on Otsu's method."""
    return threshold_otsu(data, **kwargs)


def _triangle(data: np.ndarray, **kwargs: dict) -> float:
    """Threshold based on triangle method."""
    return threshold_triangle(data, **kwargs)


def _yen(data: np.ndarray, **kwargs: dict) -> float:
    """Threshold based on Yen's method."""
    return threshold_yen(data, **kwargs)
