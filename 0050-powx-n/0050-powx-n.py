class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        if n==0:
            return 1
        x1=x
        i=1
        j=abs(n)-1
        while i<=j:
            if i!=j:
                x*=x1*x1
            else:
                x*=x1
            i+=1
            j-=1
        
        if n>0:
            return x
        else:
            return 1./x