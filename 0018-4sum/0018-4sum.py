class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        
        l = []
        nums.sort()
        i=0
        j=len(nums)-1

        i = 0
        while i < len(nums) - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            while j < len(nums) - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        l.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

                j += 1
            i += 1

        return l
        