# 2. Find number of occurrences of array2 in array1
#   Ex1: array1 = ['a', 'b', 'c', 'd', 'a', 'b', 'd', 'e', 'a', 'c']
#   array2 = ['a', 'b', 'c']
#   => 1
#   Ex2: array1 = ['a', 'a', 'a', 'a', 'a', 'a'];
#   array2 = ['a', 'a'];
#   => 5

def modulo(arrayA, arrayB):
    len_a = len(arrayA)
    len_b = len(arrayB)
    if (len_a < len_b):
        return 0
    count = 0
    numA = ''
    numB = ''

    for i in arrayA:
        numA += str(ord(i))
    for i in arrayB:
        numB += str(ord(i))

    numA = int(numA)
    numB = int(numB)
    print('numA', numA)
    print('numB', numB)
    modulo = 10 ** (len_b * 2)
    print('modulo', modulo)
    for i in range(0, len_a):
        print(numA, numB, numA % modulo , numB, count)
        if ((numA % modulo) % numB == 0):
            count += 1
        numA //= 100
    return count


array1 = ['a', 'b', 'c', 'd', 'a', 'b', 'd', 'e', 'a', 'c']
array2 = ['a', 'b', 'c']

print(modulo(array1, array2))

array1 = ['a', 'a', 'a', 'a', 'a', 'a']
array2 = ['a', 'a']

print(modulo(array1, array2))


def brute_force(array1, array2):
    if (len(array2) > len(array1)):
        return 0
    count = 0
    for i in range(0, len(array1)):
        j = i
        k = 0
        while (j < len(array1) and k < len(array2)):
            if array1[j] != array2[k]:
                break
            j += 1
            k += 1
        if (k == len(array2)):
            count += 1

    return count
