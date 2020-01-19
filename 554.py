class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        import collections
        count = collections.defaultdict(int)
        for line in wall:
            sum_wall = 0
            for brick in line[:-1]:
                sum_wall += brick
                count[sum_wall] += 1
        if not len(count):
            return len(wall)
        return len(wall) - max(count.values())