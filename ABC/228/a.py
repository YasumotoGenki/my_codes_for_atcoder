s, t, x = map(int, input().split())

for i in range(s, s + 24):
    c = i
    if c >= 24:
        c -= 24
    if c == t:
        print("No")
        exit()
    if c == x:
        print("Yes")
        exit()