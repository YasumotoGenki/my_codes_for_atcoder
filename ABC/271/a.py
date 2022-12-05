n = int(input())
ans = hex(n)[2:]
if len(ans) == 1:
    ans = '0' + ans
ans = ans.upper()
print(ans)