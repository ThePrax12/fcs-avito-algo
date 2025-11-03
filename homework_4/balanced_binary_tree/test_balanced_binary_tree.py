import pytest
from balanced_binary_tree import is_balanced


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


@pytest.mark.parametrize(
    "tree, expected",
    [
        (None, True),
        (TreeNode(1), True),
        (TreeNode(1, TreeNode(2), TreeNode(3)), True),
        (TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4)), True),
        (
            TreeNode(
                4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(6, TreeNode(5), TreeNode(7)),
            ),
            True,
        ),
        (TreeNode(1, TreeNode(2, TreeNode(3)), None), False),
        (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), False),
    ],
)
def test_basic_cases(tree, expected):
    """Тест основных случаев"""
    assert is_balanced(tree) == expected


def test_linear_trees():
    """Тест линейных деревьев"""
    right_chain = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    left_chain = TreeNode(3, TreeNode(2, TreeNode(1)))
    short_chain = TreeNode(1, None, TreeNode(2))

    assert is_balanced(right_chain) == False
    assert is_balanced(left_chain) == False
    assert is_balanced(short_chain) == True


def test_deep_imbalance():
    """Тест глубокого дисбаланса"""
    deep_unbalanced = TreeNode(
        1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))), TreeNode(6)
    )
    assert is_balanced(deep_unbalanced) == False


def test_edge_balanced_cases():
    """Тест граничных сбалансированных случаев"""
    edge_balanced = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
    asymmetric_balanced = TreeNode(
        1, TreeNode(2, None, TreeNode(3)), TreeNode(4, TreeNode(5))
    )

    assert is_balanced(edge_balanced) == True
    assert is_balanced(asymmetric_balanced) == True


def test_complex_structures():
    """Тест сложных структур: большие деревья и тонкие случаи дисбаланса"""
    large_balanced = TreeNode(
        8,
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)),
        ),
        TreeNode(
            12,
            TreeNode(10, TreeNode(9), TreeNode(11)),
            TreeNode(14, TreeNode(13), TreeNode(15)),
        ),
    )

    subtle_imbalance = TreeNode(
        1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5, TreeNode(6))
    )

    assert is_balanced(large_balanced) == True
    assert is_balanced(subtle_imbalance) == False


def test_mixed_imbalance():
    """Тест смешанного дисбаланса"""
    left_heavy = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    right_heavy = TreeNode(
        1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5, None, TreeNode(6)))
    )

    assert is_balanced(left_heavy) == False
    assert is_balanced(right_heavy) == False
