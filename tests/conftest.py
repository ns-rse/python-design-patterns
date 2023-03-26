"""Setup fixtures and config for the test."""
import numpy as np
import pytest

rng = np.random.default_rng(seed=501472)


def default_config() -> None:
    """Configure custom variables for pytest"""
    pytest.random_array = rng.random((10, 10))
