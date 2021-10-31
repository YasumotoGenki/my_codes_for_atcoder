n, m = map(int, input().split())
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

init_mod = b[0][0] % 7

if init_mod == 0 and m > 1:
    print("No")
    exit()
if init_mod > 0 and 8 - init_mod < m:
    print("No")
    exit()

init_num = b[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            pass
        else:
            if b[i][j] != init_num + i * 7 + j:
                print("No")
                exit()
print("Yes")