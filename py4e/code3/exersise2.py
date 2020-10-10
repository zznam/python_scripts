import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code3", "docs")
print(dir_path)

fname = input('Enter the file name: ')
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
list = []
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        arr = line.split()
        if len(arr) > 1:
            list.append(float(arr[1]))
avg = sum(list) / len(list)
print('Average spam confidence: ' + str(avg))

# Code: http://www.py4e.com/code3/search7.py
# Or select Download from this trinket's left-hand menu
