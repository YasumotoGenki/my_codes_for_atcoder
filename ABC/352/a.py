n, x, y, z = map(int, input().split())
if x <= z <= y or x >= z >= y:
    print("Yes")
else:
    print("No")