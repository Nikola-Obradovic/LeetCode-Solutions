class Solution:
    def isHappy(self, n: int) -> bool:
        sum1=0
        if n==7:
            return True
        while n>9:
            while n>0:
                sum1+=(n%10)*(n%10)
                n=n//10
            n=sum1
            if n==7:
                return True
            sum1=0
        return n==1
        
            

        