class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total=0
        div=0
        for i in range(len(nums)):
            if nums[i]%6==0:
                total+=nums[i]
                div+=1
        if div==0:
            return 0
        
        return int(total//div)