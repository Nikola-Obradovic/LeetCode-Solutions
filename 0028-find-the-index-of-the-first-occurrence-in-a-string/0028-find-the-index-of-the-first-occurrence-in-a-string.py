class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        if not needle:
            return 0
        s=""
        res = -1
        cnt = 0
        n = len(needle)
        x=0
        while x< len(haystack):
            if cnt < n and needle[cnt] == haystack[x]:
                s+=needle[cnt]
                if cnt == 0:
                    res = x
                cnt += 1
                if cnt == n:
                    return res
            elif cnt < n and needle[cnt] != haystack[x]:
                
                
                res=-1
                if needle[0] == haystack[x-1] or needle[0] == haystack[x]:
                    x-=cnt
                cnt = 0
                s=""
            x+=1
        
        if len(s)!=len(haystack)-res-1:
            return -1
        return res