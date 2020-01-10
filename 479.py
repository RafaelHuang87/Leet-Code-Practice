class Solution:
    def largestPalindrome(self, n: int) -> int:
        start = int(math.pow(10, n - 1))  # the start num to generate the palind
        end = int(math.pow(10, n) - 1)  # maybe the end to generate, we should judge

        max_num = int((math.pow(10, n) - 1) * (math.pow(10, n) - 1))
        try_start = int(math.pow(10, n - 1))  # the start factor
        try_end = int(math.pow(10, n) - 1)  # the max factor
        res_now = 0
        for i in range(end, start - 1, -1):
            palind = self.generate_palind(i)
            if palind > max_num:
                continue
            res_now = self.find_num(palind, try_start, try_end)
            if res_now != -1:
                return res_now
        if n == 1:
            res_now = 9
        return res_now

    def generate_palind(self, st):
        s = str(st)
        return int(s + s[::-1])

    def find_num(self, palind, min_try, max_try):
        # pay attention to the boundary, otherwise you will meet TLS
        start = max(min_try, math.ceil(palind / max_try))
        # we only need to consider the mid from start to end
        # because 91*99  is the same to 99*91
        end = int((start + min(max_try, int(palind / min_try))) / 2)
        for i in range(start, end):
            if palind % i == 0:
                return palind % 1337
        return -1
