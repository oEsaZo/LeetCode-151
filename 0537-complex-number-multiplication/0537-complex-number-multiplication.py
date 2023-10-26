class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = num1.split('+')
        r1 = int(r1)
        i1 = int(i1[:-1])
        r2, i2 = num2.split('+')
        r2 = int(r2)
        i2 = int(i2[:-1])
        return str(r1*r2 - i1*i2 ) + '+' + str(r1*i2 + r2*i1) + 'i'