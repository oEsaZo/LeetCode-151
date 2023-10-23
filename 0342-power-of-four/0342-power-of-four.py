import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            ans = math.log(n, 4)
            return ans.is_integer()
        return False
