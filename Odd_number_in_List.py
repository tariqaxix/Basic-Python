
Initial_number = int(input("Enter the initial number: "))
Last_number = int(input("Enter the last number: "))
for number in range(Initial_number, Last_number + 1):
  if number % 2 != 0:
    print(number)