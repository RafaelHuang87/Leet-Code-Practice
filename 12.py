class Solution:
    def intToRoman(self, num: int) -> str:
        output = ''
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_num_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i in range(len(num_list)):
            while num >= num_list[i]:
                num -= num_list[i]
                output += roman_num_list[i]
        return output

s = Solution()
print(s.intToRoman(55))