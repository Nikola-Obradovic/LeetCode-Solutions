class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        l=[]
        l2=[]
        for i in range(len(s)):
            l.append(s[i])
            if not s[i] in l2:
                l2.append(s[i])

        temp=l.count(l2[0])
        for i in l2:
            if l.count(i)!=temp:
                return False
        return True

        


        