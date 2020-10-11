from lru_cache import LRUCache
from my_class import MyList

a = MyList([1, 2, 3])
b = MyList([1, 2, 3])
c = a + b
print(c)

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse'))  # вернёт 'James'
cache.delete('Walter')
print(cache.get('Walter'))  # вернёт ''
