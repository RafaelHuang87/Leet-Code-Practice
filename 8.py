class Solution:
    def myAtoi(self, str: str) -> int:
        st = str.strip()
        flag = True
        strtoNum = 0
        if len(st) == 0:
            return 0
        if st[0] not in ['+', '-'] and not st[0].isdigit():
            return 0
        if st[0] == '-':
            flag = False
            st = st[1::]
        elif st[0] == '+':
            st = st[1::]
        for char in st:
            if '0' <= char <= '9':
                strtoNum = strtoNum * 10 + ord(char) - ord('0')
            else:
                break
        if strtoNum >= pow(2, 31):
            if flag:
                return pow(2, 31) - 1
            return -pow(2, 31)

        if flag:
            return strtoNum
        return -strtoNum