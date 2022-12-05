h, w = map(int, input().split())
x = [0 for _ in range(w)]
for i in range(h):
    row = input()
    for j in range(w):
        if row[j] == "#":
            x[j] += 1
print(*x)