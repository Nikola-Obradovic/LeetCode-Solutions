class Solution:
    def romanToInt(self, s: str) -> int:
        dec = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res=0
        cnt=len(s)
        i=0
        while i < cnt:
            if i!=cnt-1 and dec[s[i]]<dec[s[i+1]]:
                res+=dec[s[i+1]]-dec[s[i]]
                i=i+2
            else:
                res+=dec[s[i]]
                i=i+1
               
        return res