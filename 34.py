class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums) - 1

        if nums[0] <= target <= nums[-1]:
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    start = mid
                    end = mid
                    while start - 1 >= 0 and nums[start - 1] == target:
                        start -= 1
                    while end + 1 <= len(nums) - 1 and nums[end + 1] == target:
                        end += 1
                    return [start, end]
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return [-1, -1]

s = Solution()
print(s.searchRange([1,2,3,3,4,5,6], 3))