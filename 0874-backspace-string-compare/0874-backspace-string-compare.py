class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sl=[]
        tl=[]
        for i in range(len(s)):

            if s[i]!="#":
                sl.append(s[i])
            elif sl!=[]: 
                sl.pop()
            
        for i in range(len(t)):
            if t[i]!="#":
                tl.append(t[i])
            elif tl!=[]:
                tl.pop()
        
        return sl==tl
        