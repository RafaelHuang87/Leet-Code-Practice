import itertools
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

# Time out
        # def fact(num):
        #     fa = 1
        #     if n <= 0:
        #         return False
        #     for i in range(1, num + 1):
        #         fa *= i
        #     return fa
        # if n <= 0:
        #     return ''
        # if fact(n) < k:
        #     return ''
        # temp_list = [i for i in range(1, n + 1)]
        # per = list(itertools.permutations(temp_list))
        # result = ''
        # for value in sorted(per)[k - 1]:
        #     result += str(value)
        # return result
        ans = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            ans += num[first]
            num.pop(first)
        return ans


s = Solution()
print(s.getPermutation(9, 25996))