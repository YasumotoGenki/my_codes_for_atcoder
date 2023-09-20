s = input()
length_s = len(s)

ans = 1
for i in range(length_s):
    for j in range(i + 1, length_s + 1):
        if s[i:j] == s[i:j][::-1]:
            ans = max(ans, j - i)
print(ans)