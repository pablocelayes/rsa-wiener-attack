import pytest
from Arithmetic import is_perfect_square
from tests.fixtures.arithmetic import TEST_NUM_SQRT


@pytest.mark.parametrize("num,expected", TEST_NUM_SQRT)
def test_is_perfect_square(num: int, expected: int):
    assert is_perfect_square(num) == expected
