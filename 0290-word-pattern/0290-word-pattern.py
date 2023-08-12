class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
     
        
        dictionary={}
        l=s.split()
        
        if len(pattern)!=len(l):
            return False
        for x in range(len(l)):
            if not l[x] in dictionary.values():
                dictionary[pattern[x]]=l[x]
           

        for x in range(len(l)):
            if not pattern[x] in dictionary or l[x]!=dictionary[pattern[x]]:
                return False
        return True