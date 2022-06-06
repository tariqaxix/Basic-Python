#Method 1
List = []
number = int(input("Enter the number of element in list: "))
for i in range(1, number + 1):
  element = int(input("Enter the element of the List: "))
  List.append(element)
print("The maximum element in the List is", max(List))



#Method 2
List = [10, 18, 4, 45, 89]
List.sort()
print("Maximum in the List is:", List[-1])



#Method 3
def Maximum(List):
	max = List[0]
	for i in List:
		if i > max :
			max = i
	return max
List = [22, 54, 87, 45, 69, 89, 45, 93]
print("Maximum in the List is:", Maximum(List))




