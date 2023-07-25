class Solution:
    
    def Convert(self, s):
        number=0
        newnum=0
        found = True
        for i in s:
            for x in range(10):
                if str(x)==i:
                    number=number*10+x

        

        if(s[0]=="-"):
            return -1*number            
        return number            


    
    def myAtoi(self, s: str) -> int:
        newstring=""
        opcounter=0

        for x in range(len(s)):
            if s[x].isdigit():
                break
            if s[x]=="+" or s[x]=="-":
                
                if x>0 and x<len(s)-1 and (s[x-1]=="+" or s[x-1]=="-" or s[x+1].isspace()):
                    return 0
                    

        for x in range(len(s)):
            
            if x>0 and not s[x].isdigit() and s[x-1].isdigit():
                break
            if s[x].isalpha() or s[x]==".":
                break
            if not s[x].isspace():
                if newstring!="" or s[x]!="0":
                    newstring+=s[x]
        
        if newstring=="":
            return 0

        

        result = self.Convert(newstring)

        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result
        
