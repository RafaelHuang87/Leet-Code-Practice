class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    if (num1 <= 0 and num2 < 0) or (num1 >= 0 and num2 > 0):
                        stack.append(num1 // num2)
                    else:
                        stack.append(-(abs(num1) // abs(num2)))
        return stack[0]

s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))