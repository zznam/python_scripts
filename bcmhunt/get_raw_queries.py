network = 2
guild_address = '0xc49eaa7485685480017187cd5a11644801855c35'
member_id = 554
raw_query = "SELECT COUNT(*) as total, \
            SUM(after_amount - before_amount) as total_reward " \
            "FROM `universe_energy_txn_tab` WHERE `network`={} AND `type`={} AND `player`='{}' AND `assigned_member_id`={}"\
            .format(network, 102, guild_address, member_id)
            
print(raw_query)

raw_query = "SELECT COUNT(*) as total, SUM(after_amount - before_amount) as total_reward " \
                "FROM `universe_energy_txn_tab` WHERE `network`={} AND `type`={} AND `player`='{}' "\
                "AND `update_time` >= {}".format(network, 102, guild_address, 232)
                
print(raw_query)


raw_query = "SELECT COUNT(*) as total, SUM(after_amount - before_amount) as total_reward " \
            "FROM `universe_energy_txn_tab` WHERE `network`={} AND `type`={} AND `player`='{}' "\
            "AND `update_time` >= {} AND `update_time` <= {}".format(
                network, 102, guild_address,
                0, 45453534)
            
print(raw_query)
