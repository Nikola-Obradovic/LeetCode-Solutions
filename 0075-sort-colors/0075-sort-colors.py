class Solution:
    def Partition(self, nums, low, high):
        pivot = nums[high]
        i=low-1
        for j in range(low, high):
            if nums[j]<pivot:
                i+=1
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
        i+=1
        temp=nums[i]
        nums[i]=nums[high]
        nums[high]=temp
        
        return i

    def quickSort(self, nums, low, high):
        if high<=low:
            return
        pivot=self.Partition(nums,low,high)
        self.quickSort(nums,low,pivot-1)
        self.quickSort(nums,pivot+1,high)

    def sortColors(self, nums: List[int]) -> None:
        low=0
        high=len(nums)-1

        self.quickSort(nums,low,high)
     
