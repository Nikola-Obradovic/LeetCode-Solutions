class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        if purchaseAmount%10==0:
            return 100-purchaseAmount
        
        cnt=0
        
        while purchaseAmount>4:

            cnt+=1
            purchaseAmount=purchaseAmount-10
        
       
        purchaseAmount=0
        while cnt>0:
            purchaseAmount+=10
            cnt-=1
        
        return 100-purchaseAmount