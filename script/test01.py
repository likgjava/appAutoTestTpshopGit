import pytest


def test01():
    print("11111111111")
    assert 1
    print("222222222222222")

if __name__ == '__main__':
    pytest.main(['test01.py', '-s'])
