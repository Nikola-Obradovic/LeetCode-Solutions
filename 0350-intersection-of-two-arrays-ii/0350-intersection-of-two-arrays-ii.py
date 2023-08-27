class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        while nums2!=[]:
            if nums2[0] in nums1:
                
                nums1.remove(nums2[0])
                l.append(nums2.pop(0))

            else:
                nums2.pop(0)
        return l
            





