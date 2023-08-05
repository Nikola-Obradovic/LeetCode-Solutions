class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=[]
        nums2=nums[:]
        cnt=0
        for x in nums2:
            if x!=0:
                l.append(x)
            else:
                cnt+=1
        nums.clear()
        nums.extend(l)
        for x in range(cnt):
            nums.append(0)
        
        