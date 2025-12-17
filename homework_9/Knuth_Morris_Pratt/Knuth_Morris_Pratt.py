def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []

    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    res = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                res.append(i - m + 1)
                j = pi[j - 1]
    return res
