import pytest
from anagrams import solution


@pytest.mark.parametrize(
    "words, expected_groups",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            ["abc", "cab", "bca", "dog", "god", "odg"],
            [["abc", "cab", "bca"], ["dog", "god", "odg"]],
        ),
        (
            ["a", "b", "c"],
            [["a"], ["b"], ["c"]],
        ),
        (
            ["", ""],
            [["", ""]],
        ),
        (
            ["Listen", "Silent", "enlist"],
            [["Listen", "Silent", "enlist"]],
        ),
        (
            ["abc", "ab", "aabb", "baba", "bbaa"],
            [["abc"], ["ab"], ["aabb", "baba", "bbaa"]],
        ),
    ],
)
def test_solution(words, expected_groups):
    result = solution(words)
    result_sets = [set(g) for g in result]
    expected_sets = [set(g) for g in expected_groups]

    assert sorted(result_sets, key=lambda x: sorted(x)) == sorted(
        expected_sets, key=lambda x: sorted(x)
    )
