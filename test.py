import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):

        f()
def funco(x):
    return x + 1

def test_answer2():
    assert funco(3) == 4

def test_negative():
    assert funco(10) == 500
