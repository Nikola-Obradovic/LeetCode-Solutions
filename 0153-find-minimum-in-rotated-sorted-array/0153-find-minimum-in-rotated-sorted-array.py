class Solution:
    def findMin(self, nums: List[int]) -> int:
        first=0
        last=len(nums)-1
        mid=0
        if len(nums)==1:
            return nums[0]
        while first<=last:
            mid=(first+last)//2
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]

            if nums[last]>nums[mid]:
                last=mid
            if nums[last]<nums[mid]:
                first=mid
        
        