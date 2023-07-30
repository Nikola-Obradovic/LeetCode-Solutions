class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        templist=[1]
        templist2=[]
        result=[]
        i=0
        while i<=rowIndex:
            for x in range(len(templist)):
                if x==0:
                    templist2.append(1)
                
                if len(templist)>1 and x>0:
                    templist2.append(templist[x]+templist[x-1])
                if x==len(templist)-1 and i!=0:
                    templist2.append(1)
            
            
            result.append(templist2)
            templist=templist2
            templist2=[]
            i+=1
        
        return result[len(result)-1]