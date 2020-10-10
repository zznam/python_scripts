fhand = open('C:\\workspace\python_learn\py4e\docs\mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)