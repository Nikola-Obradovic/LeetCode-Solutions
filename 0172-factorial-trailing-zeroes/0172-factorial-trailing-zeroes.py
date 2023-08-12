import sys
sys.set_int_max_str_digits(1000000000)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        
        if n==0:
            return 0
        
        fact=1
        while n>1:
            fact=fact*n
            n-=1
        cnt=0
        s=str(fact)
        x=len(s)-1
        while x>=0:
            if s[x]=="0":
                cnt+=1
            else:
                return cnt
            x-=1
        return cnt