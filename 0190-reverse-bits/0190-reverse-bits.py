class Solution:
    def reverse(self, s):
        return s[::-1]
    def reverseBits(self, n: int) -> int:
        s = format(n, '032b')
        s=self.reverse(s)
       
        return int(s,2)