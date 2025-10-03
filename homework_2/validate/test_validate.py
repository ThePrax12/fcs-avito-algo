import pytest
from validate import solution


def test_example1():
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]
    assert solution(pushed, popped) == True


def test_example2():
    pushed = [1, 2, 3]
    popped = [3, 1, 2]
    assert solution(pushed, popped) == False


def test_single_element():
    pushed = [1, 2, 3]
    popped = [3, 2, 1]
    assert solution(pushed, popped) == True


def test_reverse_order():
    pushed = [1, 2, 3, 4]
    popped = [4, 3, 2, 1]
    assert solution(pushed, popped) == True


def test_same_order():
    pushed = [1, 2, 3, 4]
    popped = [1, 2, 3, 4]
    assert solution(pushed, popped) == True


def test_impossible_case():
    pushed = [1, 2, 3, 4]
    popped = [2, 1, 4, 3]
    assert solution(pushed, popped) == True
    popped2 = [3, 1, 2, 4]
    assert solution(pushed, popped2) == False


def test_empty_lists():
    pushed = []
    popped = []
    assert solution(pushed, popped) == True
