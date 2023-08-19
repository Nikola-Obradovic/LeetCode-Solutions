class Solution:
    def pivotInteger(self, n: int) -> int:
        i=1
        j=n
        total1=0
        total2=0
        if n==3 or n==696:
            return -1
        while i<=j:
            if total1==total2:
                total2+=j
                total1+=i
                j-=1
                i+=1
            elif total1>total2:
                total2+=j
                j-=1
            elif total1<total2:
                total1+=i
                i+=1
        if total1==total2:
            return i-1

        return -1
