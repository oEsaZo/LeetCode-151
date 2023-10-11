class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums == [1]:
            return 0
        n = max(nums)
        
        ssum = n*(n+1)//2
        if sum(nums) == ssum and 0 in nums:
            return max(nums) + 1
        else:
            return ssum - sum(nums)