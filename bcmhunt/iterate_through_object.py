class ProlongAchievementType(object):
    # pve-related
    BATTLE_PVE_PLAY = 1
    BATTLE_PVE_WIN = 2
    BATTLE_PVE_DISADV_PLAY = 3
    BATTLE_PVE_DISADV_WIN = 4
    BATTLE_PVE_LOWER_BP_PLAY = 5
    BATTLE_PVE_LOWER_BP_WIN = 6
    BATTLE_PVE_ENCOUNTER_DIFF_TYPES = 7
    BATTLE_PVE_COMMON_MONSTERS = 8
    BATTLE_PVE_UNCOMMON_MONSTERS = 9
    BATTLE_PVE_RARE_MONSTERS = 10
    BATTLE_PVE_EPIC_MONSTERS = 11
    BATTLE_PVE_LEGENDARY_MONSTERS = 12
    # item-related
    ITEM_BLOCK_USED = 20
    ITEM_ABSORB_USED = 21
    ITEM_BREAK_USED = 22
    ITEM_DODGE_USED = 23
    # teleport
    TELEPORT_TIMES = 30
    # pvp-related
    BATTLE_PVP_PLAY = 40
    BATTLE_PVP_FRIENDS = 41
    BATTLE_PVP_ACCEPT_CHALLENGE = 42
    BATTLE_PVP_WIN = 43
    # catch-related
    CATCH_PLAY = 50
    CATCH_CAUGHT_MONSTER_TYPE_1 = 51
    CATCH_CAUGHT_MONSTER_TYPE_2 = 52
    CATCH_CAUGHT_MONSTER_TYPE_3 = 53
    CATCH_CAUGHT_MONSTER_TYPE_4 = 54
    CATCH_CAUGHT_MONSTER_TYPE_5 = 55
    CATCH_CAUGHT_MONSTER_TYPE_6 = 56
    CATCH_CAUGHT_MONSTER_TYPE_7 = 57
    CATCH_CAUGHT_MONSTER_TYPE_8 = 58
    CATCH_CAUGHT_MONSTER_TYPE_9 = 59
    CATCH_CAUGHT_MONSTER_TYPE_10 = 60
    CATCH_CAUGHT_COMMON_MONSTERS = 61
    CATCH_CAUGHT_UNCOMMON_MONSTERS = 62
    CATCH_CAUGHT_RARE_MONSTERS = 63
    CATCH_CAUGHT = 64
    CATCH_CAUGHT_DIFF_TYPES = 65
    CATCH_FAILED = 66
    #own-related
    OWN_MONSTER_LEVEL = 70
    OWN_MONSTER_TYPE_1 = 71
    OWN_MONSTER_TYPE_2 = 72
    OWN_MONSTER_TYPE_3 = 73
    OWN_MONSTER_TYPE_4 = 74
    OWN_MONSTER_TYPE_5 = 75
    OWN_MONSTER_TYPE_6 = 76
    OWN_MONSTER_TYPE_7 = 77
    OWN_MONSTER_TYPE_8 = 78
    OWN_MONSTER_TYPE_9 = 79
    OWN_MONSTER_TYPE_10 = 80
    OWN_MONSTER_DIFF_TYPES = 81

def get_prolong_type_list():
    list_types = []
    for item in vars(ProlongAchievementType).items():
        if type(item[1]) == int:
            list_types.append(item[1])
    return list_types

def is_prolong_achievement(achievement_type):
    list_types = get_prolong_type_list()
    print(len(list_types))
    return achievement_type in list_types

print(is_prolong_achievement(1))
print(is_prolong_achievement(13))

print(ProlongAchievementType.OWN_MONSTER_TYPE_10)
print(getattr(ProlongAchievementType, "OWN_MONSTER_TYPE_10"))
print(getattr(ProlongAchievementType, "OWN_MONSTER_TYPE_" + str(9)))

turn = {}
current_attack_turn = turn.get("current_attack_turn", 0)
print(current_attack_turn)