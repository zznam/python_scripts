import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code4", "docs")
# fname = 'mbox.txt'
fname = 'mbox-short.txt'
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    line = line.rstrip()
    if (line.startswith("From")):
        count = count + 1
        words = line.split()
        if (len(words) > 1):
            print(words[1])
print('There were ' + str(count) + ' lines in the file with From as the first word')
