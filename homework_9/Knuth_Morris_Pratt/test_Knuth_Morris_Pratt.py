import pytest

from Knuth_Morris_Pratt import kmp_search


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
        ("abc", "abcd"),
        ("xyzxyzxyz", "xyz"),
    ],
)
def test_kmp_equals_naive(text, pattern):
    assert kmp_search(text, pattern) == naive_find_all(text, pattern)


def test_overlapping_occurrences():
    text = "aaaaa"
    pattern = "aaa"
    assert kmp_search(text, pattern) == [0, 1, 2]


def test_no_occurrences():
    assert kmp_search("abcdefgh", "ijk") == []
