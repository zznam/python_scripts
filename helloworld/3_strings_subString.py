
# sub string
myName = "NGUYEN THI THUY AN"
for i in range(len(myName)):
    print(myName[i])
count = 0

print('FIRST WORD OF MIDDLE NAME:')
for i in range(len(myName)):
    if myName[i] == ' ':
        if count == 0:
            firstSpaceIdx = i
            count += 1
        elif count == 1:
            secondSpaceIdx = i
            count += 1

print(myName[((firstSpaceIdx+1)):secondSpaceIdx])

print('FULL MIDDLE NAME:')
count = 0
for i in range(len(myName)):
    if myName[i] == ' ':
        if count == 0:
            firstSpaceIdx = i
            count += 1
        else:
            lastSpaceIdx = i

print(myName[((firstSpaceIdx+1)):lastSpaceIdx])
