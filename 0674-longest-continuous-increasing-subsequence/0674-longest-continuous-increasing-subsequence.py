class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest=1
        temp=1
        i=0
        while i < len(nums)-1:
            if nums[i]<nums[i+1]:
                temp+=1
            else:
                if longest<temp:
                    longest=temp
                temp=1
            i+=1
        
        if longest<temp:
            longest=temp
        return longest
                    
            


        