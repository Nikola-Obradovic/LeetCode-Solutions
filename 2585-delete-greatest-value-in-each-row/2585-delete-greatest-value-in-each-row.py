
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        l = []
        
        for row in range(len(grid)):
            grid[row].sort()

        total = 0
     
        x = len(grid[0]) - 1

        while x >= 0:
            i = len(grid) - 1
            temp = 0
            
            while i >= 0:
                if grid[i][x] > temp:
                    temp = grid[i][x]
                i -= 1

            
           
            l.append(temp)
          
              
            x -= 1

        for j in l:
            total += j

        return total
            
        
