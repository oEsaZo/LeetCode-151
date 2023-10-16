class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1
        for i in range(20):
            temp = res
            res = temp - (temp**2 - x)/(2*temp)
        return math.floor(res)