class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for x in s:
            if not x in t:
                return False
            if s.count(x)!=t.count(x):
                return False
        return True
        