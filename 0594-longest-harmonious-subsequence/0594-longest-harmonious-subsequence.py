class Solution:
    def findLHS(self, nums: List[int]) -> int:
        total=0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                if total<nums.count(nums[i])+nums.count(nums[i+1]):
                    total=nums.count(nums[i])+nums.count(nums[i+1])
            else:
                continue

        return total 