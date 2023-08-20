class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cnt = 0
        if len(nums) < 3:
            return 0
        
        length = 2 
        r = nums[1] - nums[0]
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == r:
                length += 1
            else:
                if length >= 3: 
                    cnt += (length - 2) * (length - 1) // 2  
                length = 2  
                r = nums[i] - nums[i-1]  
        
        if length >= 3:
            cnt += (length - 2) * (length - 1) // 2  
        
        return cnt