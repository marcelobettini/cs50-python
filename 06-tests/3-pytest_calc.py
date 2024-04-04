from calc import square
import pytest

# def test_square():
#     assert square(2) == 4   
#     assert square(3) == 9   
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# this is better and detailed, we can see the benefits when certain test or tests fails
def test_positive():
    assert square(2) == 4   
    assert square(3) == 9   
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0
def test_str():
    with pytest.raises(TypeError):
        square("Nairobi")
    

