class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        l=[]
        even=0
        odd=0
        temp=[]
        binary=bin(n)
        binary=binary[2:]

        i=len(binary)-1
        j=0

        while i>=0:
            if binary[i]=="1":
                if j%2==0:
                    even+=1
                else:
                    odd+=1
            i-=1
            j+=1
        l.append(even)
        l.append(odd)
        return l
