turns = [
    {
        "current_attack_turn": 2,
        "is_special_move": False,
        "is_strong_against": False,
        "is_resistant_to": False,
        "mon1_hp_before": 250,
        "mon1_hp_after": 250,
        "mon2_hp_before": 228,
        "mon2_hp_after": 228,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": True
        }
    },
    {
        "current_attack_turn": 1,
        "is_special_move": False,
        "is_strong_against": True,
        "is_resistant_to": False,
        "mon1_hp_before": 250,
        "mon1_hp_after": 250,
        "mon2_hp_before": 228,
        "mon2_hp_after": 208,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": False
        }
    },
    {
        "current_attack_turn": 2,
        "is_special_move": False,
        "is_strong_against": False,
        "is_resistant_to": False,
        "mon1_hp_before": 250,
        "mon1_hp_after": 160,
        "mon2_hp_before": 208,
        "mon2_hp_after": 208,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": False
        }
    },
    {
        "current_attack_turn": 1,
        "is_special_move": False,
        "is_strong_against": True,
        "is_resistant_to": False,
        "mon1_hp_before": 160,
        "mon1_hp_after": 160,
        "mon2_hp_before": 208,
        "mon2_hp_after": 188,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": False
        }
    },
    {
        "current_attack_turn": 2,
        "is_special_move": False,
        "is_strong_against": False,
        "is_resistant_to": False,
        "mon1_hp_before": 160,
        "mon1_hp_after": 72,
        "mon2_hp_before": 188,
        "mon2_hp_after": 188,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": False
        }
    },
    {
        "current_attack_turn": 1,
        "is_special_move": True,
        "is_strong_against": True,
        "is_resistant_to": False,
        "mon1_hp_before": 72,
        "mon1_hp_after": 72,
        "mon2_hp_before": 188,
        "mon2_hp_after": 148,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": False
        }
    },
    {
        "current_attack_turn": 2,
        "is_special_move": False,
        "is_strong_against": False,
        "is_resistant_to": False,
        "mon1_hp_before": 72,
        "mon1_hp_after": -38,
        "mon2_hp_before": 148,
        "mon2_hp_after": 148,
        "applied_hit_effects": {
            "dodge": False,
            "block": False,
            "break": False,
            "absorb": False
        }
    }
]
class HitEffect(object):
    DODGE = "dodge"
    BREAK = "break"
    ABSORB = "absorb"
    BLOCK = "block"

num_dodge = 0
num_block = 0
num_break = 0
num_absorb = 0

for turn in turns:
    if turn:
        current_attack_turn = turn.get("current_attack_turn", 0)
        applied_hit_effects = turn.get("applied_hit_effects", {})
        if current_attack_turn == 2:
            # block turn
            num_block += (1 if applied_hit_effects.get(HitEffect.BLOCK, False) else 0)
            num_absorb += (1 if applied_hit_effects.get(HitEffect.ABSORB, False) else 0)
            num_dodge += (1 if applied_hit_effects.get(HitEffect.DODGE, False) else 0)
        elif current_attack_turn == 1:
            num_break += (1 if applied_hit_effects.get(HitEffect.BREAK, False) else 0)
            
            
print (num_dodge, num_block, num_break, num_absorb)