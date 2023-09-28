class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i in range(len(words)-1):
            
            for j in range(len(words[i])):
                if j<len(words[i+1]) and order.index(words[i][j])>order.index(words[i+1][j]):
                    return False
                elif j<len(words[i+1]) and order.index(words[i][j])<order.index(words[i+1][j]):
                    break
            if words[i+1] in words[i] and words[i+1]!=words[i]:
                return False
        return True

        