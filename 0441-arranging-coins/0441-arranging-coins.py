class Solution:
    def arrangeCoins(self, n: int) -> int:
        row=0
        i=1
        while n>0:
            n-=i
            row+=1
            i+=1
        if n<0:
            return row-1
        return row


