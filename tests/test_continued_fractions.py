import pytest
from ContinuedFractions import rational_to_contfrac
from tests.fixtures.continued_fractions import TEST_RATIONAL_FRAC


@pytest.mark.parametrize(
    "rational_number,expected_continued_fraction, expected_convergents",
    TEST_RATIONAL_FRAC,
)
def test_rational_to_contfrac(
    rational_number: tuple[int, int],
    expected_continued_fraction: list[int],
    expected_convergents: list[tuple[int, int]],
):
    cfs, cvs = rational_to_contfrac(*rational_number)
    assert cfs == expected_continued_fraction
    assert cvs == expected_convergents
