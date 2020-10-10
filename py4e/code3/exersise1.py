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
for line in fhand:
    print(line.rstrip().upper())

# Code: http://www.py4e.com/code3/search7.py
# Or select Download from this trinket's left-hand menu
