sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

if sx < tx:
    if sx % 2 == 0 and sy % 2 == 0:
        sx += 1
    elif sx % 2 == 1  and sy %  2  == 1:
        sx += 1
elif sx > tx:
    if sx % 2 == 1 and sy % 2 == 0:
        sx -= 1
    elif sx % 2 == 0  and sy %  2  == 1:
        sx -= 1

v = abs(sy - ty)
ans = v
if v >= abs(sx - tx):
    pass
else:
    w = abs(tx - sx)
    ans += abs(w - v) // 2 + (abs(w - v) % 2)

print(ans)