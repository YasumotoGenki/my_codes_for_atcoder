s = input()

ans= []
flg = True
for i in range(len(s)):
    if s[i] == "|":
        flg ^= True
    elif flg:
        ans.append(s[i])

print("".join(ans))