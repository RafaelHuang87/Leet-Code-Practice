class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        temp = []
        nums.sort()
        medile_p = len(nums) // 2
        medile_num = nums[medile_p]
        nums.remove(medile_num)
        for i in nums:
            if medile_num >= i:
                step = medile_num - i
                temp.append(step)
            else:
                step = i - medile_num
                temp.append(step)

        return sum(temp)
