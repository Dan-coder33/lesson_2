class LRUCache:
    def __init__(self, capacity: int = 5) -> None:
        self.capacity = capacity
        self.cache = {}
        self.priority = 0

    def get(self, key: str) -> str:
        try:
            self.cache[key][1] += 1.01
            return self.cache[key][0]
        except KeyError:
            return ''

    def set(self, key: str, value: str) -> None:
        if len(self.cache) > self.capacity - 1:
            min_priority = min([v[1] for v in self.cache.values()])
            del_key = None
            for k, v in self.cache.items():
                if v[1] == min_priority:
                    del_key = k
                    break
            self.delete(del_key)

        self.cache[key] = [value, self.priority]
        self.priority += 1

    def delete(self, key: str) -> None:
        del self.cache[key]
