
import numpy as np



print(np.arange(2,8,1))



array2D_1 = np.arange(9).reshape((3,3))
print("array2D_1\n", array2D_1)
array2D_2 = np.arange(10,19).reshape(3,3)
print("array2D_2\n", array2D_2)

arr3 = np.concatenate((array2D_1, array2D_2))
print(arr3)


a = np.array([1.1, 0.5, 0.8, 1.3])
print(np.where(a < 1))


a = np.array([0.1, 0.5, 0.8, 1.3])
b = 0.75
print(np.searchsorted(a, b))


