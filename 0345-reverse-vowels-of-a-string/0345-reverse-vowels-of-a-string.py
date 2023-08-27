class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                temp=s[j]
                s[j]=s[i]
                s[i]=temp
                i+=1
                j-=1
            if not s[i] in vowels:
                i+=1
            if not s[j] in vowels:
                j-=1
        return "".join(s)             
            
