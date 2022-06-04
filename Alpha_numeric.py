#First case
number_list = [1,2,3]
alphabet_list = ['a','b','c']
for number in number_list:
  print(number)
  for alphabet in alphabet_list:
    print(alphabet)


#Second case
number_list = [1,2,3]
alphabet_list = ['a', 'b', 'c']
for number in number_list:
  for alphabet in alphabet_list:
    print(number)
    print(alphabet)