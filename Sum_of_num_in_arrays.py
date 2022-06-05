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

