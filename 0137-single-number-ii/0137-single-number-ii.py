class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if nums.count(nums[x])==1:
                return nums[x]