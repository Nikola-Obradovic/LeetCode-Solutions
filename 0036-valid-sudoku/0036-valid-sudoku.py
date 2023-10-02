class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i=0
        j=0
        
        while i<len(board):
            l=[]
            l2=[]
            for k in range(len(board)):
                
                if board[k][j].isdigit() and not board[k][j] in l:
                    l.append(board[k][j])
                elif board[k][j].isdigit() and board[k][j] in l:
                    return False 
            for m in range(len(board[i])):
                if board[i][m].isdigit() and not board[i][m] in l2:
                    l2.append(board[i][m])
                elif board[i][m].isdigit() and board[i][m] in l2:
                    return False
            i+=1
            j+=1

       
        
        start=0
        end=3
        while end<=9:
            end2=3
            start2=0
            while end2<=9:
                l=[]
                
                for k in range(start, end):
                    for m in range(start2, end2):
                        if board[k][m].isdigit() and not board[k][m] in l:
                            l.append(board[k][m])
                        elif board[k][m].isdigit() and  board[k][m] in l:
                            return False
                
                end2+=3
                start2+=3
            start+=3
            end+=3


    
        return True