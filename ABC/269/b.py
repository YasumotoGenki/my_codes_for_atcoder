s = []
a, b, c, d = -1, -1, -1, -1
for i in range(10):
    s = input()
    if '#' in s and a == -1:
        a = i + 1
        c = s.index('#') + 1
        d = s.rindex('#') + 1
    if '#' not in s and a > 0 and b == -1:
        b = i

if b == -1:
    b = 10

print(a, b)
print(c, d)