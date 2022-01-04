#m = [1, 2, [1, 3], ['a', 'b']]
#lenghtM = len(m)
#print(lenghtM)

#x = [1, 2, 3]
#y = x.copy()
#x[0] = 10
#print(x, y)

n = list(range(1, 21))
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
print(n)
print(m)

## срез списка
# m[startIndex:stopIndex:step]