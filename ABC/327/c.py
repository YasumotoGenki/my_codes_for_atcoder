a = []
for i in range(9):
    a.append(list(map(int, input().split())))

for i in range(9):
    s = set()
    for j in range(9):
        s.add(a[i][j])
    if len(s) != 9:
        print("No")
        exit()

for j in range(9):
    s = set()
    for i in range(9):
        s.add(a[i][j])
    if len(s) != 9:
        print("No")
        exit()

for h in range(0, 9, 3):
    for w in range(0, 9, 3):
        s = set()
        for i in range(3):
            for j in range(3):
                s.add(a[h + i][w + j])
        if len(s) != 9:
            print("No")
            exit()

print("Yes")