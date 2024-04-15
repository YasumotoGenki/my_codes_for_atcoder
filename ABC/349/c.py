s = input()
t = input()

s_idx = 0
if t[-1] == "X":
    for i in range(2):
        character = t[i].lower()
        flg = True
        while(s_idx < len(s) and flg):
            if s[s_idx] == character:
                if i == 1:
                    print("Yes")
                    exit()
                flg = False
            s_idx += 1

s_idx = 0
for i in range(3):
    character = t[i].lower()
    flg = True
    while(s_idx < len(s) and flg):
        if s[s_idx] == character:
            if i == 2:
                print("Yes")
                exit()
            flg = False
        s_idx += 1
print("No")
    