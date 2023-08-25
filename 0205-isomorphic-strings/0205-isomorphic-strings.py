class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}

        for i in range(len(s)):
            if not s[i] in d and not t[i] in d.values():
                d[s[i]]=t[i]
        
        
            elif d.get(s[i])==t[i]:
                continue
            else:
                return False
        return True
