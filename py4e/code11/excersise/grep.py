import re
reg = input("Enter a regular expression: ")
f = open("../mbox.txt", "r")
count = 0
for line in f:
    line = line.rstrip()
    list = re.findall(reg, line)
    count += len(list)
    pass
print("mbox.txt had %d lines that matched %s" % (count, reg))