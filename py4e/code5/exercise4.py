import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code5", "docs")
fname = 'mbox.txt'
# fname = 'mbox-short.txt'
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
countDict = dict()
for line in fhand:
    line = line.rstrip()
    if (line.startswith("From")):
        words = line.split()
        if (len(words) > 2):
            word = words[1]
            countDict[word] = countDict.get(word, 0) + 1
maxKey = ""
for key in countDict:
    curMax = countDict.get(maxKey, 0)
    if (curMax < countDict.get(key, 0)):
        maxKey = key
    pass
print(maxKey, countDict.get(maxKey, 0))
