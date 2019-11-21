class Solution:
    def romanToInt(self, s: str) -> int:
        num_list = []
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                num = - roman_dict[s[i]]
                num_list.append(int(num))
            else:
                num_list.append(int(roman_dict[s[i]]))
        return sum(num_list) + roman_dict[s[-1]]

s = Solution()
print(s.romanToInt('III'))
