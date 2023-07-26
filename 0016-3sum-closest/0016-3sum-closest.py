class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        final = nums[0] + nums[1] + nums[2]
        

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum==target:
                    return total_sum
                if abs(target - total_sum) < abs(target-final):
                    final=total_sum
                    
                
                  
                   
                   
                if total_sum < target:
                    left += 1
                else:
                    right -= 1

        return final
        