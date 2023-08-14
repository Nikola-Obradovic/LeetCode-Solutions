class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total=0
        
        while nums!=[]:
            
            cnt=int(len(str(nums[len(nums)-1])))

            if len(nums)>1:
                while cnt>0:
                    nums[0]*=10
                    cnt-=1
                total+=nums[0]+nums[len(nums)-1]
            if len(nums)==1:
                total+=nums[0]
            if len(nums)>1:
                del nums[0]
            del nums[len(nums)-1]
        return total


