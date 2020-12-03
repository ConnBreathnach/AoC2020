map = []
with open("input", 'r') as f:
    for line in f:
        map.append(line.replace("\n", '')*35) # 35 is GCD between 3, 5, 7

slope_1_1_trees = 0
slope_3_1_trees = 0
slope_5_1_trees = 0
slope_7_1_trees = 0
slope_1_2_trees = 0

for i in range(1, len(map)):
    if map[i][(i*3)%(31*3)] == "#":
        slope_3_1_trees += 1
    if map[i][i%31] == "#":
        slope_1_1_trees += 1
    if map[i][(i*5)%(31*5)] == "#":
        slope_5_1_trees += 1
    if map[i][(i*7)%(31*7)] == "#":
        slope_7_1_trees += 1
    if map[(i*2)%323][i] == "#":
        if i*2 <= 323:
            slope_1_2_trees += 1

print(slope_1_1_trees, slope_1_2_trees, slope_3_1_trees, slope_5_1_trees, slope_7_1_trees)
print(slope_1_1_trees*slope_1_2_trees*slope_3_1_trees*slope_5_1_trees*slope_7_1_trees)