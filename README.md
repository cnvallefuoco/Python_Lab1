# Python_Lab1
#Problem Statement: Convert mL to teaspoons, tablespoons, and cups.
#Data in: mL value
#Data Out: conversion values printed on the screen
#Algorithm: Assign specific variable names with input functions that calculate conversions between units of measure. 
#Print 3 conversions from mL to teaspoons, tablespoons, and cups. 
#This program is designed to convert only whole numbers.

print ("Welcome!")

print("This program will convert mL to teaspoons, tablespoon, and cups.")
user_name = input ("Please enter your name.")
mL_str = input ("Please enter your mL value.")
mL_int = int(mL_str)

tspn_int = float (mL_int / 5)
tbspn_int = float (tspn_int * 3)
cups_int = float (tbspn_int * 16)

print (user_name + ", Here are your measurements:")
print (mL_int , "mL(s) is equivalent to" , tspn_int , "Teaspoons")
print (mL_int , "mL(s) is equivalent to" , tbspn_int , "Tablespoons")
print (mL_int , "mL(s) is equivalent to" , cups_int , "Cups")

print ("Have a great day!")
