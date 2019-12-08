class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, res = {}, []
        for i in range(len(numbers)):
            if numbers[i] in s.keys():
                res.append(s[numbers[i]] + 1)
                res.append(i + 1)
                return res
            s[target - numbers[i]] = i
        return res