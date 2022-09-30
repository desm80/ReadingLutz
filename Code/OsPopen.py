import os

p = os.popen('dir')
print(p.__next__().encode('cp1251').decode('cp866'))
print(p.__next__().encode('cp1251').decode('cp866'))
# print(next(p))

# Полный протокол итерации

# i = iter(p)
# print(next(i))
# print(next(i))

