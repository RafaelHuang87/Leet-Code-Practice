class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isword = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        nodes = [self.root]
        for i, w in enumerate(word):
            newcur = []
            for node in nodes:
                for key, value in node.children.items():
                    if w == '.' or w == key:
                        if i == len(word) - 1 and value.isWord:
                            return True
                        newcur.append(value)
            nodes = newcur
        return False
