class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        strmap = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n + 1):
            pos = ""
            for j in [3, 5]:
                if i % j == 0:
                    pos += strmap[j]
            if not pos:
                pos = str(i)
            res.append(pos)
        return res