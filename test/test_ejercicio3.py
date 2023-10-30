from src.ejercicio3 import *
import pytest

@pytest.mark.parametrize(
    "word, char, expected",
    [
        ("banana", "a", 3),
        ("natalia", "n", 1),
        ("hello word", "l", 2),
        ("hello natalia", "a", 3),
    ]
)
def test_letterCounter(word, char, expected):
    assert letterCounter(word, char) == expected