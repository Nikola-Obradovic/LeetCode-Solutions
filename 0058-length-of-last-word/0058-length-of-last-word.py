class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if " " not in s:
            return len(s)
      
        
        words=s.split()
        lastword=words[len(words)-1]

        return len(lastword)



        