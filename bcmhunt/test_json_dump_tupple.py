import json

my_tupple = [3, 4]

str = json.dumps(my_tupple)

my_tupple_again = json.loads(str)

print(my_tupple_again)
print(type(my_tupple_again))

print(my_tupple[1])
print(my_tupple_again[1])

one_element_arr = [1]
print(one_element_arr[1])
print(one_element_arr[0])