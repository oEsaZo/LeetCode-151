class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        last_fall_time = 0
        for left_position in left:
            last_fall_time = max(last_fall_time, left_position)
        
        for right_position in right:
            last_fall_time = max(last_fall_time, n - right_position)
        
        return last_fall_time