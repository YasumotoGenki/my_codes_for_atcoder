n, m = map(int, input().split())

info_list = []
for i in range(n):
    info_list.append(list(map(int, input().split())))

info_list.sort()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        i_price = info_list[i][0]
        j_price = info_list[j][0]
        i_functions_set = set(info_list[i][2:])
        j_functions_set = set(info_list[j][2:])
        if i_price < j_price and j_functions_set.issubset(i_functions_set):
            print("Yes")
            exit()
        elif i_price == j_price and j_functions_set.issubset(i_functions_set) and i_functions_set - j_functions_set:
            print("Yes")
            exit()

print("No")