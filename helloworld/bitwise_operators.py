# Python program to show
# bitwise operators

a = 10
b = 4

# Print bitwise AND operation
print("a = ", bin(a))
print("b = ", bin(b))
print("a & b =", a & b, "=", bin(a & b))

# Print bitwise OR operation
print("a | b =", a | b, "=", bin(a | b))

# Print bitwise NOT operation
print("~a =", ~a, "=", bin(~a))

# print bitwise XOR operation
print("a ^ b =", a ^ b, "=", bin(a ^ b))




# Python program to show
# shift operators
 
a = 10 # 0000 1010
b = -10 # 1111 0110 
 
# print bitwise right shift operator
print("a >> 1 =", a >> 1) # a >> 1 = 0000 0101 = 5
print("b >> 1 =", b >> 1) # b >> 1 = 1111 1011 = -5 
 
a = 5
b = -10 # 1111 0110
 
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)
