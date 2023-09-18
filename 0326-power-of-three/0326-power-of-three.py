class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num=1

        while num<abs(n):
            num*=3

        return num==n
        