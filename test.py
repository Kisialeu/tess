import pytest
import allure


@allure.step("123")
def foo_test(a):
    return a + 1

def func(x):
    return x + 1

def test_answer():
    assert foo_test(3) == 4
    
def test_answer2():
    assert func(3) == 4
    
def test_answer23():
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
    
def test_answer5():
    assert funco(3) == 4

def test_negative():
    assert funco(499) == 5000
    
def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert True


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    pass

def test_mytest():
    with pytest.raises(SystemExit):
        f()
def test_answer2():
    assert func(3) == 4
