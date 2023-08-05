class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for x in range(k):
            temp=nums.pop()
            nums.insert(0,temp)