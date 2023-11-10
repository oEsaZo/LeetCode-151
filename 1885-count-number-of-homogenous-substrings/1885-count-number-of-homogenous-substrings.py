class Solution:
    def countHomogenous(self, s: str) -> int:
        ans, l = 0, 0

        for r, c in enumerate(s):
            if c == s[l]:
                ans += r-l +1
            else:
                l = r
                ans += 1
        return ans % (pow(10, 9) + 7)