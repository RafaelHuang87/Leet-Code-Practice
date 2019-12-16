class Solution:
    def diffWaysToCompute(self, input: str) -> [int]:
        end = []
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y}

        for i in range(len(input)):
            if input[i] in op.keys():
                for left in self.diffWaysToCompute(input[:i]):
                    for right in self.diffWaysToCompute(input[i + 1:len(input)]):
                        output = op[input[i]](left, right)
                        end.append(output)

        if len(end) == 0:
            end.append(int(input))
        return end