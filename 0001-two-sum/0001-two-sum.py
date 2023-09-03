class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        l[:]=nums
        nums.sort()
        i=0
        j=len(nums)-1
    

            
        while i<j:
            if nums[i]+nums[j]==target:
                if nums[i]==nums[j]:
                    for x in range(i+1, len(l)):
                        if nums[i]==l[x]:
                            return [l.index(nums[i]),x]


                return [l.index(nums[i]),l.index(nums[j])]
            if nums[i]+nums[j]<target:
                
                i+=1
            else:
                j-=1
                    