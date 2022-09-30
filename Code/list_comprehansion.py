

lst = [x for x in 'python']
print(lst)

res = []
for letter in 'python':
    res.append(letter)
print(res)


# с использованием if
# lst = [х + 10 for х in range(7) if х % 2 == 0]
# print(lst)

# использование тернарного условного оператора
# lst = [1, -5, 10, 15, -20, 7, -3]
# a = ['positive' if x > 0 else 'negative' for x in lst]
# print(a)

# с использованием вложенных циклов for
# a = [(x, y) for x in range(2) for y in range(3)]
# print(a)

# matrix = [[a for a in range(3)] for b in range(4)]
# print(matrix)
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = [[x**2 for x in row] for row in a]
# print(a)
