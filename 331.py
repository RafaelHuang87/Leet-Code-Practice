class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        t, l = 1, preorder.split(',')
        for i in l:
            if t == 0:
                return False
            if i == "#":
                t = t - 1
            else:
                t = t + 1
        return t == 0
