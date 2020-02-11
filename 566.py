class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        m = len(nums[0])
        if n * m != r * c:
            return nums
        res=[[0 for i in range(c)] for i in range(r)]
        for i in range(n):
            for j in range(m):
                res[(i*m+j) // c][(i * m + j) % c] = nums[i][j]
        return res
