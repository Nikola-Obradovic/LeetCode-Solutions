class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        maxdif=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]>maxdif:
                maxdif=nums[i+1]-nums[i]
        return maxdif
