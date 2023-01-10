# String Type
text_type_01 = 'Shivam'  # With single inverted Comma's
text_type_02 = "Shivam" "Gadekar 2132"  # With Double inverted Comma's
text_type_03 = str('Shivam')  # With the help of str Function
print(text_type_03)
# ==========================================================================================================
# Numbers
numeric_type_01 = 42  # Integer Type
numeric_type_02 = 42.0  # Float Type/ Rational Number
numeric_type_03 = 42 + 6j  # Complex Number

# ==========================================================================================================
# List Type
sequence_type_01_01 = [1, 2, 3]  # Single Type, Integer Only
sequence_type_01_02 = ['Shivam', 'Namdev', 'Gadekar']  # Single Type, String Only
sequence_type_01_03 = [[1, 2, 3], ['Shivam', 'Namdev', 'Gadekar']]  # Nested List
sequence_type_01_04 = [1, 'one', 2, 'Shivam', 'Current Affairs']  # Two Type of Data Mixed
sequence_type_01_05 = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'one', 2: 'Two'}]  # All data mixed
sequence_type_01_06 = [sequence_type_01_01, sequence_type_01_02, sequence_type_01_03]  # List called in List
# sequence_type_01_07 = [str(input('Name : ')), int(input('Phone No : '))]  # Input in List
sequence_type_01_08 = [i * i for i in range(1, 10, 1)]  # For Loop iteration in List
sequence_type_01_09 = [1, 'two', 6 + 2j, 69.69]  # Mixed Type Data
sequence_type_01_10 = [print(i) for i in sequence_type_01_02]  # For loop for List with output
sequence_type_01_11 = list()

# ==========================================================================================================
# Tuple Type
sequence_type_02_01 = (1, 2, 3, 4)  # Anything in curly bracket, separated by comma's
sequence_type_02_02 = ('Shivam', 'Namdev', 'Gadekar')  # String
sequence_type_02_03 = ((1, 2, 3, 4), ('Shivam', 'Namdev', 'Gadekar'))  # Nested Tuple
sequence_type_02_04 = ([1, 'List'], (1, 'Tuple'), {1, 'one'}, {1: 'one', 'key': 'value'})  # Mixed Type
sequence_type_02_05 = (['All List Properties'], {'All Set Properties'}, {1: 'All Dict Proper'}, 'Allowed')
sequence_type_02_06 = (i * i for i in range(1, 50, 1))
print(sequence_type_02_06)
# ==========================================================================================================
# Range Type
sequence_type_03_01 = list(print(i) for i in range(0, 15, 1))  # Range operation
# For Range operation
#   1. You Can Define limit as [for i in range(0, 10, 1)
#       1.2.  First 0 is for Start. Second 10 is Last Limit. Last 1, Step, i.e. increment by 1.

# ==========================================================================================================
# Dictionary Type
mapping_type_01 = {'Key': 'Value'}  # Defined as Key: Value in {} separated by ,
mapping_type_02 = {1: 0, 2: 1, 3: 2, 4: 3, 'Key': 'Value', 'List': sequence_type_01_02}  # Mix data
print(mapping_type_02)
mapping_type_01.get('1')
# ==========================================================================================================
# Set Type
set_type_01 = {1, 2, 3, 4}  # Simple Set
set_type_02 = {1, 2, 3, (2, 12, 15)}  # Set can Only contain Tuple Only
print(set_type_02)
set_type_03 = {}  # All list properties and set properties are same

# ==========================================================================================================
# Binary Data Types
binary_type_01 = bytes(1)  # Binary Type : bytes
binary_type_02 = bytearray(1000)  # Binary Type : bytearray
binary_type_03 = memoryview(binary_type_01)  # Binary Type : memory view

print(binary_type_01)
# print(binary_type_02)
# print(binary_type_0)
