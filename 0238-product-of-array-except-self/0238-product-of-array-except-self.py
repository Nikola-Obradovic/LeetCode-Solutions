class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        prod=1

        for x in nums:
            l.append(prod)
            prod*=x
        prod=1
        x=len(nums)-1
        while x>=0:
            l[x]=l[x]*prod
            prod*=nums[x]
            x-=1


        


        return l