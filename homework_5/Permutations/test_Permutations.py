from Permutations import permutations
import pytest


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1], [[1]]),
        ([1, 2], [[1, 2], [2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([], [[]]),
        ([-1, 0], [[-1, 0], [0, -1]]),
        ([-2, -1], [[-2, -1], [-1, -2]]),
        ([10, 20], [[10, 20], [20, 10]]),
        ([5, 3, 1], [[5, 3, 1], [5, 1, 3], [3, 5, 1], [3, 1, 5], [1, 5, 3], [1, 3, 5]]),
    ],
)
def test_permutations_exact(nums, expected):
    """Тест точного соответствия результата"""
    result = permutations(nums)
    assert result == expected


@pytest.mark.parametrize(
    "nums, expected_count",
    [
        ([1], 1),  # 1! = 1
        ([1, 2], 2),  # 2! = 2
        ([1, 2, 3], 6),  # 3! = 6
        ([1, 2, 3, 4], 24),  # 4! = 24
        ([], 1),  # 0! = 1
        ([0], 1),  # 1! = 1
        ([-1, 0, 1], 6),  # 3! = 6
        ([5, 10, 15], 6),  # 3! = 6
        ([1, 2, 3, 4, 5], 120),  # 5! = 120
    ],
)
def test_permutations_count(nums, expected_count):
    """Тест количества перестановок"""
    result = permutations(nums)
    assert len(result) == expected_count


@pytest.mark.parametrize(
    "nums, should_contain",
    [
        ([1, 2], [1, 2]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([0, 1], [0, 1]),
        ([0, 1], [1, 0]),
        ([-1, 1], [-1, 1]),
        ([-1, 1], [1, -1]),
    ],
)
def test_permutations_contains(nums, should_contain):
    """Тест что результат содержит нужные перестановки"""
    result = permutations(nums)
    assert should_contain in result


@pytest.mark.parametrize(
    "nums",
    [
        [1, 2],
        [1, 2, 3],
        [0, 1, 2],
        [-1, 0, 1],
        [5, 3, 1],
        [10, 20, 30],
    ],
)
def test_permutations_all_elements(nums):
    """Тест что каждая перестановка содержит все элементы"""
    result = permutations(nums)

    for perm in result:
        assert len(perm) == len(nums)
        assert sorted(perm) == sorted(nums)


@pytest.mark.parametrize(
    "single_element",
    [0, 1, -1, 5, 100, -100],
)
def test_single_element(single_element):
    """Тест массива с одним элементом"""
    result = permutations([single_element])
    assert result == [[single_element]]
