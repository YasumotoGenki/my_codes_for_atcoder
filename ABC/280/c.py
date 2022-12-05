s = input()
t = input()

ans = len(s) + 1
for i in range(len(s)):
    if s[i] != t[i]:
        ans = i + 1
        break
print(ans)