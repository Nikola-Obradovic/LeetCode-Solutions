class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
 
        
        dividendsign=1
        divisorsign=1
        if dividend<0:
            dividendsign=-1
        if divisor<0:
            divisorsign=-1
        
        return int(abs(dividend)//abs(divisor))*dividendsign*divisorsign