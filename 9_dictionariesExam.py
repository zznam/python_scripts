# Create and print a dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# Accessing Items
x = thisdict["model"]
print(x)
# Loop Through a Dictionary
for x in thisdict:
    print(x)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
