class Solution:
    def findNthDigit(self, n: int) -> int:
        d = 1
        base = 0
        while n > 9*10**(d-1)*d + base:
            base += 9*10**(d-1)*d
            d+=1
        number = (10**(d-1)-1)+(n-base)//d
        number = int(number)
        rmd = (n-base)%d
        if rmd == 0:
            return int(str(number)[-1])
        else:
            return int(str(number+1)[rmd-1])        