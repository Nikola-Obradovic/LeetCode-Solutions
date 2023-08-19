class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l=sentence.split()
        thefirst=l[0][0]
        last=l[0][len(l[0])-1]
        i=0
        while i<len(l)-1:
            if last!=l[i+1][0]:
                return False
            last=l[i+1][len(l[i+1])-1]
            i+=1
        
        if last==thefirst:
            return True
        return False