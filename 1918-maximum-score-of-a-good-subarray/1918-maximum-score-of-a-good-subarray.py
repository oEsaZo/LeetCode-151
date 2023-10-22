class Solution:
    def maximumScore(self, heights: List[int], k: int) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                j = stack[-1] + 1 if stack else 0
                w = i - j
                
                if j <= k and k <= i-1:
                    maxArea = max(maxArea, h * w)
            stack.append(i)

        i, j = k, k
        while i >= 0 and heights[i] >= heights[k]:
            i -= 1
        while j <= len(heights) and heights[j] >= heights[k]:
            j += 1
        maxArea = max(maxArea, heights[k] * (j - i - 1))
        
        return maxArea