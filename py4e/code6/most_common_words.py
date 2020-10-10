import os
import string
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code6", "docs")
fname = 'romeo.txt'
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)
#lst[:10] => get ten items from the beginning of the list
for key, val in lst[:10]:
    print(key, val)

# Code: http://www.py4e.com/code3/count3.py
