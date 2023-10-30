class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
   
        n = len(arr)
        res = [0] * n
        for i in range(n):
            res[i] = self.countBit(arr[i]) * 10001 + arr[i]
        res.sort()
        for i in range(n):
            res[i] %= 10001
        return res

    def countBit(self, n):
        res = 0
        while n != 0:
            res += (n & 1)
            n >>= 1
        return res