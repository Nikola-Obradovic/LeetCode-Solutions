class Solution:
    def makeFancyString(self, s: str) -> str:
        result=""
        cnt= 1
        i= 1

        while i < len(s):
            if s[i] == s[i - 1]:
                cnt+= 1
            else:
                cnt = 1
            
            if cnt < 3:
                result+=s[i - 1]
            i += 1
        
        
        result+=s[-1]  
        
        return result







        