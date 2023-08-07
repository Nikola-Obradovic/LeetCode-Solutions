class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        current=0
        maxr=0
        jmp=0

        for x in range(n-1):
            maxr = max(maxr, x + nums[x])

            if current == x:
                current = maxr
                jmp+=1
        return jmp



        
        