class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False       
        nums.sort()
        if nums[0]!=1:
            return False

        if len(nums)<nums[len(nums)-1]:
            return False
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            return False

        for i in range(len(nums)-2):
            if nums[i]+1!=nums[i+1]:
                return False

        return True