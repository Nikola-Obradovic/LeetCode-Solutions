class Solution:
    def mySqrt(self, x: int) -> int:
        epsilon=1e-6
        res = x / 2 
        while abs(res * res - x) > epsilon:
            res = (res + x / res) / 2
        return int(res)