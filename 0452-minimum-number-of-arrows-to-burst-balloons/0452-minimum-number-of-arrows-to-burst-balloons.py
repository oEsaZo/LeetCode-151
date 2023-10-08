class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrows = 1
        x = points[0][1]
        for i in range(len(points)):
            if x >= points[i][0] and x <= points[i][1]:
                continue
            else:
                arrows +=1
                x = points[i][1]
        return arrows
        
        