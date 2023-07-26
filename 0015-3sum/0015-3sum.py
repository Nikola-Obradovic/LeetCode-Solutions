class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        final = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum == 0:
                    final.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1

        return final

        