class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zerocount = s.count("0")
        onecount = s.count("1")
        comparison=""
        time=0
        l=list(s)
        complist=[]
        for i in range(onecount):
            complist.append("1")
        for i in range(zerocount):
            complist.append("0")
        
       
        
        while l!=complist:
            i=0
            while i<len(l)-1:
                if l[i]=="0" and l[i+1]=="1":
                    l[i]="1"
                    l[i+1]="0"
                    i+=1
                i+=1
            time+=1
        
        return time


        