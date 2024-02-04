n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(10 ** 6 + 1):
    current_q = [item - i * a[j] for j, item in enumerate(q)]
    b_count = 10000000
    for j in range(n):
        if current_q[j] < 0:
            break
        if b[j] > 0:
            b_count = min(b_count, current_q[j] // b[j])
    else:
        ans = max(ans, i + b_count)
print(ans)