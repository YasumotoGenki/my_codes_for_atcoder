n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0 for _ in range(m)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        s[j] += x[j]

for i in range(m):
    if a[i] > s[i]:
        print("No")
        exit()
print("Yes")