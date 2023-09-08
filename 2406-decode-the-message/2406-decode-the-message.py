class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        asciichar=97
        dictionary={}
        res=""
        for i in range(len(key)):
            if key[i]==" ":
                continue
            elif not key[i] in dictionary:
                dictionary[key[i]]=chr(asciichar)
                asciichar+=1

        for i in range(len(message)):
            if message[i]==" ":
                res+=" "
            
            else: 
                res+=dictionary.get(message[i])
        
        return res

        