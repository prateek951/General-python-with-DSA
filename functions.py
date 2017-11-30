def greet():
	
	print('Hello World')

	#def is used to define functions in python
greet() # Using parenthesis after the name of the function triggers the code property of the function	

greet()	# You can trigger the code property of the function any number of times 

#Function with arguments

def greet(name,time):
	
	print(f'Good {time} {name}') 

greet('Prateek','Morning')	# Triggers the greet function with arguments by passing Prateek and Morning as parameters

# OUTPUT -- Good Morning Prateek

name = input('Enter the name of the person')

time = input('Enter the time of the day')

greet(name,time)	# Invoke the function with the values that we got from the input

#DEFAULT PARAMETERS can be supplied to a function as well!

def greeter(name='Prateek',time='morning'):

	print(f'Good {time}, {name}')



greeter('Navneet','night')	#Since we are supplying parameters in our function call,these parameters will override the default parameters in the above function

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

print(f'The volume of the circle is : {volume}')

