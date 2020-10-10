import os
import string
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code6", "docs")
fname = 'mbox.txt'
# fname = 'mbox-short.txt'
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
totalNum = 0
for line in fhand:
    line = line.rstrip()
    # line = line.translate(str.maketrans('', '', string.punctuation))
    # line = line.lower()
    # print(line)
    for chair in line:
        chair = chair.lower()
        if (chair <= 'z' and chair >= 'a'):
            totalNum += 1
            counts[chair] = counts.get(chair, 0) + 1
        pass

t = list()
for item in counts:
    t.append((counts[item]/totalNum, item))
t.sort(reverse=True)

for item in t:
    print(item[1], round(item[0] * 100, 2))
