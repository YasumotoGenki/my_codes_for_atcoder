n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = dict()

for item in a:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1

for item in b:
    if item in d and d[item] > 0:
        d[item] -= 1
    else:
        print("No")
        exit()

print("Yes")