class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=len(s)-1
        l=[]
        while i>=0:
            l.append(s[i])
            i-=1
        
        s[:]=l

        
        