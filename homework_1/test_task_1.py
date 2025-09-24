import pytest
from task_1 import solition


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, True),
        (1, True),
        (11, True),
        (121, True),
        (1221, True),
        (12321, True),
        (1282733333333372821, True),
        (10, False),
        (100, False),
        (123, False),
        (1231, False),
        (1233211231, False),
    ],
)
def test_palindromes_basic(value, expected):
    assert solition(value) is expected
