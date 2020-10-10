import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("code3", "docs")
print(dir_path)

fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()
try:
    fhand = open(dir_path + '\\' + fname)
except:
    print('File cannot be opened:', fname)
    exit()

