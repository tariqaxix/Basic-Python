#Sum of Squares till number(n)
def SquareSum(n):
  sum = 0
  for i in range(1, n+1):
    sum = sum + (i * i)
  return sum
  
number = int(input("Enter your number: "))
print(SquareSum(number))
