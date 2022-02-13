from collections import deque

n, k = map(int, input().split())
s = input()

d = dict()

for i in range(n):
    if s[i] not in d:
        d[s[i]] = deque()
        d[s[i]].append(i)
    else:
        d[s[i]].append(i)

ans = ""
used_idx = 0
for i in range(k):
    min_char = "a"
    while(len(ans) <= i):
        if min_char in d and len(d[min_char]) > 0:
            candidate_idx = d[min_char].popleft()
            if candidate_idx < used_idx:
                pass
            elif n - candidate_idx < k - i:
                d[min_char].appendleft(candidate_idx)
                min_char = chr(ord(min_char) + 1)
            else:
                ans += min_char
                used_idx = candidate_idx
        else:
            min_char = chr(ord(min_char) + 1)
print(ans)