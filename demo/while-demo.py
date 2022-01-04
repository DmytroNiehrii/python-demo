# Calculate factorial for input value
inputValue = 0
while True:
    inputValue = input()
    if inputValue == 'exit':
        break
    x = int(inputValue)
    count = 0
    fx = 1
    while count < x:
        count += 1
        fx *= count
    else:
        print('Factorial(' + str(x) + ') = ' + str(fx))

