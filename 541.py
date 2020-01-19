class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2 * k
        res = ''

        while len(res) < len(s):
            res += s[left:mid][::-1] + s[mid:right]
            left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k
        return res
