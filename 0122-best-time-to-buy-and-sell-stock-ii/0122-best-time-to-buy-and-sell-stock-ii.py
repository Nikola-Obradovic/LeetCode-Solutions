class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        
        x=1

        while x<len(prices):
            if prices[x]>prices[x-1]:
                profit+=prices[x]-prices[x-1]
            x+=1
        return profit