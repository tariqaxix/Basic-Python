#Method 1
list = []
number = int(input("Enter the number of element in List: "))
for i in range(1, number + 1):
  element = int(input("Enter elements: "))
  list.append(element)
print("The minimum element in list is: ", min(list))



#Method 2
list = [10, 20, 1, 45, 99]
print("Smallest element is:", min(list))



#Method 3
List = [10, 20, 4, 45, 99]
List.sort()
print("Smallest element is:", *List[:1])
