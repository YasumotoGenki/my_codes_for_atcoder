expectation_list = []
dicenum = {1, 2, 3, 4, 5, 6}

for i in range(100):
    if i == 0:
        expectation_list.append(3.5)
        continue
    cur_exp = 0
    for dnum in dicenum:
        if dnum > expectation_list[-1]:
            cur_exp += dnum / 6
        else:
            cur_exp += expectation_list[-1] / 6
    expectation_list.append(cur_exp)

n = int(input())
print(expectation_list[n - 1])