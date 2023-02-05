from collections import Counter

n = int(input())
s = input()
t = input()

s_counter = Counter(s)
t_counter = Counter(t)

for key, value in s_counter.items():
    if key not in t_counter:
        print(-1)
        exit()
    elif t_counter[key] != value:
        print(-1)
        exit()
    else:
        pass

idx = n - 1
count = n
rev_t = t[::-1]
for i in range(n):
    if s[idx] == rev_t[i]:
        count -= 1
        idx -= 1
print(count)