class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        result = []
        if nums[0] > 0:
            return result
        visited = []
        for i, num_1 in enumerate(nums):
            if num_1 in visited:
                continue
            else:
                visited.append(num_1)
            j = i + 1
            k = len(nums) - 1

            while j < k:
                num_2 = nums[j]
                num_3 = nums[k]
                sum_three = num_1 + num_2 + num_3
                if sum_three == 0:
                    result.append((num_1, num_2, num_3))
                    j += 1
                    k -= 1
                elif sum_three < 0:
                    j += 1
                else:
                    k -= 1
        return set(result)

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

