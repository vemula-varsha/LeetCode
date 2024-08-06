class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_freq = [0] * 26

        for character in word:
            letter_freq[ord(character)-ord('a')] += 1

        letter_freq.sort(reverse=True)
        
        total_pushes=0

        for index, freq in enumerate(letter_freq):
            if freq == 0:
                break
            total_pushes += (index//8 + 1) * freq
        
        return total_pushes
