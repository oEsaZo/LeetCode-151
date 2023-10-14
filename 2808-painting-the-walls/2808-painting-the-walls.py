class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[0x3f3f3f3f3f3f for i in range(n+1)]for j in range(n+1)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(n+1):
                t = min(n, j + time[i] + 1)
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                dp[i+1][t] = min(dp[i+1][t], dp[i][j] + cost[i])
        return dp[n][n]