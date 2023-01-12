# ==========================================================================================================
# To Convert Binary into integer only
s = '11111111111111111111111111111111'  # 32 Bit of Memory Means
c = int(s, 2)
print(c)

# To Convert Integer to float or vice versa
x = int(22)
y = float(22.77)
float(x)  # 22.0
int(y)  # 22

# To Convert character in number/integer
x = 's'
y = ord(x)
print(y)  # 115

# To Convert integer only into hexadecimal string
x = 15
y = hex(x)
print(y)  # 0xf

# To Convert integer only into octal
x = 15
y = oct(x)
print(y)  # 0o17

# To convert set/list/dict to Tuple
list1 = [1, 2, 3, 4]  # or 'Shivam' into tuple as ('s', 'h', 'v', 'a', 'm')
print(type(list1))  # List
tuple1 = tuple(list1)  # You always need variable to assign converted data type
print(type(tuple1))  # Original List1 is in List but tuple1 is tuple

# To convert list/tuple/dict to set
list1 = {1: 2, 3: 4}  # or 'Shivam' into tuple as ('s', 'h', 'v', 'a', 'm')
print(type(list1))  # List
set1 = set(list1)  # You always need variable to assign converted data type
print(type(set1))  # Original List1 is in List but set1 is set

# To convert tuple/set to List
tuple11 = {1: 2, 3: 4}  # or 'Shivam' into tuple as ('s', 'h', 'v', 'a', 'm')
print(type(tuple11))  # List
list11 = list(tuple11)  # You always need variable to assign converted data type
print(type(list11))  # Original tuple11 is in tuple but list11 is list

# To convert tuple (key, value) into dictionary
tuple1 = ([1, 'one'], [2, 'Two'], [3, 'Three'], [4, 'Four'])
print(type(tuple1))
dict1 = dict(tuple1)
print(dict1)

# To convert real number into imaginary
a, b = 12, 15  # input
c = complex(a, b)  # Function
print(c)  # Gives Output as (12 + 15j)

# To convert integer into string integer
x = 12  # Integer
y = str(x)  # Converted into String
print(y, type(x), type(y))  # 12 <class 'int'> <class 'str'>
