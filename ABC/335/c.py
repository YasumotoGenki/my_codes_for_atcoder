n, q = map(int, input().split())
parts = [[i, 0] for i in range(1, n + 1)]
parts.reverse()
count = 0
for _ in range(q):
    query = list(map(str, input().split()))
    if query[0] == "1":
        x, y = parts[-1]
        if query[1] == "R":
            parts.append([x + 1, y])
        elif query[1] == "L":
            parts.append([x - 1, y])
        elif query[1] == "U":
            parts.append([x, y + 1])
        elif query[1] == "D":
            parts.append([x, y - 1])
    else:
        p = int(query[1])
        x, y = parts[-p]
        print(x, y)