class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        a=Counter(nums).most_common()
        a.sort(key=lambda x:-x[1])
        for i in range(len(a)):
            if a[i][0]%2==0:
                return a[i][0]
        return -1