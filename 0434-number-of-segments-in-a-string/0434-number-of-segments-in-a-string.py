class Solution:
    def countSegments(self, s: str) -> int:
        if len(s)==1 and s[0]!=" ":
            return 1
           
        
        cnt=0
        for i in range(1, len(s)):
            if s[i]==" " and s[i-1]!=" ":
                cnt+=1
            if i==len(s)-1 and s[i]!=" ":
                cnt+=1

            
        return cnt