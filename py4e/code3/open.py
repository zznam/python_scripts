fhand = open('C:\\workspace\python_learn\py4e\docs\mbox-short.txt')
# fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
