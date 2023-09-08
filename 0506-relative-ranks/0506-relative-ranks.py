class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=[]
        temp=[]
        temp[:]=score
        temp.sort()
        temp.reverse()


        for i in range(len(score)):
            if temp.index(score[i])==0:
                l.append("Gold Medal")
            elif temp.index(score[i])==1:
                l.append("Silver Medal")
            elif temp.index(score[i])==2:
                l.append("Bronze Medal")
            else:
                l.append(str(temp.index(score[i])+1))
        return l

            

        