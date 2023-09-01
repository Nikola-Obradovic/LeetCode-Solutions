class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l=[]
        temp=[]
        c1=c
        
        for i in range(len(mat)):
            
    
            for j in range(len(mat[0])):
                if c>0:
                    temp.append(mat[i][j])
                    c-=1
                    
                if c==0:
                    l.append(list(temp))
                    temp=[]
                    c=c1
                    r-=1
                    
        if r!=0:
            return mat

        return l