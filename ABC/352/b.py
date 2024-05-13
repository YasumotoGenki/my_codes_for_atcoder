s = input()
t = input()

s_idx = 0
ans = []

for i in range(len(t)):
    if s_idx < len(s) and t[i] == s[s_idx]:
        ans.append(i + 1)
        s_idx += 1

print(*ans)