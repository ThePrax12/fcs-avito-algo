import pytest
from LCS import lcs


def is_subseq(sub, s):
    j = 0
    for ch in s:
        if j < len(sub) and sub[j] == ch:
            j += 1
    return j == len(sub)


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("AGGTAB", "GXTXAYB", "GTAB"),
        ("", "abc", ""),
        ("abc", "", ""),
        ("abc", "def", ""),
        ("aaaa", "aa", "aa"),
        ("abcd", "abcd", "abcd"),
        ("abcde", "ace", "ace"),
        ("axbxcxd", "abcd", "abcd"),
        ("ABCBDAB", "BDCABA", "BCBA"),
        ("aaaaaaaa", "baaaac", "aaaa"),
    ],
)
def test_lcs_exact_cases(s1, s2, expected):
    got = lcs(s1, s2)
    assert got == expected
    assert is_subseq(got, s1)
    assert is_subseq(got, s2)


@pytest.mark.parametrize(
    "s1, s2, exp_len",
    [
        ("abcbdab", "bdcaba", 4),
        ("XMJYAUZ", "MZJAWXU", 4),
        ("abab", "baba", 3),
    ],
)
def test_lcs_length_and_validity(s1, s2, exp_len):
    got = lcs(s1, s2)
    assert len(got) == exp_len
    assert is_subseq(got, s1)
    assert is_subseq(got, s2)


def test_symmetry_length():
    s1 = "banana"
    s2 = "ananas"
    a = lcs(s1, s2)
    b = lcs(s2, s1)
    assert len(a) == len(b)
