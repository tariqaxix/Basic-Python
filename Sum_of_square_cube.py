#Sum of Squares till number(n)
def SquareSum(n):
  sum = 0
  for i in range(1, n+1):
    sum = sum + (i * i)
  return sum
  
number = int(input("Enter your number: "))
print(SquareSum(number))




#SUm of Cubes till number(n)
def CubeSum(n):
  sum = 0
  for i in range(1, n+1):
    sum = sum + (i**3)
  return sum

number = int(input("Enter your number: "))
print(CubeSum(number))
