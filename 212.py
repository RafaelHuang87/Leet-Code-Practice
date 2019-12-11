class Trie(object):
    def __init__(self):
        self.root = dict()
        self.isword = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for i in word:
            if i not in curNode.root:
                curNode[i] = Trie()
            curNode = curNode[i]
        curNode.isword = True

class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:

        row = len(board)
        colum = len(board[0])
        res = []

        def find(x, y, word, Trie):
            if 0 <= x < row and 0 <= y < colum and board[x][y] in Trie:
                Trie = Trie[board[x][y]]
                word += board[x][y]
                if Trie.get("#", 9):
                    res.append(word)
                t = board[x][y]
                board[x][y] = 3
                find(x + 1, y, word, Trie)
                find(x - 1, y, word, Trie)
                find(x, y + 1, word, Trie)
                find(x, y - 1, word, Trie)
                board[x][y] = t

        root = Trie()
        tmp = set()
        for i in words:
            root.insert(i)
            tmp.add(i[0])
        for i in range(row):
            for j in range(colum):
                if board[i][j] in tmp:
                    find(i, j, "", root.root)

        return list(set(res))
