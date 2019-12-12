class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        lines = len(matrix)
        lists = len(matrix[0])
        mat = [[0] * lists for _ in range(lines)]
        for i in range(lists):
            mat[0][i] = int(matrix[0][i])
        for i in range(lines):
            mat[i][0] = int(matrix[i][0])
        for i in range(1, lines):
            for j in range(1, lists):
                mat[i][j] = int(matrix[i][j])
                if mat[i][j] is not 0:
                    mat[i][j] = (min(mat[i - 1][j - 1], mat[i][j - 1], mat[i - 1][j]) + 1)
        result = 0
        for i in mat:
            for j in i:
                if result < j:
                    result = j
        return result ** 2