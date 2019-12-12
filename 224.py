class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res
