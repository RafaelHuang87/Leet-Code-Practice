import heapq
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.d = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.d:
            self.d[key] = 1
            ele = (self.d[key], key)
            self.q.append(ele)
            heapq.heapify(self.q)
        else:
            self.q.remove((self.d[key], key))
            self.d[key] += 1
            self.q.append((self.d[key], key))
            heapq.heapify(self.q)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if self.d.get(key, 0) == 1:
            del self.d[key]
            self.q.remove((1, key))
            heapq.heapify(self.q)
        elif self.d.get(key, 0) != 0:
            self.q.remove((self.d[key], key))
            self.d[key] -= 1
            self.q.append((self.d[key], key))
            heapq.heapify(self.q)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        ans = heapq.nlargest(1, self.q)
        return ans[0][1] if ans else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        ans = heapq.nsmallest(1, self.q)
        return ans[0][1] if ans else ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()