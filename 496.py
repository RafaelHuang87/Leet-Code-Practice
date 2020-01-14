class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            flag = False
            for j in range(nums2.index(nums1[i]) + 1, len(nums2)):
                if nums1[i] < nums2[j]:
                    flag = True
                    res.append(nums2[j])
                    break
            if not flag:
                res.append(-1)
        return res
