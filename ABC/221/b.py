s = input()
t = input()

status = 0
idx = -1
for i in range(len(s)):
    if status == 1:
        status = 2
        continue
    if s[i] != t[i]:
        if status == 2:
            print("No")
            exit()
        if i == len(s) - 1:
            print("No")
            exit()
        if s[i + 1] == t[i] and s[i] == t[i + 1]:
            status = 1
        else:
            print("No")
            exit()

print("Yes")
