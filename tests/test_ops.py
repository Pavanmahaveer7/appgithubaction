from src.math_ops import add,sub

def test_add():
    assert add(2,3)==5
    assert add(0,3)==3

def test_sub():
    assert sub(5,2)==3

    