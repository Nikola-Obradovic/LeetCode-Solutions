import copy
class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        c=1

        for i in range(1,n):
            c=a
            a=a+b
            b=c
        
        return a

        



