
r = range(10)
print(r)
# i = iter(r)
# print(next(i))
# print(next(i))
# print(next(i))
# print(list(i))
# print(list(r)[5])

# Итераторы с множеством проходов или с одним проходом

r = range(3)
# print(next(r))
i_1 = iter(r)
i_2 = iter(r)
print(next(i_1))
print(next(i_1))
print(next(i_2))
print(next(i_1))

z = zip((1, 2, 3), (10, 11, 12))
i_1 = iter(z)
i_2 = iter(z)
print(next(i_1))
print(next(i_1))
print(next(i_2))
print(next(i_1))



