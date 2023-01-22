n = int(input())
s = input()

idx = 0

while(idx < len(s)):
    if idx < len(s) - 1 and s[idx:idx + 2] == "na":
        s = s[:idx] + "nya" + s[idx + 2:]
    idx += 1
print(s)