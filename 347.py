class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        if len(nums) <= k:
            return nums
        cal = dict()
        for val in nums:
            if val not in cal.keys():
                cal[val] = 1
            else:
                cal[val] += 1
        temp = sorted(cal.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][0])
        return res

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))