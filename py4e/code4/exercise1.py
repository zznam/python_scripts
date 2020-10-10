import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code4", "docs")
fname = 'romeo.txt'
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
wordList = []
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in wordList:
            pass
        else:
            wordList.append(word)
            pass
print(sorted(wordList))
