class Solution:
    def getSkyline(self, buildings: [[int]]) -> [[int]]:
        if not buildings:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        lh = rh = l = r = 0
        res = []
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                cp = [left[l][0], max(left[l][1], rh)]
                lh = left[l][1]
                l += 1
            elif left[l][0] > right[r][0]:
                cp = [right[r][0], max(right[r][1], lh)]
                rh = right[r][1]
                r += 1
            else:
                cp = [left[l][0], max(left[l][1], right[r][1])]
                lh, rh = left[l][1], right[r][1]
                l += 1
                r += 1
            if len(res) == 0 or res[-1][1] != cp[1]:
                res.append(cp)
        res += left[l:] + right[r:]
        return res
