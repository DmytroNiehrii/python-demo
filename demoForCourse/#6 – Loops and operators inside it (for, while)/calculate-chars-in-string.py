data = "Hello world you are amazing"
character_count = {}

for char in data:
  if char in character_count:
    character_count[char] += 1
  else:
    character_count[char] = 1

print(character_count)