class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate=0
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate=nums.pop(i)     
                break
            else:
                seen.add(nums[i])
        nums.sort()

        value=1
        for i in range(len(nums)):
            if value!=nums[i]:
                return [duplicate,value]
            value+=1
        
        return [duplicate, nums[len(nums)-1]+1]
