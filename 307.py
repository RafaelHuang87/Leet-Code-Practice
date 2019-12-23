class NumArray:

    def __init__(self, nums: [int]):
        self.nums = nums
    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i: j + 1])

# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 3, 5])
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)