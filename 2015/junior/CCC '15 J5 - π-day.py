def partitions_dp(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 1 way to partition 0 into 0 parts

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i >= j:
                dp[i][j] = dp[i - j][j] + dp[i - 1][j - 1]

    return dp[n][k]


n, k = int(input()), int(input())
print(partitions_dp(n, k))
