class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strlen=len(strs[0])
        size=len(strs) 
        value="" 
        found = True
        for x in range(len(strs)):
            if strlen > len(strs[x]):
                strlen = len(strs[x])
        for x in range(strlen):
            currstring=strs[0]
            value+=currstring[x]
            for i in range(size):
                currstring=strs[i]
                if value[x]!=currstring[x] and x==0:
                    value=""
                    found=False
                    break
                elif  value[x]!=currstring[x]:
                    found=False
                    break
            if not found:
                value=value[:-1]
                break    

        return value

        