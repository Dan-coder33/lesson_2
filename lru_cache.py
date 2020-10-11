class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = {}

    def get(self, key: str) -> str:
        try:
            return self.cache[key]
        except KeyError:
            return ''

    def set(self, key: str, value: str) -> None:
        if len(self.cache) > self.capacity - 1:
            raise IndexError
        self.cache[key] = value

    def delete(self, key: str) -> None:
        del self.cache[key]



