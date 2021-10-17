n = int(input())
a = list(map(int, input().split()))

trade_history = [0 for i in range(n)]
trade_start_idx = -1

for i in range(n):
    if i != n - 1:
        if a[i] >= a[i + 1]:
            if trade_start_idx == -1:
                trade_start_idx = i
                trade_history[i] = 1
        else: # a[i] <= a[i + 1]
            if trade_start_idx != -1:
                trade_history[i] = 1
                trade_start_idx = -1


if trade_start_idx != -1:
    if a[-1] < a[trade_start_idx]:
        trade_history[-1] = 1
    else:
        trade_history[trade_start_idx] = 0

print(*trade_history)