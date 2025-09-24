import pytest
from task_2 import solition


@pytest.mark.parametrize(
    "s, expected",
    [
        ("1 2 3", 6),
        ("1 2", 2),
        ("2 4 6", 12),
        ("1", 0),
        ("1 10 7 3", 20),
        ("5 3 2", 10),
        ("7 7 7", 14),
    ],
)
def test_sum_with_odd_logic(s, expected):
    assert solition(s) == expected
