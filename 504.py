class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return str(num)

        res = ''

        num_abs = abs(num)
        while num_abs:
            rest_num = num_abs % 7
            num_abs = num_abs // 7
            res += str(rest_num)

        if num < 0:
            return '-' + res[::-1]
        else:
            return res[::-1]
