class Solution:
    def repeatedNTimes(A):
        temp = {}
        for data in A:
            if data not in temp:
                temp[data] = 1
            else:
                return data

print(Solution.repeatedNTimes([1,3,2,1]))