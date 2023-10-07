n = int(input())
cave = {}

for _ in range(n):
    food_list = list(input().split())[1:]
    target_dict = cave
    for food in food_list:
        if food not in target_dict:
            target_dict[food] = {}
        target_dict = target_dict[food]

def getResult(dict, i):
    target_key = sorted(dict.keys())
    for key in target_key:
        print("--"*i + key)
        getResult(dict[key], i+1)

getResult(cave, 0)
