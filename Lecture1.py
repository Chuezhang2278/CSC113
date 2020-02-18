import math

radius_str = input("enter radius")
radius_int = int(radius_str)

cir = 2*math.pi*radius_int
area = math.pi * (radius_int ** 2)

print(cir,area)