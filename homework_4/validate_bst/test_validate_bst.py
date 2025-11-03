import pytest
from validate_bst import validate


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


@pytest.mark.parametrize(
    "tree, expected",
    [
        (None, True),
        (TreeNode(5), True),
        (TreeNode(5, TreeNode(3), TreeNode(7)), True),
        (TreeNode(5, TreeNode(3)), True),
        (TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15)), True),
        (TreeNode(5, TreeNode(7), TreeNode(3)), False),
        (TreeNode(5, TreeNode(5)), False),
        (TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(7)), False),
        (TreeNode(5, TreeNode(3), TreeNode(7, TreeNode(4), TreeNode(9))), False),
        (TreeNode(0, TreeNode(-5), TreeNode(5)), True),
    ],
)
def test_validate_bst(tree, expected):
    """Тест валидации BST для всех основных случаев"""
    assert validate(tree) == expected


def test_linear_trees():
    """Тест линейных деревьев"""
    right_linear = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    left_linear = TreeNode(3, TreeNode(2, TreeNode(1)))

    assert validate(right_linear) == True
    assert validate(left_linear) == True


def test_duplicate_edge_cases():
    """Тест дубликатов в разных позициях"""
    assert validate(TreeNode(5, None, TreeNode(5))) == False
    assert validate(TreeNode(5, TreeNode(3, TreeNode(5)))) == False


def test_deep_nested_violations():
    """Тест глубоких нарушений на разных уровнях"""
    deep_violation = TreeNode(
        50, TreeNode(30, TreeNode(20, TreeNode(60)), TreeNode(40)), TreeNode(70)
    )

    right_violation = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(2), TreeNode(20)))

    assert validate(deep_violation) == False
    assert validate(right_violation) == False
