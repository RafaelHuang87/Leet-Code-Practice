class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if C <= E or H <= B or G <= A or D <= F:
            return (C - A) * (D - B) + (G - E) * (H - F)
        else:
            return (C - A) * (D - B) + (G - E) * (H - F) - min(min(C - E, G - A), min(C - A, G - E)) * min(min(H - B, D - F), min(D - B, H - F))
