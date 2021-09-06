myset = {"apple", "banana", "cherry"}
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("myset == thisset:", myset == thisset)

# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Set items are unordered, unchangeable, and do not allow duplicate values.

s = {100, 200, 300}
s2 = {300, 400, 500, 100}

print("s = ", s)
print("s2 = ", s2)

new = s.union(s)
print("s.union(s) =", new)

new = s.union(s2)
print("s.union(s2) =", new)

print("s|s2", s | s2)

#set union with list
# print("s | {300, 400, 500}", s | [300, 400, 500])
print("s.union([300, 400, 500])", s.union([300, 400, 500]))

s.union([300, 400, 500])
# s | [300, 400, 500] 
s | {300, 400, 500}
s.union({300, 400, 500})
s.union(set([300, 400, 500]))
s | set([300, 400, 500])
