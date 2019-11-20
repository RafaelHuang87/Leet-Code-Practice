class Solution:
    def qsort(list):
        if len(list) <= 1:
            return list
        return Solution.qsort([lt for lt in list[1:] if lt < list[0]]) + list[0:1] + Solution.qsort([rt for rt in list[1:] if rt >= list[0]])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_list = Solution.qsort(nums1 + nums2)
        if len(all_list) % 2 == 1:
            return float(all_list[len(all_list) // 2])
        else:
            return (all_list[len(all_list) // 2] + all_list[len(all_list) // 2 - 1]) / 2.0