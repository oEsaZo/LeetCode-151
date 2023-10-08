class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        n = len(x)
        if n == len(nums):
            return False 
        else:
            return True
        #     return True 
        # else:
        #     return False