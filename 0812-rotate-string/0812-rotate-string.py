class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        slist=list(s)
        goallist=list(goal)
        for i in range(len(slist)):
            
            temp=slist.pop(0)
            slist.append(temp)
            if slist==goallist:
                return True
        return False

        