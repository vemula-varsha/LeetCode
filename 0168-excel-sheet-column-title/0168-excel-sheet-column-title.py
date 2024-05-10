class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            result = chr(ord('A') + digit) + result
            columnNumber //= 26
        return result