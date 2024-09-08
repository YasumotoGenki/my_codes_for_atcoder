a, b, c = map(int, input().split())

for i in range(1, 25):
    if (b + i) % 24 == a:
        print("No")
        exit()
    if (b + i) % 24 == c:
        print("Yes")
        exit()