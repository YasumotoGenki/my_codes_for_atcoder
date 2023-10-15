N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aをソート
A.sort()
# Bをソート
B.sort()
# 累積和を計算
BS = [0]
for i, item_b in enumerate(B):
    BS.append(BS[-1] + item_b)

ans= 0
# Aの最初から走査して、Bを二分探索し、Pになる値を探る
for item_a in A:
    left_idx = 0
    right_idx = M - 1
    while(right_idx - left_idx > 1):
        middle_idx = (left_idx + right_idx) // 2
        if item_a + B[middle_idx] >= P:
            right_idx = middle_idx
        else:
            left_idx = middle_idx
    # それ以下の場合は、累積和を用いて足し算、それ以降の要素数だけPを足す
    if item_a + B[right_idx] < P:
        ans += (item_a * M) + BS[-1]
    elif item_a + B[left_idx] >= P:
        ans += P * M
    else:
        ans += P * (M - right_idx)
        ans += (item_a * right_idx) + (BS[right_idx])
print(ans)