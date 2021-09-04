import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        sub = x[i:]
        minIdx = np.argmin(sub) #min index of Sub
        swap = i + minIdx
        (x[i], x[swap]) = (x[swap], x[i])
    return x

x = np.array([2, 1, 4, 3, 5])
selection_sort(x)

print(x)