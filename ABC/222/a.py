s = input()
if len(s) < 4:
    ans = "0" * (4 - len(s)) + s
else:
    ans = s
print(ans)