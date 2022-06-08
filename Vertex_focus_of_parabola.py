
# Given equation like y = ax**2 + bx + c 
def parabola(a, b, c):
  print("The vertex is at: ", (-b/(2*a)), ",", (((4*a*c)-(b*b))/(4*a)))
  print("The focus is at:", (-b/(2*a)), ",", (((4*a*c)-(b*b)+1)/(4*a)))
  print("The directrix is: ", (c - (((b**2) + 1)/(4*a))))

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
parabola(a, b, c)





