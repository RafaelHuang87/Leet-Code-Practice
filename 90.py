class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            for i in result[:]:
                item = i[:]
                item.append(num)
                if item not in result:
                    result.append(item[:])
        return result

s = Solution()
print(s.subsetsWithDup([1,2,2]))

