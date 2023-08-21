class Solution:
    def findMin(self, nums: List[int]) -> int:
        found=False
        num=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                num=nums[i+1]
                found=True
        if found:
            return num
        return nums[0]