import pytest
from app_logic import add_numbers

def test_add_numbers_ok():
    assert add_numbers(1, 2) == 3.0
    assert add_numbers("1.5", "2.5") == 4.0

@pytest.mark.parametrize("a,b", [(None, 1), (1, None), (None, None)])
def test_add_numbers_missing(a, b):
    with pytest.raises(ValueError):
        add_numbers(a, b)

@pytest.mark.parametrize("a,b", [("x", 1), (1, "y"), ("foo", "bar")])
def test_add_numbers_type_error(a, b):
    with pytest.raises(TypeError):
        add_numbers(a, b)
