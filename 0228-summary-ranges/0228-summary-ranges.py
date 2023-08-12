class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[]:
            return []
        l=[]
        start=0
        end=0
        for x in range(len(nums)):
            if x==0 or (x>0 and nums[x]==nums[x-1]+1):
                continue
            else:
                end=x-1
                if start!=end:
                    l.append(str(nums[start])+"->"+str(nums[end]))
                else: 
                    l.append(str(nums[start]))
                start=end+1  
        end=len(nums)-1
        if start!=end:
            l.append(str(nums[start])+"->"+str(nums[end]))
        else: 
            l.append(str(nums[start]))       

        return l
