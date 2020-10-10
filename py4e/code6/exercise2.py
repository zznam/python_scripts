import os
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
for line in fhand:
    line = line.rstrip()
    if (line.startswith("From ")):
        words = line.split()
        if (len(words) > 6):
            hour = words[5].split(":")[0]
            counts[hour] = counts.get(hour, 0) + 1

t = list()
for word in counts:
    t.append((word, counts[word]))
t.sort()

for item in t:
    print(item[0], item[1])
    pass