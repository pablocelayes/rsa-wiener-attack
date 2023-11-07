import pytest
from RSAwienerHacker import hack_RSA
from tests.fixtures.rsa_data import TEST_RSA_HACK


@pytest.mark.parametrize("e,n,c,m", TEST_RSA_HACK)
def test_rational_to_contfrac(e: int, n: int, c: int, m: int):
    d = hack_RSA(e, n)
    decrypted_m = pow(c, d, n)
    assert decrypted_m == m
