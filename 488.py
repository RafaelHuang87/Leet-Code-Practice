class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        import collections
        r = self.dfs(board, collections.Counter(hand))
        return r if r < +float('inf') else -1

    def dfs(self, board, cc):
        i, j = 0, 0
        res = +float('inf')
        while j < len(board):
            while j < len(board) and board[j] == board[i]: j += 1
            length = (j - i)
            need = {3: 0, 2: 1, 1: 2}[min(3, length)]

            if cc[board[i]] >= need:
                cc[board[i]] -= need
                res = min(res, need + self.dfs(board[:i] + board[j:], cc))
                cc[board[i]] += need
            i = j
        return res if board else 0