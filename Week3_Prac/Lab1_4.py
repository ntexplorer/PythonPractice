import math

def convert_degree_to_radians(x):
    rad = x / 360 * 2 * math.pi
    return rad

degree = int(input('Enter the degree you want to convert: '))
rad = convert_degree_to_radians(degree)

print(degree)
print(rad)
print("An angle of {} in degrees is {} in radians".format(degree, rad))
