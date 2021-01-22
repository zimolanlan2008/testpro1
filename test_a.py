import pytest
a = [1,2,3]

def inc(x):
    return x + 1
a.pop

def test_answer():
    assert inc(3) == 5

if __name__ == '__main__':
    pytest.main(['test_a.py'])