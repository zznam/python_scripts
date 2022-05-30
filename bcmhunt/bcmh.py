# Given a CSV file (string), parse it into individual rows/columns

# 1
# - tokens can only contain alphanumeric letters

# name,address,streetnumber1,streetnumber2,home number

# 2

# - tokens can contain comma, need to enclose them by double quotes e.g. Nguyen Van Teo,"13 Dinh Tien Hoang, Da Lat", Vietnam

# Nguyen Van Teo
# 13 Dinh Tien hoang, Da Lat
# Vietnam


row = "name,address,streetnumber1,streetnumber2,home number"
row = """Nguyen Van Teo,"13 Dinh Tien Hoang, Da Lat", Vietnam """

arr = []

curName = ''
countDouble = 0


def formatName(name):
    start = 0
    end = len(name)
    for i in range(len(name)):
        if (name[i] == ' '):
            start += 1
        else:
            break
    for i in range(len(name) - 1, -1, -1):
        if (name[i] == ' '):
            end -= 1
        else:
            break

    if (start >= end):
        return ''

    return name[start:end]


for i in range(len(row)):
    c = row[i]
    if (c != ','):
        curName += c
        if (c == '"'):
            countDouble += 1
    elif countDouble % 2 == 0:
        arr.append(formatName(curName))
        curName = ''
        countDouble = 0
    else:
        curName += c
        if (c == '"'):
            countDouble += 1

arr.append(formatName(curName))

print(arr)
