class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=""
        max_length=0
        for i in s:
            if i not in char :
                char+=i
            else:
                max_length = max(max_length, len(char))
                char = char[char.index(i) + 1:] + i
        return max(max_length, len(char))
        