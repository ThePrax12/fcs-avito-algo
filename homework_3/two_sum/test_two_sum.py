from two_sum import solution
import pytest


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([1, 5, 3, 7], 8, (1, 2)),
        ([0, 4, 3, 0], 0, (0, 3)),
        ([-1, -2, -3, -4, -5], -8, (2, 4)),
        ([1, 2, 3, 4, 5], 9, (3, 4)),
    ],
)
def test_solution(arr, k, expected):
    assert solution(arr, k) == expected
