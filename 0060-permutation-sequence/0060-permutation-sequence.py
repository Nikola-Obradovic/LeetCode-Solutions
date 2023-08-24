from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s=""
        for i in range(1, n+1):
            s+=str(i)
        
        iterator = permutations(s)
        j=1

        for permutation in iterator:
            if j==k:
                return "".join(permutation)
            j+=1