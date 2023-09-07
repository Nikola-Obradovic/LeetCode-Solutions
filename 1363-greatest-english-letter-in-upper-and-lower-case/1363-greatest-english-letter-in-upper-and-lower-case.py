class Solution:
    def greatestLetter(self, s: str) -> str:
        
        res=""

        for i in range(len(s)):
            if s[i]==s[i].upper():
                if (s[i].lower() in s and res=="") or (s[i].lower() in s and res<s[i]):
                    res=s[i]

        return res  
