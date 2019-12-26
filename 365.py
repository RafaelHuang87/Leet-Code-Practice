class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        if x and y:
            return x + y >= z and z % math.gcd(x, y) == 0
        else:
            return z == x or z == y