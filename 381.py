class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.data = []
        self.index = 0
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if self.index == self.length:
            self.data.append(val)
            self.length += 1
        else:
            self.data[self.index] = val
        self.index += 1
        if val in self.hash:
            self.hash[val].add(self.index - 1)
            return False
        else:
            self.hash[val] = {self.index - 1}
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.hash:
            val_index = self.hash[val].pop()
            if not self.hash[val]:
                self.hash.pop(val)
            if self.index - val_index != 1:
                self.data[val_index] = self.data[self.index - 1]
                self.hash[self.data[val_index]].remove(self.index - 1)
                self.hash[self.data[val_index]].add(val_index)
            self.index -= 1
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        import random
        return self.data[random.randint(0, self.index - 1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()