# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:

    def binSearch(self, target, mountain_arr, side, found):
        low=0
        high=0
        
        if found:
            low=0
            high=side
            
            while low<=high:
                mid = (low+high)//2

                if mountain_arr.get(mid)==target:
                    return mid
            
                if mountain_arr.get(mid)<target:
                    low=mid+1
                else:
                    high=mid-1
        else:
            low=side
            high=mountain_arr.length()-1
            while low<=high:
                mid = (low+high)//2

                if mountain_arr.get(mid)==target:
                    return mid
            
                if mountain_arr.get(mid)<target:
                    high=mid-1
                else:
                    low=mid+1
        
        return -1



    def Peak(self, mountain_arr):
        low = 1
        high = mountain_arr.length() - 2

        while low != high:
            mid = low + (high - low) // 2

            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid

        return low
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        peak = self.Peak(mountain_arr)
        
        if mountain_arr.get(peak)==target:
            return peak
        
        lowerside=peak-1
        upperside=peak+1

        
        index=self.binSearch(target, mountain_arr, lowerside, True)
        

        if index!=-1:
            return index

        index=self.binSearch(target, mountain_arr, upperside, False)

        return index 
        