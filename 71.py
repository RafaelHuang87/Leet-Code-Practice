class Solution:
    def simplifyPath(self, path: str) -> str:
        temp_stack = list()
        dirs = path.split('/')
        result = '/'
        for dir in dirs:
            if not dir or dir == '.':
                continue
            if dir == '..':
                if temp_stack:
                    temp_stack.pop()
            else:
                temp_stack.append(dir)

        return result + result.join(temp_stack)

s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))
