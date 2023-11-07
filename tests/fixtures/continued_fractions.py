# [(rational_number, expected_continued_fraction, expected_convergents), ...]
# Rational number is a tuple: (numerator, denominator)
# Expected continued fraction is a list of coefficients: [a0, a1, a2, ...]
# Convergents is a list of rational numbers: [(numerator, denominator), ...]
TEST_RATIONAL_FRAC = [
    ((1, 1), [1], [(1, 1)]),
    ((1, 2), [0, 2], [(0, 1), (1, 2)]),
    ((5, 15), [0, 3], [(0, 1), (1, 3)]),
    ((27, 73), [0, 2, 1, 2, 2, 1, 2], [(0, 1), (1, 2), (1, 3), (3, 8), (7, 19), (10, 27), (27, 73)]),
    ((73, 27), [2, 1, 2, 2, 1, 2], [(2, 1), (3, 1), (8, 3), (19, 7), (27, 10), (73, 27)]),
    ((99, 70), [1, 2, 2, 2, 2, 2], [(1, 1), (3, 2), (7, 5), (17, 12), (41, 29), (99, 70)]),
    ((104348, 33215), [3, 7, 15, 1, 293], [(3, 1), (22, 7), (333, 106), (355, 113), (104348, 33215)]),
]