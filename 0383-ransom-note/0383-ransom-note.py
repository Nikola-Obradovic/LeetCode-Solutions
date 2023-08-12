class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote in magazine:
            return True

        for i in range(len(ransomNote)):
            if not ransomNote[i] in magazine:
                return False
            if ransomNote.count(ransomNote[i])>magazine.count(ransomNote[i]):
                return False
        
        return True
