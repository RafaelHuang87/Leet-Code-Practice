class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        in_str = s
        pt = p

        if pt == "":
            return not in_str

        first_match = bool(in_str) and pt[0] in {in_str[0], '.'}

        if len(pt) >= 2 and pt[1] == '*':
            return (self.isMatch(in_str, pt[2:])
                    or first_match and self.isMatch(in_str[1:], pt))
        else:
            return first_match and self.isMatch(in_str[1:], pt[1:])


s = Solution()
print(s.isMatch("ab", "c*ab"))