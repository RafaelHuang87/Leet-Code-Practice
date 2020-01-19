class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        max_val = n+m
        pos = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    pos.append((i,j))
                else:
                    matrix[i][j] = max_val
        for i,j in pos:
            for r, c in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
                if 0<=r<n and 0<=c<m and matrix[i][j]+1<matrix[r][c]:
                    matrix[r][c] = matrix[i][j] + 1
                    pos.append((r, c))
        return matrix