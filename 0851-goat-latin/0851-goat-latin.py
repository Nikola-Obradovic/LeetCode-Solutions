class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels="AEIOUaeiou"
        l=sentence.split()
        s=""
        
        for i in range(len(l)):
            if not l[i][0] in vowels:
                s+=l[i][1:]
                s+=l[i][0]
                s+="ma"
            
            elif l[i][0] in vowels:
                s+=l[i]
                s+="ma"
            for j in range(i+1):
                s+="a"
            if i!=len(l)-1:
                s+=" "
        return s
            

                




        