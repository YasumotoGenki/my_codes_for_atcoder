s = input()
t = input()

ng_list = [False] * len(t)
ng_count = 0
for i in range(len(t)):
    if s[-len(t) + i] == "?" or t[i] == "?" or s[-len(t) + i] == t[i]:
        pass
    else:
        ng_count += 1
        ng_list[i] = True

if ng_count > 0:
    print("No")
else:
    print("Yes")

for i in range(len(t)):
    if s[i] == "?" or t[i] == "?" or s[i] == t[i]:
        if ng_list[i]:
            ng_count -= 1
            ng_list[i] = False
    else:
        if not ng_list[i]:
            ng_count += 1
            ng_list[i] = True
    if ng_count > 0:
        print("No")
    else:
        print("Yes")