class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target not in nums:
            res.append(-1)
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        return [min(res), max(res)]

            
