class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.keys = []

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        else:
            if len(self.cache) == self.cap:
                del_key = self.keys[0]
                self.keys = self.keys[1:]
                del self.cache[del_key]

            self.cache[key] = value
            self.keys.append(key)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)