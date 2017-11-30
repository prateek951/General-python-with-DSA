ninja_belts = {
	
	"crystal" : 'red',

	"ryu" : 'black'
}
print(ninja_belts['crystal'])	
print(ninja_belts['ryu'])
print('yoshi' in ninja_belts) 

print(ninja_belts.keys()) # returns the keys of the dictionary

print(list(ninja_belts.keys()) #typecasting it as a result

print(ninja_belts.values()) # return red,black

vals = list(ninja_belts.values())

# Find the instances of a particular value

print(vals.count('red')) 	# 1

# ADDING A NEW NINJA TO THE DICTIONARY

ninja_belts['yoshi'] = 'red'

# ALTERNATE WAY OF DEFINING NEW DICTIONARY

person = dict(name ='Prateek',age=21,height='6ft')




		

