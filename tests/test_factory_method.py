"""Testes for Factor Method."""
import numpy as np
import pytest

from python_design_patterns.factory_method import threshold


rng = np.random.default_rng(seed=501472)
pytest.random_array = rng.random((10, 10))


@pytest.mark.parametrize(
    "data,method,expected_threshold",
    [
        (pytest.random_array, "mean", 0.45497009177756903),
        (pytest.random_array, "otsu", 0.4355642854559527),
        (pytest.random_array, "triangle", 0.38976173291463245),
        (pytest.random_array, "yen", 0.3706773360224157),
        (pytest.random_array, "li", 0.39614732379676265),
    ],
)
def test_threshold(data: np.ndarray, method: str, expected_threshold: float) -> None:
    """Test the threshold factory method."""
    assert threshold(data, method) == expected_threshold
