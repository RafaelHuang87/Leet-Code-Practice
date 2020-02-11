from numpy import long


class Solution:
    def change_bit(self, n):
        if len(str(n + 1)) != len(str(n)):
            return 1
        elif (len(str(n - 1)) != len(str(n))) or (n == 1):
            return -1
        else:
            return 0

    def find_min(self, minnum, midnum, maxnum, n):
        minabs = abs(long(minnum) - long(n))
        midabs = abs(long(midnum) - long(n))
        maxabs = abs(long(maxnum) - long(n))
        if (midabs <= maxabs):
            if (minabs <= midabs):
                return minnum
            else:
                return midnum
        else:
            if (minabs <= maxabs):
                return minnum
            else:
                return maxnum

    def nearestPalindromic(self, n):
        if len(n) < 2:
            return str(int(n) - 1)
        if (len(n) % 2) == 0:
            substr_front = n[0:len(n) // 2]
            midnum = substr_front + substr_front[::-1]
            maxsub_front = str(int(substr_front) + 1)
            maxnum = maxsub_front + maxsub_front[::-1]
            minsub_front = str(int(substr_front) - 1)
            minnum = minsub_front + minsub_front[::-1]
        else:
            substr_front = n[0:(len(n) + 1) // 2]
            midnum = substr_front + (substr_front[::-1])[1:len(substr_front)]
            maxsub_front = str(int(substr_front) + 1)
            maxnum = maxsub_front + (maxsub_front[::-1])[1:len(maxsub_front)]
            minsub_front = str(int(substr_front) - 1)
            minnum = minsub_front + minsub_front[::-1][1:len(minsub_front)]
        if midnum == n:
            midnum = "0"
        if self.change_bit(int(substr_front)) == 1:
            maxnum = '1' + ((len(n) - 1) * '0') + '1'
        if self.change_bit(int(substr_front)) == -1:
            minnum = (len(n) - 1) * '9'
        return self.find_min(minnum, midnum, maxnum, n)

