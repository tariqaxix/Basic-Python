
def Is_Triangle(a, b, c):
  if (a != 0 and b != 0 and c != 0 and (a + b + c) == 180):
    if ((a + b) >= c and (b + c) >= a and (a + c) >= b):
      return "Yes a Triangle"
    else:
      return "Not a Triangle"
  else:
    return "Not possible"
a = int(input("Enter your first angle: "))
b = int(input("Enter your second angle: "))
c = int(input("Enter your third angle: "))
print(Is_Triangle(a, b, c))





