class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        s = 0
        while left < right:
            left >>=1
            right >>=1
            s += 1

        return left << s