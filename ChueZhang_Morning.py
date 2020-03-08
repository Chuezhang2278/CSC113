# Chue Zhang, 23398187
# CSC 11300, Morning section
# Professor Yuksel
# 2/11/2020
# First in class assignment
import math
from scipy.integrate import quad as quad

# A
def min_to_mill(n):
    temp = n*60000
    return temp

print("========= A ========")
print(min_to_mill(3), "milliseconds") # n = 1, 60k; n = 2, 120k; n = 3, 180k

# B
def roots(a,b,c):
    delta = (b**2 - 4*a*c)
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

    print("========= B ========")
    print("x1:", x1, "x2:", x2)
    
roots(1,3,1) #roots(2,3,1) has x1 = -0.5, x2 = -1
             #constaint is b must be greater than A and C
# C

def f(x,a,b):
    return 6*x**3 - 4*x**2

result = quad(f, -2, 4, args=(-2,4)) # a = -1 , a = 1, [-2.6666666666666665, 3.547461016871157e-14]
print("========= C ========")
print(result)

# D

def cube(n):

    def findRadius(n):
        return n/4
    def sphereVolume(r):
        return (4/3)*math.pi*r**3
    def cubeVolume(n):
        return n**3
    
    return (cubeVolume(n)/(sphereVolume(findRadius(n)))) 

print("========= D ========")
print("appriximately",cube(20), "marbles") # at all n, 15.278874536821954 marbles

# E (no if else and loops, hard code)

def carrot():
    print("^_^_^^_^_^^_^_^^_^_^")

def ai():
    print("i    i    i    i    i")

def print4():
    ai()
    ai()
    ai()
    ai()

def finalprint():
    carrot()
    print4()
    carrot()
    print4()
    carrot()
    print4()
    carrot()
    print4()
    carrot()
    print4()
    carrot()
    print4()
    carrot()
    print4()
    carrot()

print("========= E ========")
finalprint()
