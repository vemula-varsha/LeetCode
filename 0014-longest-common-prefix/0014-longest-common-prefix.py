class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return  ""
        w=strs[0]
        for j in  range(1,len(strs)):
            cst=""
            n=min(len(w),len(strs[j]))
            for i in range(n):
                if w[i]==strs[j][i]:
                    cst+=w[i]
                else:
                    break
            w=cst
        return w
        