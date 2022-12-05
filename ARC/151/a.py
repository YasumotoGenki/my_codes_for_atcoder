n = int(input())
s = input()
t = input()

count = 0
indices = []
for i in range(n):
    if s[i] != t[i]:
        count += 1
        indices.append(True)
    else:
        indices.append(False)

if count % 2 == 1:
    print(-1)
    exit()

ans = []
s_count = 0
t_count = 0

for i in range(n):
    if indices[i]:
        if s[i] == '0' and s_count < count // 2:
            s_count += 1
            ans.append(s[i])
        elif t_count == count // 2:
            s_count += 1
            ans.append(s[i])
        else:
            t_count += 1
            ans.append(t[i])
    else:
        ans.append('0')

print(''.join(ans))