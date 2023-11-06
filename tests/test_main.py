from src.main import my_slice


def test_my_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3, 4], -1, 3) == []
    assert my_slice([], 1, 3) == []
    assert my_slice([2, 3], -5, -3) == []


