class Solution:
    def minSteps(self, n: int) -> int:

        if n==1:
            return 0
        cnt=0
        copy=1
        char=0
        while char!=n:
            if char>copy and n%char==0:
                copy=char
                cnt+=1
            else:
                char+=copy
                cnt+=1
        
        return cnt
            

        

        