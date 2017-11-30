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


# CREATE A NEW INSTANCE OF THE CLASS

pluto = Planet('Pluto',4000,40000,7.6,'Solar System')

# neptune = Planet('Neptune',40000,44444,8.4,'Solar System')

print(f'The name of the planet is : {pluto.name}')

print(f'The age of the planet is : {pluto.age}')

print(f'The radius of the planet is : {pluto.radius}')

print(Planet.shape)

print(Planet.name) 	# error : Object Planet has no name


print(Planet.commons())

print(pluto.commons())

# WE CANNOT ACCESS INSTANCE METHOD USING CLASSNAME BUT WE CAN ACCESS CLASS METHODS

print(Planet.spin('a very high speed'))	# IT CAN BE USED ON THE CLASS ITSELF  #RUNS PERFECTLY

print(pluto.spin('a very ultimate method'))
