from bisect import bisect_right, bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

large = 10 ** 9 + 1
small = 0
while(large - small > 1):
    middle = (large + small) // 2
    if bisect_right(a, middle) >= m - bisect_left(b, middle):
        large = middle
    else:
        small = middle
if bisect_right(a, small) >= m - bisect_left(b, small):
    print(small)
else:
    print(large)