class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        m = len(M)
        res = m
        root = [0] * m
        for i in range(m):
            root[i] = i
        for i in range(m):
            for j in range(i + 1, m):
                if M[i][j] == 1:
                    a = self.getRoot(root, i)
                    b = self.getRoot(root, j)
                    if a != b:
                        root[a] = b
                        res -= 1
        return res

    def getRoot(self, root, i):
        while i != root[i]:
            root[i] = root[root[i]]
            i = root[i]
        return i
