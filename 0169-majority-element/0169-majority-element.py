class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total=0
        cnt=0
        l=[]
        for x in nums:
            if x in l:
                continue
            if nums.count(x)>cnt:
                cnt=nums.count(x)
                total=x
                l.append(x)
        return total