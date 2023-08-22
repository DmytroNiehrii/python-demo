file = open('data/data.txt', 'r')

print(file.read())

# or
for line in file:
  print(line, end="")

file.close()