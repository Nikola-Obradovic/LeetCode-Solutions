class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        finalnums=nums1+nums2
        finalnums.sort()
        num = len(finalnums)-1
        if num%2==0:
            return finalnums[int(num/2)]
        else: return (finalnums[int(num/2)]+finalnums[int(num/2+1)])/2 

