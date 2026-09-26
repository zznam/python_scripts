
import json


strairi = '[{"level":1,"required_num":100,"reward_type":1,"reward_data":{"amount":100}},{"level":2,"required_num":300,"reward_type":1,"reward_data":{"amount":500}},{"level":3,"required_num":1000,"reward_type":1,"reward_data":{"amount":1000}},{"level":4,"required_num":2000,"reward_type":1,"reward_data":{"amount":2000}},{"level":5,"required_num":5000,"reward_type":1,"reward_data":{"amount":5000}},{"level":6,"required_num":10000,"reward_type":1,"reward_data":{"amount":10000}},{"level":7,"required_num":20000,"reward_type":1,"reward_data":{"amount":10000}},{"level":8,"required_num":30000,"reward_type":1,"reward_data":{"amount":10000}},{"level":9,"required_num":40000,"reward_type":1,"reward_data":{"amount":10000}},{"level":10,"required_num":50000,"reward_type":1,"reward_data":{"amount":10000}}]'
level_configs = json.loads(strairi)

print(level_configs)

for idx, level_config in enumerate(level_configs):
    isLast = idx == len(level_configs) -1 
    print(idx, isLast)
    if (level_config.get("level") == 1):
        print(level_config)
        print(level_config["required_num"])
        # print(level_config.required_num) #ERRROR


aloha = json.dumps({"level": level_config["level"], "current_num": 0, "diff_arr": []})
print(aloha)
kagawa = json.loads(aloha)
print(kagawa)
print(kagawa["level"])