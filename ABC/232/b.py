s = input()
t = input()

for i in range(len(s)):
    if i == 0:
        pre = ord(s[i]) - ord(t[i])
        if pre < 0:
            pre += 26
    else:
        cur = ord(s[i]) - ord(t[i])
        if cur < 0:
            cur += 26
        if cur != pre:
            print("No")
            exit()
else:
    print("Yes")