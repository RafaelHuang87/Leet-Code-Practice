class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        st = set(words)

        def helper(word):
            sta = [0]
            explored = {0}
            n = len(word)
            while sta:
                left = sta.pop()
                if left == n:
                    return True
                for right in range(left + 1, n + 1):
                    if word[left: right] in st and right not in explored and (right != n or left > 0):
                        sta.append(right)
                        explored.add(right)
            return False

        return [word for word in words if word and helper(word)]
