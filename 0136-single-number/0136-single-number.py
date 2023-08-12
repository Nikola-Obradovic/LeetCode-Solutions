class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique=0
        for x in range(len(nums)):
            unique^=nums[x]
        return unique