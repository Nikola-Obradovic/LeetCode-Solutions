class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        cnt=len(l)
        for i in range(len(l)):
            for j in range(len(brokenLetters)):
                if brokenLetters[j] in l[i]:
                    cnt-=1
                    break

        return cnt 

        