# A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])

for x in thistuple:
    print(x)
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

print(len(thistuple))


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


x , y = 3, 4

print(x)
print(y)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)

x = (5, 1, 3)
print((4, 100, 200) > x)


# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

c = {'a':10, 'b':1, 'c':22}
for k, v in c.items() :
    print(k)
    print(v)