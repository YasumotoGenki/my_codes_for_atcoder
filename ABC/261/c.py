n = int(input())
s = []
d = dict()
dc = dict()
for i in range(n):
    cur = input()
    s.append(cur)
    if cur not in d:
        d[cur] = 1
        dc[cur] = 0
    else:
        d[cur] += 1


for i in range(n):
    if dc[s[i]] == 0:
        print(s[i])
    else:
        print(s[i] + "(" + str(dc[s[i]]) + ")")
    dc[s[i]] += 1