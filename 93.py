class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        res = []

        def dfs(s, path, res):
            if len(s) > (4 - len(path)) * 3:
                return
            if not s and len(path) == 4:
                res.append('.'.join(path))
                return
            for i in range(min(3, len(s))):
                curr = s[:i + 1]
                if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                    continue
                dfs(s[i + 1:], path + [s[:i + 1]], res)
        dfs(s, [], res)
        return res



s = Solution()
print(s.restoreIpAddresses("25525511135"))
