from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1))
        j = list(permutations(nums))
        i = j[k-1]
        return "".join(str(x) for x in i)