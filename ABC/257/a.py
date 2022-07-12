n, x = map(int, input().split())
s = ""
for i in range(26):
    s += chr(i + ord('A')) * n
print(s[x - 1])