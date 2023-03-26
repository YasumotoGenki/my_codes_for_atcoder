n = int(input())
x = list(map(int, input().split()))

x.sort()

ans = sum(x[n:4 * n]) / (3 * n)
print(ans)