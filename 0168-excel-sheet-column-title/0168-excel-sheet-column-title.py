class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            res = chr(ord('A') + (columnNumber - 1) % 26) + res
            columnNumber = (columnNumber - 1) // 26
        return res
        