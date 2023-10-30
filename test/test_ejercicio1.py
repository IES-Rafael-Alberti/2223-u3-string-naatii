from src.ejercicio1 import *
import pytest

@pytest.mark.parametrize(
    "input, expected",
    [
        ("hola mundo", invertedString("hola mundo")),
        ("hola natalia", invertedString("hola natalia"))
    ]
)
def test_invertedString(input, expected):
    invertedString(input) == expected
def test_invertedStringError():
    with pytest.raises(ValueError):
        invertedString(1)