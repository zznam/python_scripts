import time
import datetime
d = datetime.datetime.now()
print(d)
now = time.time()
obj1 = time.localtime(now)
print(int(now))
print(obj1)


zeroHour = time.struct_time((obj1.tm_year, obj1.tm_mon, obj1.tm_mday, 0, 0, 0, obj1.tm_wday, obj1.tm_yday, obj1.tm_isdst))
zero_ts = time.mktime(zeroHour)
print(zeroHour)
print(int(zero_ts))