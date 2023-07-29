class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pair=[]
        index=0
        if numRows==1:
            return s
        for x in s:
            
            pair.append(x)
            pair.append(index)
            index+=1
            

        string=""
        
        cnt=0
        maxcnt=numRows+numRows-3
        newmax=numRows+numRows-2
        while cnt<=maxcnt:
            for x in range(len(pair)):
                if isinstance(pair[x], (int, float)) and (cnt == pair[x] or (cnt > 0 and maxcnt==pair[x]) or cnt == pair[x] % newmax or (cnt > 0 and maxcnt==pair[x]%newmax)):
                    string+=pair[x-1]
       
            if cnt>0:
                 maxcnt-=1
            cnt+=1
                      

        return string

