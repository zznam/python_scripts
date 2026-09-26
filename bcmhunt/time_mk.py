
# Python program to explain time.mktime() method 
    
# importing time module 
import time 
  
  
# time.gmtime() method will returns
# a time.struct_time object in UTC
# for the time expressed in seconds
# since the epoch
seconds = 1000000
obj1 = time.gmtime(seconds)
  
# Print time.struct_time object (in UTC)
print(obj1)
  
# Convert the time.struct_time
# object to local time expressed in
# seconds since the epoch
# using time.mktime() method
time_sec = time.mktime(obj1)

time_sec = time.mktime(obj1)
  
# Print the local time in seconds
print("\nLocal time (in seconds):", time_sec)
  
  
# time.strptime() method parse 
# a string representing a time
# according to the given format
# and returns a time.struct_time object
  
# Time string 
# t = "14 Sep 2019 10:50:00"
  
# # Parse the time string using
# # time.strptime() method
# obj2 = time.strptime(t, "% d % b % Y % H:% M:% S")
  
# # Convert the time.struct_time
# # object to local time expressed in
# # seconds since the epoch
# # using time.mktime() method
# time_sec = time.mktime(obj2)
  
# # Print the local time in seconds
# print("\nLocal time (in seconds):", time_sec)