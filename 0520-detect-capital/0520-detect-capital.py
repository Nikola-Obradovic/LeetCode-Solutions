class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allupper=True
        for i in range(len(word)):
            if word[i]!=word[i].upper():
                allupper=False
                break
        if allupper:
            return True
        
        for i in range(len(word)):
            if i!=0 and word[i]==word[i].upper():
                return False
        return True
