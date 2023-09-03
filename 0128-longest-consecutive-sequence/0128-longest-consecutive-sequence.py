class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums==[]:
            return 0

        nums.sort()

        cnt=0
        tempcnt=1
        for i in range(len(nums)-1):
            
            if nums[i]+1==nums[i+1]:
                tempcnt+=1
            elif nums[i]==nums[i+1]:
                continue


            else:
                if cnt<tempcnt:
                    cnt=tempcnt
                tempcnt=1
        
        if cnt<tempcnt:
            cnt=tempcnt
        return cnt