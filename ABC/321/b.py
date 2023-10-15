n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(101):
    final_a = a + [i]
    final_a.sort()
    if sum(final_a[1:-1]) >= x:
        print(i)
        exit()

print(-1)