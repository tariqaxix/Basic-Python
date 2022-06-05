#Method 1
list = []
number = int(input("Enter the number of element in List: "))
for i in range(1, number + 1):
  element = int(input("Enter elements: "))
  list.append(element)
print("The minimum element in list is: ", min(list))


