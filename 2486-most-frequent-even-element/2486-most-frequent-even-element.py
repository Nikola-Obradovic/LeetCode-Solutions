class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        result=-1
        most=0
        for i in range(len(nums)):
            if nums.count(nums[i])>most and nums[i]%2==0:
                most=nums.count(nums[i])
                result=nums[i]
        return result    
