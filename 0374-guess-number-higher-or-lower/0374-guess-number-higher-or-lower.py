# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i=1
        j=n
        while True:
            middle=(i+j)//2
            temp = guess(middle)
            if temp==0:
                return middle
            if temp==-1:
                j=middle-1
            if temp==1:
                i=middle+1
            
            