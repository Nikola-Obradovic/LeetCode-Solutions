class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
    

            
        while i<j:
            x=i+1
            while x<=j:
                if nums[i]+nums[x]==target:
                    l=[]
                    l.append(i)
                    l.append(x)
                    return l
                x+=1
            i+=1    

        return []          