class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        j=0
        for i in range(len(operations)):
            if operations[i]=="C":
                l.pop()
                j-=1
            elif operations[i]=="D":
                l.append(int(l[j-1])*2)
                j+=1
            elif operations[i]=="+":
                l.append(int(l[j-1])+int(l[j-2]))
                j+=1
            else:
                l.append(int(operations[i]))
                j+=1
        
        total=0

        for i in l:
            total+=i
        return total
        