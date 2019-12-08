class Solution:
    def majorityElement(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums
        temp = dict()
        for val in nums:
            if val not in temp.keys():
                temp[val] = 1
            else:
                temp[val] += 1

        return max(temp, key=lambda x: temp[x])


s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))