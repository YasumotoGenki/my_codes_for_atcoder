from collections import deque

n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        b, a = a, b
    ab.append([a, b])

ab.sort()
limit = deque()

for i in range(n):
    a, b = ab[i]
    if len(limit) == 0:
        l = None
    else:
        while(len(limit) > 0):
            l = limit.pop()
            if a > l:
                l = None
            else:
                break
    if l is None:
        limit.append(b)
    elif b > l:
        print("Yes")
        exit()
    elif b < l:
        limit.append(l)
        limit.append(b)
print("No")
