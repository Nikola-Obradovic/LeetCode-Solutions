class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        i = len(l)-1
        res=""
        while i>=0:
            if i!=0:
                res+=l[i]
                res+=" "
            else:
                res+=l[i]
            i-=1
        return res
            

