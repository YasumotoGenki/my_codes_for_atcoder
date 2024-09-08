n = int(input())
a = [[] for _ in range(n)]
for x in range(n):
    for y in range(n):
        a[x].append(list(map(int, input().split())))

s = [[[0 for  _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
for x in range(n):
    for y in range(n):
        for z in range(n):
            s[x][y + 1][z + 1] = a[x][y][z] + s[x][y + 1][z] + s[x][y][z + 1] - s[x][y][z]

q = int(input())
for _ in range(q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    ans = 0
    lx -= 1
    rx -= 1
    for x in range(lx, rx + 1):
        ans += s[x][ry][rz] - s[x][ly - 1][rz] - s[x][ry][lz - 1] + s[x][ly - 1][lz - 1]
    print(ans)
