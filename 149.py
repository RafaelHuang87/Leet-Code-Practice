from collections import defaultdict
from _decimal import Decimal
class Solution:
    def maxPoints(self, points: [[int]]) -> int:
        slopes, result = defaultdict(int), 0
        for i, point1 in enumerate(points):
            slopes.clear()
            duplicate = 1
            for _, point2 in enumerate(points[i + 1:]):
                if point1.x == point2.x and point1.y == point2.y:
                    duplicate += 1
                    continue

                slope = float('inf') if point1.x == point2.x else \
                    Decimal(point1.y - point2.y) / Decimal(point1.x - point2.x)

                slopes[slope] += 1

            if result < duplicate:
                result = duplicate

            for _, val in slopes.items():
                if val + duplicate > result:
                    result = val + duplicate

        return result
