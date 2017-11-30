# name = 'Shaun'

# age = 21





# CLASSES

class Planet:

	# CONSTRUCTOR (IT RUNS WHEN INSTANCE OF THE CLASS IS CREATED)

	def __init__(self):	
		
		#SET THE INSTANCE PROPERTIES WHEN IT IS INSTANTIATED

		self.name = 'Earth'
		self.radius = 200000
		self.gravity = 9.8
		self.system = 'Solar System'

	def __init__(self,name,radius,gravity,system):

		self.name = name 
		self.radius = radius 
		self.gravity = gravity
		self.system = system


	def orbit():
		return f'{self.name} is orbitting in the {self.system}'


#CREATE THE NEW INSTANCE OF THE CLASS

planet = Planet()	

print(f'The name of the planet is : {planet.name}')

print(f'The radius of the planet is : {planet.radius}')

print(f'The gravity of the planet is : {planet.gravity}')

print(f'The system of the planet is : {planet.system}')

print(planet.orbit())

# CREATE NEW INSTANCE OF THE PLANET

dwarfPlanet = Planet()

print(f'The name of the planet is : {dwarfPlanet.name}')

print(f'The radius of the planet is : {dwarfPlanet.radius}')

print(f'The gravity of the planet is : {dwarfPlanet.gravity}')

print(f'The system of the planet is : {dwarfPlanet.system}')

print(dwarfPlanet.orbit())

	# THIS INSTANCE ALSO GETTING THE SAME VALUES AS THE ONE INSTANCE WE CREATED ABOVE

# CREATE A NEW INSTANCE OF THE SYSTEM

pluto = Planet('Pluto',4000,5.6,'Solar System')

print(f'The name of the planet is : {pluto.name}')

print(f'The radius of the planet is : {pluto.radius}')

print(f'The gravity of the planet is : {pluto.gravity}')

print(f'The system of the planet is : {pluto.system}')

print(pluto.orbit())

# CREATE A NEW INSTANCE OF THE PLANET CLASS

neptune = Planet('Neptune',50000,7.4.'Solar System')

print(f'The name of the planet is: {neptune.name}')

print(f'The radius of the planet is: {neptune.radius}')

print(f'The gravity of the planet is: {neptune.gravity}')

print(f'The system of the planet is: {neptune.system}')

print(neptune.orbit())

	
