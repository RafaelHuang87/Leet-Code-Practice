class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        result = []
        if n == k:
            for i in range(1, n + 1):
                result.append(i)
            return [result]
        if k == 1:
            for i in range(1, n + 1):
                result.append([i])
            return result
        a = self.combine(n - 1, k - 1)
        b = self.combine(n - 1, k)

        for i in a:
            result.append([n] + i)

        result = result + b

        return result

s = Solution()
print(s.combine(4, 4))