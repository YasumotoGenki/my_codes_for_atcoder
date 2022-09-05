from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
ans = 0
while(len(a) > 1):
    ans += 1
    min_item = a.popleft()
    max_item = a.pop()
    rem = max_item % min_item
    
    a.appendleft(min_item)
    if rem != 0:
        a.appendleft(rem)
print(ans)