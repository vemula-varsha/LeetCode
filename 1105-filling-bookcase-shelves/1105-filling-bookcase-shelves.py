class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        d = [float('inf')] * (n + 1)
        d[0] = 0

        for i in range(1, n + 1):
            tt = 0
            mh= 0
            for j in range(i, 0, -1):
                tt += books[j - 1][0]
                if tt > shelfWidth:
                    break
                mh = max(mh, books[j - 1][1])
                d[i] = min(d[i], d[j - 1] + mh)

        return d[n]

        