class NumArray:

    def __init__(self, nums: List[int]):
        self.obj=nums

    def sumRange(self, left: int, right: int) -> int:
        total=0
        while left<=right:
            if left!=right:
                total+=self.obj[left]+self.obj[right]
            else:
                total+=self.obj[left]
            left+=1
            right-=1
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)