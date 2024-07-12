class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for i in words:
            if x in i:
                l.append(words.index(i))
            words[words.index(i)]="0"
        return l
            