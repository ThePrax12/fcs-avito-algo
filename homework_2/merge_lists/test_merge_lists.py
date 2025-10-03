import pytest
from merge_lists import Node, merge_dummy, merge_no_dummy


def build_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for val in lst[1:]:
        current.next = Node(val)
        current = current.next
    return head


def to_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result


def test_merge_dummy_regular():
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    merged = merge_dummy(l1, l2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]


def test_merge_dummy_one_empty():
    l1 = build_list([])
    l2 = build_list([0, 5])
    merged = merge_dummy(l1, l2)
    assert to_list(merged) == [0, 5]


def test_merge_dummy_both_empty():
    l1 = build_list([])
    l2 = build_list([])
    merged = merge_dummy(l1, l2)
    assert merged is None


def test_merge_dummy_identical_elements():
    l1 = build_list([2, 2, 2])
    l2 = build_list([2, 2])
    merged = merge_dummy(l1, l2)
    assert to_list(merged) == [2, 2, 2, 2, 2]


def test_merge_dummy_different_lengths():
    l1 = build_list([1, 4, 6])
    l2 = build_list([2])
    merged = merge_dummy(l1, l2)
    assert to_list(merged) == [1, 2, 4, 6]


def test_merge_no_dummy_regular():
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    merged = merge_no_dummy(l1, l2)
    assert to_list(merged) == [1, 1, 2, 3, 4, 4]


def test_merge_no_dummy_one_empty():
    l1 = build_list([])
    l2 = build_list([0, 5])
    merged = merge_no_dummy(l1, l2)
    assert to_list(merged) == [0, 5]


def test_merge_no_dummy_both_empty():
    l1 = build_list([])
    l2 = build_list([])
    merged = merge_no_dummy(l1, l2)
    assert merged is None


def test_merge_no_dummy_identical_elements():
    l1 = build_list([2, 2, 2])
    l2 = build_list([2, 2])
    merged = merge_no_dummy(l1, l2)
    assert to_list(merged) == [2, 2, 2, 2, 2]


def test_merge_no_dummy_different_lengths():
    l1 = build_list([1, 4, 6])
    l2 = build_list([2])
    merged = merge_no_dummy(l1, l2)
    assert to_list(merged) == [1, 2, 4, 6]
