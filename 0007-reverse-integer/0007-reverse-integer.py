class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x<0:
            sign = True
            x=abs(x)
            

        result=0

        while x!=0:
            lastdigit = x % 10
            if result > (2**31 - 1 - lastdigit) // 10:  
                return 0
            result = 10*result + lastdigit
            x=x//10

        if sign:
            return -1*result   
        else:
            return result 