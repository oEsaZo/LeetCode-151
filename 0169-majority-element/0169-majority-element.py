class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        x = freq.most_common()
        for z,y  in x:
            if  y >= len(nums) / 2:
                return z