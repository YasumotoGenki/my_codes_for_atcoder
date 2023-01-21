s = input()
length_s = len(s)
ans = 1

for i in range(1, length_s):
    ans += 26 ** i

for i in range(length_s):
    ans += 26 ** (length_s - i - 1) * (ord(s[i]) - ord('A'))
print(ans)