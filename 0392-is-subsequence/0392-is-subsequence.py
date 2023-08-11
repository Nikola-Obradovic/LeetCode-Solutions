class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        
        prev_index = -1
        
        for i in range(len(s)):
            char = s[i]
            
            char_index = t.find(char, prev_index + 1)
            if char_index == -1:
                return False
            
            if i > 0 and char_index < prev_index:
                return False
            
            prev_index = char_index
            
            if s.count(char) > t.count(char):
                return False
        
        return True