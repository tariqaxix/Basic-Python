List = []
number = int(input("Enter the number of element in list: "))
for i in range(1, number + 1):
  element = int(input("Enter the element of the List: "))
  List.append(element)
print("The maximum element in the List is", max(List))
