n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)
ans = 0

ans += (x // sum_a) * n
rem = x % sum_a

for i in range(n):
    rem -= a[i]
    ans += 1
    if rem < 0:
        print(ans)
        exit()