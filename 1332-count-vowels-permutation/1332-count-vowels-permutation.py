class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp_arr = [[0]*5 for _ in range(n+1)]
        dp_arr[1] = [1, 1, 1, 1, 1]
        for i in range(2, n+1):

            dp_arr[i][0] = dp_arr[i-1][1] + dp_arr[i-1][2] + dp_arr[i-1][4]

            dp_arr[i][1] = dp_arr[i-1][0] + dp_arr[i-1][2]

            dp_arr[i][2] = dp_arr[i-1][1] + dp_arr[i-1][3]

            dp_arr[i][3] = dp_arr[i-1][2]

            dp_arr[i][4] = dp_arr[i-1][2] + dp_arr[i-1][3]
        return sum(dp_arr[n])% ((10**9)+7)