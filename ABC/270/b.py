x, y, z = map(int, input().split())

if x > 0:
    if 0 < y < x:
        if y > z > 0:
            print(abs(x))
        elif z > y:
            print(-1)
        else:
            print(abs(2 * z) + abs(x))
    else:
        print(abs(x))
else:
    if x < y < 0:
        if y < z < 0:
            print(abs(x))
        elif z < y:
            print(-1)
        else:
            print(abs(2 * z) + abs(x))
    else:
        print(abs(x))