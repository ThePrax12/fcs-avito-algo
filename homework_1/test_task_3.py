import pytest
from task_3 import solition


@pytest.mark.parametrize(
    "N, expected_primes_lt_N",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),  # 2
        (10, 4),  # 2,3,5,7
        (20, 8),  # 2,3,5,7,11,13,17,19
        (100, 25),
        (1000, 168),
    ],
)
def test_primes_count(N, expected_primes_lt_N):
    assert solition(N) == expected_primes_lt_N
