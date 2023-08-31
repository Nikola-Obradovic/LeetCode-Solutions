class Solution:
    def Reverse(self,s):
        return s[::-1]
    def reverseWords(self, s: str) -> str:
        l=s.split()
        news=""

        for i in range(len(l)):
            news+=self.Reverse(l[i])
            if i!=len(l)-1:
                news+=" "
        return news