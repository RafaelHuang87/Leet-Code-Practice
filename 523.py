class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False
        l = len(nums)
        tmp = 0
        m = {0: -1}
        for i in range(l):
            tmp += nums[i]
            t = tmp % k if k else tmp
            if t in m:
                if i - m[t] > 1:
                    return True
            else:
                m[t] = i
        return False
