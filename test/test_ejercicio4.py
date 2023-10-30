from src.ejercicio4 import *
import pytest

@pytest.mark.parametrize(
    "char, expected",
    [
        ("a", 3),
        ("n", 2),
        ("b", 1),
    ]
)
def test_letterCounter(char, expected):
    assert letterCounterWithCount(char) == expected