n = int(input())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

def check(array_a, array_b, n):
    flg = True
    for i in range(n):
        for j in range(n):
            if array_a[i][j] == 1:
                if array_b[i][j] != 1:
                    flg = False
    return flg

def rotation(array_a, n):
    new_array = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_array[i][j] = array_a[n - 1 - j][i]
    return new_array


for i in range(4):
    if check(a, b, n):
        print("Yes")
        exit()
    a = rotation(a, n)
print("No")