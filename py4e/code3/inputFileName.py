import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code3", "docs")
print(dir_path)

fname = input('Enter the file name: ')
try:
    fhand = open(dir_path +'\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Code: http://www.py4e.com/code3/search7.py
# Or select Download from this trinket's left-hand menu
