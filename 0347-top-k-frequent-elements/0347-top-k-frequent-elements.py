from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)  
        sorted_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)  

        result = [item[0] for item in sorted_list[:k]]  

        return result
