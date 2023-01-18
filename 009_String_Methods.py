# Python String Methods
# It does not change value in variable, it just displays it.
# To assign updated string, variable need to define
# To activate string methods, assign string to variable,
# then press variable and dot operator to list methods (str1.[Then List appears Here]

str1 = 'shivam'
str2 = 'SHIVAM'
str3 = ' Hi I am Shivam, 55'
str4 = '1232456460'
str5 = 'SHivam'

# Capitalize First Letter
capitalize_ = str1.capitalize()
print(capitalize_)

# Convert string to Lower Case
lower_case = str2.casefold()
print(lower_case)

# Returns Centered String (Don't Know, What is This)
centered_string = str3.casefold()
print(centered_string)

# Count Repetitions of string
repeat = str3.count('am')
print(repeat)

# Returns Encoded version of String
encode = str3.encode()
print(encode)

# Ends With
ends_with = str1.endswith('m')
print(ends_with)

# find Function
find = str1.find('v')
print(find)

# Format String()
print('Hello {}, World {}'.format(12, 15))  # Variables can be added, in place of 12 and 15 and in {} also.
print('Hello {1}, World {0}'.format('first', 'second'))

# format_map

# index()
index = str3.index("55")  # Returns Position of value only
print(index)

# isalnum()
isalnum = str4.isalnum()  # Returns True value, if there is no space
print(isalnum)

# isalpha
isalpha = str3.isalpha()  # Returns True if they consist only alphabet
print(isalpha)

# isdecimal
isdecimal = str5.isdecimal()
print(isdecimal)

# isdigit
print(str4.isdigit())
print(str5.rjust(2))
