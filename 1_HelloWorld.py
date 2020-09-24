#!/usr/bin/python
from collections import defaultdict

squares = [1, 4, 9, 16, 25]
squares2 = [3, 2, 1]
print('# print the list')
print(squares)
print('# last item: index -1# last item: index -1')
print(squares[-1])  # 25
print('#print a shadow copy list')
print(squares[:])
print('#concatenation two lists')
print(squares + squares2)

print("# something's wrong here, lean quick power in python")
cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3  # replace the wrong value,  # the cube of 4 is 64, not 65!
print(cubes)

print("# tuples_tuples")

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)

tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print("After deleting tup : ")
try:
    print(tup)
except NameError:
    print("well, it WASN'T defined after all!")
else:
    print("sure, it was defined.")


print("Basic Tuples Operations")

print("Repetition with tuple:")
print(('Hi!', 'High') * 4)

print("Length of tuple:")
print(len((1, 2, 3)))

print("check exist item in tuple:")
print(3 in (1, 2, 3))

print("iteration with tuple:")
for x in (1, 2, 3):
    print(x)

L = ('spam', 'Spam', 'SPAM!')

print('item at index')
print(L[2])  # Offsets start at zero
print(L[-1])  # Negative: count from the right
print(L[1:])  # Slicing fetches sections
print(L[2:])  # Slicing fetches sections
print(L[3:])  # Slicing fetches sections
print(L[-1:])  # Slicing fetches sections

print('index of item')
print(L.index("spam"))

numbers = defaultdict(int)
numbers['one'] = 1
numbers['two'] = 2
print(numbers['three'])
try:
    numbers['three']
except NameError:
    print("well, it's ERROR!")
else:
    print("No, it's NOT ERROR!")
