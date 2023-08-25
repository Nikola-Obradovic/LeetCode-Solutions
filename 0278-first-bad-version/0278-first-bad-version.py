# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n+1
        while low<=high:
            mid=(high+low)//2
            if isBadVersion(mid)==True and isBadVersion(mid-1)==False:
                return mid
            elif isBadVersion(mid)==False and isBadVersion(mid+1)==True:
                return mid+1
            elif isBadVersion(mid)==True:
                high=mid-1
            else:
                low=mid+1
        
