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
        if (len(words) > 1):
            print(words[1])
            counts[words[1]] = counts.get(words[1], 0) + 1
print(counts)

t = list()
for word in counts:
    t.append((counts[word], word))
t.sort(reverse=True)

            
print(t[0][1], t[0][0])