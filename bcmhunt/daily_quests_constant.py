from random import randrange

class DailyAchievementType(object):
    DAILY_LOGIN = 500
    DAILY_PVE_WIN = 501
    DAILY_PVP_PLAY = 502
    DAILY_CATCH_ATTEMPT = 503
    DAILY_TELEPORT = 504
    DAILY_STAMINA_USED = 505
    DAILY_BATTLE_INSURANCE = 506
    #
    DAILY_PVE_TYPE_1 = 511
    DAILY_PVE_TYPE_2 = 512
    DAILY_PVE_TYPE_3 = 513
    DAILY_PVE_TYPE_4 = 514
    DAILY_PVE_TYPE_5 = 515
    DAILY_PVE_TYPE_6 = 516
    DAILY_PVE_TYPE_7 = 517
    DAILY_PVE_TYPE_8 = 518
    DAILY_PVE_TYPE_9 = 519
    DAILY_PVE_TYPE_10 = 520
    #
    DAILY_PVE_MAP_1 = 521 # jungle
    DAILY_PVE_MAP_2 = 522 # mountain
    DAILY_PVE_MAP_3 = 523 # desert
    #
    DAILY_MONSTER_LEVEL_UP = 524
    
def get_daily_type_list():
    list_types = []
    for item in vars(DailyAchievementType).items():
        if type(item[1]) == int:
            list_types.append(item[1])
    return list_types

def get_daily_pve_by_type_list():
    list_types = []
    for i in range(1, 11):
        list_types.append(getattr(DailyAchievementType, "DAILY_PVE_TYPE_" + str(i)))
    return list_types

def get_daily_pve_by_map_list():
    list_types = []
    for i in range(1, 4):
        list_types.append(getattr(DailyAchievementType, "DAILY_PVE_MAP_" + str(i)))
    return list_types

def get_choices(cls):
    return [(value, key) for key, value in cls.__dict__.items() if key[:1] != '_']

def get_values(cls):
    return [value for key, value in cls.__dict__.items() if key[:1] != '_']

print(get_daily_type_list())
print(get_daily_pve_by_type_list())
print(get_daily_pve_by_map_list())



achievement_dict = {}


achievement_dict[511] = 24232
pve_by_type_list = get_daily_pve_by_type_list()
exist = False
for type in pve_by_type_list:
    current = achievement_dict.get(type)
    if current:
        exist = True
        break
if not exist:
    ran_idx = randrange(len(pve_by_type_list))
    ran_type = pve_by_type_list[ran_idx]
    print("creating...")
    
    
print('getattr(DailyAchievementType, "DAILY_PVE_TYPE_" + str(i))', getattr(DailyAchievementType, "DAILY_PVE_TYPE_" + str(1)))

print("get_choices", get_choices(DailyAchievementType))
print("get_values", get_values(DailyAchievementType))


class MonsterType(object):
    NONE = 0
    EARTH = 1
    ELECTRIC = 2
    WATER = 3
    FIRE = 4
    ICE = 5
    WIND = 6
    DARK = 7
    LIGHT = 8
    SPIRIT = 9
    NEUTRAL = 10
    
print("get_values", get_values(MonsterType))