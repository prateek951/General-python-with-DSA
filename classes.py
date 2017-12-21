# FROM planet MODULE WITHIN THE SPACE PACKAGE IMPORT PLANET CLASS

from space.planet import Planet

# import the calc module

#import the planet_mass method and planet_vol methods

from space.cal import planet_mass,planet_vol

# NOW WE CAN CREATE A NEW INSTANCE OF THE PLANET HERE

mercury = 	Planet('Mercury',444444,8.9,'Solar System')

# INVOKE THOSE METHODS

mercury_mass = planet_mass(mercury.gravity,mercury.radius)

mercury_vol = planet_vol(mercury.radius)

print(f'The mass of {mercury.name}is : {mercury_mass}')

print(f'The volume of {mercury.name} is : {mercury_vol}')


