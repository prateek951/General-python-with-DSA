class Planet:

	shape = 'round'	# Class variable indicates that all instances of the class Planet are round in shape
	
	#shape is a class variable is shared equally among all the instances of the class
	
# 	"""docstring for Planet"""

	# __init__ is just like constructor function in other programming languages which is invoked as soon as a new instance of the class is created!
	def __init__(self, name,radius,age,gravity,system):

		#self refers to the instance which invoked the this __init__ function and sets the values for every instance of the class when it
		#is created
		
		self.name = name
		self.radius = radius
		self.age = age 
		self.gravity = gravity 
		self.system = system 
		
		#This defines a class method!
		@classmethod
		# Here cls variable is accessing the class variable shape in the classmethod
		def commons(cls):
			
			return f'All planets are {cls.shape} in shape because of gravity'
		
		#This defines a static method!
		@staticmethod

		#METHOD HAS ACCESS ONLY TO THE PARAMETERS THAT WE PASS IT INDIVIDUALLY

		def spin(speed='20000 miles per hour'):
				
			return f'The planet spins at {speed}'


# Create a new instance of the Planet class to set the values for the pluto object
pluto = Planet('Pluto',4000,40000,7.6,'Solar System')

# neptune = Planet('Neptune',40000,44444,8.4,'Solar System')

print(f'The name of the planet is : {pluto.name}')

print(f'The age of the planet is : {pluto.age}')

print(f'The radius of the planet is : {pluto.radius}')

print(Planet.shape)

print(Planet.name) 	# error : Object Planet has no name

#Using the class name you can invoke the class method
print(Planet.commons())
#Using the instance we created we can invoke the class method(no errors in this case also)
print(pluto.commons())

# Using classname we cannot access instance methods but we can access static and class methods using the classname

print(Planet.spin('a very high speed'))	#Using the classname we can fire static methods

print(pluto.spin('a very ultimate method'))	#Since static variables and methods are shared equally among all the objects of the class,
#they can be invoked using the instances we created
