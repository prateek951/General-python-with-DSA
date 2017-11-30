# WHILE LOOPS IN PYTHON
age = 25
num = 0

def printAgePrinter(num,age):
	
	while num<age:

	print('Your age is about to reach the age we know',num)
	num++		#EACH TIME TELL THE AGE OF THE PERSON AND INCREMENT IT BY IT SO AS TO GET CLOSER TO THE TARGET

#When num reaches to the value of age(25) it breaks out of the loop

# Now outside the function,the value of num is again 0 because it is now in global scope!

def check_even_odd(num,age):
while num<age:

	if num == 0

		num+=1
		continue #Abandon the current iteration and begin with the new iteration

	if num%2==0:
		#Check for evenness of the n
		print('Your age is even',num)
		#If age is even but it has exceeded 10 break out of outer if
		if num > 10
		break
	else:
		print('Your age is odd',num)
	num++
printAgePrinter(2,33)
check_even_odd(2,33)
