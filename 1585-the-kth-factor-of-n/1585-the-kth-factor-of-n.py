class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        factors = []
        while i <=n:
            if n%i == 0:
                factors.append(i)
                i+=1
            else:
                i+=1
        if k > len(factors):
            return -1
        return factors[k-1]