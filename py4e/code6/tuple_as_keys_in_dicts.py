directory = dict()

last = "Nam"
first = "Nguyen"
number = 65
directory[last,first] = number
last = "An"
first = "Nguyen"
number = 60
directory[last,first] = number

for last, first in directory:
    print(first, last, directory[last,first])
    pass