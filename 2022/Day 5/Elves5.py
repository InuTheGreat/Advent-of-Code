with open("input.txt") as f:
    lin = f.readlines()
for x in range(9):
    print(str(x) + "  :" + str(lin[x]))