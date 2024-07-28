from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for i in range(q):
    b, k = map(int, input().split())
        # 2分探索（差分がいくつか）
    ng = -1
    ok = 200000001
    
    while(ok - ng > 1):
        middle = (ng + ok) // 2
        left_idx = bisect_left(a, b - middle)
        right_idx = bisect_left(a, b + middle + 1)

        if right_idx - left_idx >= k:
            ok = middle
        else:
            ng = middle
    print(ok)
