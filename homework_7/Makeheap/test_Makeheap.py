import random
import pytest

from Makeheap import makeheap_n_log_n, makeheap


def is_min_heap(arr):
    """Проверка, что массив удовлетворяет свойству мин кучи"""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


@pytest.mark.parametrize(
    "data",
    [
        [],
        [1],
        [2, 1],
        [1, 2],
        [4, 1, 3, 8, 5],
        [5, 3, 8, 1, 4, 7, 2],
        [3, 3, 3, 3, 3],
        [0, -1, 5, -10, 7, 7, 2],
        list(range(10)),
        list(range(9, -1, -1)),
    ],
)
def test_makeheap_functions_build_valid_min_heap(data):
    arr1 = data.copy()
    arr2 = data.copy()

    heap1 = makeheap_n_log_n(arr1)
    heap2 = makeheap(arr2)

    for heap in (heap1, heap2):

        assert sorted(heap) == sorted(data)

        assert is_min_heap(heap)


@pytest.mark.parametrize("n", [1, 2, 5, 10, 50])
def test_random_arrays(n):
    """Случайные массивы для дополнительной проверки"""

    rng = random.Random(42 + n)
    data = [rng.randint(-100, 100) for _ in range(n)]

    arr1 = data.copy()
    arr2 = data.copy()

    heap1 = makeheap_n_log_n(arr1)
    heap2 = makeheap(arr2)

    for heap in (heap1, heap2):
        assert sorted(heap) == sorted(data)
        assert is_min_heap(heap)
