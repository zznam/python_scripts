counts = dict()
counts["monday"] = 5
counts["tuesday"] = 5
key = "monday"
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1

print(counts)

counts[key] = counts.get(key, 0) + 1
print(counts)

print('values: '+ str(counts.values()))
print('keys: '+ str(counts.keys()))
