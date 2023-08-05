class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        lowest=100000000
        
        for x in prices:
            found=True
            if x<lowest:
                lowest=x
            elif x-lowest>profit:
                profit=x-lowest
        return profit