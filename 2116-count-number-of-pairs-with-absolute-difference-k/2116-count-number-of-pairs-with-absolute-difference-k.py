class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt=0
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if abs(nums[i]-nums[j])==k:
                    cnt+=1
        
        return cnt
        