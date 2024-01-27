class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            cumsum = 0
            for j in range(k+1):
                if j == 0:
                    dp[i][j] = 1
                    cumsum += 1
                else:
                    cumsum += dp[i-1][j]
                    if j-i >= 0:
                        cumsum -= dp[i-1][j-i]
                    dp[i][j] = cumsum % 1000000007
        return dp[n][k]