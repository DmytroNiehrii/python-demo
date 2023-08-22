user_data = int(input("Enter some number: "))

if user_data < 0:
  print("It is negative number")
elif user_data > 0 and user_data <= 10:
  print("Number is positive between 0 and 10")
elif user_data > 10:
  print("Number is positive more then 10")
else:
  print("Number is zero")