class Solution:
    def judgeCircle(moves):
        i = j = 0
        for move in moves:
            if move is 'U':
                i += 1
            elif move is 'D':
                i -= 1
            elif move is 'L':
                j += 1
            else:
                j -= 1
        return i == j == 0

print(Solution.judgeCircle("UDUD"))