from math_logic import sum, multiply, divide, find_max, find_min

def test_multiply():
    assert multiply(1, 2) == 2

def test_divide():
    assert divide(4, 2) == 2

def test_find_max():
    assert find_max(1, 2) == 2

def test_find_min():
    assert find_min(4, 5) == 4