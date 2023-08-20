class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        my_set=set()
        cnt=0
        nums.sort()
        nums.reverse()
        backup=0
        for x in nums:
            if not x in my_set:
                my_set.add(x)
                cnt+=1
                if x>backup:
                    backup=x
                if cnt==3:
                    return x
        return backup