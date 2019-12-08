class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        temp1, temp2 = version1.split('.'), version2.split('.')
        for i in range(max(len(temp1), len(temp2))):
            if i >= len(temp1) and int(temp2[i]) != 0:
                return -1
            elif i >= len(temp2) and int(temp1[i]) != 0:
                return 1
            if i < len(temp1) and i < len(temp2):
                if int(temp1[i]) > int(temp2[i]):
                    return 1
                elif int(temp2[i]) > int(temp1[i]):
                    return -1
        return 0

s = Solution()
print(s.compareVersion(version1 = "1.01", version2 = "1.001"))