def greet():
	
	print('Hello World')


greet()	#INVOKE THE GREET FUNCTION


greet()	# CAN BE INVOKED ANY NUMBER OF TIMES


def greet(name,time):
	
	print(f'Good {time} {name}')

greet('Prateek','Morning')

#Good Morning Prateek

name = input('Enter the name of the person')

time = input('Enter the time of the day')

greet(name,time)	# Invoke the function with the values that we got from the input

#DEFAULT PARAMETERS

def greeter(name='Prateek',time='morning'):

	print(f'Good {time}, {name}')



greeter('Navneet','night')



#CALCULATE THE AREA OF THE CIRCLE

def area(radius):
	
	print(f'The area of the circle is {3.142*radius*radius}')


radius = input('Enter the radius of the circle')

radius = int(radius) #in previous statement radius was a string now it is typecasted to an integer

area(radius)	#INVOKE THE FUNCTION TO CALCULATE THE AREA


#CALCULATE THE VOLUME OF THE CIRCLE

#FIRST GET THE AREA OF THE CIRCLE AND TAKE THE LENGTH OF CYCLINDER FROM THE USER

height = input('Enter the length of the cylinder')

radiuss = input('Enter the radius of the circle')

def volume(radiuss,height):
	
	areaa = 3.14*radiuss*radiuss

	return areaa*height


volume = volume(radiuss,height)

print('The volume of the circle is',volume)

