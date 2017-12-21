nums = [1,2,33,322,11,94]

sorted(nums)

#COLLECTION OF ITEMS WHICH DON'T ALLOW DUPLICATES IS KNOWN AS A SET

# SETS DO NOT PRESERVE ORDER

set(nums)

# CREATE A DICTIONARY

ninjas = {
	
	'ryu' : 'black',

	'yoshi' : 'red',


	'prateek' : 'yellow'

}

print(ninjas.values())

set(ninjas.values())   #black red yellow

# CALCULATE HOW MANY INSTANCES ARE OF A PARTICULAR BELT COLOR

def countInstances(dictionary):
	

	# FIRST MAKE A LIST OF ALL THE BELTS

	belts = list(dictionary.values())

	#cycle over all the belts

	for belt in set(belts)	# WE WANT UNIQUENESS 

		belt = belts.count(belt)

		print(f'There are {num} {belt} belts')


countInstances(ninjas)