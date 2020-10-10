import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code5", "docs")
fname = 'words.txt'
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
wordList = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        wordList[word] = wordList.get(word, 0) + 1
print(wordList)
