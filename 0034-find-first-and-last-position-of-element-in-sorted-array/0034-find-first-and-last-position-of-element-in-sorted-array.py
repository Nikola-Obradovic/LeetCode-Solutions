class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        if len(nums)<1:
            return [-1,-1]

        while low<=high:
            if nums[high]==target and nums[low]==target:
                return [low,high]
            mid=int((high+low)//2)
            if target<nums[mid]:
                high=mid-1
            if target>nums[mid]:
                low=mid+1
            if target==nums[mid]:
                i=mid
                j=mid
                while i>=0 and nums[mid]==nums[i]:
                    i-=1
                while j<len(nums) and nums[mid]==nums[j]:
                    j+=1
                return [i+1,j-1]
                
                
        return [-1,-1]