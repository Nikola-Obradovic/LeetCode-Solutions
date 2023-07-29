


class Solution:
  
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)
        cnt=0
        for x in nums:
            if x==val:
                k-=1

        j = len(nums)-1        
        for x in range(len(nums)):
            if nums[j]==val:
                while j>=0 and nums[j]==val:
                    j-=1
            if nums[x]==val and nums[j]!=val:
                temp = nums[x]
                nums[x] = nums[j]
                nums[j]= nums[x]
                j-=1
            
        

        


        return k