from collections import deque

n = int(input())
a = list(map(int, input().split()))
dq = deque()
for i in range(n):
    dq.append(a[i])

flip_flg = False
while(dq):
    r = dq.pop()
    if r == 0 and not flip_flg:
        continue
    elif r == 1 and flip_flg:
        continue
    dq.append(r)
    l = dq.popleft()
    if l == 0 and not flip_flg:
        flip_flg = True
        continue
    elif l == 1 and flip_flg:
        flip_flg = False
        continue
    else:
        print("No")
        exit()
print("Yes")