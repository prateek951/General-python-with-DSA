for n in range(5):
	
	#Looping over the range from 0 to 5-1(excluding 5)
	print(n)
	# 0 1 2 3 4 is the output

for n in range(3,10):
	
	#Looping over the range from 0 to 10-1(excluding 10)
	print(n)
	# 3 4 5 6 7 8 9 is the output

for n in range(0,20,4):
	
	#Looping over the range from 0 to 20-1(excluding 20)
	print(n)
	# 0 4 8 12 16 is the output each time we go into the loop we get an increment of 4

friends = ['prateek','nischal','navneet']

for friend in range(len(friends)):

		print(friend,friends[friend])

############################

# REVERSE LOOP

for n in range(len(friends)-1,-1,-1):
	
	print(n,friends[n])
