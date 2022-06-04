def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		factorial = 1
		while(n > 1):
			factorial = factorial * n
			n = n - 1
		return factorial

number = int(input("Enter a number: "))
print("Factorial of",number,"is", factorial(number))

