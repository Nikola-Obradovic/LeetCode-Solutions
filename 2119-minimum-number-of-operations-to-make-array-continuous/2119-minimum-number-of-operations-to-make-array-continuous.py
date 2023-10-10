class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))  

        res = n
        for i, start in enumerate(nums):
            end = start + n - 1  
            index = bisect_right(nums, end)  
            uniqueLen = index - i
            res = min(res, n - uniqueLen)
        return res
