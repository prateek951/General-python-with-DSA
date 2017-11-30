my_name = 'ryu' #GLOBAL SCOPE VARIABLE


def print_name():

	#HERE WE ARE OVERRIDING THE GLOBAL VARIABLE

	global my_name

	my_name = 'prateek'

	print('The name inside the function is',my_name)

	#prateek

print_name()

print('Outside the function the name is',my_name)

	#prateek
