# Greet the user
print  ("Welcome!")

# Describe the program
print ("This program will convert mL to teaspoons, tablespoon, and cups.")

# Prompt the user for input data
user_name = input ("Please enter your name: ")
mL_str = input ("Please enter your mL value: ")

# Convert string to an integer value (just in case the user entered in a number in word form)
mL_int = int (mL_str)

# Convert mL to tspn
tspn_int = float (mL_int / 5)
# Convert tspn to tbspn
tbspn_int = float (tspn_int * 3)
# Convert tbspn to cups
cups_int = float (tbspn_int * 16)

# Output the information to the user
print (user_name + ", Here are your measurements:")
print (mL_int , "mL(s) is equivalent to " , tspn_int , "Teaspoons")
print (mL_int , "mL(s) is equivalent to " , tbspn_int , "Tablespoons")
print (mL_int , "mL(s) is equivalent to " , cups_int , "Cups")

print ("Have a great day!")
