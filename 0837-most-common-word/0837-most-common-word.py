class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = [word.strip(string.punctuation).lower() for word in re.split(r'[ ,]+', paragraph) if word.strip(string.punctuation).isalpha()]
        commonword=""
        cnt=0
        for i in range(len(l)):
            temp=l.count(l[i])
            if temp>cnt and not l[i] in banned and not l[i].upper() in banned:
                cnt=temp
                commonword=l[i]
        
        return commonword
            

        

        