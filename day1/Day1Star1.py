balances = []
BAL_TO_FIND = 2020
with open("star1input", 'r') as file:
    for line in file:
        balances.append(int(line))
for i in balances:
    for j in balances:
        for k in balances:
            if i + j + k == BAL_TO_FIND:
                print("Bal 1: " + str(i))
                print("Bal 2: " + str(j))
                print("Bal 3: " + str(k))
                print("Mul : " + str(i*j*k))