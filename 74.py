class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix or matrix == [[]] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        i = 0
        while i < len(matrix) - 1:
            if matrix[i][0] <= target <= matrix[i][-1]:
                break
            i += 1

        def binary_search(temp_list, target):
            if not temp_list:
                return False
            mid = len(temp_list) // 2
            if target == temp_list[mid]:
                return True
            elif target > temp_list[mid]:
                return binary_search(temp_list[mid + 1:], target)
            else:
                return binary_search(temp_list[:mid], target)

        return binary_search(matrix[i], target)
        # lo, hi = 0, len(matrix[i]) - 1
        # while lo <= hi:
        #     mid = (lo + hi) // 2
        #     if target == matrix[i][mid]:
        #         return True
        #     if target < matrix[i][mid]:
        #         hi = mid - 1
        #     else:
        #         lo = mid + 1
        #
        # return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))




