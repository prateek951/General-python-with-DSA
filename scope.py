my_name = 'ryu' #GLOBAL SCOPE VARIABLE

def print_name():

	global my_name	#Using the same my_name variable that is defined outside this block at the top!

	my_name = 'prateek'	#Here we are overriding the global variable(so now my_name is now prateek both in the local as well as the global scope)

	print('The name inside the function is',my_name)

	#prints prateek

print_name() 	#invoke the function

print('Outside the function the name is',my_name)	#Outside the function also know the name is prateek since we overrided the global version of

#my_name in the method print_name
