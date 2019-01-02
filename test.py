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
    assert funco(499) == 500
    
def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    pass

def test_mytest():
    with pytest.raises(SystemExit):
        f()
