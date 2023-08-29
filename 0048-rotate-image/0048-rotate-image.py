class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=[]
        temp=[]
        
        j=0
        while len(l)<len(matrix):
            temp=[]
            i=len(matrix)-1
            while i>=0:
                temp.append(matrix[i][j])
                i-=1
            l.append(temp)
            del temp
            j+=1
        
        matrix[:] = l



