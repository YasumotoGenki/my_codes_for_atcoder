s = input()
flg = True
if s[0].upper() != s[0]:
    flg = False
if len(s) > 1 and s[1:].lower() != s[1:]:
    flg = False
if flg:
    print("Yes")
else:
    print("No")