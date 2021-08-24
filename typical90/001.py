N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

right = 10 ** 9
left = 1
middle = (right + left) // 2

while (right - left > 1):
    count = 0
    pre_cut = 0
    for i in range(N):
        if A[i] - pre_cut >= middle:
            count += 1
            pre_cut = A[i]
    if L - pre_cut >= middle:
        count += 1
    if count >= K + 1:
        left = middle
    else:
        right = middle
    middle = (right + left) // 2

print(left)