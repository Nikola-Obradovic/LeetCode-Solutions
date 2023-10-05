class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=int(len(nums)//3+0.5)
        l=[]
        
        while nums!=[]:
            value=nums[0]
            if nums.count(value)>n:
                l.append(value)
            
            while value in nums:
                nums.remove(value)
        
        return l