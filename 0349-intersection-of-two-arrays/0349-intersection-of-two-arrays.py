class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        i=0
        while i<len(nums1) and i<len(nums2):
            if nums1[i] in nums2:
                if not nums1[i] in l:
                    l.append(nums1[i])
            if nums2[i] in nums1:
                if not nums2[i] in l:
                    l.append(nums2[i])
            i+=1
        return l           