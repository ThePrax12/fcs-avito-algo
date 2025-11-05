import random
import time
import pytest
from Compare import quicksort_recur, mergesort_recur


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 1, 5, 2, 5], [1, 2, 5, 5, 5]),
        ([-1, 0, 3, -5, 2], [-5, -1, 0, 2, 3]),
    ],
)
def test_quicksort_correct(arr, expected):
    """Тест корректности быстрой сортировки"""
    assert quicksort_recur(arr[:]) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 1, 5, 2, 5], [1, 2, 5, 5, 5]),
        ([-1, 0, 3, -5, 2], [-5, -1, 0, 2, 3]),
    ],
)
def test_mergesort_correct(arr, expected):
    """Тест корректности сортировки слиянием"""
    assert mergesort_recur(arr[:]) == expected


def test_mergesort_vs_quicksort_same_result():
    """Тест, что обе сортировки дают одинаковый результат"""
    random.seed(0)
    arr = [random.randint(-1000, 1000) for _ in range(2000)]
    q = quicksort_recur(arr[:])
    m = mergesort_recur(arr[:])
    assert q == m


def test_quicksort_time_difference():
    """Тест, что быстрая сортировка работает дольше на больших данных"""
    small = [random.randint(0, 1000) for _ in range(1000)]
    large = [random.randint(0, 1000) for _ in range(20000)]

    t1 = time.perf_counter()
    quicksort_recur(small)
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    quicksort_recur(large)
    t4 = time.perf_counter()

    small_time = t2 - t1
    large_time = t4 - t3

    assert large_time > small_time * 2


def test_mergesort_time_difference():
    """Тест, что сортировка слиянием работает дольше на больших данных"""
    small = [random.randint(0, 1000) for _ in range(1000)]
    large = [random.randint(0, 1000) for _ in range(40000)]

    t1 = time.perf_counter()
    mergesort_recur(small)
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    mergesort_recur(large)
    t4 = time.perf_counter()

    small_time = t2 - t1
    large_time = t4 - t3

    assert large_time > small_time * 2
