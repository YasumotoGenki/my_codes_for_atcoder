n, m, h, k = map(int, input().split())
s = input()
xy = dict()
for i in range(m):
    x, y = map(int, input().split())
    if x not in xy:
        xy[x] = set()
    xy[x].add(y)

current = [0, 0]

for move in s:
    if move == "R":
        current[0] += 1        
    elif move == "L":
        current[0] -= 1
    elif move == "U":
        current[1] += 1
    elif move == "D":
        current[1] -= 1
    h -= 1
    if h < 0:
        print("No")
        exit()
    if current[0] in xy and current[1] in xy[current[0]] and h < k:
        h = k
        xy[current[0]].remove(current[1])
print("Yes")