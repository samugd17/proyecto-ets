import pytest
from tablestars import *

@pytest.fixture
def user1():
    return User()

@pytest.fixture
def user2():
    return User()

@pytest.fixture
def user3():
    return User()

def test_test():
    assert test(2, 2) == 4
    assert test(4, 2) == 6
    assert test(4, 4) == 8
