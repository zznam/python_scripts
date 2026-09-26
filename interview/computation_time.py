import datetime
''' Given an integer array nums and an integer k
write a function that returns the k most frequent elements.'''

time1 = datetime.datetime.now()
print(time1)

for i in range(2000):
    for j in range(200):
        for k in range(200):
            p = i * j * k
time2 = datetime.datetime.now()
print(time2)


print("n = 200, dTime:", time2 - time1)