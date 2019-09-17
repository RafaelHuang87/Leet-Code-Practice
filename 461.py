"""
Solution for Leet Code 461.
"""


class Solution:
    def hammingDistance(x, y):
        x = format(x, 'b')
        y = format(y, 'b')
        temp = ""
        if len(x) < len(y):
            for i in range(len(y) - len(x)):
                temp += "0"
            x = temp + x
        if len(y) < len(x):
            for i in range(len(x) - len(y)):
                temp += "0"
            y = temp + y
        return sum(el1 != el2 for el1, el2 in zip(x, y))


print(Solution.hammingDistance(1, 4))

