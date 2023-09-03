class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0]

        for i in range(1, n+1):
            binary = str(bin(i)[2:])
            l.append(binary.count("1"))

        return l

        
        