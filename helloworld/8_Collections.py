#!/usr/bin/env python3

# Counter
# from collections import Counter
# cnt = Counter()
# list = [1,2,3,4,1,2,6,7,3,8,1]
# cnt = Counter(list)
# print(cnt[1])
# In this dictionary, the value of a key should be the 'count' of that key.
# cnt = Counter({1:3,2:4})
# print(list(cnt.elements()))

# list = [1,2,3,4,1,2,6,7,3,8,1]
# cnt = Counter(list)
# print(cnt.most_common())

# cnt = Counter({1:3,2:4})
# deduct = {1:1, 2:2}
# cnt.subtract(deduct)
# print(cnt)

# defaultdict
# from collections import defaultdict

# count = defaultdict(int)
# names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
# for names in names_list:
#     count[names] +=1
# print(count)

# OrderedDict

# from collections import Counter, OrderedDict

# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# print(od)
# for key, value in od.items():
#     print(key, value)

# list = ["a","c","c","a","b","a","a","b","c"]
# cnt = Counter(list)
# od = OrderedDict(cnt.most_common())
# for key, value in od.items():
# OrderedDict

# from collections import deque

# list = ["a","b","c"]
# deq = deque(list)
# print(deq)
# deq.append("d")
# deq.appendleft("e")
# print(deq)
# deq.pop()
# deq.popleft()
# print(deq)
# print(deq.clear())

#################################
# Please select Python 3 for running this code in IDE
# Python code to demonstrate ChainMap and
# keys(), values() and maps

# importing collections for ChainMap operations
# import collections

# # initializing dictionaries
# dic1 = { 'a' : 1, 'b' : 2 }
# dic2 = { 'b' : 3, 'c' : 4 }

# # initializing ChainMap
# chain = collections.ChainMap(dic1, dic2)

# # printing chainMap using maps
# print ("All the ChainMap contents are : ")
# print (chain.maps)

# # printing keys using keys()
# print ("All keys of ChainMap are : ")
# print (list(chain.keys()))

# # printing keys using keys()
# print ("All values of ChainMap are : ")
# # As a rule of thumb, when one key appears in more than one associated dictionaries,
# #   ChainMap takes the value for that key from the first dictionary.
# print (list(chain.values()))


#################################
# Python code to demonstrate namedtuple() and
# Access by name, index and getattr()

# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Anna', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))

# Adding values

# initializing iterable
li = ['Messi', '19', '411997']

# initializing dict
di = {'name': "Adam", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))
