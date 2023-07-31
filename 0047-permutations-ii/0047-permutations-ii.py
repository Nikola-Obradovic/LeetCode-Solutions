class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        l= list(itertools.permutations(nums))
        s={tuple(x) for x in l}
        ul=[list(x) for x in s]
        return ul