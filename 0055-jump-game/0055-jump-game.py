class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x=0
        cnt=nums[x]
        while len(nums)>1:
            if nums[x]==0:
                return False
            temp=nums[x]
            y=0
            while y<temp:
                cnt-=1
                x+=1
                if x==len(nums)-1:
                    return True
                if nums[x]>=temp or nums[x]>cnt:
                    cnt=nums[x]
                    temp=nums[x]
                    y=-1
                y+=1
                
            
        return True