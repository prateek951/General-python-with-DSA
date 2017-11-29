

# FOR LOOPS IN PYTHON

#CYCLE THROUGH ALL THE NINJAS COLLECTION

ninjas = ['Ryu','crystal','yoshi','ken']

for ninja in ninjas:
	
	print(ninja)

# output

	# Ryu
	# crystal
	# yoshi
	# ken

#CYCLING THROUGH A PORTION OF SPECIFIC LIST


for ninja in ninjas[1:3]:
	
	print(ninja)

# output

	#crystal
	#yoshi

for ninja in ninjas:

	if ninja == 'Ryu':

		#hey I am ryu here inside

		print(f'{ninja} - black belt')

		#Ryu - black belt

		break;

	else:
		
		printf(ninja)
			
		#ken

#BREAK KEYWORD TO BREAK OUT FROM THE LOOP




















