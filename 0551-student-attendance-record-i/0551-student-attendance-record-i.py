class Solution:
    def checkRecord(self, s: str) -> bool:
        abscnt=0
        latecnt=0

        for i in range(len(s)):
            if s[i]=="P":
                latecnt=0
            if s[i]=="A":
                latecnt=0
                abscnt+=1
            if s[i]=="L":
                latecnt+=1
            if latecnt==3:
                return False
            if abscnt==2:
                return False
        return True    
