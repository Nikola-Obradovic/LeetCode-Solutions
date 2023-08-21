class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        mid=0
        found=False
        while first<=last:
            mid=(first+last)//2
            if target<nums[mid]:
                last=mid-1
            if target>nums[mid]:
                first=mid+1
            if target==nums[mid]:
                found=True
                break
        if found:
            return mid
        return -1
