class Solution:
    def countBits(self, N: int) -> List[int]:
        stem = [0]
        while len(stem) < N+1:
            stem.extend([s + 1 for s in stem])
            
        return stem[:N+1]
        