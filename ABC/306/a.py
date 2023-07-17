n = int(input())
s = input()

ans = ""
for i in range(n):
    for j in range(2):
        ans += s[i]

print(ans)