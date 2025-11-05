import random
import time
import pytest
from Iterative import quicksort_iter, mergesort_iter


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
def test_quicksort_iter_correct(arr, expected):
    """Тест корректности итеративной быстрой сортировки"""
    data = arr[:]
    out = quicksort_iter(data)
    assert out == expected
    assert data == expected


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
def test_mergesort_iter_correct(arr, expected):
    """Тест корректности итеративной сортировки слиянием"""
    data = arr[:]
    out = mergesort_iter(data)
    assert out == expected
    assert data == arr


def test_iter_sorts_match_on_random():
    """Тест совпадения результатов алгоритмов на случайных данных"""
    random.seed(42)
    arr = [random.randint(-1000, 1000) for _ in range(5000)]
    q = quicksort_iter(arr[:])
    m = mergesort_iter(arr[:])
    assert q == m == sorted(arr)


def test_quicksort_iter_time_difference():
    """Тест, что быстрая сортировка дольше на больших данных"""
    random.seed(0)
    small = [random.randint(0, 10_000) for _ in range(2_000)]
    large = [random.randint(0, 10_000) for _ in range(40_000)]

    t1 = time.perf_counter()
    quicksort_iter(small)
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    quicksort_iter(large)
    t4 = time.perf_counter()

    small_time = t2 - t1
    large_time = t4 - t3
    assert large_time > small_time * 2


def test_mergesort_iter_time_difference():
    """Тест, что сортировка слиянием дольше на больших данных"""
    random.seed(0)
    small = [random.randint(0, 10_000) for _ in range(2_000)]
    large = [random.randint(0, 10_000) for _ in range(80_000)]

    t1 = time.perf_counter()
    mergesort_iter(small)
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    mergesort_iter(large)
    t4 = time.perf_counter()

    small_time = t2 - t1
    large_time = t4 - t3
    assert large_time > small_time * 2
