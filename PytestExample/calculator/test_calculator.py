import pytest
#print(pytest.__version__)

from main import add,subtract,divide

def test_addition():
    assert add(3,5) == 8
    assert add(-1,5) == 4
    assert add(-3,-2) == -5

def test_subtract():
    assert subtract(3,5) == -2
    assert subtract(-1,5) == -6
    assert subtract(-3,-2) == -1

def test_divide():
    assert divide(15,5) == 3
    assert divide(-5,5) == -1
    assert divide(30,-2) == -15