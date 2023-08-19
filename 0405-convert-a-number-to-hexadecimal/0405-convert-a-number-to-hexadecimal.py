class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return hex(num)[2:]
        else:
            twos_complement = 2 ** 32 + num
            return hex(twos_complement)[2:]