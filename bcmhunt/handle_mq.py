def handle_pve_action(network, data):
    player = data["player"].lower()
    assigned_member_id = data.get("assigned_member_id", 0)
    battle_result = data.get("battle_result", 0)
    block_data = data.get(
        "block_data", {
            "types": [-1],
            "rarity": [-1],
            "block_mon_bp": 0,
            "species": 0,
            "battle": {
                "required_stamina": 0
            }
        })
    block_battle_data = block_data.get("battle", {})
    required_stamina = block_battle_data.get("required_stamina", 0)

    print(required_stamina)


handle_pve_action(2, {
    "player": "43434",
    "block_data": {
        "battle": {
            "required_stamina": 200
        }
    }
})
