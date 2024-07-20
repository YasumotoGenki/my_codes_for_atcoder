s, t = map(str, input().split())

for w in range(1, len(s)):
    for c in range(1, w + 1):
        tmp = []
        for i in range(c - 1, len(s), w):
            tmp.append(s[i])
        if "".join(tmp) == t:
            print("Yes")
            exit()

print("No")