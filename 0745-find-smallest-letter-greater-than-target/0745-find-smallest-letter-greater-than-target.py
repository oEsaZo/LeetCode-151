class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters = sorted(set(letters))
        idx = letters.index(target)
        if max(letters) == target:
            return letters[0]
        return letters[idx+1]