# ==========================================================================================================
# Tuple Methods
# List and Tuples are Almost same but, you cannot update or delete single element in tuple
# Tuples are Immutable
# You can iterate through Tuple
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 7, 9)
tup2 = (2, 3, 6, 4, 5, 8, 9, 1, 2, 8, 8, 8, 4)

# index()
print(tup1.index(8))  # Takes value and returns first index position

# len()
print(len(tup1))

# count()
print(tup1.count(8))  # Takes Value and returns times appeared

# del()
del tup1

# Iterating through tuples
for index, i in enumerate(tup2):
    print(index, i)


for i in tup2:
    print(i, 'is Number')


# Accessing Tuple
x = list(tup2[2:])
print(x)
p = tup2.index(3)
x = list(tup2[p-1: p])
print(x)

x = tuple('Shivam')  # Printed as ('S', 'h', 'i', 'v', 'a', 'm')
print(x)