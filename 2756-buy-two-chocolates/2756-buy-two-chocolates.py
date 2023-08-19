class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        temp=money
        temp=temp-prices[0]
        temp=temp-prices[1]

        if temp>=0:
            return temp
        
        return money