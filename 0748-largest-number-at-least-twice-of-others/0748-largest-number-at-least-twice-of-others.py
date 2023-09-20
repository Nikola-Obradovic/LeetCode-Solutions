class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        largest=-1
        index=-1
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
                index=i
        nums.pop(index)
        slargest=-1
        for i in range(len(nums)):
            if nums[i]>slargest:
                slargest=nums[i]
                
        if slargest*2<=largest:
            return index
        return -1