n = int(input())
a = input()
b = input()

if int(a) > int(b):
    a, b = b, a

mod = 998244353
new_a, new_b = [], []
new_a.append(a[0])
new_b.append(b[0])

for i in range(1, n):
    if a[i] > b[i]:
        new_a.append(b[i])
        new_b.append(a[i])
    else:
        new_a.append(a[i])
        new_b.append(b[i])

print(int("".join(new_a)) * int("".join(new_b)) % mod)