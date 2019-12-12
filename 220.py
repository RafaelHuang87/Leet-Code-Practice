class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        lenth = len(nums)
        a = set()
        for i in range(lenth):
            if t == 0:
                if nums[i] in a:
                    return True
            else:
                for atem in a:
                    if abs(nums[i] - atem) <= t:
                        return True
            a.add(nums[i])
            if len(a) == k + 1:
                a.remove(nums[i - k])
        return False
