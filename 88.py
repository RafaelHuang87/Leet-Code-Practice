class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            del nums1[m]
        for i in range(n, len(nums2)):
            del nums2[n]

        nums1 += nums2
        nums1.sort()
