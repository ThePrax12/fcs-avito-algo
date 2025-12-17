def rabin_karp(text, pattern, base=13377331, mod=1000000007):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    #полиномиальный хеш
    def build_hash(s):
        h = 0
        for ch in s:
            h = (h * base + ord(ch)) % mod
        return h

    p_hash = build_hash(pattern)
    w_hash = build_hash(text[:m])

    power = pow(base, m - 1, mod)
    res = []

    for i in range(n - m + 1):
        if w_hash == p_hash:
            if text[i:i + m] == pattern:
                res.append(i)

        if i < n - m:
            left = ord(text[i])
            right = ord(text[i + m])

            w_hash = (w_hash - left * power) % mod
            w_hash = (w_hash * base + right) % mod

    return res
