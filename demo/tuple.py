# Кортежи
# Tuple is faster for iteration comparing list, immutable (it means var1 = var2 leads to copy tuple)
x = (9, 8, 7, 6)
y = 9, 8, 7, 6
print(type(x), type(y))

x = tuple('string')
print(x)

