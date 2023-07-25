class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        newstring = ""
        
        for character in s:
            if character in newstring:
                cnt = max(cnt, len(newstring))
                newstring = newstring[newstring.index(character) + 1:]
            
            newstring += character
        
        cnt = max(cnt, len(newstring))
        return cnt

               

