class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for i in range(len(strs)):
            l = list(strs[i])
            l.sort()
            key = ''.join(l)
            
            if not key in dictionary:
                dictionary[key]=[]
            dictionary[key].append(strs[i])

        res=[]

        for key,value in dictionary.items():
            res.append(value)
        
        return res

           
