import random
import pytest

from K_th import quick_select


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([5, 4, 3, 2, 1], 1, 5),
        ([5, 4, 3, 2, 1], 5, 1),
        ([1], 1, 1),
        ([2, 2, 2, 2], 3, 2),
        ([-1, 0, 3, -5, 2], 1, 3),
        ([-1, 0, 3, -5, 2], 5, -5),
    ],
)
def test_quick_select_examples(nums, k, expected):
    """Тест корректности на фиксированных наборах"""
    assert quick_select(nums[:], k) == expected


def test_quick_select_does_not_mutate_input():
    """Тест что исходный список не мутирует"""
    nums = [3, 1, 4, 1, 5, 9, 2]
    original = nums[:]
    _ = quick_select(nums, 3)
    assert nums == original


def test_quick_select_matches_sorted_random_small():
    """Случайные малые массивы: результат совпадает с сортировкой по убыванию"""
    random.seed(0)
    for _ in range(20):
        n = random.randint(1, 12)
        arr = [random.randint(-10, 10) for _ in range(n)]
        k = random.randint(1, n)
        expected = sorted(arr, reverse=True)[k - 1]
        assert quick_select(arr[:], k) == expected
