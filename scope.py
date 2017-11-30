my_name = 'ryu' #GLOBAL SCOPE VARIABLE

def print_name():

	global my_name	#Using the same my_name variable that is defined outside this block at the top!

	my_name = 'prateek'	#Here we are overriding the global variable(so now my_name is now prateek both in the local as well as the global scope)

	print('The name inside the function is',my_name)

	#prints prateek

print_name()

print('Outside the function the name is',my_name)

	#prateek
