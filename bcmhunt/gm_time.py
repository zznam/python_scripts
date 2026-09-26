import time
import calendar


def get_timestamp():
    return int(time.time())


def get_end_day_timestamp():
    struct_now = time.gmtime()
    t = (struct_now.tm_year, struct_now.tm_mon, struct_now.tm_mday, 0, 0, 0,
         struct_now.tm_wday, struct_now.tm_yday, struct_now.tm_isdst)
    return calendar.timegm(t) + 24 * 60 * 60


def from_yyyymmdd_to_ts(str_date):
    year = int(str_date[0:4])
    mon = int(str_date[4:6])
    mday = int(str_date[6:8])
    print(year, mon, mday)
    t = (year, mon, mday, 0, 0, 0)
    return calendar.timegm(t)


def from_ts_to_yyyymmdd(ts):
    struct_now = time.gmtime(ts)
    ret = ""
    ret += str(struct_now.tm_year)
    ret += str(struct_now.tm_mon) if struct_now.tm_mon > 9 else (
        "0" + str(struct_now.tm_mon))
    ret += str(struct_now.tm_mday) if struct_now.tm_mday > 9 else (
        "0" + str(struct_now.tm_mday))
    return ret


print(get_timestamp())
print(get_end_day_timestamp())

ts = from_yyyymmdd_to_ts("20220630")
print(ts)
print(from_ts_to_yyyymmdd(ts))


init_date = from_ts_to_yyyymmdd(get_timestamp())
print(init_date)



def get_pre_dates(day_num):
    ts = get_timestamp()
    dates = []
    while day_num > 0:
        ts -= 86400
        print("ts", ts)
        date = from_ts_to_yyyymmdd(ts)
        dates.append(date)
        day_num -= 1
    return dates


print(get_pre_dates(7))

if True:
    level_config = None
else:
    (_, level_config, _) = (1, 2, 3)

print(level_config)

parent = {"child1": "343","child2": "345",}
child = "child1"
if (child in parent):
    print(parent[child])
    
cfg_key = str(500) + "_" + str(1)
print(cfg_key)
