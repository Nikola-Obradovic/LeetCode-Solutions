class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num=set(nums)
        n=len(nums)
        l=[]

        for i in range(1,n+1):
            if i not in num:
                l.append(i)
        return l

