n = int(input())

x = '4' * (n // 4)
if n % 4:
    x = str(n % 4) + x

m = 0
for c in x:
    m += int(c) * 2

print(m)
print(x)