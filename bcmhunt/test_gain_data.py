def get_mon_token_ids(battle_data, key):
    token_ids = []
    if battle_data:
        mon_data = battle_data.get(key, [])
        for mon in mon_data:
            token_id = mon.get("token_id", None)
            if token_id:
                token_ids.append(token_id)
    return token_ids

def cal_bp_dict_and_gain_data(require_update, battle_data):
    acceptor_mon_token_ids = get_mon_token_ids(battle_data, "acceptor_monster_data")
    challenger_mon_token_ids = get_mon_token_ids(battle_data, "challenger_monster_data")
    acceptor_num_mon_level_up = 0
    challenger_num_mon_level_up = 0
    gain_exp_monsters = {}
    monster_bp_dict = {}
    if "gain_exp_monsters" in battle_data and len(
            battle_data["gain_exp_monsters"]) > 0:
        gain_exp_monster_ids = battle_data["gain_exp_monsters"].keys()
        universe_monster_records = []
        universe_monster_record_dict = {}
        for universe_monster_record in universe_monster_records:
            universe_monster_record_dict[
                universe_monster_record.token_id] = universe_monster_record
        monster_records = []
        monster_record_dict = {}
        for monster_record in monster_records:
            monster_record_dict[monster_record.token_id] = monster_record

        for token_id, gain_exp in battle_data["gain_exp_monsters"].items():
            token_id = int(token_id)
            monster_record = monster_record_dict.get(token_id)
            final_exp = 50
            current_level = 1
            if require_update:
                final_exp += gain_exp
            final_level = 2
            gain_exp_monsters[token_id] = {
                "gain_exp": gain_exp,
                "level": final_level,
            }
            if final_level > current_level:
                if token_id in acceptor_mon_token_ids:
                    acceptor_num_mon_level_up += 1
                elif token_id in challenger_mon_token_ids:
                    challenger_num_mon_level_up += 1

    print(acceptor_num_mon_level_up, challenger_num_mon_level_up)
    print(acceptor_mon_token_ids, challenger_mon_token_ids)


