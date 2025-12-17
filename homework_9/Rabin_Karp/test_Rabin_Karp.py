import pytest

from Rabin_Karp import rabin_karp


def naive_find_all(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    return [i for i in range(n - m + 1) if text[i:i + m] == pattern]


@pytest.mark.parametrize(
    "text, pattern",
    [
        ("", ""),
        ("", "a"),
        ("a", ""),
        ("a", "a"),
        ("a", "b"),
        ("aaaaa", "aa"),
        ("aaaaa", "aaa"),
        ("abababab", "aba"),
        ("abababab", "bab"),
        ("hello world", "world"),
        ("hello world", " "),
        ("mississippi", "issi"),
        ("mississippi", "mississippi"),
        ("mississippi", "mississippii"),
        ("abcxabcdabxabcdabcdabcy", "abcdabcy"),
        ("тест тестирование тест", "тест"),
    ],
)
def test_rabin_karp_matches_naive(text, pattern):
    assert rabin_karp(text, pattern) == naive_find_all(text, pattern)


def test_no_false_positives_basic():
    text = "abcde" * 20
    pattern = "cdef"
    assert rabin_karp(text, pattern) == []


def test_single_occurrence_at_end():
    text = "xxxxxy"
    pattern = "y"
    assert rabin_karp(text, pattern) == [5]
