from lru_cache import LRUCache
from my_class import MyList

a = MyList([1, 2, 3])
b = MyList([1, 2, 3])
c = a + b
print(c)  # вернет [2, 4, 6]

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
print(cache.get('Jesse'))  # вернёт 'James'
cache.delete('Walter')
print(cache.get('Walter'))  # вернёт ''

# cache.set('1', '1')
# cache.set('2', '2')
# cache.set('3', '3')
# cache.set('4', '4')
# cache.set('5', '5')
# print(cache.get('1'))
# cache.set('6', '6')
# cache.set('7', '7')

