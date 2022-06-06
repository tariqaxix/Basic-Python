
#Simple Interest
def Simple_Interest(principal,time,rate):
	print('The principal is', principal)
	print('The time period is', time)
	print('The rate of interest is',rate)
	SimpleInterest = (principal * time * rate)/100
	print('The Simple Interest is', SimpleInterest)
	return SimpleInterest

Simple_Interest(3000,2,4)



#Compound Interest
def Compound_Interest(principle, rate, time):
	Amount = principle * (pow((1 + rate / 100), time))
	CompoundInterest = Amount - principle
	print("Compound interest is", CompoundInterest)

Compound_Interest(3000,2,4)





