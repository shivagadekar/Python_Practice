# ==========================================================================================================

# This Program will Help to Understand All Python List Method

list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

# copy()
list2 = list1.copy()  # Copy list or use list2 = list1

# append()
list2.append('nine')  # Add element at the end of list

# clear()
list1.clear()  # Clears whole list by deleting all elements


# del()
del list1  # Delete Full List

# Defining Again, because we cleared in previous line by clear(), command
list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# count()
print(list1.count('zero'))

# extend()
list1.extend('9')  # Adds string character wise as ['n', 'i', 'n', 'e'] and Takes Only String

# index()
print(list1.index('three'))  # Takes actual value and returns index starting from 0

# insert()
list1.insert(10, 'ten')  # takes index and add value at that position

# pop()
print(list1.pop())  # Removes value at index no, if not given, returns random

# remove()
print(list1.remove('nine'))  # Remove value, not index

# reverse()
list1.reverse()  # Does not return/prints anything, modifies parent list

# sort()
list1.sort()  # Does not return/prints anything, modifies parent list

list1 = [i for i in range(0, 10)]
print(list1)
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # Both are equal
print(list1)

# len()
print(len(list1))

# min()
print(min(list1))

# max()
print((max(list1)))

# sum()
print(sum(list1))

# any()
print(any(list1))

# all()
print(all(list1))
