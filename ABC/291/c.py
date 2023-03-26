n = int(input())
s = input()
points = dict()
points[0] = set([0])
cur = [0, 0]
for i in range(n):
    if s[i] == 'R':
        cur[0] += 1
    elif s[i] == 'L':
        cur[0] -= 1
    elif s[i] == 'U':
        cur[1] += 1
    elif s[i] == 'D':
        cur[1] -= 1
    if cur[0] in points:
        if cur[1] in points[cur[0]]:
            print("Yes")
            exit()
        else:
            points[cur[0]].add(cur[1])
    else:
        points[cur[0]] = set([cur[1]])
print("No")