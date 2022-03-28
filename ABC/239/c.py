x1, y1, x2, y2 = map(int, input().split())

for i in range(-2, 3):
    for j in range(-2, 3):
        if i ** 2 + j ** 2 != 5:
            continue
        if (x2 - (x1 + i)) ** 2 + (y2 - (y1 + j)) ** 2 != 5:
            continue
        print("Yes")
        exit()
print("No")