class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0

        count = 0
        multiplier = 1  

        while n >= multiplier:
            quotient = n // (multiplier * 10)
            remainder = n % (multiplier * 10)

           
            count += quotient * multiplier
            count += min(max(remainder - multiplier + 1, 0), multiplier)

            multiplier *= 10

        return count


        