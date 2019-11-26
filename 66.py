class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        temp = ''
        for value in digits:
            temp += str(value)

        temp = str(int(temp) + 1)
        result = []
        for value in temp:
            result.append(int(value))

        return result

s = Solution()
print(s.plusOne([4,3,2,9]))

