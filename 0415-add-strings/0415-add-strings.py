import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            res = 0
            for n in num:
                res = res*10 + ord(n) - ord('0')
            return res
        return str(str2int(num1) + str2int(num2))