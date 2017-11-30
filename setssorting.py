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


# Create a dictionary of ninjas(A dictionary is collection of key-values pairs just like object-literals in javascript)
ninjas = {
	'ryu' : 'black',
	'yoshi' : 'red',
	'prateek' : 'yellow'
}

print(ninjas.values())	# Prints all the values in the above key values pairs in the form of a list

set(ninjas.values())   #Makes a set of the values in above key value pairs but each time in different order.

# Method to calculate how many instances are there for a particular belt color!

def countInstances(dictionary):
	
	# First make a list of all the dictionary values
	belts = list(dictionary.values())

	#cycle over all the belts

	for belt in set(belts)	# Make a set of belts to maintain uniqueness as set does't allow duplicacies!

		belt = belts.count(belt)	#Count the instances of each belt!!

		print(f'There are {num} {belt} belts')


countInstances(ninjas)
