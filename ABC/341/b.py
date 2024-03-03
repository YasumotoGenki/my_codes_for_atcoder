n = int(input())
a = list(map(int, input().split()))
st = dict()
for i in range(n - 1):
    s, t = map(int, input().split())
    count = a[i] // s
    a[i + 1] += t * count
print(a[-1])