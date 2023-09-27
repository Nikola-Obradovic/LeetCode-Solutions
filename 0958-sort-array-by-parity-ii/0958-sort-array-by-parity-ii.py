class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        res=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        even.sort()
        odd.sort()
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        
        return res