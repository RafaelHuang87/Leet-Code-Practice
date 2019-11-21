class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums = sorted(nums)
        result = []
        if len(nums) < 4 or nums[0] + nums[1] + nums[2] + nums[3] > target or nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return result

        for i in range(len(nums)):
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                x = j + 1
                y = len(nums) - 1
                while x < y:
                    sum_res = nums[i] + nums[j] + nums[x] + nums[y]
                    if sum_res == target:
                        result.append((nums[i], nums[j], nums[x], nums[y]))
                        x += 1
                        while x < y and nums[x] == nums[x - 1]:
                            x += 1
                    elif sum_res < target:
                        x += 1
                    else: y -= 1
        print(result)
        return set(result)

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))