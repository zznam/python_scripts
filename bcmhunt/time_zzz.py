import time
seconds = time.time()
print("Seconds since epoch =", seconds)	


# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
gm_time = time.gmtime(seconds)
print("Local time:", local_time)
print("UTC time:", gm_time)