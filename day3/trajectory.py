map = []
with open("input", 'r') as f:
    for line in f:
        map.append(line.replace("\n", '')*3)

trees = 0

for i in range(len(map)):
    if map[i][(i*3)%93] == "#":
        trees += 1

print(trees)