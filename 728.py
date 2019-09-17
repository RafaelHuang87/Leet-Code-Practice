"""
Solution for Leet Code 728.
"""


class Solution:
    def selfDividingNumbers(left, right):
        list = []
        for i in range(left, right+1):
            list.append(i)
            j = str(i)
            for digit in j:
                if digit is "0" or i % int(digit) is not 0:
                    list.remove(i)
                    break
        return list


print(Solution.selfDividingNumbers(1, 22))