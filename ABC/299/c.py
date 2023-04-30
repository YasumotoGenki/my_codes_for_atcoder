n = int(input())
s = input()

ans = -1
stack = 0
stack_flg = False

for i in range(n):
    if s[i] == 'o':
        stack += 1
    else:
        if stack > 0:
            ans = max(ans, stack)
        stack = 0
        stack_flg = True

if stack_flg and stack > 0:
    ans = max(ans, stack)
print(ans)