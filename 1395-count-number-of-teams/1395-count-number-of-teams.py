class Solution:
    def numTeams(self, rating: List[int]) -> int:
        c=0
        for i in range(len(rating)):
            ls=lb=rs=rb=0
            for j in range(i):
                if(rating[j]<rating[i]):
                    ls+=1
                elif rating[j]>rating[i]:
                    lb+=1
            for k in range(i+1,len(rating)):
                if rating[k]>rating[i]:
                    rb+=1
                elif rating[k]<rating[i]:
                    rs+=1
            c+= ls*rb +lb*rs
        return c
                    
            
        