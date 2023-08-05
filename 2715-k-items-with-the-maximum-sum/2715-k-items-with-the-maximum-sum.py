class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        l=[]
        for x in range(numOnes):
            l.append(1)
        for x in range(numZeros):
            l.append(0)
        for x in range(numNegOnes):
            l.append(-1)
        x=0
        total=0
        while x<k:
            total+=l[x]
            x+=1
        return total
