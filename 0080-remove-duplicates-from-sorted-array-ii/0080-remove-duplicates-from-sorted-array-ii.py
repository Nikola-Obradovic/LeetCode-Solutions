class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cnt=0
        x=0
        while x<len(nums):
            
            if x<len(nums)-1 and nums[x]==nums[x+1]:
                cnt+=1
                temp=nums[x]
                x+=1
                while x<len(nums)-1 and temp==nums[x+1]:
                    x+=1
                    nums[x]=100000
            else:
                x+=1
                cnt+=1
        nums.sort()
        return cnt