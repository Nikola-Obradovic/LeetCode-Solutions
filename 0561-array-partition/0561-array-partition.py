class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total=0
        nums.sort()
        i=0
        while i <len(nums)-1:
            total+=min(nums[i],nums[i+1])
            i+=2
        return total