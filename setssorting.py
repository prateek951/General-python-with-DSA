nums = [1,2,33,322,11,94]

sorted(nums)	# Sorts the array

for num in nums
	print(num)	# Prints the numbers in sorted order

#Collection of items which don't allow duplicates is known as a set!
#Sets do not preserve order

set(nums)
#Makes a set of the nums array

for num in nums
	print(num)	# Print the numbers in any order since it is a set each time we will get a different order in which the items get printed


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
