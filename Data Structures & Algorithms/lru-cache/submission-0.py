class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []       
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.stack.remove(key)  
            self.stack.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.stack.remove(key)   
        elif len(self.cache) >= self.capacity:
            lru_key = self.stack.pop(0)  
            self.cache.pop(lru_key)
        self.cache[key] = value
        self.stack.append(key)
