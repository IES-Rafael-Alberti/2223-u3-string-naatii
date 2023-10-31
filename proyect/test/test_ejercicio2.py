from src.ejercicio2 import * 
import pytest

@pytest.mark.parametrize(
    "input, expected",
    [
        ("hola", "hola"),
        ("manzana", "manzana"),
        ("pera", "pera"),
    ]
)
def test_whatIsSecuency(input, expected):
    assert whatItsSecuency(input) == expected