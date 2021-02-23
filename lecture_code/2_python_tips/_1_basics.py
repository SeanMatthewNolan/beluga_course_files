# This file includes basic Python commands

# Printing to Console
print('Hello World')

# Basic mathematically operations are as expected
var1 = (10 + 5)/(2 * 4)

# Except exponentiation
var2 = 2 ** 3  # 2 to the third power

# ^ performs bitwise xor
var3 = 5 ^ 3  # = 12 = 0b1010 ^ 0b0110 = 0b1100

# More advanced mathematically operations are stored in the math library
import math

var4 = math.sin(2 * math.pi)

# Basic Types
# Integers
int1 = 10
int2 = int(3.2)

# Floats
float1 = 10.794
float2 = 3.1e-12
float3 = float(19)

# Strings
str1 = 'I am a string'
str2 = str(10.1)

# Concatenate Strings
str3 = 'I ' + 'am ' + 'another ' + 'string '

# Format String
str4 = 'Integer: {0:d}\nFloat: {1:.4f}'.format(int1, float1)

# Lists (mutable array)
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
list2 = [int1, float1, str1]

# Indexing
first_item = list1[0]
fourth_item = list1[3]
second_to_last_item = list1[-2]

# Slices
list_slice1 = list1[2:5]
list_slice2 = list1[3:]
list_slice3 = list1[:-2]
list_slice4 = list1[0:5:2]

# Concatenate Lists
list3 = list1 + list2

# Append to List
list3.append('new_item')

# Remove item
popped_item = list3.pop(-1)

# Tuples (immutable array)
tuple1 = (int2, str2)

# Dictionaries are specified in key value pairs (order is not guarenteed)
dict1 = {'key0': 0, 'key1': 'one', 'key2': 2.0}
dict_val = dict1['key1']

# None is an empty type, useful for placeholders or test existance
nothing = None



