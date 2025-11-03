import pytest
from Traversal import BST, TreeNode


@pytest.mark.parametrize(
    "values, expected_inorder",
    [
        ([5], [5]),
        ([5, 3, 7], [3, 5, 7]),
        ([5, 3, 7, 1, 4, 6, 9], [1, 3, 4, 5, 6, 7, 9]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
    ],
)
def test_insert_and_inorder(values, expected_inorder):
    """Тест вставки и inorder обхода"""
    bst = BST()
    for value in values:
        assert bst.insert(value) == True
    assert bst.inorder() == expected_inorder


def test_insert_duplicates():
    """Тест вставки дубликатов"""
    bst = BST()
    assert bst.insert(5) == True
    assert bst.insert(3) == True
    assert bst.insert(5) == False
    assert bst.insert(3) == False
    assert bst.inorder() == [3, 5]


def test_empty_tree():
    """Тест пустого дерева"""
    bst = BST()
    assert bst.inorder() == []
    assert bst.preorder() == []
    assert bst.postorder() == []


@pytest.mark.parametrize(
    "values, expected_preorder, expected_postorder",
    [
        ([5, 3, 7], [5, 3, 7], [3, 7, 5]),
        ([5, 3, 7, 1, 4, 6, 9], [5, 3, 1, 4, 7, 6, 9], [1, 4, 3, 6, 9, 7, 5]),
        ([1, 2, 3], [1, 2, 3], [3, 2, 1]),
    ],
)
def test_preorder_postorder(values, expected_preorder, expected_postorder):
    """Тест preorder и postorder обходов"""
    bst = BST()
    for value in values:
        bst.insert(value)
    assert bst.preorder() == expected_preorder
    assert bst.postorder() == expected_postorder


@pytest.mark.parametrize(
    "values, expected_reverse_inorder",
    [
        ([5, 3, 7], [7, 5, 3]),
        ([5, 3, 7, 1, 4, 6, 9], [9, 7, 6, 5, 4, 3, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
    ],
)
def test_reverse_inorder(values, expected_reverse_inorder):
    """Тест reverse inorder обхода"""
    bst = BST()
    for value in values:
        bst.insert(value)
    assert bst.reverse_inorder() == expected_reverse_inorder


@pytest.mark.parametrize(
    "values, expected_reverse_preorder, expected_reverse_postorder",
    [
        ([5, 3, 7], [5, 7, 3], [7, 3, 5]),
        ([5, 3, 7, 1, 4, 6, 9], [5, 7, 9, 6, 3, 4, 1], [9, 6, 7, 4, 1, 3, 5]),
    ],
)
def test_reverse_preorder_postorder(
    values, expected_reverse_preorder, expected_reverse_postorder
):
    """Тест reverse preorder и postorder обходов"""
    bst = BST()
    for value in values:
        bst.insert(value)
    assert bst.reverse_preorder() == expected_reverse_preorder
    assert bst.reverse_postorder() == expected_reverse_postorder


def test_single_node():
    """Тест дерева с одним узлом"""
    bst = BST()
    bst.insert(42)
    assert bst.inorder() == [42]
    assert bst.preorder() == [42]
    assert bst.postorder() == [42]
    assert bst.reverse_inorder() == [42]


def test_bst_property():
    """Тест что inorder дает отсортированный результат"""
    bst = BST()
    values = [10, 5, 15, 2, 7, 12, 20]
    for value in values:
        bst.insert(value)
    assert bst.inorder() == sorted(values)


def test_negative_numbers():
    """Тест с отрицательными числами"""
    bst = BST()
    values = [0, -5, 5, -10, 10]
    for value in values:
        bst.insert(value)
    assert bst.inorder() == [-10, -5, 0, 5, 10]


def test_reverse_inorder_correctness():
    """Тест что reverse_inorder = обращенный inorder"""
    bst = BST()
    values = [5, 3, 7, 1, 9]
    for value in values:
        bst.insert(value)

    inorder = bst.inorder()
    reverse_inorder = bst.reverse_inorder()
    assert reverse_inorder == inorder[::-1]


def test_right_skewed_tree():
    """Тест правостороннего дерева"""
    bst = BST()
    values = [1, 2, 3, 4, 5]
    for value in values:
        bst.insert(value)

    assert bst.inorder() == [1, 2, 3, 4, 5]
    assert bst.preorder() == [1, 2, 3, 4, 5]
    assert bst.reverse_inorder() == [5, 4, 3, 2, 1]


def test_left_skewed_tree():
    """Тест левостороннего дерева"""
    bst = BST()
    values = [5, 4, 3, 2, 1]
    for value in values:
        bst.insert(value)

    assert bst.inorder() == [1, 2, 3, 4, 5]
    assert bst.preorder() == [5, 4, 3, 2, 1]
    assert bst.reverse_inorder() == [5, 4, 3, 2, 1]


def test_mixed_operations():
    """Тест смешанных операций"""
    bst = BST()

    assert bst.inorder() == []

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.inorder() == [3, 5, 7]

    assert bst.insert(5) == False
    assert bst.inorder() == [3, 5, 7]
