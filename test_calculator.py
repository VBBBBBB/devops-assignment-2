import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

# Intentional error test to demonstrate CI failure initially
def test_intentional_failure():
    # This assertion is intentionally incorrect: 2 + 2 != 5
    assert add(2, 2) == 5, "Intentional failure for CI demonstration"
