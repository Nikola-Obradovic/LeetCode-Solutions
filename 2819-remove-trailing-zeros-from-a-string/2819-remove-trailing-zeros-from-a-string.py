class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i=len(num)-1

        while num[i]=="0":
            num=num[:-1]
            i-=1
        return num