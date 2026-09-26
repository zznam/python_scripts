# Ternary Operators

is_nice = True
state = "nice" if is_nice else "not nice"
print('state:', state)
nice = True

#True == 1 and False == 0
personality = ("mean", "nice")[nice]
print("The cat is:", personality)

output = None
msg = output or "No data returned"
print(msg)

# define function parameters with dynamic default values


def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)


my_function("John")
my_function("Mike", "anonymous123")