class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        l=[]
        while i<j:
            if numbers[i]+numbers[j]==target:
                l.append(i+1)
                l.append(j+1)
                return l
            if target>numbers[i]+numbers[j]:
                i+=1
            if target<numbers[i]+numbers[j]:
                j-=1
            
            

            
        