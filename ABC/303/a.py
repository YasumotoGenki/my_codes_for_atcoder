n = int(input())
s = input()
t = input()

flg = True
for i in range(n):
    if s[i] == t[i]:
        pass
    elif s[i] in ["o", "0"] and t[i] in ["o", "0"]:
        pass
    elif s[i] in ["1", "l"] and t[i] in ["1", "l"]:
        pass
    else:
        print("No")
        exit()
print("Yes")