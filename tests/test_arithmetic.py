import pytest
from Arithmetic import is_perfect_square


@pytest.mark.parametrize("num,expected", [
    (4, 2),
    (0, 0),
    (15, -1),
    (25, 5),
    (18, -1),
    (901, -1),
    (1000, -1),
    (1024, 32),
])
def test_is_perfect_square(num: int, expected: int):
    assert is_perfect_square(num) == expected
