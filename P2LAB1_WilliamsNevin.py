#Nevin Williams
#9/9/26
#P2LAB1
#circle formula calculator

#imports math module
import math
#gets radius of circle and makes it a float
rc  = float(input("What is the radius of the circle?: "))

#formulas for diameter, circumference, and area
dc = rc * 2
cc = 2 * math.pi * rc
ac = math.pi * rc ** 2

#prints diameter, circumference, and area
print("\nThe diameter of the circle is:",dc)
print("\nThe circumference of the circle is:",round(cc,2))
print("\nThe area of the circle is:",round(ac,3))