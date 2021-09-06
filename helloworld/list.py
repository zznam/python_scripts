
list1 = ['a', 'b', 'c']
list2 = ['c', 'a', 'b']
print(list1 == list2)

l = [2, 3, [4, 5]]
l2 = l.copy()
l2[0] = 88
print(l)
print(l2)

student = {
    1: {
        'name': 'Anna',
        'age': '27',
        'sex': 'Female'
    },
    2: {
        'name': 'Mike',
        'age': '22',
        'sex': 'Male'
    }
}
print(student[1]['age'])
print(type(student))
print(type(student[1]))
print(type(student[1]['age']))


X = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']

print(X[1][2][1][-1])