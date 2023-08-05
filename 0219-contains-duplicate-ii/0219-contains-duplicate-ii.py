class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=[]
        for x in range(len(nums)):
            l.append((nums[x], x))
        l.sort()
        for x in range(len(l)-1):
            if l[x][0]==l[x+1][0] and k>=abs(l[x][1]-l[x+1][1]):
                return True
        return False

        