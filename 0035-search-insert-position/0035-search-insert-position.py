class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(len(nums)):
            if nums[x]==target:
                return x
        
        for x in range(len(nums)-1):
            if target>nums[x] and target<nums[x+1]:
                return x+1
        
        if target < nums[0]:
            return 0
        return len(nums)