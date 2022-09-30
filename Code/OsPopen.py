import os

p = os.popen('dir')
# print(p.__next__())
# print(p.__next__())
# print(next(p))

# Полный протокол итерации

i = iter(p)
print(next(i))
print(next(i))

