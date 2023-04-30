from bisect import bisect_left

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for i in range(n):
    seek_element = a[i] - x
    idx = bisect_left(a, seek_element)
    if idx < n and a[idx] == seek_element:
        print("Yes")
        exit()
print("No")