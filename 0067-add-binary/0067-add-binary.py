class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=""
        temp=0
        carry=0
        i=len(a)-1
        j=len(b)-1
     
        while i>=0 and j>=0:
            
            if a[i]=="0" and b[j]=="0":
                if carry>0:
                    s+="1"
                else: 
                    s+="0"
                carry=0

            if (a[i]=="1" and b[j]=="0") or (a[i]=="0" and b[j]=="1"):
                temp=1+carry
                if temp==2:
                    s+="0"
                    carry=1
                else:
                    s+="1"
                    
                temp=0
                
                
            if a[i]=="1" and b[j]=="1":
                temp=1+carry
                              
                if temp==2:
                    s+="1"
                else:
                    s+="0"
                temp=0
                carry=1
            i-=1
            j-=1
        i+=1
        j+=1
        x=abs(i-j)
        if x==0:
            if carry==1:
                s+="1"
            return s[::-1]
        x-=1
        if len(a)>len(b):
            while x>=0:
                if carry==1 and a[x]=="0":
                    s+="1"
                    carry=0
                elif carry==1 and a[x]=="1":
                    s+="0"
                    carry=1
                elif carry==0 and a[x]=="0":
                    s+="0"
                elif carry==0 and a[x]=="1":
                    s+="1"
                x-=1
        else:
           while x>=0:
                if carry==1 and b[x]=="0":
                    s+="1"
                    carry=0
                elif carry==1 and b[x]=="1":
                    s+="0"
                    carry=1
                elif carry==0 and b[x]=="0":
                    s+="0"
                elif carry==0 and b[x]=="1":
                    s+="1" 
                x-=1
        if carry==1:
            s+="1"
        
        return s[::-1]
        

             

