#First Method
def SumArray(array):
	sum=0
	for i in array:
		sum = sum + i
	return(sum)
array=[]
array = [2, 5, 6, 8]
n = len(array)
x = SumArray(array)
print ('Sum of the element in the array is ', x)



#Second Method
array = []
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = sum(array)
print("The sum of element in array is ", x)