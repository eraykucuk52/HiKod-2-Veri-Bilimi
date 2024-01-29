# data type
# string, integer, float, boolean

dataType_string1 = "eray"
dataType_string2 = "6"
dataType_string3 = "06Ankara"
dataType_string4 = "0.6"
dataType_string5 = ""

dataType_integer = 52

dataType_float = 52.6

# boolean returns True or False 
# and boolean have just two value (True/False)

# I will try to convert my string values to integer
# if you want to convert string to integer, use int()
# int(dataType_string1) 
# We could not make this conversion because 
# our "eray" characters do not represent an int value.

print(int(dataType_string2)) # 6

# int(dataType_string3) 
# We got an error again

# I will try to convert my string values to float
# if you want to convert string to float, use float()
print(float(dataType_string4)) # 0.6

# I will try to convert my string values to boolean
# if you want to convert string to boolean, use bool()
a = bool(dataType_string1)
b = type(a)
print(a,"-",b) # True

print(bool(dataType_string5)) # False

# I will try to convert my integer values to string
# if you want to convert integer to string, use str()
print(repr(str(dataType_integer))) # '52'

# I will try to convert my integer values to float
# if you want to convert integer to float, use float()
print(float(dataType_integer)) # 52.0

# I will try to convert my integer values to boolean
# if you want to convert integer to boolean, use bool()
print(bool(dataType_integer)) # True

# I will try to convert my float values to string
# if you want to convert float to string, use str()
print(repr(float(dataType_integer))) # '52.6'

# I will try to convert my float values to integer
# if you want to convert float to float, use int()
print("e",int(dataType_integer)) # 52

# I will try to convert my integer values to boolean
# if you want to convert float to boolean, use bool()
print(bool(dataType_integer)) # True