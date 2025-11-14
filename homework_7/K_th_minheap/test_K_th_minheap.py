import pytest

from K_th_minheap import kth_largest_without_heapq, kth_largest_with_heapq


@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([10], 1, 10),
        ([3, 1, 5, 2, 4], 1, 5),
        ([3, 1, 5, 2, 4], 2, 4),
        ([3, 1, 5, 2, 4], 3, 3),
        ([3, 1, 5, 2, 4], 4, 2),
        ([3, 1, 5, 2, 4], 5, 1),
        ([5, 5, 5, 5], 1, 5),
        ([5, 5, 5, 5], 3, 5),
        ([-1, -5, 0, 10], 1, 10),
        ([-1, -5, 0, 10], 2, 0),
        ([-1, -5, 0, 10], 3, -1),
        ([-1, -5, 0, 10], 4, -5),
        (list(range(10)), 1, 9),
        (list(range(10)), 10, 0),
        (list(range(9, -1, -1)), 1, 9),
        (list(range(9, -1, -1)), 5, 5),
    ],
)
def test_kth_largest_functions(arr, k, expected):
    """Проверяем обе реализации на известных ответах"""
    res1 = kth_largest_without_heapq(arr, k)
    res2 = kth_largest_with_heapq(arr, k)

    assert res1 == expected
    assert res2 == expected
    assert res1 == res2


@pytest.mark.parametrize(
    "arr,k",
    [
        ([3, 1, 5, 2, 4], 1),
        ([3, 1, 5, 2, 4], 2),
        ([3, 1, 5, 2, 4], 3),
        ([3, 1, 5, 2, 4], 4),
        ([3, 1, 5, 2, 4], 5),
        (list(range(100)), 10),
        (list(range(100)), 50),
    ],
)
def test_kth_largest_against_sort(arr, k):
    """Сверяем с эталоном через сортировку по убыванию"""
    expected = sorted(arr, reverse=True)[k - 1]

    res1 = kth_largest_without_heapq(arr, k)
    res2 = kth_largest_with_heapq(arr, k)

    assert res1 == expected
    assert res2 == expected
    assert res1 == res2
