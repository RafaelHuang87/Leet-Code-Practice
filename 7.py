class Solution:
    def reverse(x):
        x = str(x)
        if (x[0] != '-'):
            x = int(x[::-1])
        else:
            x = int(x[0] + x[:0:-1])
        if (x > pow(2, 31) - 1 or x < -pow(2, 31)):
            return 0
        return x


print(Solution.reverse(-120))
