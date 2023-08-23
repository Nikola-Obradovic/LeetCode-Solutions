class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        oldx=0
        temp=0
        x=1
        for i in range(n-1):
            temp=x
            x+=oldx
            oldx=temp
        
        return x