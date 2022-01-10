from itertools import permutations

N, M = map(int, input().split())

AB = set()
for i in range(M):
    a, b = map(int, input().split())
    AB.add(tuple((a, b)))
CD = []
for i in range(M):
    c, d = map(int, input().split())
    CD.append([c, d])

for perm_list in permutations(range(N)):
    map_dict = dict()
    ans = False
    for i, j in enumerate(perm_list):
        map_dict[j + 1] = i + 1
    flg = True
    for c, d in CD:
        new_c = map_dict[c]
        new_d = map_dict[d]
        if new_c > new_d:
            new_c, new_d = new_d, new_c
        if (new_c, new_d) not in AB:
            flg = False
            break
    if flg:
        print("Yes")
        exit()
print("No")