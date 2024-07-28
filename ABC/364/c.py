n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

sweet = 0
salt = 0
ans = n
for i in range(n):
    sweet += a[i]
    salt += b[i]
    if sweet > x or salt > y:
        print(i + 1)
        exit()

print(n)