battle_data = {
    'challenger_monster_data': [{
        'token_id': 37377,
        'species': 515,
        'species_name': 'Kousti',
        'rarity': 7,
        'pri_type': 5,
        'current_exp': 2211,
        'current_level': 12,
        'origin_stats': [94, 103, 100, 0, 101, 107],
        'stats': [94, 103, 100, 0, 101, 107],
        'bp': 84,
        'hp': 94,
        'atk': 103,
        'def': 100,
        'spa': 0,
        'spd': 101,
        'sp': 107,
        'attached_item_id': 0,
        'attached_item_type': 0,
        'attached_item_subtype': 0,
        'buff_battle_percentages': [0, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 0
        }
    }, {
        'token_id': 1672705,
        'species': 60,
        'species_name': 'Pigster',
        'rarity': 1,
        'pri_type': 10,
        'current_exp': 98,
        'current_level': 1,
        'origin_stats': [74, 71, 60, 0, 27, 70],
        'stats': [74, 71, 60, 0, 27, 70],
        'bp': 50,
        'hp': 74,
        'atk': 71,
        'def': 60,
        'spa': 0,
        'spd': 27,
        'sp': 70,
        'attached_item_id': 0,
        'attached_item_type': 0,
        'attached_item_subtype': 0,
        'buff_battle_percentages': [0, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 0
        }
    }, {
        'token_id': 1672961,
        'species': 46,
        'species_name': 'Suwat',
        'rarity': 1,
        'pri_type': 10,
        'current_exp': 99,
        'current_level': 1,
        'origin_stats': [51, 69, 75, 0, 21, 58],
        'stats': [51, 69, 75, 0, 21, 58],
        'bp': 45,
        'hp': 51,
        'atk': 69,
        'def': 75,
        'spa': 0,
        'spd': 21,
        'sp': 58,
        'attached_item_id': 0,
        'attached_item_type': 0,
        'attached_item_subtype': 0,
        'buff_battle_percentages': [0, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 0
        }
    }, {
        'token_id': 1685761,
        'species': 602,
        'species_name': 'Bilanzer',
        'rarity': 9,
        'pri_type': 2,
        'current_exp': 936,
        'current_level': 7,
        'origin_stats': [161, 218, 243, 68, 74, 194],
        'stats': [177, 218, 243, 68, 74, 194],
        'bp': 159,
        'hp': 177,
        'atk': 218,
        'def': 243,
        'spa': 68,
        'spd': 74,
        'sp': 194,
        'attached_item_id': 1793,
        'attached_item_type': 3,
        'attached_item_subtype': 1,
        'buff_battle_percentages': [10, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 5
        }
    }, {
        'token_id': 1686017,
        'species': 606,
        'species_name': 'Ultrox',
        'rarity': 9,
        'pri_type': 9,
        'current_exp': 596,
        'current_level': 5,
        'origin_stats': [225, 185, 182, 92, 84, 136],
        'stats': [258, 185, 182, 92, 84, 136],
        'bp': 150,
        'hp': 258,
        'atk': 185,
        'def': 182,
        'spa': 92,
        'spd': 84,
        'sp': 136,
        'attached_item_id': 11009,
        'attached_item_type': 3,
        'attached_item_subtype': 2,
        'buff_battle_percentages': [15, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 10
        }
    }, {
        'token_id': 1686273,
        'species': 604,
        'species_name': 'Polipus',
        'rarity': 9,
        'pri_type': 7,
        'current_exp': 350,
        'current_level': 4,
        'origin_stats': [182, 150, 209, 86, 82, 154],
        'stats': [200, 150, 209, 86, 82, 154],
        'bp': 143,
        'hp': 200,
        'atk': 150,
        'def': 209,
        'spa': 86,
        'spd': 82,
        'sp': 154,
        'attached_item_id': 18945,
        'attached_item_type': 3,
        'attached_item_subtype': 1,
        'buff_battle_percentages': [10, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 5
        }
    }],
    'challenger_team_avg':
    154,
    'acceptor_team_avg':
    158,
    'acceptor_monster_data': [{
        'token_id': 167520,
        'species': 119,
        'species_name': 'Pindoe',
        'rarity': 2,
        'pri_type': 5,
        'current_exp': 183738,
        'current_level': 51,
        'origin_stats': [172, 185, 235, 78, 117, 183],
        'stats': [197, 185, 235, 78, 117, 183],
        'bp': 161,
        'hp': 197,
        'atk': 185,
        'def': 235,
        'spa': 78,
        'spd': 117,
        'sp': 183,
        'attached_item_id': 0,
        'attached_item_type': 3,
        'attached_item_subtype': 2,
        'buff_battle_percentages': [15, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 10
        }
    }, {
        'token_id': 920077,
        'species': 56,
        'species_name': 'Gleeter',
        'rarity': 1,
        'pri_type': 9,
        'current_exp': 6370587,
        'current_level': 88,
        'origin_stats': [197, 163, 266, 0, 125, 181],
        'stats': [197, 163, 345, 0, 125, 181],
        'bp': 155,
        'hp': 197,
        'atk': 163,
        'def': 345,
        'spa': 0,
        'spd': 125,
        'sp': 181,
        'attached_item_id': 0,
        'attached_item_type': 2,
        'attached_item_subtype': 3,
        'buff_battle_percentages': [0, 0, 30, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 35,
            'break': 0,
            'absorb': 0
        }
    }, {
        'token_id': 736767,
        'species': 103,
        'species_name': 'Torchus',
        'rarity': 2,
        'pri_type': 4,
        'current_exp': 166738,
        'current_level': 50,
        'origin_stats': [176, 190, 186, 85, 107, 153],
        'stats': [176, 190, 186, 85, 107, 153],
        'bp': 149,
        'hp': 176,
        'atk': 190,
        'def': 186,
        'spa': 85,
        'spd': 107,
        'sp': 153,
        'attached_item_id': 0,
        'attached_item_type': 0,
        'attached_item_subtype': 0,
        'buff_battle_percentages': [0, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 0
        }
    }, {
        'token_id': 258784,
        'species': 74,
        'species_name': 'Sahasra',
        'rarity': 1,
        'pri_type': 7,
        'current_exp': 2026691,
        'current_level': 76,
        'origin_stats': [214, 229, 153, 0, 122, 173],
        'stats': [214, 251, 153, 0, 122, 173],
        'bp': 149,
        'hp': 214,
        'atk': 251,
        'def': 153,
        'spa': 0,
        'spd': 122,
        'sp': 173,
        'attached_item_id': 0,
        'attached_item_type': 1,
        'attached_item_subtype': 2,
        'buff_battle_percentages': [0, 10, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 4,
            'absorb': 0
        }
    }, {
        'token_id': 210437,
        'species': 114,
        'species_name': 'Reinlekt',
        'rarity': 2,
        'pri_type': 2,
        'current_exp': 124487,
        'current_level': 47,
        'origin_stats': [190, 180, 174, 82, 108, 168],
        'stats': [190, 180, 174, 82, 108, 168],
        'bp': 150,
        'hp': 190,
        'atk': 180,
        'def': 174,
        'spa': 82,
        'spd': 108,
        'sp': 168,
        'attached_item_id': 0,
        'attached_item_type': 0,
        'attached_item_subtype': 0,
        'buff_battle_percentages': [0, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 0
        }
    }, {
        'token_id': 55284,
        'species': 115,
        'species_name': 'Flooty',
        'rarity': 2,
        'pri_type': 3,
        'current_exp': 151288,
        'current_level': 49,
        'origin_stats': [172, 168, 190, 84, 134, 183],
        'stats': [172, 168, 190, 84, 134, 183],
        'bp': 155,
        'hp': 172,
        'atk': 168,
        'def': 190,
        'spa': 84,
        'spd': 134,
        'sp': 183,
        'attached_item_id': 0,
        'attached_item_type': 0,
        'attached_item_subtype': 0,
        'buff_battle_percentages': [0, 0, 0, 0, 0, 0],
        'hit_effect_probabilities': {
            'dodge': 0,
            'block': 0,
            'break': 0,
            'absorb': 0
        }
    }],
    'stage':
    3,
    'expiry_time':
    1656404190,
    'start_time':
    1656403878,
    'end_time':
    0,
    'challenger_win_count':
    2,
    'acceptor_win_count':
    0,
    'winner_ticket_id':
    26077,
    'gain_exp_monsters': {
        '1686017': 16,
        '1685761': 20,
        '1686273': 20
    },
    'used_item_ids': [1793, 18945, 11009]
}

cal_bp_dict_and_gain_data(True, battle_data)
