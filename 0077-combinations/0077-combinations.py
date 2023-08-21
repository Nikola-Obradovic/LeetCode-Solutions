from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[]
        for x in range(1, n+1):
            l.append(x)
        return list(combinations(l, k))
        
