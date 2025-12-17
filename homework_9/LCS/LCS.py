def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = dp[i + 1][j] if dp[i + 1][j] >= dp[i][j + 1] else dp[i][j + 1]

    # восстановление одной LCS
    i, j = n, m
    ans = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans.append(s1[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    ans.reverse()
    return "".join(ans)
