n = int(input())

s = []
for i in range(n):
    s.append(list(input()))

for h in range(n):
    black_count = s[h][:6].count("#")
    if black_count >= 4:
        print("Yes")
        exit()
    for w in range(6, n):
        if s[h][w - 6] == "#":
            black_count -= 1
        if s[h][w] == "#":
            black_count += 1
        if black_count >= 4:
            print("Yes")
            exit()

for w in range(n):
    black_count = 0
    for h in range(6):
        if s[h][w] == "#":
            black_count += 1
    if black_count >= 4:
        print("Yes")
        exit()
    for h in range(6, n):
        if s[h - 6][w] == "#":
            black_count -= 1
        if s[h][w] == "#":
            black_count += 1
        if black_count >= 4:
            print("Yes")
            exit()

for h in range(n - 5):
    for w in range(n - 5):
        black_count = 0
        for i in range(6):
            if s[h + i][w + i] == "#":
                black_count += 1
            if black_count >= 4:
                print("Yes")
                exit()

for h in range(n - 5):
    for w in range(n - 1, 4, -1):
        black_count = 0
        for i in range(6):
            if s[h + i][w - i] == "#":
                black_count += 1
            if black_count >= 4:
                print("Yes")
                exit()

print("No")