class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in range(len(details)):
            w=details[i]
            if(int(w[11:13])>60):
                c+=1
        return c