n, q = map(int, input().split())
x = [i for i in range(1, n + 1)]
num2idx = dict()
for i in range(1, n + 1):
    num2idx[i] = i - 1

for i in range(q):
    num = int(input())
    idx = num2idx[num]
    if idx == n - 1:
        x1 = x[idx]
        x2 = x[idx - 1]
        x[idx] = x2
        x[idx - 1] = x1
        num2idx[x1] = idx - 1
        num2idx[x2] = idx
    else:
        x1 = x[idx]
        x2 = x[idx + 1]
        x[idx] = x2
        x[idx + 1] = x1
        num2idx[x1] = idx + 1
        num2idx[x2] = idx
print(*x)