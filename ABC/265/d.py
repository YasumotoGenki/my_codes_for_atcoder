from bisect import bisect_left

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

accum = [0]
for i in range(n):
    accum.append(a[i] + accum[-1])

y, z = 1, 2    

while(y <= n - 2 and z <= n - 1):
    if accum[z] - accum[y] == q:
        # binary search
        accum_x_idx = bisect_left(accum, accum[y] - p)
        accum_w_idx = bisect_left(accum, accum[z] + r)
        if accum[accum_x_idx] == accum[y] - p and accum_w_idx <= n and accum[accum_w_idx] == accum[z] + r:
            print("Yes")
            exit()
        z += 1
        y += 1

    elif accum[z] - accum[y] < q:
        z += 1
    else:
        y += 1
print("No")