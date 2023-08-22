executionInProgress = True
iterationCount = 0
while executionInProgress:
  try:
    numValue = int(input("Enter number: "))
    print( numValue + 10)
    executionInProgress = False
  except ValueError:
    print('Only numbers accepted, try again...')
  finally:
    iterationCount += 1
print(str(iterationCount), 'iterations')