class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums = sorted(nums)
        visited = []
        difference = float('inf')
        result = 0

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
                if sum_three == target:
                    return target
                elif abs(sum_three - target) < difference:
                    difference = abs(sum_three - target)
                    result = sum_three
                if sum_three < target:
                    j += 1
                else:
                    k -= 1
        return result

s = Solution()
print(s.threeSumClosest([6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10], -52))