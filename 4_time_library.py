import time
seconds = time.time()
print("Seconds since epoch =", seconds)
# seconds passed since epoch
local_time = time.ctime()
print("Local time:", local_time)
local_time2 = time.localtime()
print("Local time:", local_time2)
print("today is: " + str(local_time2.tm_year) + "/" +
      str(local_time2.tm_mon) + "/" + str(local_time2.tm_mday))
# Python time.sleep()
print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
