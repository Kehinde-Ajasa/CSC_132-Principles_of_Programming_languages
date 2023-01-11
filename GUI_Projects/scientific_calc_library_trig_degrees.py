# First we import the math module

# we're importing all the function in the math module; but we'll be working with just the Trigonometry functions
from math import *

# The following code returns the values of trig functions ...
# Say our expression is Cos(x)... x is now in Degrees and not the default (radian)


def Sin(num):
	return sin(radians(num))


def Cos(num):
	return cos(radians(num))


def Tan(num):
	return tan(radians(num))


def Cosec(num):
	return 1/(sin(radians(num)))


def Sec(num):
	return 1/(cos(radians(num)))


def Cot(num):
	return 1/(tan(radians(num)))


def Asin(num):
	return asin(num) * 180/pi


def Acos(num):
	return acos(num) * 180/pi


def Atan(num):
	return atan(num) * 180/pi


"""
Again, the functions we created here are like Degree versions of the Trig...
Just like we can switch from radian to Degree on our everyday Scientific Calculators....
Use sentence case "Sin(90)" for degrees and Lower case "sin(90)" for Radians

Hope this is clear enough...
"""
