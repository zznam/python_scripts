import urllib.request

url = input('Input URL: ')
try:
    fhand = urllib.request.urlopen(url)
except:
    print("Invalid URL!")
    exit()
count  = 0
total = 0
for line in fhand:
    str = line.decode()
    if count < 3000:
        if count + len(str) < 3000:
            print(str.strip())
        else:
            print(str[:(3000-count)])
    print(len(str))
    count+= len(str)
print("Total characters: ", count)

