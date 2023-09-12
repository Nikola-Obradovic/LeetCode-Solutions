import random
class Solution:


    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.flipped = {} 


    def flip(self) -> List[int]:
        while True:
            random_row = random.randint(0, self.m - 1)
            random_col = random.randint(0, self.n - 1)
            if (random_row, random_col) not in self.flipped:
                self.flipped[(random_row, random_col)] = 1     
           
                return [random_row, random_col]


    def reset(self) -> None:
        self.flipped = {}


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()