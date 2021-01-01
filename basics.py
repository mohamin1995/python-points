

numbers = [1,5,8]
squares = [n**2 for n in numbers]

print(squares)

planet = 'planet'

chars = [char+'! ' for char in planet]
print(chars)
planet = planet.upper()
print(planet)
planet = planet.lower()
print(planet)

claim = 'im mohammad amin'
words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

output = '/'.join([month, day, year])
print(output)

output_2 = "{}, you'll always be the {}th planet to me.".format('mohammad!', 1)
print(output_2)

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
output_3 = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)

print(output_3)