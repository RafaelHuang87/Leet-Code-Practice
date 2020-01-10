class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center


    def randPoint(self) -> List[float]:
        nr = math.sqrt(random.random()) * self.r
        alpha = random.random() * 2 * 3.141592653
        newx = self.x + nr * math.cos(alpha)
        newy = self.y + nr * math.sin(alpha)
        return [newx, newy]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()